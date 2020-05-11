#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.30%)
# Likes:    1839
# Dislikes: 217
# Total Accepted:    408.5K
# Total Submissions: 918.5K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start, end = 0, len(nums)-1
        
        while start+1 < end:
            mid = start + (end-start)//2
            target = nums[end]
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        
        return min(nums[start], nums[end])
        # if nums[start] < nums[end]:
        #     return start
        # else:
        #     return end        
# @lc code=end

