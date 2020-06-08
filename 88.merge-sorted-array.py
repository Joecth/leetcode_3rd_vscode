#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (38.37%)
# Likes:    2060
# Dislikes: 4011
# Total Accepted:    568.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n - 1
        num_zeros = m - n
        i = m - 1
        k = len(nums1) - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        if i > 0:
            # return nums1   # just the ANSWER
            pass
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        
        
        
        
    def merge_old(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
           
        num_zeros = len(nums1) - len(nums2)
        idx_1 = num_zeros - 1
        idx_2 = len(nums2) - 1

        k = -1
        while idx_1 >= 0 and idx_2 >= 0:
            if nums1[idx_1] >= nums2[idx_2]: # CAUTIOUS! case of "="
                nums1[k] = nums1[idx_1]
                idx_1 -= 1
            elif nums1[idx_1] < nums2[idx_2]:
                nums1[k] = nums2[idx_2]            
                idx_2 -= 1
            
            k -= 1
            
        # if idx_2 < 0:
        #     nums1[0:len(nums1)+k] = nums1[:]
        if idx_1 < 0:
            nums1[0:len(nums1)+k+1] = nums2[0:idx_2+1]
            
                
# @lc code=end

