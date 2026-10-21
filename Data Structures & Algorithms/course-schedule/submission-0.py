class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(set)

        for cur, pre in prerequisites:
            preMap[cur].add(pre)

        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                return True
            
            visited.add(curr)
            for i in preMap[curr]:
                if not dfs(i):
                    return False
            
            visited.remove(curr)
            preMap[curr] = []
            return True
        
        for i in range (numCourses):
            if not dfs(i):
                return False
        
        return True