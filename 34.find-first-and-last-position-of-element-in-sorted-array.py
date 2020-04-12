#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (35.27%)
# Likes:    2850
# Dislikes: 127
# Total Accepted:    448.4K
# Total Submissions: 1.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
"""
[5,7,7,8,8,10], 8
 l             r
API1   3   
API2        5
return (3, 5-1)

if Not found e.g., to find 6
[5,7,7,8,8,10], 6
API1's return 5 ==  API2's return 5
return (-1, -1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # return self.helper_O_N(nums, target)
        return self.helper_O_lgN(nums, target)

    def helper_O_N(self, nums, target):
        if not nums:
            return [-1, -1]
        # find left most
        l = self.b_left(nums, target)
        has_l = False
        if l < len(nums) and nums[l] == target:
            has_l = True
        if not has_l:
            return [-1, -1]
        
        r_bound = l
        while r_bound < len(nums) and nums[r_bound] == target:
            r_bound += 1
            
        return [l, r_bound-1]

    def b_left(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target: # or nums[mid] > target:
                r = mid
            else:
                l = mid+1
        return l

    
    def helper_O_lgN(self, nums, target):
        if not nums:
            return [-1, -1]
        l = self.b_left(nums, target)
        has_l = False
        if l < len(nums) and nums[l] == target:
            has_l = True
        if not has_l:
            return [-1, -1]
        
        r = self.b_right(nums, target)
        # if l == r:
        #     return [-1, -1]
        return [l, r-1]


    def b_right(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
        # i, j = 0, len(nums)
        # while i < j:
        #     mid = (i+j)//2
        #     if nums[mid] > target:
        #         i = mid
        #     else:
        #         j = mid + 1

        # if l == i:
        #     return [-1, -1]
        # return [l, i-1]


# @lc code=end

