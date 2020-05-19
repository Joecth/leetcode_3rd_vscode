#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (41.69%)
# Likes:    3356
# Dislikes: 51
# Total Accepted:    243.9K
# Total Submissions: 575.5K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#

# @lc code=start
"""
    ''  r   o   s   
''  0   1   2   3
   prev
h   1   1   2   3

o   2   2   
r   3
s   4
e   5
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.O_MxN(word1, word2)
        # return self.O_Nx2(word1, word2)
        return self.O_Nx1(word1, word2)
    
    def O_Nx1(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [0 for j in range(n+1)]
        
        for j in range(1, n+1):
            dp[j] = j
        # print(dp)
        
        # prev = dp[0]
        for i in range(1, m+1):
            prev = dp[0]    # Important!
            dp[0] = i
            for j in range(1, n+1):
                current = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                prev = current
            # print(dp)
        return dp[-1]
                
    def O_Nx2(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [0 for j in range(n+1)]
        
        
        for j in range(1, n+1):
            dp[j] = j
        # print(dp)
        
        for i in range(1, m+1):
            prev_row = dp.copy()
            dp[0] = i
            ch1 = word1[i-1]
            for j in range(1, n+1):
                ch2 = word2[j-1]
                if ch1 != ch2:
                    dp[j] = min(dp[j], dp[j-1], prev_row[j-1]) + 1
                else:
                    dp[j] = prev_row[j-1]
            # print(dp)
        return dp[-1]
    
    def O_MxN(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            dp[i][0] = i
            
        for i in range(1, m+1):
            ch1 = word1[i-1]
            for j in range(1, n+1):
                ch2 = word2[j-1]
                if ch1 != ch2:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
        
        
    def minDistance_old(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # dp[0][0] = 0
        

        for i in range(0, m+1):
            for j in range(0, n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if i <= m and j <= n and word1[i-1] != word2[j-1]:     # index problem...
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = dp[i-1][j-1]
        # print(dp)
        return dp[m][n]     
# @lc code=end

