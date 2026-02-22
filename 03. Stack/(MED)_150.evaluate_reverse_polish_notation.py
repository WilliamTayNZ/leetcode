# COMPSCI 130 lol

# Clean solution with int(operand1 / operand2) to truncate
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append(operand1 + operand2)
            elif token == "-":
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append(operand1 - operand2)
            elif token == "*":
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append(operand1 * operand2)
            elif token == "/":
                # Use int() to truncate towards 0
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
        
        return stack[0]

class FirstTruncateSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 + operand2)
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 * operand2)
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Want to truncate towards 0
                res_floor = operand1 // operand2
                res_float = operand1 / operand2

                if res_floor >= 0:
                    stack.append(res_floor)
                elif res_floor == res_float:
                    stack.append(res_floor)
                else:
                    stack.append(res_floor + 1)
            else:
                stack.append(int(token))

        return stack[0]


# The input represents a valid arithmetic expression in a reverse polish notation.
# This means we don't have to handle invalid expressions.

# Truncate towards zero means division rounds closer to 0
# i.e rounding down when result is positive, rounding up when result is negative

# December 2nd, 2025