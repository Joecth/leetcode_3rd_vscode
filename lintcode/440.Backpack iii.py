# 440. Backpack III
# 
# Given n kinds of items, and each kind of item has an infinite number available. The i-th item has size A[i] and value V[i].

# Also given a backpack with size m. What is the maximum value you can put into the backpack?

# Example
# Example 1:

# Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
# Output: 15
# Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.
# Example 2:

# Input: A = [1, 2, 3], V = [1, 2, 3], m = 5
# Output: 5
# Explanation: Strategy is not unique. For example, put five item 0 (A[0] = 1, V[0] = 1) into backpack.
# Notice
# You cannot divide item into small pieces.
# Total size of items you put into backpack can not exceed m.

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        # return 111
        if not A or m == 0 or len(A) != len(V):
            return 0
        # return self.O_NxWxK_TLE(A, V, m)
        # return self.O_W_TLE(A, V, m)
        return self.O_W_Faster(A, V, m)
        
    def O_W_Faster(self, A, V, m):
        dp = [0] * (m+1)
        
        for i in range(len(A)):
            for w in range(A[i], m+1):
                dp[w] = max(dp[w], dp[w-A[i]]+V[i])
        return dp[-1]
        
    def O_W_TLE(self, A, V, m):
        dp = [0] * (m+1)
        
        for i in range(len(A)):
            for w in reversed(range(A[i], m+1)):
                for k in range(1, int(w/A[i])+1): # means "Able to take A[i]"
                    dp[w] = max(dp[w], dp[w-k*A[i]] + k*V[i])
            # print(dp)
                    
        return dp[-1]
        
        
    def O_NxWxK_TLE(self, A, V, m):
        # dp = [0] + [0] * m
        dp = [([0] * (m+1)) for i in range(len(A)+1)]
        # print(dp)
        
        # for i in range(1, len(A)):
        for i in range(1, len(A)+1):
            for w in reversed(range(0, m+1)):
                max_cur = int(w/A[i-1])
                # for k in range(0, max_cur):
                for k in range(0, max_cur+1):
                    # dp[w] = max(dp[w], dp[w-k*A[i]] + k*V[i])
                    if w-k*A[i-1] >= 0:
                        dp[i][w] = max(dp[i-1][w], dp[i-1][w-k*A[i-1]] + k*V[i-1])
                    # else:
                    #     dp[i][w] = dp[i-1][w]
            # print(dp)
        return dp[-1][-1]


sol = Solution()
print(sol.backPackIII(A=[2,3,5,7], V=[1,5,2,4], m=10))