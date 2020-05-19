# 562. Backpack IV
# Given an integer array nums[] which contains n unique positive numbers, num[i] indicate the size of ith item. An integer target denotes the size of backpack. Find the number of ways to fill the backpack.

# Each item may be chosen unlimited number of times

# Example
# Example1

# Input: nums = [2,3,6,7] and target = 7
# Output: 2
# Explanation:
# Solution sets are: 
# [7]
# [2, 2, 3]
# Example2

# Input: nums = [2,3,4,5] and target = 7
# Output: 3
# Explanation:
# Solution sets are: 
# [2, 5]
# [3, 4]
# [2, 2, 3]


class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums or target == 0:
            return 0
        # return self.O_NxW(nums, target)
        return self.O_W(nums, target)

    def O_W(self, nums, target):
                
        dp = [1] + [0] * target
        for i in range(len(nums)):
            cur_weight = nums[i]
            for w in range(nums[i], target+1):
                dp[w] = dp[w] + dp[w-cur_weight]
            # print(dp)
        return dp[-1]
        # return count
        
    def O_NxW(self, nums, target):
        """
                0 1 2 3 4 5 6 7 8 9 10
        0          1 0 0 0 0 0 0 0 0 0 0 
        item1:2    1 0 1 0 1 0 1 0 1 0 1
        item2:3    1 0 1 1 1 1 1 1 1 1 1
                            ★
        item3:6    
        item3:7
        """        
        # under i items, with max j weigths, the maximum methods!
        dp = [[0 for j in range(target+1)] for i in range(len(nums)+1)]
        
        dp[0][0] = 1
        
        # for w in range(1, len(target)+1):
        #     dp[0][w] = 0
            
        for i in range(1, len(nums)+1):
            cur_weight = nums[i-1]
            for w in range(0, target+1):
                if w-cur_weight >= 0:
                    dp[i][w] = dp[i-1][w] + dp[i][w-cur_weight]
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[-1][-1]


