class Solution:
    def isValid(self, s: str) -> bool:
        input_stack =[]
        char_map = {')' : '(', ']' : '[', '}' : '{'}

        for ch in s:
            if ch in char_map:
                if input_stack and input_stack[-1] == char_map[ch]:
                    input_stack.pop()
                else:
                    return False
            else:
                input_stack.append(ch)
        
        return (len(input_stack) == 0)

        