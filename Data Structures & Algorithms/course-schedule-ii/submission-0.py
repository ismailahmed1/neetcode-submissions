class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []

        preMap = defaultdict(set)
        for cur, pre in prerequisites:
            preMap[cur].add(pre)

        finished = set()
        cycle = set()

        
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in finished:
                return True
            
            cycle.add(curr)
            for i in preMap[curr]:
                if not dfs(i):
                    return False
            
            cycle.remove(curr)
            finished.add(curr)
            res.append(curr)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
