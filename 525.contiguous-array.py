#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (44.94%)
# Likes:    1232
# Dislikes: 58
# Total Accepted:    66.5K
# Total Submissions: 154.7K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#

# @lc code=start
"""
        1 1 1 0 0 1 0 0 1 
sum   0 1 2 3 2 1 2 1 0 1
i       0 1 2 3 4 5 6
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        d = {0:-1}
        ans = tmp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp -= 1
            else:
                tmp += 1
            
            if tmp in d:
                ans = max(i - d[tmp], ans)
            else:
                pass # 不需要更新i，因為是要找最長的
                d[tmp] = i
        return ans

# @lc code=end

