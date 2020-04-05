#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.63%)
# Likes:    3006
# Dislikes: 4751
# Total Accepted:    1M
# Total Submissions: 3.9M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
   def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1

        a = abs(x)
        s = ''
        for ch in str(a):
            s = ch + s

        ans = int(s) 
        if sign == 1:
            MAX = 2**31-1
            if ans > MAX:
                return 0
            return ans
            # return min(ans, 2**31-1)
        else:
            MAX = 2**31
            if ans > MAX:
                return 0
            return -1 * ans
# @lc code=end