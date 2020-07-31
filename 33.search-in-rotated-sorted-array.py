#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.68%)
# Likes:    4045
# Dislikes: 413
# Total Accepted:    609.4K
# Total Submissions: 1.8M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return self.search_old(nums, target)
        if not nums:
            return -1
        n = len(nums)
        start, end = 0, len(nums)-1
        while start + 1 < end:
            # print(start, end)
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[end]:   # long head
                # if nums[mid] > target:
                if nums[mid] > target >= nums[start]:
                    end = mid
                else:
                    start = mid
            else: # nums[mid] < nums[end], long tail
                # if nums[mid] < target:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        # print(start, end)
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
                
    def search_old(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) >>1
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur < nums[0]:
                if cur < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:   # cur > nums[0]
                if nums[lo] <= target < cur:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1
# @lc code=end

