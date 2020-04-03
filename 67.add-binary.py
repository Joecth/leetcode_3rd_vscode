#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (42.68%)
# Likes:    1487
# Dislikes: 254
# Total Accepted:    404.3K
# Total Submissions: 946.7K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return self.helper_old(a, b)
        return self.helper(a, b)
    def helper(self, a, b):
        if not a: return b
        if not b: return a
        
        if len(a) < len(b):
            a, b = b, a
            
        a, b = a[::-1], b[::-1]
        carry = i = 0
        res = ''
        while i < len(a):
            m, n = ord(a[i]) - ord('0'), 0
            if i < len(b):
                n = ord(b[i]) - ord('0')
            total = m + n + carry
            carry, digit = total//2, total%2
            res += str(digit)
            i += 1
            
        if carry:
            res += str(carry)
        return res[::-1]        
# @lc code=end

