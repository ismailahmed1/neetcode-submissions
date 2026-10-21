class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1::]:
            i = 0 
            while i < len(prefix) and i < len(word) and word[i] == prefix[i]:
                i += 1
            prefix = prefix[0:i]
        
        if not prefix:
            return ""
        
        return prefix
        