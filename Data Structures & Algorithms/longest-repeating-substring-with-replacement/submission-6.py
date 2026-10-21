class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_array = [0] * 26
        l, r = 0, 0 
        max_length = 0 

        while r < len(s):
            char_array[ord(s[r]) - ord('A')] += 1

            while (r - l + 1) - max(char_array) > k:
                char_array[ord(s[l]) - ord('A')] -= 1
                l += 1

            length = r - l + 1
            max_length = max(max_length, length)
            r += 1
            
            
        
        return max_length


                