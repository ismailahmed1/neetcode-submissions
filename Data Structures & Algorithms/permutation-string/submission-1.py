class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:   
        count1 = {}
        for i in range(26):
            count1[chr(ord('a') + i)] = 0
        for ch in s1:
            count1[ch] += 1

        count2 = {}
        for i in range(26):
            count2[chr(ord('a') + i)] = 0
        #lecaabee
        #count1 = {a: 1, b: 1, c: 1}
        #s1 = "abc", s2 = "lecabee"
        # count2 = {l: 0, e: 1, c: 1}
    
        l, r = 0, 0 
        while r < len(s2):
            count2[s2[r]] += 1
            if count1 == count2:
                return True
            if (r - l) == len(s1) - 1:
                count2[s2[l]] -= 1
                l += 1
            r += 1
        
        return False


    