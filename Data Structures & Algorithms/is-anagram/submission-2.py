class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for ch in s:
            sMap[ch] += 1

        for ch in t:
            tMap[ch] += 1

        return sMap == tMap