#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (34.51%)
# Likes:    1063
# Dislikes: 2739
# Total Accepted:    547.3K
# Total Submissions: 1.6M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return self.helper1(s)
        return self.helper2(s, 0, len(s)-1)
    
    def helper2(self, s, a, b):
        start, end = a, min(len(s)-1, b)
        
        # while start + 1< end:  # side by side if even, and same one if odd, for pure string
        while start < end:
            # left, right = s[start], s[end]
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
                
            if s[start].lower() != s[end].lower():
                return False
                
            start += 1
            end -= 1
        return True
    
    def helper1(self, s):
        start, end = 0, len(s)-1
        # while start + 1< end:  # side by side if even, and same one if odd, for pure string
        while start < end:
            # left, right = s[start], s[end]
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
                
            if s[start].lower() != s[end].lower():
                return False
                
            start += 1
            end -= 1
        return True
    
#     def isPalindrome_old(self, s: str) -> bool:
#         l, r = 0, len(s)-1
        
#         while l < r:
#             while l < r and not s[l].isalnum():
#                 l += 1
#             while l < r and not s[r].isalnum():
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             else:
#                 l += 1
#                 r -= 1
#         return True
# @lc code=end

