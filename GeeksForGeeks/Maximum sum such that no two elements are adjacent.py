#code
# " 3 2           5 10 7 "
#   3  
#     max(3,2).  
class Solution:
    def foo(self, nums):
        # dp[i] means 
        # "Maximum sum such that no two elements are adjacent"
        # till index i
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        # dp[2] = max(nums[2]+dp[2-2], dp[2-1])
        
        for i in range(2, len(range(nums))):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            """
            O(1) sol
            tmp = max(nums[i]+dp0, dp1)
            dp0 = dp1
            dp1 = tmp
            """
        return dp[-1]