#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (44.87%)
# Likes:    2433
# Dislikes: 177
# Total Accepted:    266.8K
# Total Submissions: 587.5K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize for i in range(n+1)]
        dp[0] = 0
        
        for i in range(0, n+1):
            x = 1
            while x*x <= i:
                dp[i] = min(dp[i], 1+dp[i-x*x])
                x += 1
        return dp[-1]        
# @lc code=end

