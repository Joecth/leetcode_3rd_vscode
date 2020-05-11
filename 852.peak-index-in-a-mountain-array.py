#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start, end = 0, len(A)-1
        
        while start+1 < end:
            mid = start + (end-start)//2
            if (A[mid] > A[mid-1]):
                start = mid
            else:
                end = mid
        
        if A[start] > A[end]:
            return start
        return end
                
    def O(self, A):    
        if len(A) == 1:
            return 0
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return i-1

        return len(A)-1
# @lc code=end

