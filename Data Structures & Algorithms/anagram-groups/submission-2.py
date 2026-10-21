class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_arr = []
        res = defaultdict(list)
        for word in strs:
            tempMap = [0] * 26
            for ch in word:
                tempMap[ord(ch) - ord('a')]+=1
            
            res[tuple(tempMap)].append(word)
        
        return list(res.values())
        


