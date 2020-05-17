#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.96%)
# Likes:    1513
# Dislikes: 228
# Total Accepted:    278.2K
# Total Submissions: 817.2K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.O_MxN(obstacleGrid)
        # return self.O_M(obstacleGrid)
        return self.O_M_cleancode(obstacleGrid)
    
    def O_M_cleancode(self, obstacles):
        m, n = len(obstacles), len(obstacles[0])
        
        if obstacles[0][0]==1: return 0
        dp = [0 for j in range(n)]
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacles[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j-1]
        return dp[-1]
    
    def O_M(self, obstacles):
        m, n = len(obstacles), len(obstacles[0])
        
        if obstacles[0][0] == 1: return 0
        
        # dp = [[1 for j in range(n)] for i in range(m)]
        dp = [1 for j in range(n)]
        for j in range(1, len(dp)):
            if obstacles[0][j]:
                dp[j] = 0
            else:
                dp[j] = dp[j-1]
        
        for i in range(1, m):
            for j in range(0, n):
                if obstacles[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0: 
                        dp[j] = dp[j-1] + dp[j] # L + Upper
                # print(dp, i, j)
        return dp[-1]
    
    def O_MxN(self, obstacleGrid):
        # if not obstacleGrid:
        #     return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # if i == 0 or j == 0:
                    #     dp[i][j] = 1      ## cannot solve case: obstacleGrid==[[1,0]] 
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
# @lc code=end

