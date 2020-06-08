#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (55.77%)
# Likes:    677
# Dislikes: 1030
# Total Accepted:    283.4K
# Total Submissions: 504.6K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # return self.bf_main(num)
        return self.O_1(num)

    def O_1(self, num):
        if num <= 0: 
            return 0
        return (num-1) % 9 +1

    
    def bf_main(self, num):
        if num <= 9:
            return num
        while num > 9:
            # print(num)
            num = self.bf(num)
        return num
    
    def bf(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res
    # def helper(self, num)        
# @lc code=end

