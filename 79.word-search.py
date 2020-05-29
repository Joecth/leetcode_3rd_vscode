#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (33.91%)
# Likes:    3350
# Dislikes: 165
# Total Accepted:    441.9K
# Total Submissions: 1.3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# 
# Constraints:
# 
# 
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
from copy import deepcopy
# from collections import deque
DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return []
        # return self.bfs_old(board, word)
        return self.dfs_main(board, word)   # KEY: no go back & DFS
    
    def dfs_main(self, board, word):
        ans = False
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(i, j, board, word, visited, 0):                        
                        return True
                    visited[i][j] = False
        return False
    
    def dfs(self, i, j, board, word, visited, idx):
        if word[idx] != board[i][j]:
            # print(word[:idx+1])
            return False
        
        if idx == len(word)-1:
            return True
        
        for direction in DIRECTIONS:
            next_i, next_j = i+direction[0], j+direction[1]
            # if self.is_valid(next_i, next_j, board) 
            if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
                continue
            if not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                if self.dfs(next_i, next_j, board, word, visited, idx+1):
                    return True
                visited[next_i][next_j] = False
        return False
    
    def is_valid(self, i, j, board):
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]):
            return False
        return True
    # def bfs_new(board, word):
    #     ans = False
    #     m, n = len(board), len(board[0])
    #     visited = [[False for _ in range(n)] for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             # if not visited[i][j]:
    #             if board[i][j] == word[0]:
    #                 self.bfs_new_helper(i, j, board, visited, word)
                    # visited[i][j] = True
                
#     def bfs_new_helper(self, i, j, board, visited, word):
#         Q = deque()
#         Q.append((i, j))
#         idx = 1
#         while Q:
#             for _ in range(len(Q)):
#                 cur_i, cur_j = Q.popleft()
                
#                 for direction in DIRECTIONS:
#                     next_i = cur_i + direction[0]
#                     next_j = cur_j + direction[1]
                    
#                     if board[next_i][next_J] == word[idx]:
                        
#                         idx += 1
        
        
    def bfs_old(self, board, word):
        ans = False
        # visited = [[False for j in range(len(board[0]))]for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False for j in range(len(board[0]))]for i in range(len(board))]
                    ans = self.helper(board, i, j, word, False, visited) or ans  
                    if ans:
                        return ans
        return ans
    
    '''
    First version failed AT:
    [["C","A","A"],
     ["A","A","A"],
     ["B","C","D"]]
    "AAB"
    '''
    def helper(self, board, row, col, item, ans, visited):
        # if not item:
        #     return True
        if visited[row][col] == True:
            return False
        
        if board[row][col] == item[0]:
            visited[row][col] = True
            if len(item) == 1:
                return True
            else:
                item = item[1:]
        else:
            return False
        
        if row < len(board)-1:
            # print(row, col)
            if not visited[row+1][col]:
                tmp = visited[row+1][col]
                # ans = self.helper(board, row+1, col, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row+1, col, item, ans, visited) or ans
                visited[row+1][col] = tmp
            if ans:
                return True
        if row > 0:
            if not visited[row-1][col]:
                tmp = visited[row-1][col]
                # ans = self.helper(board, row-1, col, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row-1, col, item, ans, visited) or ans
                visited[row-1][col] = tmp
            if ans:
                return True
        if col < len(board[0])-1:
            if not visited[row][col+1]:
                tmp = visited[row][col+1]
                # ans = self.helper(board, row, col+1, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row, col+1, item, ans, visited) or ans
                visited[row][col+1] = tmp
            if ans:
                return True
        if col > 0:
            if not visited[row][col-1]:
                tmp = visited[row][col-1]
                # ans = self.helper(board, row, col-1, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row, col-1, item, ans, visited) or ans
                visited[row][col-1] = tmp
            if ans:
                return True
            
        return False        
# @lc code=end

