#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.86%)
# Likes:    6468
# Dislikes: 781
# Total Accepted:    871.8K
# Total Submissions: 3.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return self.helper_TLE_1(nums)
        # return self.helper_TLE_2(nums)
        return self.helper(nums)
    
    def helper(self, nums):
        nums.sort()
        # print(nums)
        res = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            start, end = i+1, len(nums)-1
            
            """ OPTIMIZATION_1 """
            if nums[i] > 0 and nums[i] + nums[start] + nums[end] > 0:
                break
            # if nums[end] < 0 and nums[i] + nums[end-1] + nums[end] < 0:
            #     break
            if i > 0 and nums[i] == nums[i-1]:  # Necessary
                continue
            """ END OF OPTIMIZATION_1 """
            # while start + 1 < end:
            while start < end:
                # total = nums[i] + nums[start] + nums[end]
                # if total == 0:
                """ 2Sum style: set total == target """
                total = nums[start] + nums[end]
                if total == target:
                    res.append([nums[i], nums[start], nums[end]])
                    """ OPTIMIZATION_2 """
                    # start += 1
                    while start+1<end and nums[start+1] == nums[start]:
                        start += 1
                    start += 1
                    while start+1<end and nums[end-1] == nums[end]:
                        end -= 1
                    end -= 1
                    # end -= 1
                    """ END OF OPTIMIZATION_2 """
                elif total < target:
                    start += 1
                else:
                    end -= 1

            # if target == nums[start] + nums[end]:
            #     res.append([nums[i], nums[start], nums[end]])
        return res
        # return list(set([tuple(ans) for ans in res]))   # to solve [[0,0,0], [0,0,0]]  from [0,0,0,0]
    
    
    def helper_TLE_2(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            """ OPTIMIZATION_1 """
            
            """ END OF OPTIMIZATION_1 """
            start, end = i+1, len(nums)-1
            while start+1 < end:
                # total = nums[i] + nums[start] + nums[end]
                # if total == 0:
                """ 2Sum style: set total == target """
                total = nums[start] + nums[end]
                if total == target:
                    res.append([nums[i], nums[start], nums[end]])
                elif total < target:
                    start += 1
                else:
                    end -= 1
            # print(i, start, end)
            if target == nums[start] + nums[end]:
                res.append([nums[i], nums[start], nums[end]])
        return res
    
    
    def helper_TLE_1(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            
            while start+1 < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    res.append([nums[i], nums[start], nums[end]])
                elif total < 0:
                    start += 1
                else:
                    end -= 1
            # print(i, start, end)
            if nums[i] + nums[start] + nums[end] == 0:
                res.append([nums[i], nums[start], nums[end]])                        
        return res
    
    def helper_old(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):  # i, l, r
            l, r = i + 1, len(nums) - 1
            # total = nums[i] + nums[l] + nums[r] # prune here
            # if nums[i] > 0:     # left most
            #     return res      
            # if nums[r] < 0:     # right most
            #     return res
            if nums[i] > 0 and nums[i] + nums[l] + nums[r] > 0: # r can be small
                break
            if nums[r] < 0 and nums[i] + nums[r-1] + nums[r] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:            # -99 8 10 99
                total = nums[i] + nums[l] + nums[r]
                if total == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    ''' The following "whiles" are CRUCIAL...'''
                    # -4 -1 -1 0 1 2 
                    #        idx
                    #     i   1  
                    #     l   2
                    #     r   5
                    ''' #[-2 -1 0 1 2 3] failed for [-1 0 1] 'cause l & r overlapped '''
                    while l < r and nums[l+1] == nums[l]:  
                        l += 1
                    # l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    # r -= 1
                    #'''                    
                    l, r = l + 1, r - 1   #''' l+1 should before while of r '''
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
        
# @lc code=end

