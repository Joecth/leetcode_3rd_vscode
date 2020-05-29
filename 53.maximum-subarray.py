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
        return self.O_1(nums)
        return self.O_N(nums)
    
    def O_1(self, nums):
        n = len(nums)
        if n == 0: return 0
        ans = dp = nums[0]  # dp: cur_max; ans: global max
        for i in range(1, n):
            # dp = max(dp, dp+nums[i])  # WRONG CONCEPT
            dp = max(dp+nums[i], nums[i])
            ans = max(ans, dp)
        return ans
        
    def O_N(self, nums):
        n = len(nums)
        if n == 0: return 0
        # maximum subarr, with ith not included
        dp = [0 for i in range(n+1)]
        ans = dp[0] = nums[0]
        """ WRONG
        dp[1] = max(dp[0], dp[0]+nums[1], nums[1])
        dp[2] = max(dp[1], dp[1]+nums[2], nums[2])
        """
        """ CORRECT
        dp[1] = max(dp[0]+nums[1], nums[1])
        dp[2] = max(dp[1]+nums[2], nums[2])
        """
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ans = max(ans, dp[i])
        
        return ans
# @lc code=end

