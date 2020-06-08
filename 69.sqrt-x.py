#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.07%)
# Likes:    1255
# Dislikes: 1845
# Total Accepted:    536.4K
# Total Submissions: 1.6M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1 :
            return 0
        if x == 1 :
            return 1
        # return self.b_search(x)
        return self.newton(x)
    
    def b_search(self, x):
        # if x <= 1: 
        #     return x
        
        root = x
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            if mid * mid > x:
                end = mid
            else:
                start = mid
        
    def newton(self, x):
        
        C = x0 = x
        while True:
            xi = 0.5 * (x0 + C/x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)
        # https://www.bilibili.com/video/BV1PK411s72g?from=search&seid=16501413507066443085
        
        
    def old(self, x):
        l, r = 0, x
        
        while l <= r:
            mid = l + (r-l)//2
            # print(l, r, mid)
            if  mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r = mid
            else:
                l = mid + 1
                
# @lc code=end

