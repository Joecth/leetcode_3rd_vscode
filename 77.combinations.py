#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (52.54%)
# Likes:    1336
# Dislikes: 66
# Total Accepted:    278.5K
# Total Submissions: 520.5K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        
        # self.helper_old(n, k, 0, [], 0) 
        res = []
        self.helper(n, k, [], 0, res)
        return res          # EITHER
        return self.result  # EITHER
         
    
    def helper(self, n, k, item, idx, res):
        # if idx == k:
        if len(item) == k:
            res.append(item.copy())
            self.result.append(item.copy())
            return
        
        for i in range(idx, n):
            item.append(i+1)
            # self.helper(n, k, item, idx+1)
            self.helper(n, k, item, i+1, res)
            item.pop()
    
    def helper_old(self, n, k, i, item, level):
        if len(item) == k:
            self.result.append(item.copy())
            return 
        if i > n:
            return  
        
        item.append(i)  # 1
        self.helper_old(n, k, i+1, item, level+1)
        item.pop()
        self.helper_old(n, k, i+2, item, level+1)
        ""        
# @lc code=end

