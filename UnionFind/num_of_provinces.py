from path_compression import FindUnion_PathComp

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = FindUnion_PathComp(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    provinces.union(i, j)
        r = set()
        
        for item in provinces.root:
            r.add(provinces.find(item))
        return len(r)