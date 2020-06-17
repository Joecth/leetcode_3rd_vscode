class DataType:
    HOUSE = 1
    EMPTY = 0
    
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # return self.house_oriented_TLE(grid)
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
    
        # print(row_count)
        # print(col_count)
        # print(row_dist)
        # print(col_dist)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    continue
                output = min(output, row_dist[i] + col_dist[j])
        return output
        
        
    def house_oriented_TLE(self, grid):
        # write your code here
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
        
        # print(f'dist: {dist}')
        # print(f'reachable_count: {reachable_count}')
        
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
                        visited.add((next_x, next_y))
                        Q.append([next_x, next_y])
                        reachable_count[next_x][next_y] += 1
                    # if grid[next_x][next_y] == DataType.HOUSE:
            cur_dist += 1
            
    def is_valid(self, x, y, grid, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        # if grid[x][y] == DataType.HOUSE:
        #     return False
        return True