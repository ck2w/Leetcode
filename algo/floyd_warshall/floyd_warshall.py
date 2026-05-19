import math

def floyd_warshall(n, edges):
    """
    有向图全源最短路径
    n: 节点数 (节点编号 0 ~ n-1)
    edges: [(u, v, w), ...] 有向边 u->v 权重w
    """
    dist = [[math.inf] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]   
    # next_node，只为路径重建时使用

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w          # 只设单向
        next_node[u][v] = v

    # dp[k][i][j] = 只允许经过节点 {1, 2, ..., k} 作为中间节点时，从 i 到 j 的最短距离。
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def get_path(next_node, i, j):
    if next_node[i][j] is None:
        return None  # 不可达
    path = [i]
    while i != j:
        i = next_node[i][j]
        path.append(i)
    return path

def has_negative_cycle(dist, n):
    return any(dist[i][i] < 0 for i in range(n))


# ─── 使用例子 ───────────────────────────────────────────
#
#  有向图结构：
#
#   0 ──2──> 1 ──3──> 3
#   |        |        ^
#   6        1        |
#   v        v        |
#   2 <──1── 3 ──1───>+
#
#  注意：2->3 无边，需绕路

edges = [
    (0, 1, 2),
    (0, 2, 6),
    (1, 3, 3),
    (1, 3, 1),  # 重复边取更短的（初始化时后者覆盖前者）
    (3, 2, 1),
    (3, 3, 0),
]

# 更清晰的例子
edges = [
    (0, 1, 2),   # 0->1, 权重2
    (0, 2, 6),   # 0->2, 权重6
    (1, 3, 1),   # 1->3, 权重1
    (3, 2, 1),   # 3->2, 权重1
]

n = 4
dist, next_node = floyd_warshall(n, edges)

# 打印距离矩阵
print("距离矩阵：")
header = "     " + "  ".join(f"  {j}" for j in range(n))
print(header)
for i in range(n):
    row = []
    for j in range(n):
        val = dist[i][j]
        row.append("  ∞" if val == math.inf else f"{val:3d}")
    print(f"  {i}  {'  '.join(row)}")

# 打印所有可达路径
print("\n所有可达路径：")
for i in range(n):
    for j in range(n):
        if i != j and dist[i][j] < math.inf:
            path = get_path(next_node, i, j)
            print(f"  {i} -> {j}  距离={dist[i][j]}  路径={' -> '.join(map(str, path))}")

# 负权环检测
if has_negative_cycle(dist, n):
    print("\n⚠️  图中存在负权环！")
else:
    print("\n✅ 无负权环")