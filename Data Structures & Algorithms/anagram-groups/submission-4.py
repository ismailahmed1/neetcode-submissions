class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordMap = defaultdict(list)

        for word in strs:
            char_array = [0] * 26
            for ch in word:
                char_array[ord(ch) - ord('a')] += 1
            
            wordMap[tuple(char_array)].append(word)
        
        return list(wordMap.values())