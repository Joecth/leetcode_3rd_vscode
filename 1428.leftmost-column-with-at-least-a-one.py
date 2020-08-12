#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column with at Least a One
#
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description/
#
# algorithms
# Medium (46.44%)
# Likes:    137
# Dislikes: 17
# Total Accepted:    51.2K
# Total Submissions: 109.3K
# Testcase Example:  '[[0,0],[1,1]]'
#
# (This problem is an interactive problem.)
# 
# A binary matrix means that all elements are 0 or 1. For each individual row
# of the matrix, this row is sorted in non-decreasing order.
# 
# Given a row-sorted binary matrix binaryMatrix, return leftmost column
# index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
# -1.
# 
# You can't access the Binary Matrix directly.  You may only access the matrix
# using a BinaryMatrix interface:
# 
# 
# BinaryMatrix.get(row, col) returns the element of the matrix at index (row,
# col) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which
# means the matrix is rows * cols.
# 
# 
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged
# Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
# result in disqualification.
# 
# For custom testing purposes you're given the binary matrix mat as input in
# the following four examples. You will not have access the binary matrix
# directly.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: mat = [[0,0],[1,1]]
# Output: 0
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: mat = [[0,0],[0,1]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: mat = [[0,0],[0,0]]
# Output: -1
# 
# Example 4:
# 
# 
# 
# 
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in a non-decreasing way.
# 
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
from bisect import bisect_left
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    # def O_
        # return self.O_MxLogN(binaryMatrix)
        return self.O_M_plus_N(binaryMatrix)
    
    def O_M_plus_N(self, arr):
        m, n = arr.dimensions()
        if m == 0 or n == 0:
            return 0
        ret = n
        i, j = m-1, n-1
        while i >= 0 and j >= 0:
            if arr.get(i, j) == 1:
                if j == 0:
                    ret = j
                    break
                ret = j
                j -= 1
            else:
                i -= 1
        return ret if ret < n else -1
    
    def O_MxLogN(self, binaryMatrix):
        m, n = binaryMatrix.dimensions()
        if m == 0 or n == 0:
            return 0
        
        ret = sys.maxsize
        """
        1 1 1, 1 ==> 0
        0 1 1, 1 ==> 1
        0 0 0, 1 ==> 3
        """
        # 下一行的結尾不需要在最後 ==> 加在二分裡的優化
        # 在第0個column可以直接 break 退出 
        for i in range(m):
            # idx = BSearch each row(binaryMatrix, 1)
            # idx = bisect_left(binaryMatrix[i], 1) # Not Subscriptble
            idx = self.b_left(binaryMatrix, i, 1, n)
            if idx < n:
                ret = min(idx, ret)
        return ret if ret != sys.maxsize else -1
    
    def b_left(self, arr, i, target, n):
        start, end = 0, n - 1 #len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if arr.get(i, mid) < target:    # means 0
                start = mid
            else:
                end = mid
            
        if arr.get(i, start) == 1:
            return start
        elif arr.get(i, end) == 1:
            return end
        return end + 1    # means len(arr)
# @lc code=end

