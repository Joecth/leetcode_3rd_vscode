#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.53%)
# Likes:    3959
# Dislikes: 124
# Total Accepted:    262K
# Total Submissions: 595.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        return self.helper_O1(nums, k)
    

    def helper_O1(self, nums, k):
        # pre_fix = [0] + [0]*len(nums)
        # for i in range(1, len(pre_fix)):
        #     pre_fix[i] = pre_fix[i-1] + nums[i-1]        
        
        # for i in range(len(sum)):
        # TODO: lookup pre_fix[i] - pre_fix[j] == k ==>
        #               prefix[i]-k in lookup
        
        lookup = defaultdict(int)
        lookup[0] = 1
        pre_sum = 0
        ans = 0
        for i in range(len(nums)):
            # diff = k-nums[i]        # Failed at [1,2,1,2,1], 3
            pre_sum += nums[i]
            diff = pre_sum - k
            if diff in lookup:
                ans += lookup[diff]
            
            lookup[pre_sum] += 1
        return ans
            
            
    def helper_O2_TLE(self, nums, k):   # 69/80 cases passed (N/A)
        pre_fix = [0] + [0]*len(nums)
        
        for i in range(1, len(pre_fix)):
            pre_fix[i] = pre_fix[i-1] + nums[i-1]
        
        ans = 0
        for i in range(len(pre_fix)):
            for j in range(0, i):
                if pre_fix[i] - pre_fix[j] == k:
                    ans += 1
        return ans
                           
    def helper_O3_TLE(nums):
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                if sum(nums[i:j]) == k:
                    # print(i, j)
                    ans += 1

        return ans   
# @lc code=end

