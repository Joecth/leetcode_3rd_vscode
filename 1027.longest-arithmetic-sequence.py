#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#
# https://leetcode.com/problems/longest-arithmetic-sequence/description/
#
# algorithms
# Medium (53.40%)
# Likes:    604
# Dislikes: 34
# Total Accepted:    35.7K
# Total Submissions: 66.3K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array A of integers, return the length of the longest arithmetic
# subsequence in A.
# 
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0
# <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
# if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.
# 
# 
# 
# Example 2:
# 
# 
# Input: [9,4,7,2,10]
# Output: 3
# Explanation: 
# The longest arithmetic subsequence is [4,7,10].
# 
# 
# 
# Example 3:
# 
# 
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation: 
# The longest arithmetic subsequence is [20,15,10,5].
# 
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
# 
# 
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        # return self.old(A)
        return self.O_NxN(A)
            
    def O_NxN(self, A): # Where's the connection to LIS?
        # [3,6,9,12,13]
        # when i=1, A[i]=6:
        # dp=[{3:2}]
        # when i=2, A[i]=9:
        # dp=[{3:2}, {6:2, 3:3}]
        # when i=2, A[i]=12:
        # dp=[{3:2}, {6:2, 3:3}, {9:2, 6:2, 3:4}, {10:2, 7:2, 4:2, 1:2}]
        # return max([2,3,4,2])
            
        dp = [dict() for i in range(len(A))]
        max_len = 2
        for i in range(1, len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 1) + 1   # min length btw 2 items is 2
                max_len = max(max_len, dp[i][A[i] - A[j]])
            # print(dp[i])
        return max_len        
# @lc code=end

