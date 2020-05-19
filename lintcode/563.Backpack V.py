# 563. Backpack V
# Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

# Each item may only be used once

# Example
# Given candidate items [1,2,3,3,7] and target 7,

# A solution set is: 
# [7]
# [1, 3, 3]
# return 2

"""
            0 1 2 3 4 5 6 7 
0           1 0 0 0 0 0 0 0
item1:1     1 1 1 1 1 1 1 1
item2:2    
item3:3
item4:3
item5:7
"""

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        dp = [1] + [0] * target
        
        for i in range(len(nums)):
            cur_weight = nums[i]
            for w in reversed(range(cur_weight, target+1)):
                dp[w] = dp[w] + dp[w-cur_weight]
            # print(dp)
        return dp[-1]