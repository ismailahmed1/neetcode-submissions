class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + '#' + word
        return output
            

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0 
        output = []

        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l : r ])

            l = r + 1
            r += length
            word = s[l:r + 1]
            output.append(word)
            l = r + 1
            r = l 
        
        return output