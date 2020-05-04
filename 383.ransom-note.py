#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (51.65%)
# Likes:    547
# Dislikes: 187
# Total Accepted:    193.6K
# Total Submissions: 362.8K
# Testcase Example:  '"a"\n"b"'
#
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return
# false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return ransomNote in magazine
        r_map = Counter(ransomNote)
        m_map = Counter(magazine)

        for k in r_map.keys():
            if k not in m_map or m_map[k] < r_map[k]:
                return False
            # m_map[k] -= 1
    
        return True        
# @lc code=end

