#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (35.01%)
# Likes:    1017
# Dislikes: 470
# Total Accepted:    228K
# Total Submissions: 632.8K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # return self.my_sol(tokens)
        return self.sol(tokens)
    
    def sol(self, tokens):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()
    
    def my_sol(self,tokens):
        op = ['+', '-', '*', '/']
        stack = []
        
        for i in range(len(tokens)):
            # print(stack) 
            if tokens[i] in op:
                t = tokens[i]
                a = stack.pop()
                b = stack.pop()
                res = 0
                if t == '+':
                    res = a + b
                elif t == '-':
                    res = b - a
                elif t == '*':
                    res = a * b
                else:
                    # res = abs(b / a) // 1
                    res = int(b / a)
                stack.append(res)
                continue
            stack.append(int(tokens[i]))
        return int(stack[-1])        
# @lc code=end
