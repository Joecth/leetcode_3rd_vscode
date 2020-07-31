# 1147. Work Plan
# 中文English
# Xiaomei is the manager in charge of the team and needs to make the work plans for the team to help the team generate the most value. Every week, the team will have alternative tasks, one is a simple task, and the other is a complex task. In week i, the value of the team’s completion of simple tasks is low_ilow
# ​i
# ​​ , and the value of completion of complex tasks is high_ihigh
# ​i
# ​​ . Due to the technical difficulty of the complex task itself, if the team chooses to perform the complex task in week i, they need to concentrate on preparation without doing any task in week i-1. If the team choose to perform a simple task in week i, there is no need to make any preparations in advance. Now that Xiaomei's team has received a list of expected tasks for the next n weeks, please help Xiaomei determine the weekly work schedule that help the team generate the most value.

# Example
# Example 1:

# Input:low=[4,2,3,7],hard=[3,5,6,9]
# output:17
# Explanation:
# Pick simple task in the first week, value = 4
# Prepare for the second week and pick complex task in the third week, value = 4 + 6 = 10
# Pick a simple task in the fourth week, value = 10 + 7 = 17
# Example 2:

# Input:low=[1,3,5,9],high=[3,5,7,9]
# Output:19
# Notice
# 1 \leq |low|,|high| \leq 100001≤∣low∣,∣high∣≤10000
# 1 \leq low[i],high[i] \leq 100001≤low[i],high[i]≤10000

class Solution:
    """
    @param low: the simple task
    @param high: the complex task
    @return: the most value
    """
    def workPlan(self, low, high):
        # Write your code here.
        if not low or not high or len(low) != len(high):
            return 0
        # return self.O_Nx2(low, high)
        # return self.O_Nx1(low, high)   
        return self.O_3x1(low, high)  # can also have O_3x2
        
    def O_3x1(self, low, high):
        n = len(low)
        """
        ith day, dp[i][0] Max Value with low; 
                 dp[i][1] Max Value with high
        """
        # dp = [[0] * n for _ in range(2)]
        # dp = [[0]*1 for _ in range(n)]
        dp = [0] * 3
        dp[0] = low[0]
        if n == 1:
            return low[0]
        
        # 1st day
        # dp[1][0] = max(dp[1-1][0], dp[1-1][1]) + low[1]
        # dp[1][1] = 0 + high[1]
        dp[1] = max(dp[1-1] + low[1], 0 + high[1])
        if n == 2:
            return dp[1]
            # return max(dp[1][0], dp[1][1])
            
        for i in range(2, len(low)):
            # dp[i] = max(dp[i-1] + low[i], dp[i-2] + high[i])
            dp[i%3] = max(dp[(i-1)%3] + low[i], dp[(i-2)%3] + high[i])
        
        return dp[(n-1)%3]
        # return max(dp[n-1][0], dp[n-1][1])    
        
    def O_Nx1(self, low, high):
        n = len(low)
        """
        ith day, dp[i][0] Max Value with low; 
                 dp[i][1] Max Value with high
        """
        # dp = [[0] * n for _ in range(2)]
        # dp = [[0]*1 for _ in range(n)]
        dp = [0] * n
        dp[0] = low[0]
        if n == 1:
            return low[0]
        
        # 1st day
        # dp[1][0] = max(dp[1-1][0], dp[1-1][1]) + low[1]
        # dp[1][1] = 0 + high[1]
        dp[1] = max(dp[1-1] + low[1], 0 + high[1])
        if n == 2:
            return dp[1]
            # return max(dp[1][0], dp[1][1])
            
        for i in range(2, len(low)):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + low[i]
            # dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + high[i]
            dp[i] = max(dp[i-1] + low[i], dp[i-2] + high[i])
        
        return dp[n-1]
        # return max(dp[n-1][0], dp[n-1][1])    
        
    def O_Nx2(self, low, high):
        n = len(low)
        """
        ith day, dp[i][0] Max Value with low; 
                 dp[i][1] Max Value with high
        """
        # dp = [[0] * n for _ in range(2)]
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = low[0]
        if n == 1:
            return low[0]
        
        # 1st day
        dp[1][0] = max(dp[1-1][0], dp[1-1][1]) + low[1]
        dp[1][1] = 0 + high[1]
        if n == 2:
            return max(dp[1][0], dp[1][1])
            
        for i in range(2, len(low)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + low[i]
            dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + high[i]
        
        return max(dp[n-1][0], dp[n-1][1])