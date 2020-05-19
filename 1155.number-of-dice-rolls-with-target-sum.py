#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (49.30%)
# Likes:    521
# Dislikes: 29
# Total Accepted:    30.4K
# Total Submissions: 61.4K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# 
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
# 
# 
# Example 1:
# 
# 
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
# 
# 
# Example 4:
# 
# 
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# 
# 
# Example 5:
# 
# 
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= d, f <= 30
# 1 <= target <= 1000
# 
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # return self.helper_TODO(d, f, target)
        # return self.helper(d, f, target)
        return self.helper(d, f, target)
    
    
    def helper(self, d, f, target):
        
        kMod = 10**9 + 7
        dp = [[0 for j in range(target+1)] for i in range(d+1)]
        
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                lp = min(j, f)
                for k in range(1, lp + 1):
                    dp[i][j] += dp[i - 1][j - k]
        return dp[d][target] % kMod    
        
    def helper_failed(self, dice, faces, target):
        for f in range(faces+1):
            if f <= target:
                dp[1][f] = 1
        
        for d in range(2, dice+1):
            for t in range(1, target+1):
                for f in range(1, faces+1):
                    if t-f >= 0:
                        dp[d][t] += dp[d-1][t-f]
                        dp[d][t] %= kMod
    
        return dp[dice][target]
                    
    def helper_old(self, d, f, target):
        kMod = 10**9 + 7
        dp = [[0 for j in range(target+1)] for i in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, f+1):
                for k in range(j, target+1):
                    dp[i][k] = (dp[i][k] + dp[i-1][k-j]) % kMod
        return dp[-1][-1]
        
    
    def helper_TODO(self, d, f, target):
        # dp: get target number
        mod = 10**9 + 7
        
        @lru_cache(maxsize=None)
        def dp(i, t):
            if i == 0: return 1 if t == 0 else 0
            
            # Pruning 
            if t > f * i or t < i: return 0
            ans = 0
            for k in range(1, min(f, t) + 1):
                ans = (ans + dp(i-1, t-k)) % mod
            return ans
        return dp(d, target)
    
    
                
            
                
# @lc code=end

