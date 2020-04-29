class UnionFind(number):

    def __init__():
        self.parent = [i for i in range(number)]
        self.rank = [0 for _ in range(number)]

    # 木の根を求める
    def find(self,number):
        if parent[number] == number:
            return number
        else:
            return self.find(parent[number])

    # 集合を併合
    def unite(self,x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        else:
            if rank[x] >= rank[y]:
                parent[y] = x
            else:
                parent[x] = y
            if rank[x] == rank[y]:
                rank[x] += 1

    # xとyが同じ集合に属するかの判定
    def same(self,x,y):
        return self.find(x) == self.find(y)
