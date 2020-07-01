#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (32.40%)
# Likes:    2303
# Dislikes: 105
# Total Accepted:    196.4K
# Total Submissions: 584.8K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#

# @lc code=start
from copy import deepcopy
# from collections import deque
DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        # return self.bfs_old(board, word)
        # return self.word_by_word_TLE(board, words)
        return self.pre_fix_hash(board, words) # Inverse thought of word_by_word
    
    def pre_fix_hash(self, board, words):
        words_set = set(words)
        pre_fix_set = set()
        for word in words:
            for i in range(len(word)):
                pre_fix_set.add(word[:i+1])
                
        n, m = len(board), len(board[0])
        res = []
        # visited = set()
        # visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # traverse board
                self.search(board, words_set, pre_fix_set, i, j, board[i][j], res, set([(i, j)]))
        return set(res)
        # ref: https://www.jiuzhang.com/solution/word-search-ii/#tag-other-lang-python
    
    def search(self, board, words_set, pre_fix_set, x, y, item, res, visited):
        if item not in pre_fix_set:
            return 
        if item in words_set:
            res.append(item)
            # print(res)
            
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if self.is_valid2(next_x, next_y, board, pre_fix_set, item, visited):
                orig_state = item
                item += board[next_x][next_y]
                visited.add((next_x, next_y))
                self.search(board, words_set, pre_fix_set, next_x, next_y, item, res, visited)
                item = orig_state
                visited.remove((next_x, next_y))
    
    def is_valid2(self, x, y, board, pre_fix_set, item, visited):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        if (x, y) in visited:
            return False
        if item + board[x][y] not in pre_fix_set:
            return False
        return True
    
    def word_by_word_TLE(self, board, words):
        res = []
        for word in words:
            if self.dfs_main(board, word):
                res.append(word) 
        return res
        # return self.dfs_main(board, word)   # KEY: no go back & DFS
    
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
            if self.is_valid(next_i, next_j, board, visited):
            # if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
                # continue
                # if not visited[next_i][next_j]:
                    visited[next_i][next_j] = True
                    if self.dfs(next_i, next_j, board, word, visited, idx+1):
                        return True
                    visited[next_i][next_j] = False
        return False
    
    def is_valid(self, i, j, board, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if visited[i][j] == True:
            return False
        return True
    
    def findWords_old(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word) 
        return res
    
    
    
    '''
    TLE when multiple words to search
    '''
    def exist_old(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return []
        
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

