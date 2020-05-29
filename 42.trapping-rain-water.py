#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.17%)
# Likes:    6553
# Dislikes: 114
# Total Accepted:    486.3K
# Total Submissions: 1M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        l_dp = [0 for _ in range(n)]
        l_dp[0] = height[0]
        for i in range(1, n):
            l_dp[i] = max(l_dp[i-1], height[i])

        r_dp = [0 for _ in range(n)]
        r_dp[n-1] = height[n-1]
        for j in reversed(range(0, n-1)):
            r_dp[j] = max(r_dp[j+1], height[j])

        ans = 0#[0] * n
        for k in range(n):
            ans += (min(l_dp[k], r_dp[k]) - height[k]) * 1
        
        return ans

# @lc code=end

