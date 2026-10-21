class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1: r]
        
        best = ""
        for i in range (len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            best = max(best, even, odd, key=len)
        
        return best

        