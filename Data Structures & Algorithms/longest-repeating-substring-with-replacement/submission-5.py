class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        for i in range(26):
            char_count[chr(ord('A') + i)] = 0
        max_count = 0 
        l, r = 0, 0

        while r < len(s):
            char_count[s[r]] += 1
            if (r - l + 1) - max(char_count.values()) <= k:
                count = r - l + 1
            else:
                char_count[s[l]] -= 1 
                l += 1

            r+= 1

            max_count = max(max_count, count)
        
        return max_count


            



