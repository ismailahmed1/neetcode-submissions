class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for i in s:
            sMap[i] +=1
        
        for i in t:
            tMap[i] +=1


        return sMap == tMap