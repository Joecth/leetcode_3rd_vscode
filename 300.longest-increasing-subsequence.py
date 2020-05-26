#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.04%)
# Likes:    4241
# Dislikes: 101
# Total Accepted:    352.9K
# Total Submissions: 835.1K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.helper(nums)
        return self.helper_B_search(nums)

    
    def helper_B_search(self, nums):
        if not nums: return 0
        n = len(nums)
        
        
        # dp = [0 for _ in range(n+1)]
        # LIS for length equals to ith
        dp = []
        
        for i in range(n):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
                # continue
            else:
                if len(dp) <= 10:   # Optimization according to len(dp)
                    for j in range(len(dp)):
                        if nums[i] <= dp[j]:
                            dp[j] = nums[i]
                            break
                else:              
                    target = nums[i]
                    start, end = 0, len(dp)-1
                    while start + 1 < end:
                        mid = start + (end-start)//2
                        if dp[mid] == target:
                            # dp[mid] = target
                            # break
                            start = mid
                        elif dp[mid] < target:
                            start = mid
                        else:
                            end = mid
                    if dp[start] >= target:
                        dp[start] = target                            
                    elif dp[end] >= target:
                        dp[end] = target        
                    
            # print(dp)
                        
        return len(dp)    
    
    
    def helper(self, nums):
        if not nums: return 0
        n = len(nums)
        
        
        # dp = [0 for _ in range(n+1)]
        # LIS for length equals to ith
        dp = []
        
        for i in range(n):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            else:
                for j in range(len(dp)):
                    if nums[i] <= dp[j]:
                        dp[j] = nums[i]
                        break
        return len(dp)
    
# @lc code=end

