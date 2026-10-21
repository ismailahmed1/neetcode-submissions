class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range (n + 1):
            ones = 0 
            for i in range (32):
                if num & (1 << i):
                    ones += 1
                    
            output.append(ones)
        return output
        