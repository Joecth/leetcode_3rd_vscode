#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.65%)
# Likes:    4331
# Dislikes: 128
# Total Accepted:    486.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums : return 0
        if len(nums) == 1: return nums[0]
        # return self.O_1(nums)
        # return self.O_SeqDP_2xN(nums)
        return self.O_SeqDP_2x1_arr(nums)
    
    def O_SeqDP_2x1_arr(self, nums):
        n = len(nums)
        
        """
        dp[0]: no-rob
        dp[1]: rob
        """
        dp = [0 for i in range(2)]
        dp[1] = nums[0]
        
        for j in range(1, n):
            prev_norob = dp[0]
            dp[0] = max(dp[0], dp[1])
            dp[1] = prev_norob + nums[j]
            # print(dp)
        return max(dp)
        
    
    def O_SeqDP_2x1(self, nums):
        n = len(nums)
        norob = 0
        rob = 0
        
        for j in range(n):
            prev_norob = norob
            norob = max(norob, rob)
            rob = prev_norob + nums[j]
        return max(norob, rob)
    
    def O_SeqDP_2xN(self, nums):
        """
        # dp[0][j] up to jth house, no-rob, max profit
        # dp[1][j] up to jth house, rob, max profit
        """
        n = len(nums)
        dp = [[0] * n for i in range(2)]
        # print(dp)
        
        for j in range(n):
            dp[0][j] = max(dp[0][j-1], dp[1][j-1])
            dp[1][j] = dp[0][j-1] + nums[j]
        # print(dp)            
        return max(dp[-1])
    
    def O_1(self, nums):
        n = len(nums)
                
        dp = [nums[0], max(nums[0], nums[1]), 0]
        if n == 0: 
            return 0
        elif n <= 2:
            return dp[n-1]
        
        for i in range(2, n):
            dp[i%3] = max(dp[(i-2)%3]+nums[i], dp[(i-1)%3])
        
        return dp[(n-1)%3]
        
    def O_N(self, nums):
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums[0],           nums[1])
        elif n == 3: return max(nums[0] + nums[2], nums[1])

        # up to ith house, maximum $ I can get
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # dp[2] = max(dp[0] + nums[2], dp[1]) 
                    
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
    
    
    def rob_old(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0]+ nums[2], nums[1]) 
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        dp[2] = max(dp[0]+ nums[2], dp[1])
        
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        return dp[i]
            
                    
# @lc code=end

