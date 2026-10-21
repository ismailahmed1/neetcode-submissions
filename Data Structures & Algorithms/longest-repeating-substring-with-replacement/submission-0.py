class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            max_freq = max(charMap.values())
            
            # Check if the current window is valid
            if (r - l + 1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            
            # Update the result
            res = max(res, r - l + 1)
        
        return res
