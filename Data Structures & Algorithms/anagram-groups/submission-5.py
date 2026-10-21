class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordMap = defaultdict(list)

        for word in strs:
            charArr = [0] * 26
            for ch in word:
                charArr[ord(ch) - ord("a")] += 1
            
            wordMap[tuple(charArr)].append(word)
        
        res = []

        for lst in wordMap.values():
            res.append(lst)
        
        return res

