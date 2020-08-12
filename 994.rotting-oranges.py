#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (47.55%)
# Likes:    2219
# Dislikes: 188
# Total Accepted:    145K
# Total Submissions: 294.4K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
# 
#

# @lc code=start
class OrangeType(object):
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        Q = collections.deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == OrangeType.ROTTEN:
                    Q.append((i, j))
                if grid[i][j] == OrangeType.FRESH:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        # print(Q)
        days = 0
        affected = set()    # visited
        while Q:
            # print(Q)
            for _ in range(len(Q)):
                now_i, now_j = Q.popleft()
                for delta_i, delta_j in DIRECTIONS:
                    next_i = now_i + delta_i
                    next_j = now_j + delta_j
                    # check valid!
                    # 1. check coordinate
                    # 2. check whether visited
                    # 3. check original OrangeType  ! CAUTIOUS! EMPTY ALSO not OK!
                    if self.is_valid(next_i, next_j, grid, affected):
                        Q.append((next_i, next_j))
                        affected.add((next_i, next_j))
            days += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == OrangeType.FRESH and (i, j) not in affected:
                    return -1
        return days-1
    
    def is_valid(self, i, j, grid, affected):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if (i, j) in affected:
            return False
        if grid[i][j] == OrangeType.ROTTEN or grid[i][j] == OrangeType.EMPTY:
            return False
        return True
        
# @lc code=end

