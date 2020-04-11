#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (53.82%)
# Likes:    3202
# Dislikes: 101
# Total Accepted:    487.8K
# Total Submissions: 903.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#

# @lc code=start
"""
[2,3,6,7]
"""
from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if not candidates: return []
        self.res = []
        self.helper(candidates, target, 0, 0, [])
        # print(self.res)
        return self.res
    
    def helper(self, nums, target, i_start, sum_, item):    
        # idx means starting positin in for loop in next recursion
        if sum_ == target:
            self.res.append(item.copy())
            return
        if sum_ > target:
            return 
        
        for i in range(i_start, len(nums)):
            item += [nums[i]]
            self.helper(nums, target, i, sum_+nums[i], item)    # 同位置可重覆選，所以用i            
            item.pop()
                    
# @lc code=end

