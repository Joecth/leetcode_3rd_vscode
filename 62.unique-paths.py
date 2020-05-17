#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (51.66%)
# Likes:    2676
# Dislikes: 187
# Total Accepted:    420K
# Total Submissions: 808.8K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
# 
# 
#

# @lc code=start
"""
1 1 1 1
1 2 3 4
1 3 6 10
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.O_MxN(m, n)
        return self.O_M(m, n)
        return self.O_M_cleancode(m, n)
    
    def O_M_cleancode(self, m, n):
        dp = [0 for j in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]
    
    def O_M(self, m, n):
        dp = [1 for j in range(n)] # for the cur row
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] +         dp[j-1]
                        # dp2d[i-1][j]   dp2d[i][j-1]
        return dp[-1]
                
    def O_MxN(self, m, n):
        dp = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]   
# @lc code=end

