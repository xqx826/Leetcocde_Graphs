# we want to minimize the height of the tree

from logging import root


class UnionFind_Rank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
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
    
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFind_Rank(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.is_connected(1, 5))  # true
print(uf.is_connected(5, 7))  # true
print(uf.is_connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.is_connected(4, 9))  # true