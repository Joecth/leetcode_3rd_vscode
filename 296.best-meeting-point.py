#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#
# https://leetcode.com/problems/best-meeting-point/description/
#
# algorithms
# Hard (57.00%)
# Likes:    442
# Dislikes: 36
# Total Accepted:    34.7K
# Total Submissions: 60.6K
# Testcase Example:  '[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# A group of two or more people wants to meet and minimize the total travel
# distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
# home of someone in the group. The distance is calculated using Manhattan
# Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# 
# Example:
# 
# 
# Input: 
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 6 
# 
# Explanation: Given three people living at (0,0), (0,4), and
# (2,2):
# The point (0,2) is an ideal meeting point, as the total travel
# distance 
# of 2+2+2=6 is minimal. So return 6.
# 
#

# @lc code=start
class DataType:
    HOUSE = 1
    EMPTY = 0
    
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    # def shortestDistance(self, grid):
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # return self.empty_oriented(grid)
        # return self.house_oriented(grid)
        return self.find_centroid(grid)
    
    def find_centroid(self, grid):
        """
        [
            [0,1,0,0],
            [1,0,1,1],
            [0,1,0,0]
        ]
        """
        # One axis
        row_count = [sum(row) for row in grid]
        col_count = [0]* len(grid[0])
        row_dist = [0]* len(grid)
        col_dist = [0]* len(grid[0])
        output = sys.maxsize
        for i in range(len(grid)):    
            for j in range(len(grid[0])):
                col_count[j] += grid[i][j]
                
        for index_p in range(len(row_count)):
            for index_h in range(len(row_count)):
                row_dist[index_p] += abs(index_h - index_p) * row_count[index_h]
        
        for index_p in range(len(col_count)):
            for index_h in range(len(col_count)):
                col_dist[index_p] += abs(index_h - index_p) * col_count[index_h]
    
        print(row_count)
        print(col_count)
        print(row_dist)
        print(col_dist)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if grid[i][j] == 1:   # Should add this when building post-office
                #     continue
                output = min(output, row_dist[i] + col_dist[j])
        return output    
    
    def house_oriented(self, grid):
        # write your code here
        """
        [
            [0,1,0,0],
            [1,0,1,1],
            [0,1,0,0]
        ]
        """
        n, m = len(grid), len(grid[0])
        dist = [[0 for _ in range(m)] for _ in range(n)]
        reachable_count = [[0 for _ in range(m)] for _ in range(n)]
        
        house_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == DataType.HOUSE:
                    house_count += 1
                    self.bfs_house_oriented(grid, i, j, dist, reachable_count)
        
        print(f'dist: {dist}')
        print(f'reachable_count: {reachable_count}')
        
        min_dist = sys.maxsize
        for i in range(n):
            for j in range(m):
                if reachable_count[i][j] == house_count and dist[i][j] < min_dist : # and dist[i][j] != 0:  # shouldn't be a HOUSE, should be handled in reachable_count
                    min_dist = dist[i][j]
                    
        if min_dist == sys.maxsize:
            return -1
        return min_dist
    
    def bfs_house_oriented(self, grid, x, y, dist, reachable_count):
        Q = collections.deque()
        Q.append([x, y])
        
        visited = set()
        visited.add((x, y))
        
        cur_dist = 0
        
        while Q:
            for _ in range(len(Q)):
                now_x, now_y = Q.popleft()
                dist[now_x][now_y] += cur_dist
                for delta_x, delta_y in DIRECTIONS:
                    next_x = now_x + delta_x
                    next_y = now_y + delta_y
                    if self.is_valid(next_x, next_y, grid, visited):
                        Q.append([next_x, next_y])
                        visited.add((next_x, next_y))
                        reachable_count[next_x][next_y] += 1
                        dist[next_x][next_y]
                    # if grid[next_x][next_y] == DataType.HOUSE:
            cur_dist += 1
            
    def is_valid(self, x, y, grid, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        # if grid[x][y] == DataType.HOUSE:
            # return False
        return True
    
    # O(N^4)
    def empty_oriented(self, grid):
        # write your code here
        """
        [
            [0,1,0,0],
            [1,0,1,1],
            [0,1,0,0]
        ]
        """
        g_min = 0
        # pos = [0, 0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == DataType.EMPTY:
                    g_min = max(g_min, self.bfs_BF(grid, i, j))
        return g_min
    
    def bfs_BF(self, grid, x, y):
        Q = collections.deque()
        Q.append([x, y])
        visited = set((x, y))
        distance = 0
        
        while Q:
            for _ in range(len(Q)):
                now_x, now_y = Q.popleft()
                for delta_x, delta_y in DIRECTIONS:
                    next_x = now_x + delta_x
                    next_y = now_y + delta_y
                    if self.is_valid(next_x, next_y, grid, visited):
                        Q.append([next_x, next_y])
                        visited.add((next_x, next_y))
                    
                    if grid[next_x][next_y] == DataType.HOUSE:
                        pass
                    
        return distance
    
    # def is_valid(self, x, y, grid, visited):
        # pass        
# @lc code=end

