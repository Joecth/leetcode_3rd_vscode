#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (45.10%)
# Likes:    4620
# Dislikes: 173
# Total Accepted:    609.1K
# Total Submissions: 1.3M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
'''
1 1 1 1 0
1 1 0 1 0
1 1 0 1 0
0 0 0 0 0
'''
# for 
#     for 
#         bfs_graph
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time complexity : O(M×N) where M is the number of rows and N is the number of columns.
        Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).
        """
        if not grid or not grid[0]: return 0;
        # visited = ['X'*len(grid[0]) for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Starts BFS
                if grid[i][j] == '1':
                    self.helper(i, j, grid)
                    count += 1
                    
        return count
    
    def helper(self, r, c, grid):
        Q = deque()
        Q.append((r, c))
        dr = [-1, 0, 1,  0]
        dc = [0,  1, 0, -1]

        while Q:
            I, J = Q.popleft()
            for idx in range(4):
                i, j = I+dr[idx], J+dc[idx] 
                if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j] != '1':
                    continue
                Q.append((i, j))
                grid[i][j] = 'X'


    def helper_old(self, i, j, grid):
        Q = deque()
        # Q.push((grid[i][j], i, j))
        Q.append((i, j))
        while Q:
            i, j = Q.popleft()
            
            # up, down, left, right
            if i > 0 and grid[i-1][j] == '1' :
                Q.append((i-1, j))
                grid[i-1][j] = 'X'
            if j > 0 and grid[i][j-1] == '1':
                Q.append((i, j-1))
                grid[i][j-1] = 'X'
            if i < len(grid)-1 and grid[i+1][j] == '1':
                Q.append((i+1, j))
                grid[i+1][j] = 'X'
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                Q.append((i, j+1))
                grid[i][j+1] = 'X'

# print('aaaaa')
print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
# @lc code=end

