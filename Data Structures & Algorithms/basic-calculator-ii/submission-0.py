class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == '*':
                    prev = stack.pop()
                    stack.append(prev * num) 
                else:
                    prev = stack.pop()
                    stack.append(int(prev/num))
                op = char
                num = 0
        return sum(stack)