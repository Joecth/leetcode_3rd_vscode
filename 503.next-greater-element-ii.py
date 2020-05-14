#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (54.42%)
# Likes:    1265
# Dislikes: 64
# Total Accepted:    84.4K
# Total Submissions: 153.4K
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Monotonic Stack
        if not nums:
            return []
        
        res = [-1] * len(nums)
        S = []
        # arr = nums
        for i in range(len(nums)):
            while S and nums[S[-1]] < nums[i]:
                idx = S.pop()
                res[idx] = nums[i]
            S.append(i) 
        # return res     # Failed at [1,2,1] => [2,-1,-1], should be[2,-1,2], 
                         # so, we need post-handle
            
        for i in range(len(nums)):  # one more loop
            while S and nums[S[-1]] < nums[i]:
                idx = S.pop()
                res[idx] = nums[i]
        return res        
# @lc code=end

