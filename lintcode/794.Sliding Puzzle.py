from copy import deepcopy
DIRECTIONS = [[-1,0], [1,0], [0,-1], [0,1],]
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    # 華容道
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        """
        移動，最多會移動多少次？
        總狀態有多少種？
        A[9,9] ==> 9!
        ans = 1
        for i in rnage(10):
            ans *= i
        ans == 362880
        10^5~10^6 完全可以接受，用BFS做吧！
        
        用什麼表示當前的狀態呢？
        state ==> list of list，比較好寫
        ==> string:"283104765" 有點太醜
        """
        return self.mine(init_state, final_state)
        
    # TLE...
    def mine(self, init_state, final_state):
        if not init_state or not final_state:
            return -1
        """
        [                       
            [2,8,3],            [1,2,3],            
            [1,0,4],    ==>     [8,0,4],
            [7,6,5]             [7,6,5]
        ]
        """
        
        START = None
        n, m = len(init_state), len(init_state[0])
        for i in range(n):
            for j in range(m):
                if init_state[i][j] == 0:
                    START = (i, j)
                    
        Q = collections.deque()
        Q.append((START[0], START[1], init_state))
        # Q.append(init_state)
        visited = {self.encode_grid(init_state): 0}     # state --> distance
        steps = 0
        while Q:
            print(Q)
            # for _ in range(len(Q)):
            now_x, now_y, now_state = Q.popleft()
            if now_state == final_state:
                return visited[self.encode_grid(now_state)]
            encoding_grid = self.encode_grid(now_state)
            for next_x, next_y, next_state in self.find_next_states(now_x, now_y, deepcopy(now_state), visited):
                Q.append((next_x, next_y, next_state))
                visited[self.encode_grid(next_state)] = visited[encoding_grid] + 1
            # steps += 1
            
        return -1
        
    def find_next_states(self, x, y, state, visited):
        res = []
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if self.is_valid(next_x, next_y, state):
                state[x][y], state[next_x][next_y] = state[next_x][next_y], state[x][y]
                if self.encode_grid(state) in visited:
                    continue
                res.append([next_x, next_y, deepcopy(state)])
                state[x][y], state[next_x][next_y] = state[next_x][next_y], state[x][y]
        return res
    
    def is_valid(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        return True
    
    def encode_grid(self, state):
        return tuple([tuple(row) for row in state])