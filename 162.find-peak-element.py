#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end-start)//2
            if (nums[mid] > nums[mid-1]):
                start = mid
            else:
                end = mid
        
        if nums[start] > nums[end]:
            return start
        return end
        



    def O(self, nums):
        if len(nums) == 1:
            return 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1
# @lc code=end

