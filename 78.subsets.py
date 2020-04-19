#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (58.50%)
# Likes:    3130
# Dislikes: 73
# Total Accepted:    511.6K
# Total Submissions: 869.2K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.res = []
        self.helper(nums, 0, [])
        return self.res

    def helper(self, nums, idx, item):
        if idx == len(nums):
            self.res.append(item.copy())
            return

        item.append(nums[idx])
        self.helper(nums, idx+1, item)
        item.pop()
        self.helper(nums, idx+1, item)
# @lc code=end

