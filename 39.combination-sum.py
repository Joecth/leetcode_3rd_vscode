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
        # self.helper(candidates, target, 0, 0, [])
        self.helper_2way(candidates, target, 0, [])
        return self.res
    
    def helper_2way(self, nums, target, idx, item):
        if len(nums) == idx:
            return 
        
        if target == 0:
            self.res.append(item.copy())
            return
        
        # [2,2,3], [7]
        # [2,2,3], [2,3,2], [3,2,2], [7]
        for i in range(idx, len(nums)): # idx: depth of bactktracking
            if target > 0:  #　TODO: SORT first is better!
                target -= nums[i]
                item.append(nums[i])
                # self.helper_2way(nums, target, idx+1, item)   # SHOULDN'T GO BACK PREV elem
                self.helper_2way(nums, target, i, item)
                item.pop()
                target += nums[i]
        """
        if idx == len(nums):
            return
        if target-nums[idx] == 0:
            self.res.append(item.copy())    # FAILED when 7 is last elem 
            return
        # self.helper_2way(nums, target-nums[idx], idx+1, item+[nums[idx]]) 
        self.helper_2way(nums, target, idx+1, item)
        """
        
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
            
            # item += []
            # self.helper(nums, target, i, sum_+nums[i], item)
    
    
#     def combinationSum_old(self, candidates: List[int], target: int) -> List[List[int]]:
#         if not candidates: 
#             return []
#         self.result = []
#         # self.counters = {}
#         l = sorted(candidates, key=lambda val: val)
#         self.helper(l, 0, target, [], 0)
        
#         return self.result

#     '''
    
#     '''
#     def helper(self, l, idx, rem, item, level):
#         if rem == 0:
#             self.result.append(item.copy())
#             return
#         if idx == len(l) or rem < l[idx] or rem < 0:
#             return
        
#         # 2 3 6 7     7               2
#         elem = l[idx]
#         item.append(elem)
#         rem -= elem
#         # if rem < elem:        SHOULDN'T TRUNCATE HERE 
#         #     return      #1 < 2       2 2 
#         self.helper(l, idx, rem, item, level+1)
#         item.pop()
#         rem += elem
#         self.helper(l, idx+1, rem, item, level+1)
                            
# @lc code=end

