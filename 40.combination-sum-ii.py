#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (46.06%)
# Likes:    1451
# Dislikes: 56
# Total Accepted:    298K
# Total Submissions: 645K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
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
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = set()
        self.helper(candidates, target, 0, 0, [])
        # print(self.res)
        return [list(item) for item in self.res]
    
    def helper(self, nums, target, i_start, sum_, item):
        if sum_ == target:
            # self.res += [item.copy()]
            self.res.add(tuple(item))
            return 
        if sum_ > target:
            return 
        
        for i in range(i_start, len(nums)):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            item += [nums[i]]
            self.helper(nums, target, i+1, sum_+nums[i], item)
            item.pop()        
# @lc code=end

