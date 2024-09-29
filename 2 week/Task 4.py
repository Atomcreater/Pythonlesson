#227. Basic Calculator II
#https://leetcode.com/problems/basic-calculator-ii/description/?envType=problem-list-v2&envId=string
class Solution:
    def calculate(self, s: str) -> int:
        value, n = 0, len(s)
        sign = '+'
        stack = []

        for i, char in enumerate(s):
            if char.isdigit():
                value = value * 10 + int(char)

            if i == n - 1 or char in '+-*/':
                if sign == '+':
                    stack.append(value)
                elif sign == '-':
                    stack.append(-value)
                elif sign == '*':
                    stack.append(stack.pop() * value)
                elif sign == '/':

                    stack.append(int(stack.pop() / value))

                sign = char

                value = 0

        return sum(stack)
