#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (32.73%)
# Likes:    1604
# Dislikes: 301
# Total Accepted:    306.4K
# Total Submissions: 934.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        return self.helper_O3_O1(nums, target)
        # return self.helper_O3_ON(nums, target)
    
    def helper_O3_O1(self, nums, target):
        nums.sort()
        res = set()
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1
                # nums[i] + nums[j] + nums[j+1] + nums[j+2] > target
                """ Optimization here"""
                # if nums[i] > target and nums[i] + nums[j] + nums[l] + nums[r] < target:
                #     break     TODO:

                if nums[r] < target and nums[i] + nums[j] + nums[r-1] + nums[r] < target:
                    continue
                
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                """ End of Optimization """
                
                while l < r:
                    # while l < r and nums[l] == nums[l+1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r-1]:
                    #     r -= 1
                        
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    diff = tmp - target
                    if diff == 0:
                        res.add(tuple([nums[i], nums[j], nums[l], nums[r]]))    
                        # Caution! other language may not be able to hash list in set, TODO!
                        # Better Alg. in my js implementation
                        l += 1
                        r -= 1
                    elif diff < 0:
                        l += 1
                    else:
                        r -= 1
        return res
        
    def helper_O3_ON(self, nums, target):
        res = set()
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                d = {}
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if target - total in d:
                        g = [nums[i], nums[j], nums[k], target-total]
                        res.add(tuple(sorted(g)))
                    d[nums[k]] = k
        return res
        
# @lc code=end

