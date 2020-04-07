#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.80%)
# Likes:    2186
# Dislikes: 1723
# Total Accepted:    676.8K
# Total Submissions: 1.9M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        res = strs[0] 
        for i in range(1, len(strs)):
            s = strs[i]
            
            # tmp = ''
            count = 0
            for j in range(min(len(res), len(s))):  # TODO: pick the shortest str in strs instead of strs[0] as global res at very beginning to make this faster
                                                    # AND, make this as outer loop instead of inner loop
                if res[j] != s[j]:
                    break
                # tmp += res[j]
                count += 1
                
            # print(count) 
            res = res[:count]  
        return res
                
        
#     def longestCommonPrefix_old(self, strs: List[str]) -> str:
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
        
#         shortest = min(strs, key=len)
#         for i, ch in enumerate(shortest):
#             for other in strs:
#                 if other[i] != ch:
#                     return shortest[:i]
#         return shortest
        
# @lc code=end

