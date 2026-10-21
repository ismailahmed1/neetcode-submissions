class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        output = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, subs):
            if i == len(digits):
                output.append(subs)
                return
            
            for ch in digitToChar[digits[i]]:
                dfs (i + 1, subs + ch)
        
        dfs(0, "")
        return output