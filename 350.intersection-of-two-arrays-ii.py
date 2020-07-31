#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (50.50%)
# Likes:    1169
# Dislikes: 373
# Total Accepted:    317.2K
# Total Submissions: 625.6K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#

# @lc code=start
from collections import Counter 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = Counter(nums1)
        s2 = Counter(nums2)

        ans = []
        for k in s1.keys():
            n = min(s1[k], s2.get(k, 0))
            for _ in range(n):
                ans.append(k)
        return ans
# @lc code=end

