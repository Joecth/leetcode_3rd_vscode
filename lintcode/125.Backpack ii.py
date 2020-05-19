# There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.

# What's the maximum value can you put into the backpack?

# Example
# Example 1:

# Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
# Output: 9
# Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9 
# Example 2:

# Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
# Output: 10
# Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10 
# Challenge
# O(nm) memory is acceptable, can you do it in O(m) memory?

# Notice
# A[i], V[i], n, m are all integers.
# You can not split an item.
# The sum size of the items you want to put into backpack can not exceed m.
# Each item can only be picked up once

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        # return self.O_W(m, A, V)
        return self.O_W_Faster(m, A, V)
        
    def O_W_Faster(self, m, A, V):
        if not A or m == 0 or len(A) != len(V):
            return 0
        
        dp = [0] + [0] * m
        
        for i in range(len(A)):
            for w in reversed(range(A[i], m+1)):
                dp[w] = max(dp[w], dp[w-A[i]] + V[i])
            # print (dp)
        return dp[-1]
        
    def O_W(self, m, A, V):
        if not A or m == 0 or len(A) != len(V):
            return 0
        
        dp = [0] + [0] * m
        
        for i in range(len(A)):
            for w in reversed(range(len(dp))):
                if w-A[i] >= 0:
                    dp[w] = max(dp[w], dp[w-A[i]] + V[i])
                else:
                    dp[w] = dp[w]
                
        return dp[-1]
        
