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
"""
 arr        1 1 1 
 presum     0 1 2 3     as key
 idx                    as value
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        # return self.helper_O1(nums, k)
        return self.helper(nums, k)
    
    def helper(self, nums, k):
        # subarray sum ==> pre_sum
        # arr: 1,1,1 ==> pre_sum: 1, 2, 3
        
        #     1. PLAN A
        # for end in n:
        #     for start in n:
        #         if pre_sum[end] - pre_sum[start] == k:
        #             count += 1
        # return count
        
    
        #     2. PLAN B, Optimization
        # Even FASTER?!
        # YES! since for each nums[end], it's searching this value: nums[end]-k
        # seen = {pre_sum at i: [idx1, idx2, idx3]}
        # for end in n:
        #     if nums[end] - k in seen:
        #         count += len(seen)  ==> WRONG, as j should < end
        """ 1. build pre_sum """        
        n = len(nums)
        # pre_sum = [0] * n   ==> FAILED! need a 0 as an offset
        # pre_sum[0] = nums[0]
        pre_sum = [0] * (n+1)
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        # print(pre_sum)
        """ 2. PLAN A, TLE """
        # count = 0
        # for end in range(n+1):
        #     # for start in range(0, n+1):   # BUG when k == 0, CASE: [1], 0
        #     for start in range(0, end):
        #         if pre_sum[end] - pre_sum[start] == k:
        #             # count += end - start
        #             count += 1
        # return count
        
        """ 3. PLAN B """
        count = 0
        from collections import defaultdict
        d = defaultdict(list)
        for end in range(n+1):
            if pre_sum[end] - k in d:
                count += len(d[pre_sum[end] - k])
            d[pre_sum[end]].append(end)
        return count
    
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
    
    def subarraySum_new(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        if len(nums) == 1:
            return int(nums[0] == k)
        
        pre_sum = [0] + [0] * len(nums)
        d = {}
        for i in range(1, len(pre_sum)):
            pre_sum[i] += pre_sum[i-1] + nums[i-1]
            d[pre_sum[i]] = i    
        print(pre_sum)
        
        ans = 0
        for i in range(len(pre_sum)):
            if pre_sum[i] - k in pre_sum:
                ans += 1
        return ans
        
        
        
    def subarraySum_(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            count += prefix.get(total-k, 0)
            prefix[total] = prefix.get(total, 0) + 1
            print(prefix) 
        return count
# @lc code=end

