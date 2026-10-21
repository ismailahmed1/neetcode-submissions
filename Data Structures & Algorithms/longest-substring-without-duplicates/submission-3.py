class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        length = 0 
        max_length = 0 

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                length += 1
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    length -= 1
            
            max_length = max(max_length, length)

        return max_length