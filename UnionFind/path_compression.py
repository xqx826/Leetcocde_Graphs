# optimization for quick union

from re import S


class FindUnion_PathComp:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # check height for each tree
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_y] > self.root[root_x]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1    
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)