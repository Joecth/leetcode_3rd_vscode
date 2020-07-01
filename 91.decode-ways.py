#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.81%)
# Likes:    2571
# Dislikes: 2752
# Total Accepted:    392.4K
# Total Submissions: 1.6M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
'''
1 2 6 5

dp[idx]
dp[0]  "" 0
dp 1      1 if  s[0] = [1,9], 0
dp 2      
          dp1 +    s[1] btw 1~9?1:0
            plus
            
          s[0:2] btw 1~26?1:0 ==> 
          dp0 + s[1] btw 1~9?1:0
         
12       

dp 3      dp[1] +  26 s[1:3]  btw 1~26?1:0
            plus
          dp[2] +  6  s[2] btw 1~9?1:0
            
dp[n] = dp[n-1] + 
'''

"""
"12"
dp  i       self,   dp[i-1]
 dp[0]:     1       0
 dp[1]:     1       1
 dp[1] = dp[0] + 1
 
"226"
dp  i       self,   dp[i-1]
 dp[0]:     1       0
 dp[1]:     1       1
 dp[1] = dp[0] + 1
"""
"""
29      dp: 1 2

92      dp: 1 1
"""

class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        # return self.numDecodings_dp_old(s)
        # return self.again_FAILED(s)
        # return self.sol1_recur_TLE(s, 0)    # can be solved by using lru_cache
        # return self.sol2_recur_memo(s, 0, {}) # TOP-DOWN
        # return self.sol3_bottomup_dp(s, 0)  # BOTTOM-UP
        # return self.my_dp_O_N_FAILED(s)
        return self.my_dp_O_N(s)
        return self.my_dp_O_1(s)    # TODO...
            
    def my_dp_O_N(self, s):
        dp = [0] * (len(s)+1)

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1
         
        for i in range(2, len(s) + 1): 
            # One step jump
            if int(s[i-1]) != 0 :   
                dp[i] += dp[i - 1]
            # Two step jump
            if  10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i - 2]
        # print(dp)
        return dp[len(s)]
        # https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
    def my_dp_O_N_FAILED(self, s):
        """
           i
        22 6
           ^
        2 26
          ^^
        """
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        """ Following len(s) >= 2 """
        n = len(s)
        dp = [0] * n
        
        dp[0] = 1
        # dp[1] = 
        dp[1] = 1 if (int(s[0:2]) > 26 or s[1] == '0') else 2
        if 1 <= int(s[0:2]) <= 26:
            dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = 1
            
        for i in range(2, len(s)+1):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1 : i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[n-1]
                
        
    
    # Time: O(n)
    # Space: O(n) -> O(1), w/ rolling array 
    def sol3_bottomup_dp(self, s, idx): # Induction Rule
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i+1]
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]
            
    # https://www.laioffer.com/en/videos/2018-05-14-91-decode-ways/  , 9:20
    
    # Time: O(1) * (N+1) = O(N)
    # Space: O(N)
    def sol2_recur_memo(self, s, idx, memo):
        if idx in memo:
            return memo[idx]
        if idx == len(s):
            # memo[idx] = 1
            # return memo[idx]  # not necessary
            return 1

        ways = 0
        if 1 <= int(s[idx]) <= 9:
            ways += self.sol2_recur_memo(s, idx+1, memo)
        if 10 <= int(s[idx:idx+2]) <= 26:   # 看 s[index] & s[index+1] 能被decode
            ways += self.sol2_recur_memo(s, idx+2, memo)
        memo[idx] = ways
        return memo[idx]
        # https://www.laioffer.com/en/videos/2018-05-14-91-decode-ways/  , 6:25, with Recursion-Tree expansion
        
    
    # Time: O(2^N)
    # Space: O(N), call stack
    @lru_cache(maxsize=None)
    # https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
    def sol1_recur_TLE(self, s, idx):
        if idx == len(s):
            return 1
        ways = 0
        if 1 <= int(s[idx]) <= 9:
            ways += self.sol1_recur_TLE(s, idx+1)
        if 10 <= int(s[idx:idx+2]) <= 26:   # 看 s[index] & s[index+1] 能被decode
            ways += self.sol1_recur_TLE(s, idx+2)
        return ways
        # https://www.laioffer.com/en/videos/2018-05-14-91-decode-ways/  , 2:28, with Recursion-Tree expansion
        
    def again_FAILED(self, s):
        dp = [0] * len(s)
        if s[0] == '0':
            return 0
        dp[0] = 1 
        
        # ISSUE: 100
        for i in range(1, len(s)):
            # if s[i] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
            #     dp[i] = dp[i-1] + 1
            # else:
            #     dp[i] = dp[i-1]
            if s[i] != '0':
                pass
                
        return dp[len(s)-1]
        
    def numDecodings_dp_old(self, s):
        if not s: return 0
        len_s = len(s)
        dp = [1] + [0] * len_s
        for i in range(1, len_s + 1):
            if s[i - 1] != '0': 
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26: 
                dp[i] += dp[i - 2]
        return dp[len_s]

    def numDecodings_wrong(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] + [0 for i in range(len(s))]
        dp[0] = 0
        # if 0 < ord(s[0]) - ord('0') <= 9:
        if self.is_valid_1_digit(s[0]):
            dp[1] = 1
        else:
            dp[1] = 0
            
        for j in range(2, len(s)+1):
            if self.is_valid_1_digit(s[j-1:j]):
                if dp[1] != 0:  # case of 01
                    dp[j] = dp[j-1] + 1
            if self.is_valid_2_digits(s[j-2:j]):
                dp[j] +=  dp[j-2] + 1
            # if self.is_valid_2_digits(s[j-2:j]):
            #     dp[j] = dp[j-2] + 1
            # else:
            #     dp[j] = dp[j-2]
            # if self.is_valid_1_digit(s[j-1]):
            #     dp[j] +=  dp[j-1] + 1
            # else:
            #     dp[j] += dp[j-1] #dp[j-1]
                
        return dp[-1]    
            
    def is_valid_1_digit(self, s):
        if 0 < ord(s[0]) - ord('0') <= 9:
            return True
        else:
            return False
    
    def is_valid_2_digits(self, s2):
        # if 0 < ord(s2) - ord('0') <= 26:
        if 10 <= int(s2) <= 26:
            return True
        else:
            return False
# @lc code=end

