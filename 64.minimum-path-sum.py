#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (51.32%)
# Likes:    2389
# Dislikes: 52
# Total Accepted:    340.6K
# Total Submissions: 655.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
"""
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
 0 0 0.          0
 0 1 4           5
 0 2 min(2,4)+5  min(7,5)+1
 0 6 min(6,7)+2  min(8,6)+1

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # return self.O_MxN(grid)
        return self.O_N(grid)
    
    def O_N(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0 for j in range(n)]
        # dp[0] = grid
        for i in range(m):
            for j in range(n):
                # dp[j] = 
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
    
    def O_MxN(self, grid):
        if not grid or not grid[0]:
            return 0
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        
    def minPathSum_old(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        dp = [[0 for j in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i == 1:
                    dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
                elif j == 1:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
                else: # (0 <= i <=len(dp)-1) and (0 <=j <= len(dp[0])-1):
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]
        # print(dp)
        return dp[-1][-1]

# @lc code=end

