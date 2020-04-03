#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.86%)
# Likes:    6730
# Dislikes: 303
# Total Accepted:    833.5K
# Total Submissions: 1.8M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper_O_k(nums):
            if len(nums) < 2:
                return nums[0]

            # dp = [0] * len(nums)
            dp0 = nums[0]
            dp1 = max(dp0+nums[1], nums[1])
            g_max = max(dp0, dp1)
            
            for i in range(2, len(nums)):   # TODO: start from 1 to make this faster 
                # dp0, dp1 = max(), dp0
                # dp2 = max(dp1 + nums[2], nums[2])
                tmp = max(dp1 + nums[i], nums[i])
                dp1 = tmp
                g_max = max(dp1, g_max)
                
            return g_max
            
        def helper_O_N(nums):
            if len(nums) < 2:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0]+nums[1], nums[1])
            g_max = max(dp[0], dp[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1]+nums[i], nums[i])
                g_max = max(g_max, dp[i])
            return g_max
        return helper_O_k(nums)        
# @lc code=end

