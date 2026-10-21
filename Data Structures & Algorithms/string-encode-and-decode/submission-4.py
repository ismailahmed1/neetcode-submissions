class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res


    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0 

        while r < len(s):
            while s[r] != "#":
                r += 1
                continue

            wordLen = s[l: r]

            l = r + 1
            r = l + int(wordLen)
            res.append(s[l: r])
            l = r
        
        return res




        


