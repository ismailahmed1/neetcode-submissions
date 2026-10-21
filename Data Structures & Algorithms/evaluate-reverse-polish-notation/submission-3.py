class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish_stack = []
        operations = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operations:
                polish_stack.append(i)
            else:
                val = int(polish_stack.pop())
                if i == '+':
                    val += int(polish_stack.pop())
                elif i == '-':
                    val = int(polish_stack.pop()) - val 
                elif i == '*':
                    val *= int(polish_stack.pop())
                elif i == '/':
                    val = int(polish_stack.pop()) / val 
                polish_stack.append(val)

        return int(polish_stack[-1])