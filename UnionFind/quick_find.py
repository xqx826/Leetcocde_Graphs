# UnionFind using quick find
"""
Each index represents a node and the value = the root node of that node
"""

class UnionFind_QuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                # let root_x to be the new root
                # whenever we see a index that has y as it's root, change it to x
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFind_QuickFind(10)
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