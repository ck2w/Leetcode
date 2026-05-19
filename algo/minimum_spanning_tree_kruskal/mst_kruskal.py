class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # 同一集合，会成环

        # 矮树接到高树下，树高不增加
        if self.rank[px] < self.rank[py]:
            px, py = py, px   # # 保证 px 是较高的那棵
        self.parent[py] = px  # 按秩合并,矮树(py) 接到高树(px) 下
        if self.rank[px] == self.rank[py]: # 只有两棵一样高时，合并后高度才+1
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])  # 按权重排序
    uf = UnionFind(n)
    mst, total = [], 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break
    return mst, total