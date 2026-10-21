class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap = [0] * 26
        runningMap = [0] * 26
        output = []

        for ch in p:
            pMap[ord(ch) - ord('a')] += 1
        
        l, r = 0, 0

        while r < len(s):
            runningMap[ord(s[r]) - ord('a')] += 1

            if (r - l + 1) > len(p):
                runningMap[ord(s[l]) - ord('a')] -= 1
                l += 1

            if runningMap == pMap:
                output.append(l)
            
            r += 1
        
        return output
            

        

