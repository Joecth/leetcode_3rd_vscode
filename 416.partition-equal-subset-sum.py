#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (42.57%)
# Likes:    2520
# Dislikes: 69
# Total Accepted:    174.6K
# Total Submissions: 402.8K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:  # ODD can't be partitioned into 2 parts
            return False
        
        target = total // 2
        if max(nums) > target:
            return False

        # return self.bt_main_TLE(nums)
        # return self.dp_O_N(nums, target)    # with j's optimization
        return self.dp_O_1(nums, target)    # with j's optimization
    
    def dp_O_1(self, nums, target):
        n = len(nums)
        # dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp = [True] + [False] * target
            
        for i in range(1, n+1):
            # for j in range(target, -1, -1):
            for j in range(target, nums[i-1]-1, -1):
                # if j - nums[i-1] >= 0: 
                    # dp[j] = dp[j] or dp[j-nums[i-1]]
                dp[j] = dp[j] or dp[j-nums[i-1]]                    
                # if j - nums[i-1] >= 0: 
                #     dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i-1]] and True)
                #                                                     # take myself
                # else:
                #     dp[i][j] = dp[i-1][j]
            # print(dp)
        # return dp[n-1][target]
        return dp[-1]
    
    def dp_O_N(self, nums, target):
        """
        half_sum : 11
                 0 1 2 3 4 5 6 7 8 9 10 11
        item1 1  T T F F                F
        item2 5  T T F F F T 
        item3 11
        item4 5
        meaning of dp array ? 
        whether the weights can be achieved by the items
        my_weight = nums[i]
        if i-my_weight >=0:
            dp[i][w] = dp[i-1][w]  or     (dp[i-1][w-my_weight] and True)
                     UP(DONT TAKE cur)     TAKE current  
        else:
            dp[i-1][j]
        """
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = True
            
        for i in range(1, n+1):
            # for j in range(target, -1, -1):
            for j in range(target, nums[i-1]-1, -1):
                # if j - nums[i-1] >= 0: 
                    # dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i-1]] and True)
                                                                    # take myself
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i-1]] and True)
                # else:
                #     dp[i][j] = dp[i-1][j]
            # print(dp)
        return dp[n-1][target]
    
    def bt_main_TLE(nums):        
        res = [False]
        # nums.sort()
        self.bt_TLE(nums, 0, 0, target, res)
        return res[0]
            
    def bt_TLE(self, nums, idx, now_sum, target, res):
        if idx >= len(nums):
            return 
        if res[0]:
            return 
        if now_sum > target:
            return
        if now_sum == target:
            res[0] = True
            return
        
        # item.append(nums[idx])
        self.bt_TLE(nums, idx+1, now_sum+nums[idx], target, res)
        # item.pop()
        self.bt_TLE(nums, idx+1, now_sum, target, res)
        
#         total = sum(nums)
#         if total % 2: return False
        
#         target = int(total/2)
#         dp = [([True] +  [False]*target) for i in range(len(nums))]
        
        
#         for i in range(1, len(dp)):
#             for w in range(1, len(dp[0])):
#                 cur_weight = nums[i]
#                 if i - cur_weight >= 0:
#                     dp[i][w] = dp[i-1][w] or (dp[i-1][w-cur_weight] and True)
#                 else:
#                     dp[i][w] = dp[i-1][w]
                    
#         return dp[-1][-1]
        
# @lc code=end

