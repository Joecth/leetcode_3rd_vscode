#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (39.80%)
# Likes:    1189
# Dislikes: 236
# Total Accepted:    72.7K
# Total Submissions: 179.4K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

# @lc code=start
DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        # return self.fr_mountain(matrix)
        return self.fr_sea(matrix)  # 20 times FASTER than fr_mountain
    
    def fr_sea(self, matrix):
        """
        [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
        """
        n, m = len(matrix), len(matrix[0])
        Q_pacific = collections.deque()
        Q_atlantic = collections.deque()
        for j in range(m):
            Q_pacific.append([0, j])
            Q_atlantic.append([n-1, j])

        for i in range(n):
            Q_pacific.append([i, 0])
            Q_atlantic.append([i, m-1])
        
        pcf_visited = self.bfs_fr_sea(matrix, Q_pacific)
        atl_visited = self.bfs_fr_sea(matrix, Q_atlantic) 
        
        # Get intersection of two visited
        res = []
        for pos in pcf_visited:
            if pos in atl_visited:
                res.append([pos[0], pos[1]])
        
        return res
        
    def bfs_fr_sea(self, grid, Q):
        visited = set()
        for x, y in Q:
            visited.add((x, y))
        while Q:
            for _ in range(len(Q)):
                now_x, now_y = Q.popleft()
                for delta_x, delta_y in DIRECTIONS:
                    next_x = now_x + delta_x
                    next_y = now_y + delta_y
                    if self.is_valid_fr_sea(now_x, now_y, next_x, next_y, grid, visited):
                        Q.append([next_x, next_y])
                        visited.add((next_x, next_y))
        return visited
    
    def is_valid_fr_sea(self, now_x, now_y, x, y, grid, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[now_x][now_y] > grid[x][y]:
            return False
        if (x, y) in visited:
            return False
        return True
        
    
    
    
    def fr_mountain(self, matrix):
        """
        [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.bfs_valid_cell(i, j, matrix):
                    res.append([i, j])
        return res
        
        
    def bfs_valid_cell(self, x, y, matrix):
        n, m = len(matrix), len(matrix[0])
        
        Q = collections.deque()
        Q.append([x, y])
        visited = set()
        visited.add((x, y))
        reach_pacific = False if x != 0 and y != 0 else True
        reach_atlantic = False if x != n-1 and y != m-1 else True
        # print('START: ', x, y)
        while Q:
            for _ in range(len(Q)):
                now_x, now_y = Q.popleft()
                # print("now_x, now_y: ", now_x, now_y)
                # print("visited: ", visited)
                for delta_x, delta_y in DIRECTIONS:
                    next_x = now_x + delta_x
                    next_y = now_y + delta_y
                    # print(next_x, next_y)
                    if self.is_valid(now_x, now_y, next_x, next_y, matrix, visited):
                        # print('hihi')
                        if next_x == 0 or next_y == 0:
                            reach_pacific = True
                        if next_x == n-1 or next_y == m-1:
                            reach_atlantic = True
                        if reach_pacific and reach_atlantic:
                            return True
                        Q.append((next_x, next_y))
                        visited.add((next_x, next_y))
        ans = reach_pacific and reach_atlantic
        # print(ans)
        return ans
        
    def is_valid(self, now_x, now_y, next_x, next_y, grid, visited):
        if next_x < 0 or next_y < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
            return False
        if (next_x, next_y) in visited:
            return False
        if grid[now_x][now_y] < grid[next_x][next_y]:
            return False
        return True        
# @lc code=end

