#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (50.53%)
# Likes:    1612
# Dislikes: 1953
# Total Accepted:    428.4K
# Total Submissions: 839.4K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return self.O_NlogN(nums)
        # return self.O_N_old(nums)
        return self.O_N(nums)
    
    def O_N(self, nums):
        n = len(nums)
        for i in range(n):      # similar to leetcode.41
            while nums[i] >= 0 and nums[i] < n and nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])
        
        # print (nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return n
            
    
    def O_N_old(self, nums):
        # Cycle Sort : https://www.youtube.com/watch?v=1E1Vnq5EsYg
        start, end = 0, len(nums)
        
        while start < end:
            # cur = nums[start]:
            # j = start
            if nums[start] != start and nums[start] < end:
            # if nums[j] != j and nums[j] < end:
                self.swap(nums, start, nums[start])
            else: 
                start += 1
            """
            if nums[start] == start:
                start += 1
            else:
                if nums[start] < end: # 100, 0, 1, 3, 4
                    self.swap(nums[start], nums[nums[start]])
                else:
                    pass
            start += 1
            """
        # print(nums)
        for i in range(end):
            if i != nums[i]:
                return i
        return end
    
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
        
    
    def O_NlogN(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
# @lc code=end

