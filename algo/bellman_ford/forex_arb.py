# n对货币对，每对货币对之间兑换都有bid ask price，货币对之间可以自由兑换。
# 但是A换B和B换A要用分别用bid和ask price。
# 怎么看货币对A，B之间是否存在外汇套利机会。
# pair (A/B):  bid = 市场买入A的价格(用B计价), ask = 市场卖出A的价格(用B计价)

# 思路
# 乘积不好直接用图算法处理，图算法擅长处理加法（最短路）。
# −log(r1​)+(−log(r2​))+(−log(r3​)) < 0 
# edge EUR→USD: weight = -log(1.082)
# edge USD→EUR: weight = -log(1/1.083) = +log(1.083)
import math
from math import inf
from typing import Optional


def bellman_ford_forex(nodes: list[str],
                       edges: list[tuple[str, str, float]],
                       source: str
                       ) -> tuple[Optional[dict], Optional[dict]]:
    """    
    返回:
        (D, prev) — 正常情况
        (None, None) — 检测到负权环（存在套利机会）
    """
    V = len(nodes)

    # D: 从 source 到各节点的最短路径长度（-log 空间）
    D = {z: (0 if z == source else inf) for z in nodes}
    # prev: 记录每个节点的前驱，用于复现路径
    prev = {z: None for z in nodes}

    # 松弛 V-1 轮
    for _ in range(V - 1):
        D_next = D.copy()
        for u, v, w in edges:
            if D[u] != inf and D[u] + w < D_next[v]:
                D_next[v] = D[u] + w
                prev[v] = u
        D = D_next

    # 第 V 轮检测负权环（套利检测）
    for u, v, w in edges:
        if D[u] != inf and D[u] + w < D[v]:
            return None, None   # 有负权环 → 存在套利

    return D, prev


def reconstruct_path(prev: dict,
                     source: str,
                     target: str) -> Optional[list[str]]:
    """沿 prev 回溯还原路径，与原版逻辑完全一致。"""
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if path[0] != source:
        return None   # target 从 source 不可达
    return path


def build_forex_graph(pairs: list[dict]
                      ) -> tuple[list[str], list[tuple[str, str, float]]]:
    """
    pairs 格式:
        [{"base": "USD", "quote": "EUR", "bid": 0.92, "ask": 0.921}, ...]

    建边规则:
        base → quote : rate = bid        （你卖 base，得 bid 个 quote）
        quote → base : rate = 1 / ask   （你用 quote 买 base）
    两个方向权重均为 -log(rate)。
    """
    currency_set = set()
    edges = []

    for p in pairs:
        base, quote, bid, ask = p["base"], p["quote"], p["bid"], p["ask"]
        currency_set.add(base)
        currency_set.add(quote)

        # base → quote
        edges.append((base, quote, -math.log(bid)))
        # quote → base
        edges.append((quote, base, -math.log(1.0 / ask)))

    nodes = sorted(currency_set)
    return nodes, edges


# ─────────────────────────────────────────────
# 套利环提取（负权环路径还原）
# ─────────────────────────────────────────────

def find_arbitrage_cycle(nodes: list[str],
                         edges: list[tuple[str, str, float]]
                         ) -> Optional[tuple[list[str], float]]:
    """
    对每个节点作为 source 跑一次 Bellman-Ford。
    发现负权环时，用 prev + 走 V 步的方式定位环并还原路径。
    返回 (cycle_path, profit_multiplier) 或 None。
    """
    V = len(nodes)

    for source in nodes:
        D = {z: (0 if z == source else inf) for z in nodes}
        prev = {z: None for z in nodes}

        for _ in range(V - 1):
            D_next = D.copy()
            for u, v, w in edges:
                if D[u] != inf and D[u] + w < D_next[v]:
                    D_next[v] = D[u] + w
                    prev[v] = u
            D = D_next

        # 第 V 轮：找到被松弛的节点（它在某个负权环上或其下游）
        cycle_node = None
        for u, v, w in edges:
            if D[u] != inf and D[u] + w < D[v]:
                cycle_node = v
                break

        if cycle_node is None:
            continue   # 该 source 无负权环，换下一个

        # 沿 prev 走 V 步，确保落入环内（离开通往环的"尾巴"）
        node_in_cycle = cycle_node
        for _ in range(V):
            node_in_cycle = prev[node_in_cycle]

        # 从环内节点出发，沿 prev 绕一圈还原完整环路径
        path = []
        cur = node_in_cycle
        while True:
            path.append(cur)
            cur = prev[cur]
            if cur == node_in_cycle:
                break
        path.append(node_in_cycle)
        path.reverse()

        # 计算真实套利收益率（转回 rate 乘积）
        profit = 1.0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            # 从 edges 中找到对应权重
            rate = next(math.exp(-w) for (eu, ev, w) in edges
                        if eu == u and ev == v)
            profit *= rate

        return path, profit

    return None


# ─────────────────────────────────────────────
# 使用示例
# ─────────────────────────────────────────────

pairs = [
    {"base": "USD", "quote": "EUR", "bid": 0.9200, "ask": 0.9210},
    {"base": "EUR", "quote": "GBP", "bid": 0.8600, "ask": 0.8610},
    {"base": "GBP", "quote": "USD", "bid": 1.2900, "ask": 1.2910},
    {"base": "USD", "quote": "JPY", "bid": 148.50, "ask": 148.60},
    {"base": "JPY", "quote": "EUR", "bid": 0.00630, "ask": 0.00631},
]

nodes, edges = build_forex_graph(pairs)

print("=== 最短路径（无套利时）===")
D, prev = bellman_ford_forex(nodes, edges, source="USD")

if D is None:
    print("检测到套利机会（存在负权环）")
else:
    for target in [n for n in nodes if n != "USD"]:
        path = reconstruct_path(prev, "USD", target)
        cost = D[target]
        rate  = math.exp(-cost) if cost != inf else 0
        print(f"USD → {target} : 隐含汇率 {rate:.6f}  路径: {' → '.join(path) if path else '不可达'}")

print("\n=== 套利环检测 ===")
result = find_arbitrage_cycle(nodes, edges)
if result:
    cycle, profit = result
    print(f"发现套利机会！")
    print(f"路径    : {' → '.join(cycle)}")
    print(f"收益率  : {profit:.6f}x  ({(profit-1)*100:.4f}%)")
else:
    print("无套利机会")