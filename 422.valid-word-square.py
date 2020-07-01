#
# @lc app=leetcode id=422 lang=python3
#
# [422] Valid Word Square
#
# https://leetcode.com/problems/valid-word-square/description/
#
# algorithms
# Easy (37.17%)
# Likes:    166
# Dislikes: 113
# Total Accepted:    28.8K
# Total Submissions: 76.7K
# Testcase Example:  '["abcd","bnrt","crmy","dtye"]'
#
# Given a sequence of words, check whether it forms a valid word square.
# 
# A sequence of words forms a valid word square if the k^th row and column read
# the exact same string, where 0 ≤ k < max(numRows, numColumns).
# 
# Note:
# 
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# 
# 
# 
# Example 1:
# 
# Input:
# [
# ⁠ "abcd",
# ⁠ "bnrt",
# ⁠ "crmy",
# ⁠ "dtye"
# ]
# 
# Output:
# true
# 
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".
# 
# Therefore, it is a valid word square.
# 
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ "abcd",
# ⁠ "bnrt",
# ⁠ "crm",
# ⁠ "dt"
# ]
# 
# Output:
# true
# 
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crm".
# The fourth row and fourth column both read "dt".
# 
# Therefore, it is a valid word square.
# 
# 
# 
# Example 3:
# 
# Input:
# [
# ⁠ "ball",
# ⁠ "area",
# ⁠ "read",
# ⁠ "lady"
# ]
# 
# Output:
# false
# 
# Explanation:
# The third row reads "read" while the third column reads "lead".
# 
# Therefore, it is NOT a valid word square.
# 
# 
#

# @lc code=start
"""
[
    "ball",
    "asee",
    "let.",
    "lep."
]
"""
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words or not words[0]:
            return False
        n = len(words)
        # n = len(words)
        m = max(len(word) for word in words)
        
        if n != m:
            return False
        
        grid = []
        for i in range(n):
            item = words[i]
            if len(words[i]) < m:
                item += (m-len(words[i])) * '.'
            grid.append(item)
        
        for i in range(n):
            for j in range(i+1, m):
            # for j in range(m):
                if grid[i][j] != grid[j][i]:
                    return False
        return True        
# @lc code=end

