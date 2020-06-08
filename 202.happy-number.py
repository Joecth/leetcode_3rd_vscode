#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (48.83%)
# Likes:    1758
# Dislikes: 378
# Total Accepted:    418.9K
# Total Submissions: 836.8K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # return self.O_N(n)
        return self.O_1(n)
    
    def O_1(self, n):
        fast = slow = n
        while slow != 1 and fast != 1:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if slow == fast:
                break
        # print(slow, fast)
        if slow == 1 or fast == 1:
            return True
        return False
        
    def get_next(self, n):
        res = 0
        while n > 0:
            digit = n % 10
            res += digit * digit
            n //= 10    
        return res
    
    def O_N(self, n):
        seen = set()
        while n != 1:
            n = self.bf(n)
            if n in seen:
                return False
            seen.add(n)
        return True
    
    def bf(self, n):
        res = 0
        while n > 0:
            digit = n % 10
            res += digit * digit
            n //= 10
        return res
    
    def isHappy_old(self, n: int) -> bool:        
        d = {}
        s = 0
        while n > 0:
            # for i in range(len(str(n))):
            carry, digit = n//10, n%10
            s += digit**2
            n = carry
            if carry == 0:
                if s == 1:
                    return True
                
                if s in d:
                    break
                d[s] = ''
                n, s = s, 0
        return False
            
        
# @lc code=end

