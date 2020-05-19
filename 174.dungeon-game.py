#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game/description/
#
# algorithms
# Hard (29.16%)
# Likes:    1166
# Dislikes: 29
# Total Accepted:    83.6K
# Total Submissions: 283.6K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess.
# 
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or
# contain magic orbs that increase the knight's health (positive integers).
# 
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step.
# 
# 
# 
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
# 
# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN ->
# DOWN.
# 
# 
# 
# 
# -2 (K)
# -3
# 3
# 
# 
# -5
# -10
# 1
# 
# 
# 10
# 30
# -5 (P)
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.
# 
# 
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # return self.O_MxN(dungeon)
        return self.O_N(dungeon)
    
    def O_N(self, dungeon):
        if not dungeon or not dungeon[0]: return 1
        
        #dp[i][j] mininum life required at dungeon[i][j]
        m, n = len(dungeon), len(dungeon[0])
        dp = [0] * n
        
        # dp[n-1] = max(1 - dungeon[m-1][n-1], 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m-1 and j == n-1:
                    dp[j] = max(1 - dungeon[m-1][n-1], 1)
                elif i == m-1:
                    dp[j] = max(dp[j+1] - dungeon[i][j], 1)
                elif j == n-1:
                    dp[j] = max(dp[j] - dungeon[i][j], 1)
                else:
                    dp[j] = min(
                                    max(dp[j+1] - dungeon[i][j], 1),
                                    max(dp[j] - dungeon[i][j], 1)
                                )
        return dp[0]                 
                
    def O_MxN(self, dungeon):
        if not dungeon or not dungeon[0]: return 1
        
        #dp[i][j] mininum life required at dungeon[i][j]
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1 - dungeon[m-1][n-1], 1)
                elif i == m-1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 1)
                elif j == n-1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 1)
                else:
                    dp[i][j] = min(
                                    max(dp[i][j+1] - dungeon[i][j], 1),
                                    max(dp[i+1][j] - dungeon[i][j], 1)
                                )
        return dp[0][0]        
# @lc code=end

