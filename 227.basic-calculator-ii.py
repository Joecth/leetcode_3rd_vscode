#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (36.70%)
# Likes:    1491
# Dislikes: 260
# Total Accepted:    190.2K
# Total Submissions: 514.9K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#

# @lc code=start
"""
case 1. 3 2 ==> 3 4 ==> sum(S)
case 2. 3   ==> 1   ==> sum(S)
case 3. same as case 1
"""

class Solution:
    def calculate(self, s: str) -> int:
        # return self.old(s)
        return self.sol_0817(s)
    def old(self, s):
        # def calculate(self, s: str) -> int:
        num = 0
        res = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                pre_op = c
        return sum(stack)
    def sol_0817(self, s):
        """
        IDEA: stack 裡的大家都是相加的
        issues:
            1. 怎麼判斷「第一個數字?!」: an integer has more than 1 digit
            2. 
        """
        stack = []
        # return self.dfs(s, 0, stack)
        # return sum(stack)
        s += "+0"      # 這行是事後諸葛, 不然最後一個oprater無法被用到，在死在 prev_op裡
        n = len(s)
        # for i in range(n):
        idx = 0
        num = 0
        prev_op = '+'   # 這行是事後諸葛
        while idx < n:
            ch = s[idx]
            if ch == ' ':
                idx += 1
                continue
            if ch in '1234567890':
                num = num * 10 + int(ch)
            else:
                assert(ch in '+-*/')
                # if ch == '+':
                if prev_op == '+':
                    stack.append(num)
                # elif ch == '-':
                elif prev_op == '-':
                    stack.append(-num)
                # elif ch == '*':
                elif prev_op == '*':
                    res = stack.pop() * num
                    stack.append(res)
                else: # prev_op == '/':
                    # else:
                        # res = stack.pop() // num # BUG for "14-3/2"
                    prev = stack.pop()
                    if prev * num >= 0:
                        res = prev // num
                    else:
                        res = abs(prev) // num
                        # else: # 不會有負號的出現，不需要
                        res = -res
                    stack.append(res)
                prev_op = ch
                num = 0
            idx += 1
            # print(stack)
        return sum(stack)

    
    
#     def dfs(self, s, idx, stack):
#         if idx == len(s):
#             return 0
#         cur = 0
#         for i in range(idx, len(s)):
#             if idx == 0:
                
#             if s[i]  == ' ':
#                 continue
#             if s[i] in "1234567890":
#                 cur = cur * 10 + int(s[i])
#             else:
#                 if s[i] == '+':
#                     stack.append(stack.pop() + cur)
#                 elif s[i] == '-':
#                     stack.append(stack.pop() - cur)
#                 elif s[i] == '*':
#                     cur = 
        
        
# @lc code=end

