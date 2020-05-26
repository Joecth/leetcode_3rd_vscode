#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (63.20%)
# Likes:    608
# Dislikes: 928
# Total Accepted:    52.3K
# Total Submissions: 81.7K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
# 
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
# 
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
# 
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
# 
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return self.helper(piles)
        return self.helper2(piles)
    
    def helper2(self, piles):
        return True
    
    def helper(self, piles):
        cache = {}
        def firstscore(i,j):
            if i>=j: return 0
            if j==i+1 and j < len(piles): return piles[i]
            if (i,j) in cache: return cache[i,j]
            res = max(piles[i]+min(firstscore(i+2,j), firstscore(i+1,j-1)) , piles[j-1] + min(firstscore(i+1,j-1), firstscore(i,j-2)))
            cache[i,j] = res
            return res

        Alex = firstscore(0,len(piles))
        Lee = sum(piles) - Alex
        return Alex > Lee
        # https://leetcode.com/problems/stone-game/discuss/154647/python-solution-using-memorization-with-Chinese-explanation
            
# @lc code=end

