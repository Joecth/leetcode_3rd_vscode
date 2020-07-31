#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (62.33%)
# Likes:    1956
# Dislikes: 79
# Total Accepted:    156.5K
# Total Submissions: 250.5K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#

# @lc code=start
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n+1)]
        self._ranks = [1 for i in range(n+1)]
    
    def Find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.Find(self._parents[u])
        return self._parents[u]
        # while u != self._parents[u]:
        #     self._parents[u] = self._parents[self._parents[u]]
        #     u = self._parents[u]
        # return u
    
    def Union(self, u, v):
        pu = self.Find(u)
        pv = self.Find(v)
        if pu == pv: 
            return False
        if self._ranks[pv] < self._ranks[pu]:
            self._parents[pv] = pu
        elif self._ranks[pv] > self._ranks[pu]:
            self._parents[pu] = pv
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True

'''
1 1 1 1 0
1 1 0 1 0
1 1 0 1 0
0 0 0 0 0
'''
from collections import deque
DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        # return self.dfs_main(grid)
        n, m = len(grid), len(grid[0])
        uf = UnionFindSet(n*m)
        count = n * m
        for i in range(n):
            for j in range(m):
                # if grid[i][j] == '1':
                if grid[i][j] == 1:
                    if j < m-1 and grid[i][j+1] == 1:
                        # if uf.Union(grid[i][j], grid[i][j+1]):
                        if uf.Union(i*m+j, i*m+j+1):
                            count -= 1
                    if i < n-1 and grid[i+1][j] == 1:
                        # if uf.Union(grid[i][j], grid[i+1][j]):
                        if uf.Union(i*m+j, (i+1)*m+j):
                            count -= 1
                else:# if grid[i][j] == '0':
                    count -= 1
            # print(count)
        
        d = collections.defaultdict(int)
        for i in range(n*m+1):
            d[uf.Find(i)] += 1
        # print(d)
        if count == 0:
            return 0
        return max(d.values())
        # return count
        
    def dfs_main(self, grid):
        n, m = len(grid), len(grid[0])
        visited = set()
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.dfs(grid, i, j, visited)
                    count += 1
                    # print('count: ', count)
        return count

    def dfs(self, grid, i, j, visited):
        visited.add((i, j))
        # print(i, j)
        for delta_i, delta_j in DIRECTIONS:
            next_i = i + delta_i
            next_j = j + delta_j
            if self.is_valid(grid, next_i, next_j, visited):
                self.dfs(grid, next_i, next_j, visited)
    
    def is_valid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y] == '0':
            return False
        return True
        
        
# @lc code=end

