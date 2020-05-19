#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house/description/
#
# algorithms
# Easy (51.35%)
# Likes:    744
# Dislikes: 78
# Total Accepted:    81.9K
# Total Submissions: 158.9K
# Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
#
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
# 
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
# 
# Note:
# All costs are positive integers.
# 
# Example:
# 
# 
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
# into blue. 
# Minimum cost: 2 + 5 + 3 = 10.
# 
# 
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        f = costs[0]
        for i in range(1, len(costs)):
            red = min(f[1], f[2]) + costs[i][0]
            green = min(f[0], f[2]) + costs[i][1]
            blue = min(f[0], f[1]) + costs[i][2]
            f = [red, green, blue]
        return min(f)
        
    def minCost_old(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        elif n == 1:
            return min(costs[0][0], costs[0][1], costs[0][2])
        elif n == 2:
            return min(costs[0][0] + min(costs[1][1], costs[1][2]),
                       costs[0][1] + min(costs[1][2], costs[1][0]),
                       costs[0][2] + min(costs[1][0], costs[1][1]),
                      )
        # elif n == 3:
        #     return min(costs[0][0])
        
        # up to ith house, the min costs to paint the house... T
        # dp = [0 for j in len(costs)] TODO: NO USE
        
        for n in reversed(range(len(costs) - 1)):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        if len(costs) == 0: return 0
        return min(costs[0]) # Return the minimum in the first row.        
# @lc code=end

