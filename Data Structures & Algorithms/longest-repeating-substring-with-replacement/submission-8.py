class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charArr = [0] * 26
        l, r = 0, 0
        maxLength = 0 

        while r < len(s):
            charArr[ord(s[r]) - ord('A')] += 1

            while (r - l + 1) - max(charArr) > k:
                charArr[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxLength = max(maxLength, (r - l + 1))
            r += 1
        

        return maxLength


            
                
                
