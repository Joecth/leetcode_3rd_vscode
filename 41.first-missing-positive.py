#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.96%)
# Likes:    3167
# Dislikes: 764
# Total Accepted:    317.2K
# Total Submissions: 1M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        # return self.O_N(nums)   # pass
        # return self.O_1_Tagging(nums)
        return self.O_1_Hashing(nums)
    
    
    def O_1_Hashing(self, nums):
        """
        3,4,-1,1    2
        1,-1,3,4
        
        f==hash : "nums[i]"" ==> should be at pos of "nums[i]-1"
                    1               0
                    3               2
                    4               3
        """
        n = len(nums)
        for i in range(n):
            # idx = nums[i]-1  BUGGY!!! INFINITE LOOP
            # while nums[i] > 0 and nums[i] <= n and nums[i] != nums[idx]:
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:            
                # print(nums)
                self.swap(nums, nums[i]-1, i) # stores nums[i] to nums[idx]
        
        for i in range(n):
            if nums[i] != i+1:  # 3 should be at pos 2
                return i+1
        return n+1  # also satisfy []
    
    def swap(self, nums, to, fr):
        nums[to], nums[fr] = nums[fr], nums[to]
        
        
    def O_1_Tagging(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = float('inf')
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:    # -4 already turned into -MAX,
                            # here is to handle duplicates
                nums[num-1] = -abs(nums[num-1])
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return  n+1
        # https://www.youtube.com/watch?v=8DqewGsVNkI
        
    def O_N(self, nums):
        n = len(nums)
        states = [0 for j in range(n)]
        
        for i in range(n):
            j = nums[i]
            if j > 0 and j <= n:
                states[j-1] = 1
        print (states)
        
        for i in range(n):
            if states[i] == 0:
                return i+1
        return n+1        
# @lc code=end

