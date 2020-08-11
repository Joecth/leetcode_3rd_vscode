#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (53.98%)
# Likes:    1873
# Dislikes: 289
# Total Accepted:    184.9K
# Total Submissions: 339.4K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
"""
die  --> live: -1
live --> die :  2
count(board, i, j),  數1以及2
update(); -1 ==> 1, 2 ==> 0
"""
DIRECTIONS = [[0, -1], [0, 1], [1, 0], [-1, 0],
              [1, 1], [-1,-1], [1,-1], [-1,1]
             ]
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    lives = self.count(board, i, j)
                    if lives == 3:
                        board[i][j] = -1
                if board[i][j] == 1:
                    lives = self.count(board, i, j)
                    if lives < 2 or lives > 3:
                        board[i][j] = 2
        self.update(board)
        # https://www.youtube.com/watch?v=9AsUixzUGa0
        
    def update(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
    
    
    def count(self, board, row, col):
        res = 0
        for delta_i, delta_j in DIRECTIONS:
            next_i = row + delta_i
            next_j = col + delta_j
            # if self.is_valid(next_i, next_j, board):
            if next_i < 0 or next_j < 0 or next_i >= len(board) or next_j >= len(board[0]):
                continue
            if board[next_i][next_j] == 2 or board[next_i][next_j] == 1:
                res += 1
        return res
    
    
                        
# @lc code=end

