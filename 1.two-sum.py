#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.19%)
# Likes:    14097
# Dislikes: 513
# Total Accepted:    2.7M
# Total Submissions: 6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in d:
                return [d[diff], j]
                # return [78]
            d[nums[j]] = j
        return []              

print(Solution().twoSum([3,4,6,2], 9))
# @lc code=end

