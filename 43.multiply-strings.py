#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (32.87%)
# Likes:    1666
# Dislikes: 760
# Total Accepted:    285.1K
# Total Submissions: 853.6K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
#     res = [0] * (len(num1) + len(num2))
#     for i in xrange(len(num1)-1, -1, -1):
#         carry = 0
#         for j in xrange(len(num2)-1, -1, -1):
#             tmp = int(num1[i])*int(num2[j])+carry 
#             # take care of the order of the next two lines
#             carry = (res[i+j+1] + tmp) // 10  
#             res[i+j+1] = (res[i+j+1] + tmp) % 10
#             # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
#         res[i] += carry
#     res = "".join(map(str, res))
#     return '0' if not res.lstrip("0") else res.lstrip("0")    
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': 
            return '0'
        res = [0] * (len(num1) + len(num2))
        
        carry = 0
        for i in reversed(range(len(num1))):
            carry = 0
            for j in reversed(range(len(num2))):
                m = ord(num1[i]) - ord('0')
                n = ord(num2[j]) - ord('0')
                total =  m * n + carry
                # take care of the order of the next two lines
                carry = (res[i+j+1] + total) // 10 
                res[i+j+1] = (res[i+j+1] + total) % 10
            # print(total, l, carry)
            res[i] += carry

        
        ans = ''.join(map(str, res))
        return ans.lstrip('0')
        # https://leetcode.com/problems/multiply-strings/discuss/17746/Python-easy-to-understand-solution-without-overflow-(with-comments).
                          
        
    def multiply_old(self, num1: str, num2: str) -> str:
        a = self.string2num(num1)
        b = self.string2num(num2)
        
        return str(a*b)
        
    def string2num(self, n):
        ret = 0
        for i in range(len(n)):
            digit = ord(n[i]) - ord('0')
            ret = 10*ret + digit
        
        return ret
        
            
# @lc code=end

