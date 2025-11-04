class Solution:
    def evalRPN(self, tokens) -> int:

        stack = []

        for value in tokens:
            if value.lstrip('-').isdigit():
                stack.append(int(value))
            else:
                b = stack.pop()
                a = stack.pop()
                if value == "+":
                    stack.append(a + b)
                elif value == "-":
                    stack.append(a - b)
                elif value == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[0]
            

        