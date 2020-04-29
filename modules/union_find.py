class UnionFind():

    def __init__(self,number):
        self.parent = [i for i in range(number)]
        self.rank = [0 for _ in range(number)]

    # 木の根を求める
    def find(self,number):
        if self.parent[number] == number:
            return number
        else:
            return self.find(self.parent[number])

    # 集合を併合
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            if self.rank[x] >= self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するかの判定
    def same(self,x,y):
        return self.find(x) == self.find(y)



