#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (33.71%)
# Likes:    3018
# Dislikes: 76
# Total Accepted:    234K
# Total Submissions: 692.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#

# @lc code=start
'''
heights      [2 1 5 6 2 3]
dis_l        [0 1 0 0 3 0]
dis_r        [0 4 1 0 1 0]

For idx in range(len(heights)):
    (dis_l + 1 + dis_r) * heights[idx]

res   [0 (1+4+1)*1, (0+1+1)*2, 0, (1+1+1)*2, 0]
return max(res)
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # return self.greedy(heights)
        return self.mono_stack(heights)
    
    def mono_stack(self, heights):
        # pass
        # https://www.youtube.com/watch?v=GYuBQacXr1A
        n = len(heights)
        stack = []
        stack.append(-1)
        
        g_max = 0
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                g_max = max(g_max, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        # print(stack)
        
        while stack[-1] != -1:
            g_max = max(g_max, heights[stack.pop()] * (n - stack[-1] - 1))
        
        return g_max
        
        
    def greedy(self, heights):
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

