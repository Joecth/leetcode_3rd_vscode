#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (33.94%)
# Likes:    3505
# Dislikes: 127
# Total Accepted:    366.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return amount==0
        if amount==0: return 0
        
        dp = [1] + [float('inf')]*amount
        coins_set = set(coins)
        
        for i in range(1, len(dp)):
            if i in coins_set:
                dp[i] = 1
                continue
            
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])    # 1 means self for this time
        if dp[-1] != float('inf'):
            return dp[-1]
        return -1
            
    # Time complexity : O(S∗n). On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
    # Space complexity : O(S). We use extra space for the memoization table.    
    def coinChange_old(self, coins: List[int], amount: int) -> int:
        # coins [1,2,5]
        # dp[1] 1 coins[0]
        # dp[2] 1 coins[1]
        # dp[3]:
        #     dp[1] + $2coins[1]
        #     dp[2] + $1coins[0]
        # dp[4]:
        #     dp[3] + $1
        #     dp[2] + $2
        # dp[5]:
        #     dp[4] + $1
        #     dp[3] + $2
        #     dp[0] + $5
        # dp[6]:
        #     dp[5] + $1
        #     dp[4] + $2
        #     dp[1] + $5
        # ans: dp[i] = min(dp[i-1], dp[i-2], dp[i-5]) + 1
            
        # if amount == 0:
        #     return -1
        
        coins.sort()
        
        dp = [0] + [float('inf')] * amount
        # for coin in coins:  # DANGEROUS for case -- [1],0
        #     dp[coin] = 1
        #     1  2 . 3 . 4 . 5 .6 . 7
        # [0, 1, 1, -1, -1, 1, -1, -1]
        coin : [99999, 9999, 99999999]
        for i in range(len(dp)):
            if dp[i] == float('inf'):
                for j in range(len(coins)):
                    if i < coins[j]:
                        break       # by assumption that coins is already adopted with coins.sort()
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)# + 1
        
        if dp[amount] == float('inf'):
            ans = -1
        else:
            ans = dp[amount]
        return ans
        # REMEMBER to CHECK boundary condition
# @lc code=end

