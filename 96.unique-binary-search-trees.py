#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (50.03%)
# Likes:    2854
# Dislikes: 106
# Total Accepted:    266.3K
# Total Submissions: 527K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#

# @lc code=start
'''
1   a
2   a   b   
     b a
3  c
     [a b]   
   T[3] = T[0]xT[2] + T[1]xT[1] + T[2]xT[0]
4  T[4] = T[0]xT[3] + T[1]xT[2] + T[2]xT[1] + T[3][0]

5)
         1                2                 3      
    {}  {2 3 4 5}      {1}  {3 4 5}    {1 2}   {4 5}
         5         
{1 2 3 4 }  {}

6)   
     1                2                  3      
  {}  {2 3 4 5 6}  {1}  {3 4 5 6}  {1 2}   {4 5 6}

     6.       5                  4
     
     
'''

class Solution:
    def numTrees(self, n):
        # return self.DP(n)
        if n == 0: return 0
        
        d = {0:1, 1:1}
        cnt = 0
        return self.dfs(n, d, cnt)
    
    def DP(self, n):
        """
        F(i, n): case as G(n) with i as root
        G(3) = F(1,3)    +  F(2,3) +    F(3,3)
              G(0)*G(2)    G(1)*G(1)   G(2)*G(0)
        G(n) = \sum_{1}^{n}( G(i-1)*G(n-i) )
        """
        G = [0] * (n+1)
        G[0] = G[1] = 1
        for tmp in range(2, n+1):
            for i in range(1, tmp+1):
                G[tmp] += G[i-1] * G[tmp-i]
        return G[n]
        # ref: https://www.youtube.com/watch?v=GgP75HAvrlY
        # Time: N^2
        # Space: N
    
    def dfs(self, n, d, cnt):
        if n in d:
            return d[n]
        
        for i in range(1, n+1):
            leftCombination = self.dfs(i-1, d, cnt)
            rightCombination = self.dfs(n-i, d, cnt)
            cnt += leftCombination * rightCombination
            
        d[n] = cnt
        return cnt
            
    
    def numTrees_Generalization(self, n: int) -> int:
        dp = [0] + [0]*n    # 0 0 0 0 0 0 0
        dp[0] = 1
        dp[1] = 1
        # dp[2] = 2
        '''
        dp[n] = dp0 * dp[n-1] + dp1*dp(n-2) ..... dp(n-2)*dp1 + dp[n-1]*dp0
        dp[3] = dp[0]*dp[2] + dp1*dp1 + dp2*dp0
                    2           1           2
        dp[4] = dp0 * dp3 + dp1*dp2  + 
                 1    5      1   2      2 1
        '''                                     # n==3
        for i in range(2, n+1):                 # 0 1 2
            if dp[i]:
                    continue
            for j in range(0, n):   # 2 1 0
                dp[i] += dp[j]*dp[(i-1)-j]           #dp2= dp1*dp0; dp3 = dp2*dp0       
        return dp[n]

        
# @lc code=end

