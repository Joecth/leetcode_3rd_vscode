# import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return self.O_N(x, n)
        return self.O_1(x, n)
        # if n == 0: return 1
        # return self.dfs(x, n)
    # def O_1(self, x, n):
    #     flag = 1
    #     if n < 0:
    # def dfs(self, x, n):  ＃ 負的無法
    #     if n == 0: 
    #         return 1
    #     if n%2 == 1:
    #         return self.dfs(x, n//2) ** 2 * x
    #     return self.dfs(x, n//2) ** 2
    
    def O_1(self, x, n):
        flag = 1
        if n < 0:
            flag = -1
        n = abs(n)
        
        base = x
        mask = 1
        ret = 1
        # for i in range(1, 32):
        for i in range(32):
            if mask << i & n > 0:
                ret *= base 
            base *= base
        return 1/ret if flag == -1 else ret
        
    def O_N(self, x, n):
        flag = 1
        # if x < 0:  # WRONG! should be n
        if n < 0:        
            flag = -1
        n = abs(n)
        base = [0 for _ in range(32)]
        base[0] = x
        # base[1] = base[0] * base[0]
        # base[2] = base[1] * base[1]
        for i in range(1, 32):
            base[i] = base[i-1] * base[i-1]
        
        ret = 1
        mask = 1
        for i in range(32):
            if mask << i & n > 0:
                ret *= base[i]
        return 1/ret if flag == -1 else ret
        # ref: https://kknews.cc/code/v5mp5pl.html        
        
    def myPow_old(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n < 0:
            # return XXXX # TODO
            n1 = abs(n) - 1                         # n == -2**31
            return (1/x) * (1/self.pos_pow(x, n1))  # 2^(-4) == 1/2^4 ==  1/2 * 1/2^3
        return self.pos_pow(x, n)
    
    def pos_pow(self, base, idx):
        res = 1
        while idx > 0:
            # print(base, idx)
            if idx % 2 == 1:
                res *= base
            base *= base
            idx //= 2
        return res
        
    '''
    res base    idx
    1   2       10
    1   4       5
    4   16      2    
    4   256     1
    ans 
    '''    
        
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0 or x  == 1: 
#             return 1
#         if n == 1:
#             return x
#         if n < 0:       #2**(-3) ==  1/2**3 == 2* 2**(-4)
#             # n = -(n+1)
#             n = abs(n) + 1
#             return x * (1/self.pos_pow(x, n))
#         return self.pos_pow(x, n)
            
#     def pos_pow(self, x, n):
#         # print(x, n)
#         res = 1    
#         while n > 0:
#             if n % 2 != 0:
#                 res *= x
#             # x = x ** 2      # TODO: CAUTIOUS, Numerical result out of range for (2, -2**31)
#             x = x * x         # SHOULD USE THIS!
#             n = n//2
            
#         return res
#     '''
#     for neg number: 
#     [-2**31, 2**31 -1]
    
# res   base index
# 1     2    9      ** --> ans!
# 2     4    4
# 2     16   2
# 2     256  1


# 1     2    10
# 1     4    5
# 4     16   2
# 4     256  1
#     '''        
        # if not n:
        #     return 1
        # if not x:
        #     return 0
        # ans = self.helper(x, n)
        # if n < 0:
        #     ans = 1/ans
        # return ans
        
#         return self.iterative(x, n)
#         # ans = self.helper(x, n) 
#         # if n < 0:
#         #     ans = 1/ans
#         # return ans
        
#         return self.dp_sol(x, n)
#     x means base; n means index
#     x^n
    
#     3^10
#     (3^2)^5
#     (3^2^2)^2 * 3^2
#     def pow(self, x, n):
#         while n>0 :
#             # n /= 2
#             q, r = divmod(n, 2)
#             n = q
#             x = x**2
    
    '''
    1024 
    p       1     1    2*2    2*2 * 2*2*2    
    q       2     2*2  2*2*2     
    abs(n)  10    5    2      1
    '''
    def iterative(self, x, n):
        m = abs(n)
        p, q = 1, x     # p q 是底數，
        while m > 0:
            if (m & 1) == 1:
                p *= q      #(2**2) * 2**(2**(2**(2)))
            m //= 2
            q *= q
        return 1/p if n < 0 else p

    def helper(self, x, n):
        n = abs(n)  # CRUCIAL
        if n <= 1:
            return x**n
        
        ans = self.helper(x, n-1) * x
        
        return ans
        '''
        n   3       2    1   0  
        ret 3*3*3   3*3  3*1 1
        '''       
        
    ''' TLE for 0.00001, 2**31 -1 '''
    def dp_sol(self, x, n):
        if x > 0 or not n%2:
            sign = 1
        else:
            sign = -1
        
        flag = True if n > 0 else False
        abs_flr = math.floor(abs(n))     # -3.45 => 3, 3.45 => 3
    
        tail = abs(abs(n) - abs_flr)     #  0.45
        
        n = abs(n)
        # dp = [0] * (n+1)   # Memory Error when n is 2**31-1
        # dp[0] = 1
        dp0 = 1
        dp1 = abs(x) #abs_flr
        # for i in range(1, n+1):
        #     dp[i] = dp[i-1] * x
        for tmp in range(2, n+1):
            # dp0, dp1 = dp0*dp1, dp0
            dp0, dp1 = dp1*abs(x), dp0
            
        # ans = dp[-1] * x**tail
        ans = dp0*dp1 * x**tail
        
        return sign * (ans if flag else 1/ans)
        
        
    ''' Memory Error when n is 2**31 -1'''
    def dp_sol_memory_error(self, x, n):
        flag = 1 if n < 0 else 0
        abs_flr = math.floor(abs(n))     # -3.45 => 3, 3.45 => 3
    
        tail = abs(abs(n) - abs_flr)     #  0.45
        
        n = abs(n)
        dp = [0] * (n+1)   # Memory Error when n is 2**31-1
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = dp[i-1] * x
        
        ans = dp[-1] * x**tail
        return ans if not flag else 1/ans
        
        ''' TLE
        res = 1.0
        for _ in range(abs(n)):
            if n > 0:
                res *= x
            else:
                res /= x
        return res
        '''

        