
# Bellman-Ford 算法
- 解决的是单源最短路径问题：从一个起点出发，找到到所有其他节点的最短距离。
- 它比 Dijkstra 更通用，因为能处理负权边。代价是性能更慢：O(V·E) 而非 O(E log V)。


# 问题定义
- 给定带权有向图，从源点 s 出发，求到所有节点的最短路径。
- 允许负权边，但不能有负权环（否则路径可以无限缩短，无解）。


# 思考
- s to z visits every vertex<=1次，至多访问一次
- shortest path |P|<= n-1 edges


# recurrence, dp
- 定义状态：D(i,z)=length of shortest path from s to z using <=i edges.
- base case: D(0,s)=0 and for all z !=s, D(0,z)=inf
- 转移方程：D(i,z)=min{D(i-1,y)+w(y,z), on all y near z}
- 最终答案：dist(z)=min{D(i,z), on all i}
- 为什么重复 V-1 轮？ 最短路径最多经过 V-1 条边。每轮松弛至少能确定"再多走一跳"的最优距离。


# 负权环检测
- 这是 Bellman-Ford 相对于 Dijkstra 的独特能力。做完 V-1 轮后，再做第 V 轮：
- Bellman-Ford 检测到的负权环，只需要满足一个条件：环上的节点从 s 可达。不一定s在里面。

```
for u, v, w in edges:
    if dist[u] + w < dist[v]:
        # 还能继续松弛 → 存在负权环！
        return "negative cycle detected"
```

# u, v, w 是一条有向边的三个属性：
- u: 起点（from node）
- v: 终点（to node）
- w: 权重/weight（这条边的"代价"，可以是距离、时间、费用等，可以为负）