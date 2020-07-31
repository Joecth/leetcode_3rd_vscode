#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (31.25%)
# Likes:    1446
# Dislikes: 87
# Total Accepted:    155.3K
# Total Submissions: 494.5K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n,  = len(s1), len(s2)
        if m + n != len(s3):
            return False
        # dp = [False] * (len(s3)+1)
        # return self.helper_WRONG(s1, s2, s3, 0, 0, dp, 0)
        return self.sol_dp(s1, s2, s3)
        return self.dfs_main(s1, s2, s3)
        return self.dfs_lru(s1, s2, s3, 0, 0, 0)
    
    def dfs_main(self, s1, s2, s3):
        valid = invalid = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        # return self.dfs(s1, s2, s3, 0, 0, 0, invalid)
        return self.dfs2(s1, s2, s3, 0, 0, 0, valid)
    
    def dfs2(self, s1, s2, s3, i, j, k, valid):
        if valid[i][j]:
            return True
        if len(s3) == k:
            return True
        ok = i < len(s1) and s1[i] == s3[k] and self.dfs2(s1, s2, s3, i+1, j, k+1, valid) or \
             j < len(s2) and s2[j] == s3[k] and self.dfs2(s1, s2, s3, i, j+1, k+1, valid)
        if ok:
            valid[i][j] = True
        return ok
    
    def dfs(self, s1, s2, s3, i, j, k, invalid):
        if invalid[i][j]:
            return False
        if k == len(s3):
            return True
        valid = i < len(s1) and s1[i] == s3[k] and self.dfs(s1, s2, s3, i+1, j, k+1, invalid) or \
                j < len(s2) and s2[j] == s3[k] and self.dfs(s1, s2, s3, i, j+1, k+1, invalid)
        if not valid:
            invalid[i][j] = True
        return valid
    
    # from functools import lru_cache
    # @lru_cache(maxsize=512)
    def dfs_lru(self, s1, s2, s3, i, j, k):
        # if invalid[i][j]:
        #     return False
        if k == len(s3):
            return True
        valid = i < len(s1) and s1[i] == s3[k] and self.dfs_lru(s1, s2, s3, i+1, j, k+1, invalid) or \
                j < len(s2) and s2[j] == s3[k] and self.dfs_lru(s1, s2, s3, i, j+1, k+1, invalid)
        # if not valid:
        #     invalid[i][j] = True
        return valid    
    """
    s1\s2  ''   d   b   b   c   a       
    ''     T    F              
    a       
    a           ←↑
    b
    c
    c
    
    s3  "a a d b b " 
    """
    def sol_dp(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0: dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[0+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+0-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
        
    # dfs
    def helper_WRONG(self, s1, s2, s3, i, j, dp, idx):    # WRONG!  dp==>memo
        # i = j = 0
        for k in range(idx, len(s3)):
            if s3[k] != s1[i] and s3[k] != s2[j]:
                return False
            elif s3[k] == s1[i] and s3[k] == s2[j]:
                dp[k] = self.helper_WRONG(s1, s2, s3, i+1,j, dp, idx+1) or self.helper(s1, s2, s3, i,j+1, dp, idx+1)
            elif s3[k] == s1[i]:
                dp[k] = self.helper(s1, s2, s3, i+1, j, dp, idx+1)
            else:
                dp[k] = self.helper(s1, s2, s3, i, j+1, dp, idx+1)
        return dp[len(s3)-1]   # ==> ?!
    
    def WRONG(self, s1, s2, s3):
        # s1:ab  
        # s2:bca
        # s3:abcba
        i = j = 0
        for k in range(len(s3)):
            if i < m and s3[k] == s1[i]:    #WRONG!
                i += 1
            elif j < n and s3[k] == s2[j]:
                j += 1
            else:
                return False
        return True        
# @lc code=end

