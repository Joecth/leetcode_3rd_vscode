#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (49.72%)
# Likes:    936
# Dislikes: 80
# Total Accepted:    140.2K
# Total Submissions: 279.7K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # return self.helper(s)
        return self.tricks(s)
        
    # Time: O(N):
    # Space: O(N) 
    def tricks(self, s):
        set_ = set()
        for i in range(len(s)):
            if s[i] not in set_:
                set_.add(s[i])
            else:
                set_.remove(s[i])
                
        if len(set_) == 0:
            return len(s)
        else:
            return len(s) - len(set_) + 1          
    
    # Time: O(N + K): K: num of keys
    # Space: O(N)
    def helper(self, s):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
            
        count = 0
        has_odd = False
        for k in d.keys():
            if d[k] % 2 != 0:
                count += d[k] - 1
                has_odd = True
            else:
                count += d[k]
        return count + 1 if has_odd else count        
    def old():
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            
        res = 0
        max_odd = 0
        flag = 0
        for k in d.keys():
            if not d[k] % 2:
                res += d[k]
            else:
                # max_odd = max(max_odd, d[k])
                res += d[k] - 1
                flag = 1
                
        return res + flag        
# @lc code=end

