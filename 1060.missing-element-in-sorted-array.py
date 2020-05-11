#
# @lc app=leetcode id=1060 lang=python3
#
# [1060] Missing Element in Sorted Array
#
# https://leetcode.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (54.42%)
# Likes:    401
# Dislikes: 20
# Total Accepted:    21.8K
# Total Submissions: 40K
# Testcase Example:  '[4,7,9,10]\n1'
#
# Given a sorted array A of unique numbers, find the K-th missing number
# starting from the leftmost number of the array.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
# 
# 
# Example 2:
# 
# 
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# 
# 
# Example 3:
# 
# 
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is
# 6.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8
# 
#

# @lc code=start        
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def missing_count(nums, idx, start=0):
            # should >= 0
            return nums[idx] - nums[start] - (idx-start)
        
        missing_len = missing_count(nums, len(nums)-1)
            
        if k > missing_len:
            return nums[-1] + k - missing_len
        
        start, end = 0, len(nums)-1
        
        while start+1 < end:
            mid = start + (end-start)//2
            missing_len = missing_count(nums, mid, start)
            if missing_len < k:
                start = mid
                k -= missing_len
            else:
                end = mid
        return nums[start] + k            
# @lc code=end