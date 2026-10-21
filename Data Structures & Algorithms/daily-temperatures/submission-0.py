class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temperature, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append((t, i))
        
        while stack:
            stackInd = stack.pop()[1]
            res[stackInd] = 0
        
        return res
