#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (60.35%)
# Likes:    4396
# Dislikes: 239
# Total Accepted:    493.8K
# Total Submissions: 816.4K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
from typing import List
"""
                                                            3,3
                                            2,3
                         1,3 ((
    0,3 (((                   1,2 (()   
        0,2 ((()            0,2   1,1
            0,1 ((())
                0,0 ((()))

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.helper(n, n, n, "")
        return self.res
        
    def helper(self, n, l, r, item=""): # l, r mean "how many I can use"
                                        # TODO: optimize with shallower call stack
        # if len(item) == 2*n:
        if len(item) == n*2:
            self.res.append(item)
            return 

        # if l > 0:
        # for i in range(2):  # 2 means two choices at each state, but ) should be after (, so only 1: (
        if l > 0:
            item = item + '('                   # TODO: better to make this into one-line
            self.helper(n, l-1, r, item)        # self.helper(n, l-1, r, item+'(')
            item = item[:-1]
        if l < r:
            item = item + ')'
            self.helper(n, l, r-1, item)

print(Solution().generateParenthesis(3))  
# Time: Catalan Number: https://johnmayhk.wordpress.com/2014/02/03/cn/
# @lc code=end

