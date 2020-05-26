#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (36.22%)
# Likes:    2484
# Dislikes: 62
# Total Accepted:    167.4K
# Total Submissions: 455.1K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        
        h = [0 for j in range(n)]
        g_max = cur = 0
        for i in range(m):
            # level_h = h.copy()
            for j in range(n):
                # level_h[j] += matrix[i][j]
                if matrix[i][j] == "1":
                    h[j] += 1
                else:
                    h[j] = 0
            # print(h)
            cur = self.largestRectangleArea(h)
            g_max = max(g_max, cur)
        return g_max
                
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)

        # left[i], right[i] represent how many bars are >= than the current bar

        left = [1] * n
        right = [1] * n
        max_rect = 0

        # calculate left
        for i in range(0, n):
            # for k in range(l): BF
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]    # For case like [3,9,8, 6,5,2], now is 2, thus should still check heights[j] to get "3"
                else: break

        # calculate right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, heights[i] * (left[i] + right[i] - 1))

        return max_rect
        # ref:https://leetcode.flowerplayer.com/2019/04/16/leetcode-84-largest-rectangle-in-histogram-%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af%e5%88%86%e6%9e%90/            
# @lc code=end