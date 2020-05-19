# Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

# Example
# Example 1:
# 	Input:  [3,4,8,5], backpack size=10
# 	Output:  9

# Example 2:
# 	Input:  [2,3,5,7], backpack size=12
# 	Output:  12
	
# Challenge
# O(n x m) time and O(m) memory.

# O(n x m) memory is also acceptable if you do not know how to optimize memory.

# Notice
# You can not divide any item into small pieces.

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # return self.O_NxW(m, A)
        # return self.O_W(m, A)
        return self.O_W_Faster(m, A)
    
    def O_W_Faster(self, m, A):
        if not A or m == 0:
            return 0
            
        dp = [0] + [0] * m
        
        for i in range(len(A)):
            for w in reversed(range(A[i], len(dp))):
                dp[w] = max(dp[w], dp[w-A[i]] + A[i])
            # print(dp)
        return dp[-1]
        
    def O_W(self, m, A):
        if not A or m == 0:
            return 0
            
        dp = [0] + [0] * m
        
        for i in range(len(A)):
            for w in reversed(range(len(dp))):
                if w-A[i] >= 0:
                    dp[w] = max(dp[w], dp[w-A[i]]+A[i])
                else:
                    dp[w] = dp[w]
            # print(dp)
        return dp[-1]
                
    def O_NxW(self, m, A):
        if not A or m == 0:
            return 0
        
        #     
        dp = [([0] + [0] * m) for i in range(len(A)+1)]
        # print(dp)
        for i in range(1, len(dp)):
            for w in reversed(range(len(dp[0]))):
                if w-A[i-1] >= 0:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-A[i-1]] + A[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # print(dp)
        
        return dp[-1][-1]

sol = Solution()
print(sol.backPack(10, [3,4,8,5]))