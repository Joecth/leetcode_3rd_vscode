#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (59.48%)
# Likes:    2585
# Dislikes: 111
# Total Accepted:    182.8K
# Total Submissions: 303.2K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        final = 0
        
        for middle in range(len(s)):
            final += self.create(s, middle, middle)
            final += self.create(s, middle, middle + 1)
            
        return final
        # https://www.jiuzhang.com/solution/palindromic-substrings/#tag-other


    def create(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1    
        
        return count        
        
# @lc code=end

