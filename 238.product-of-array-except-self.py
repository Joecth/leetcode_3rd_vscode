#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (58.98%)
# Likes:    4030
# Dislikes: 345
# Total Accepted:    431K
# Total Submissions: 729.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start

"""
Input:  [1,2,3,4]
[1  1  2 6]
[24 12 4 1]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        # res = r = l = [1] * len(nums)   # HIS IS MUTABLE ELEMENT
        l = [1] * len(nums)   # HIS IS MUTABLE ELEMENT
        
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        # print(l)
        
        r = [1] * len(nums)
        for j in reversed(range(0, len(nums)-1)):
            r[j] = r[j+1] * nums[j+1]
        # print(r)
        
        res = [1] * len(nums)
        for k in range(0, len(nums)):
            res[k] = l[k] * r[k]
            
        return res
                
# @lc code=end

