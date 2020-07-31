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
from typing import List
DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        # return self.dfs_main(grid)
        n, m = len(grid), len(grid[0])
        uf = UnionFindSet(n*m)
        count = n * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if j < m-1 and grid[i][j+1] == '1':
                        # if uf.Union(grid[i][j], grid[i][j+1]):
                        if uf.Union(i*m+j, i*m+j+1):
                            count -= 1
                    if i < n-1 and grid[i+1][j] == '1':
                        # if uf.Union(grid[i][j], grid[i+1][j]):
                        if uf.Union(i*m+j, (i+1)*m+j):
                            count -= 1
                else:# if grid[i][j] == '0':
                    count -= 1
            # print(count)
        return count
        
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
    
    def method_UF(self, grid):
        # return self.numIslands_old(grid)
        
        # def find(parent, i):
        #     if parent[i] != i:
        #         parent[i] = find(parent[i])        
        # def union(parent, x, y):
        #     root_X = find(x)
        #     root_Y = find(y)
        #     if root_x != root_y:
        # n, m = len(grid),len(grid[0])
        # if not n or not m:
        #     return 0
        # uf = UnionFindSet(n*m)
        # count = 0
        # visited = set()
        # # visited.add(())
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == '1':
        #             visited.add((i, j))
        #             for delta_x, delta_y in DIRECTIONS:
        #                 next_x = i + delta_x
        #                 next_y = j + delta_y
        #                 if self.is_valid_uf(next_x, next_y, grid, visited):
        #                     uf.Union(m*i+j, m*next_x+next_y)
        #                     visited.add((next_x, next_y))
        #                     count += 1
        # return count
        pass
    
    def is_valid_uf(self, x, y, grid, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[x][y] == '0':
            return False
        if (x, y) in visited:
            return False
        return True
        
                
    def numIslands_old(self, grid: List[List[str]]) -> int:
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

    def helper_(self, i, j, grid):
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
    
    
        
        
    def numIslands_oldold(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # arr = [[0 for j in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        count = 0
        
        arr = np.pad(grid, ((1,1), (1,1)))
        print(arr)
        
        # for i in range(1, len(arr)):
        #     for j in range(1, len(arr[0])):
        for i in range(1, len(arr)-1):
            for j in range(1, len(arr[0])-1):
                if arr[i][j] == '1':
                    self.bfs((arr[i][j], i, j), arr)
                    count += 1
        return count
        
    def bfs(self, item, arr):
        Q = deque()
        Q.append(item)
        
        while Q:
            val, i, j = Q.popleft()
            if val == '1':
                arr[i][j] = '0'
                
            if arr[i][j-1] == '1':         # '0' is True...
                Q.append((arr[i][j-1], i, j-1))
                arr[i][j-1] = 'x'
            if arr[i-1][j] == '1':
                Q.append((arr[i-1][j], i-1, j))
                arr[i-1][j] = 'x'
            if arr[i][j+1] == '1':
                Q.append((arr[i][j+1], i, j+1))
                arr[i][j+1] = 'x'
            if arr[i+1][j] == '1':
                Q.append((arr[i+1][j], i+1, j))
                arr[i+1][j] = 'x'

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
# @lc code=end

