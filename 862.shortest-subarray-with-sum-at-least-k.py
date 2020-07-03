#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (23.40%)
# Likes:    1077
# Dislikes: 30
# Total Accepted:    30.8K
# Total Submissions: 126.9K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
# 
# If there is no non-empty subarray with sum at least K, return -1.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1], K = 1
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2], K = 4
# Output: -1
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-1,2], K = 3
# Output: 3
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        return self.my_mono_Q(A, K)
    
    def my_mono_Q(self, A, K):
        N = len(A)
        pre_sum = [0] * (N+1)
        for i in range(N):
            pre_sum[i+1] = pre_sum[i] + A[i]
            
        Q = collections.deque()
        ans = sys.maxsize
        for j in range(N+1):
            # 考慮A裡有負數的情況, pre_sum就會下降了；它對 pre_sum 造成了一個山谷
            # 1. 到山谷才能拿到的值，經過山谷之前只會更小，所以前面不會再是答案
            # 2. 山谷之前只是讓長度更長不會更短
            while Q and pre_sum[j] <= pre_sum[Q[-1]]:
                Q.pop() # 塞的時候從右邊check
            
            # 都是正數的情況
            while Q and pre_sum[j] - pre_sum[Q[0]] >= K:
                i = Q.popleft() # 找答案時候從左邊
                ans = min(ans, j - i)
                
            Q.append(j)
        
        return ans if ans < sys.maxsize else -1                
# @lc code=end

