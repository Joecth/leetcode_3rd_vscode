class DataType:
    EMPTY = 0
    WALL = 1

DIRECTIONS = [(1,2), (-1,2), (2,1), (-2,1)]
# time: O(n*m)
# space: O(n*m)
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        
        # 定義
        Q = collections.deque()
        distance = {}
        
        # 加起始點
        Q.append((0,0))
        distance[(0,0)] = 0
        last_point = {}
        
        """
        1. Java 怎麼辦 
            (x, y) -> x*m + y
        2. 為什麼不提前出來
        
        JAVA:
            1. 自定義類
            2. 二維數組
            3. pair
            4. 二維數組轉一維
            5. 用string x + "," + y
        
        OA: 2: 快，所以二維數組, int visited[][]
        onsite: 1(equal), 2也還沒到真很醜
        動規：as 騎士最短路徑I
        """
        
        # BFS循環
        while Q:
            x, y = Q.popleft()
            
            # if x == n - 1 and y == m - 1:   # UGLY, 也不會降低時間複雜度
            #     return distance[(x, y)]
            # 找所有 neighbors
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                # 判斷是否合法
                if self.is_valid(next_x, next_y, grid, distance):
                    Q.append((next_x, next_y))
                    last_point[(next_x, next_y)] = (x, y)
                    distance[(next_x, next_y)] = distance[(x, y)] + 1
                    
        if (n - 1, m - 1) not in distance:
            return -1
        path = self.find_path(grid, last_point)
        # print(path)
        return distance[(n - 1, m - 1)]
        
    def is_valid(self, x, y, grid, distance):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x, y) in distance:
            return False
        if grid[x][y] == DataType.WALL:
            return False
        return True
    
    def find_path(self, grid, last_point):
        n, m = len(grid), len(grid[0])
        x, y = n - 1, m - 1
        
        path = [(n - 1, m - 1)]
        while x != 0 or y != 0:
            x, y = last_point[(x, y)]
            path.append([(x, y)])
        return path[::-1]