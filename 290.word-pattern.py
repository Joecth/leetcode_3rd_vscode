#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.41%)
# Likes:    1021
# Dislikes: 144
# Total Accepted:    182.5K
# Total Submissions: 498.1K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # return self.Failed_not_Bijection(pattern, str)
        return self.fix_Bijection_O_2xN(pattern, str)
    
    def fix_Bijection_O_2xN(self, pattern, str):
        s_list = str.split()
        if len(pattern) != len(s_list):
            return False
        map_ps = {}
        for i in range(len(pattern)):
            # pattern[i] ==> s_list[i]
            if pattern[i] in map_ps:
                if map_ps[pattern[i]] != s_list[i]:
                    return False
            else:
                map_ps[pattern[i]] = s_list[i]
        
        map_str = {}
        for j in range(len(s_list)):
            if s_list[j] in map_str:
                if map_str[s_list[j]] != pattern[j]:
                    return False
            else:
                map_str[s_list[j]] = pattern[j]
        
        return True
        
    def Failed_not_Bijection(self, pattern, str):
        s_list = str.split()
        if len(pattern) != len(s_list):
            return False
        map_ps = {}
        for i in range(len(pattern)):
            # pattern[i] ==> s_list[i]
            if pattern[i] in map_ps and map_ps[pattern[i]] != s_list[i]:
                    return False
            else:
                map_ps[pattern[i]] = s_list[i]
        
        return True
    
    def old():
        # a --> dog
        # b --> cat
        l_str_split = str.split(' ')
        if len(pattern) != len(l_str_split):
            return False
        d = {}
        l_pat, l_str = [], []
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = l_str_split[i]
            else:
                if d[pattern[i]] != l_str_split[i]:
                    return False
            
            if pattern[i] not in l_pat:
                l_pat.append(pattern[i])
            if l_str_split[i] not in l_str:
                l_str.append(l_str_split[i])
        
        return len(l_pat) == len(l_str)
                
# @lc code=end

