#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.34%)
# Likes:    3870
# Dislikes: 127
# Total Accepted:    635.3K
# Total Submissions: 1.4M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#

# @lc code=start
"""
0 1
1 1
2 2
3 dp0
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # self.d = {0:1, 1:1}
        # return self.dfs(n)
        
        # return self.O_N(n)
        # return self.O_1(n)
        return self.O_1_rollingArray(n)
    
    def dfs(self, n):
        # if n in self.d:
        #     return self.d[n]
        if n not in self.d:
            tmp = self.dfs(n-1) + self.dfs(n-2)
            self.d[n] = tmp
        return self.d[n]
    
    def O_1(self, n):
        if n <= 1:
            return 1
        dp0 = dp1 = 1
        ans = 0
        for i in range(2, n+1):
            ans = dp0 + dp1
            dp0 = dp1
            dp1 = ans
            
        return ans
            
    def O_N(self, n):
        # dp0, dp1 = 1, 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # dp[2] = dp[0] + dp[1]
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
    def O_1_rollingArray(self, n):
        # dp = [0] * (n+1)
        dp = [0] * 3
        dp[0] = 1
        dp[1] = 1
        # dp[2] = dp[0] + dp[1]
        # for i in range(2, len(dp)):
        for i in range(2, n+1):
            dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
        
        # return dp[-1]    
        return dp[n%3]
# @lc code=end

