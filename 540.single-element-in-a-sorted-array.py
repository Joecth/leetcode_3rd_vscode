#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] == nums[mid-1]:
                # 3 3 5
                    start = mid + 1
                else:
                # 3 5 5
                    end = mid - 1
            
        return nums[start]        
    def O(self, nums):
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
# @lc code=end

