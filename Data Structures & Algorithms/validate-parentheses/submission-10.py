class Solution:
    def isValid(self, s: str) -> bool:
        closeToStart = {')' : '(', '}': '{', ']': '['}
        stack = []

        for i in range(len(s)):
            if s[i] not in closeToStart:
                stack.append(s[i])
            
            elif stack and closeToStart[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        

        return len(stack) == 0
        