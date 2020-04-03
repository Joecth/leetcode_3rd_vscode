#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.73%)
# Likes:    1732
# Dislikes: 123
# Total Accepted:    436K
# Total Submissions: 953.4K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []
            
        def helper_bf(nums, target):
            # res = None
            g_min_diff = float('inf')
            res = float('inf')
            for i in range(0, len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    for k in range(j+1, len(nums)):
                        diff = abs(nums[i] + nums[j] + nums[k] - target)
                        # print(i, j, k, diff, g_min_diff)
                        if diff < g_min_diff:
                            # print([nums[i], nums[j], nums[k]])
                            # res = [nums[i], nums[j], nums[k]]
                            g_min_diff = diff
                            res = [nums[i], nums[j], nums[k]]
            return sum(res)
        
        def helper(nums, target):
            
            nums.sort(key=lambda x:x)
            # g_min_diff = float('inf')
            res = [float('inf')]
            
            for i in range(0, len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue 
                    
                l = i+1
                r = len(nums)-1
                ## TODO: store sum in advance to make this faster
                while l < r:
                    arr = [nums[i], nums[l], nums[r]]
                    if abs(sum(arr)-target) < abs(sum(res)-target):
                        res = arr
                    if sum(arr) - target == 0:
                        # break
                        return target
                    elif sum(arr) < target:
                        l += 1
                    else:
                        r -= 1
            return sum(res)
        return helper(nums, target)

# @lc code=end

