class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustList = defaultdict(int)

        for a, b in trust:
            trustList[a] -= 1
            trustList[b] += 1
        
        for i in range (1, n + 1):
            if trustList[i] == (n - 1):
                return i
        
        return -1
        