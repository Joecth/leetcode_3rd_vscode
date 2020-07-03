#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (36.93%)
# Likes:    2312
# Dislikes: 106
# Total Accepted:    265.8K
# Total Submissions: 703.1K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#

# @lc code=start
import sys
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        return self.helper(s, nums)
    
    def helper(self, s, nums):
        start = 0
        n = len(nums)
        min_len = sys.maxsize
        total = 0
        for end in range(n):
            total += nums[end]
            while total >= s:
                min_len = min(min_len, end-start+1)
                total -= nums[start]
                start += 1
                
        return min_len if min_len != sys.maxsize else 0
        
    def old():
        '''
                [2,3,1,2,4,3]
        ps =    [0,2,5,6,8,12,15]    # pre_sum

        curr_idx 0
        result = float('inf')
        if diff  (8-curr_idx) - 7 >= 0 
            result = min(result, 8-curr_idx)
            update curr_idx to index of value 8
        '''
        if not nums:
            return 0
        
        accu = 0
        ps = [0] * (len(nums)+1)
        for i in range(1, len(ps)):
            accu += nums[i-1]
            ps[i] = accu
            
        # ps[-1] = ps[-2] + nums[-1]
        print(ps)
        
        curr_idx = 0
        result = float('inf')
        for k in range(1, len(ps)):
            
            # SHOULD REPLACE THIS W/ B-SEARCH, to search the residual
            # if ps[k]-ps[curr_idx] - s >= 0:
            if ps[k]-ps[curr_idx] - s >= 0:    
                while ps[k]-ps[curr_idx] - s >= 0:
                    curr_idx += 1
                curr_idx -= 1
            
                result = min(result, k-curr_idx)
                # curr_idx = k
        
        if result == float('inf'):
            result = 0
        return result
        
        
            
                
# @lc code=end

