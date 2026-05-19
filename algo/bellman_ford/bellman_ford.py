from math import inf

def bellman_ford_dp(nodes, edges, source):
    V = len(nodes)
    # D length of shortest path from s to z
    D = {z: (0 if z == source else inf) for z in nodes}  
    # 记录每个节点的前驱，为了复现path
    prev = {z: None for z in nodes}  

    for _ in range(V - 1):
        D_next = D.copy()
        for u, v, w in edges:
            if D[u] != inf and D[u] + w < D_next[v]:
                D_next[v] = D[u] + w
                prev[v] = u   # v 是从 u 松弛来的
        D = D_next

    # 负权环检测：再检测一轮
    for u, v, w in edges:
        if D[u] != inf and D[u] + w < D[v]:
            return None, None

    return D, prev


def reconstruct_path(prev, source, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    # 检查路径确实从 source 出发
    if path[0] != source:
        return None  # target 从 source 不可达
    return path


nodes = ['s', 'b', 'a', 'e', 'd', 'f']
edges = [('s','b',5),('b','a',3),('b','e',8),
         ('a','e',-2),('e','b',2),('a','d',4),
         ('d','a',3),('e','f',5)]

D, prev = bellman_ford_dp(nodes, edges, 's')

for target in ['b', 'a', 'e', 'd', 'f']:
    path = reconstruct_path(prev, 's', target)
    print(f"s → {target} : {D[target]}  路径: {' → '.join(path)}")