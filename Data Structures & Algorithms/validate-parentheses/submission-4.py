class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        s_stack = []

        for i in range (len(s)):
            if i > 0 and len(s_stack)!= 0 and s[i] in bracket_map and bracket_map[s[i]] == s_stack[-1]:
                    s_stack.pop()
            else:
                s_stack.append(s[i])
        
        return len(s_stack) == 0

            