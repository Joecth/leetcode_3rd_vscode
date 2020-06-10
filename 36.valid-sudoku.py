#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (47.09%)
# Likes:    1530
# Dislikes: 439
# Total Accepted:    351K
# Total Submissions: 730.7K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = m = 9
        digits = '1234567890'
        for i in range(n):
            map_s = set()
            for j in range(m):
                cur = board[i][j] 
                if cur in digits:
                    if cur in map_s: 
                        return False
                    else:
                        map_s.add(cur)
                    
        for j in range(m):
            map_s = set()
            for i in range(n):
                cur = board[i][j]
                if cur in digits:
                    if cur in map_s: 
                        return False
                    else:
                        map_s.add(cur)
        
        for b in range(9):
            map_s = set()
            q = b // 3
            r = b % 3
            for i in range(n//3):
                for j in range(m//3):
                    cur = board[i+q*3][j+r*3]
                    if cur in digits:
                        if cur in map_s:
                            return False
                        else:
                            map_s.add(cur)
        return True
        
        
    def isValidSudoku_old(self, board: List[List[str]]) -> bool:
        
        dict_cols = defaultdict(defaultdict)
        for i in range(len(board)):
            dict_row = defaultdict(str)
            if i % 3 == 0:
                dict_boxes = defaultdict(defaultdict)
            
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in dict_row:
                        return False
                    else:
                        dict_row[board[i][j]] = True
                        
                    if board[i][j] in dict_cols[j]:
                        return False
                    else:
                        dict_cols[j][board[i][j]] = True
                        
                    # if board[i][j] in dict_boxes
                    if 0 <= j % 9 <= 2:
                        if board[i][j] in dict_boxes[0]:
                            return False
                        dict_boxes[0][board[i][j]] = True
                    elif 3 <= j % 9 <= 5:
                        if board[i][j] in dict_boxes[1]:
                            return False                        
                        dict_boxes[1][board[i][j]] = True
                    elif 6 <= j % 9 <= 8:
                        if board[i][j] in dict_boxes[2]:
                            return False                        
                        dict_boxes[2][board[i][j]] = True
        return True
                    
                    
        
# @lc code=end

