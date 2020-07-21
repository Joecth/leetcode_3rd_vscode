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
        return self.helper(nums)
        return self.helper_opt(nums)
    
#     def helper_opt(self, nums):
#         n = len(nums)    
#         res = [1] * n
#         prev = 1
#         for i in range(1,n):
#             res[i] = prev * nums[i-1]
#             prev = res[i]
#         # print(res)
        
#         suffix = 1
#         for j in range(n-2, -1, -1):
            
            
#         print(res)
#         return res
    
    def helper(self, nums):
        n = len(nums)
        l = [1] * n
        r = [1] * n
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        # print(l)
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        # res = [1] * n
        for j in range(n):
            l[j] *= r[j]
        return l
#     def old():
#         # res = r = l = [1] * len(nums)   # HIS IS MUTABLE ELEMENT
#         l = [1] * len(nums)   # HIS IS MUTABLE ELEMENT
        
#         for i in range(1, len(nums)):
#             l[i] = l[i-1] * nums[i-1]
#         # print(l)
        
#         r = [1] * len(nums)
#         for j in reversed(range(0, len(nums)-1)):
#             r[j] = r[j+1] * nums[j+1]
#         # print(r)
        
#         res = [1] * len(nums)
#         for k in range(0, len(nums)):
#             res[k] = l[k] * r[k]
            
#         return res
        
        
#     def productExceptSelf_old(self, nums: List[int]) -> List[int]:
        
#         # --> prefix_product_l: [1, 1, 2, 6]
#         #         p_l[1]: prod(0) 
#         #         p_l[2]: prod(0~1)
#         #         p_l[3]: nums[0]*nums[1]*num[2]
        
#         prod_l = [1] * len(nums)
#         accu = 1
#         for i in range(1, len(nums)):
#             accu *= nums[i-1]
#             prod_l[i] = accu
#         # prod_l ==> [1,1,2,6]
        
#         prod_r = [1] * len(nums)
#         accu = 1            
#         for j in reversed(range(0, len(nums)-1)): # [0,1,2] ==> [2,1,0]
#             accu *= nums[j+1]
#             prod_r[j] = accu
            
#         # prod_r ==> [24, 12, 4, 1]
#         #         p_r[0]: prod(1~3)
#         #         p_r[1]: prod(2~3)                  
#         #         p_r[2]: prod(3)
#         #         p_r[3]: 1
        
#         result = []
#         '''np.mul(p_l, p_l)'''
#         for k in range(len(nums)):
#             val = prod_l[k] * prod_r[k]
#             result.append(val)
            
#         return result                
# @lc code=end

