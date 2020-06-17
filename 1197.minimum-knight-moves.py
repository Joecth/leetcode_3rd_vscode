#
# @lc app=leetcode id=1197 lang=python3
#
# [1197] Minimum Knight Moves
#
# https://leetcode.com/problems/minimum-knight-moves/description/
#
# algorithms
# Medium (34.37%)
# Likes:    263
# Dislikes: 114
# Total Accepted:    24.7K
# Total Submissions: 69.1K
# Testcase Example:  '2\n1'
#
# In an infinite chess board with coordinates from -infinity to +infinity, you
# have a knight at square [0, 0].
# 
# A knight has 8 possible moves it can make, as illustrated below. Each move is
# two squares in a cardinal direction, then one square in an orthogonal
# direction.
# 
# 
# 
# Return the minimum number of steps needed to move the knight to the square
# [x, y].  It is guaranteed the answer exists.
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# 
# 
# Example 2:
# 
# 
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
# 
# 
# 
# Constraints:
# 
# 
# |x| + |y| <= 300
# 
# 
#

# @lc code=start
class DataType:
    WALL = 1
    ROAD = 0

DIRECTIONS = [
                [1, 2], [1, -2], [-1, 2], [-1, -2],
                [2, 1], [2, -1], [-2, 1], [-2, -1],
               ]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # write your code here
        # if not grid or not grid[0]:
        #     return -1
        # if (source.x == destination.x) and (source.y == destination.y):
        if x == 0 and y == 0:
            return 0
            
        # n, m = len(grid), len(grid[0])
        
        Q = collections.deque()
        # Q.append([source.x, source.y])
        Q.append([0, 0])
        visited = set()
        # visited.add((source.x, source.y))
        visited.add((0, 0))
        steps = 0
        
        while Q:
            for _ in range(len(Q)):
                now_x, now_y = Q.popleft()
                # if (x, y) == destination:
                #     break
                for delta_x, delta_y in DIRECTIONS:
                    next_x = now_x + delta_x
                    next_y = now_y + delta_y
                    # if self.is_valid(next_x, next_y, grid, visited):
                        # if [next_x, next_y] == [destination.x, destination.y]:
                    if self.is_valid(next_x, next_y, visited):
                        if [next_x, next_y] == [x, y]:
                            return steps+1
                        
                        Q.append([next_x,  next_y])
                        visited.add((next_x, next_y))
            steps += 1            
        return -1
        
    # def is_valid(self, x, y, grid, visited):
    def is_valid(self, x, y, visited):
        # if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        #     return False
        # if grid[x][y] == DataType.WALL:
        #     return False
        if (x, y) in visited:
            return False
        return True                
# @lc code=end

