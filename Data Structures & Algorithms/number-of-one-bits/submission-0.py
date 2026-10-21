class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_count = 0

        while n:
            ones_count += n % 2 
            n = n >> 1
        
        return ones_count
        