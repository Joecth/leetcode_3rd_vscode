#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (57.38%)
# Likes:    643
# Dislikes: 21
# Total Accepted:    36.8K
# Total Submissions: 62.6K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
# 
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
# 
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
# 
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
# 
# Examples:
# 
# 
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# 
# 
# 
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# 
# 
# 
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# 
# 
# 
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# 
# 
# Note:
# 
# 
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
# 
# 
#

# @lc code=start
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        final_board = [[1, 2, 3], [4, 5, 0]]
        # final_state = self.board_to_state(final_board)
        init_board = board
        
        Q = collections.deque()
        distance = {}
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 0:
                    start_x, start_y = x, y
        try:
            start_x
        except:
            return -1
        
        init_state = self.board_2_state(init_board)
        Q.append((start_x, start_y, init_state))    # init_state should be in tuple or string
        # steps = 0
        distance[self.board_2_state(init_board)] = 0
        
        while Q:
            x, y, now_state = Q.popleft()
            if self.state_2_board(now_state) == final_board:
                return distance[now_state]
            
            for next_x, next_y, next_state in self.find_next_states(x, y, now_state, distance):
                
                Q.append((next_x, next_y, next_state))
                distance[(next_state)] = distance[(now_state)] + 1
            # steps += 1
        return -1
    
    def find_next_states(self, x, y, state, distance):
        next_states_list = []
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if self.is_valid(state, next_x, next_y):
                board = self.state_2_board(state)   # tuple to list
                board[x][y], board[next_x][next_y] = board[next_x][next_y], board[x][y]
                # board[x][y], board[next_x][next_y] = board[next_x][next_y], board[x][y]
                next_state = self.board_2_state(board)
                if next_state in distance:
                    continue
                next_states_list.append((next_x, next_y, next_state))
        return next_states_list
                
    def state_2_board(self, state):
        # (
        #   (1,2,3),    ==> list
        #   (4,0,5)
        # )
        # print(state)
        return [list(t) for t in state]
            
    def board_2_state(self, board):
        # print(board)
        return tuple([tuple(l) for l in board])
                
    def is_valid(self, state, x, y):
        # SINCE we use tuple instead of str, we can get n & m from state
        if x < 0 or y < 0 or x >= len(state) or y >= len(state[0]):
            return False
        return True        
# @lc code=end

