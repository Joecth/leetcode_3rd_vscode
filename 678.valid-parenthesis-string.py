#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (34.00%)
# Likes:    1384
# Dislikes: 43
# Total Accepted:    76.4K
# Total Submissions: 243.4K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].
# 
# 
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.helper(s)

    def helper(self, s):
        l = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                l.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if l: 
                    l.pop()
                elif star:
                    star.pop()
                else: # not l and not star:
                    return False
        if not l:
            return True

        # open left issue:
        while l:
            if not star:
                return False
            
            if l[-1] > star[-1]:
                return False
            else:
                l.pop()
                star.pop()

        return True

    def helper_TLE(self, s, n):
        # n = 0
        for i in range(len(s)):
            if s[i] == '(':
                n += 1
            elif s[i] == ')':
                n -= 1
                if n < 0 :
                    return False
            elif s[i] == '*':
                return self.helper(s[i+1:], n+1) or self.helper(s[i+1:], n-1) or self.helper(' '+s[i+1:], n)
            else:
                pass
                
        # print(n)
        return n == 0        
# @lc code=end

