# UnionFind using quick union
 
class UnionFind_QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # pick x to be the root
            self.root[root_y] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

