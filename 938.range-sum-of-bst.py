#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (81.04%)
# Likes:    1306
# Dislikes: 229
# Total Accepted:    230.7K
# Total Submissions: 283.8K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
# 
# The binary search tree is guaranteed to have unique values.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
            10
        5           (15)
    3     (7)    Null     18


             (10)
        5              15
   3         7      13     18
1    Null (6) 
"""

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: 
            return 0
        res = [0]
        # self.helper(root, L, R, res)
        # return res[0]
        return self.dfs(root, L, R) # Pruning!
    
    def dfs(self, root, L, R):
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.dfs(root.left, L, R)
        if root.val < R:
            res += self.dfs(root.right, L, R)
        return res
        

    def helper(self, root, L, R, res):
        if not root:
            return
        # if root.val < L:    # NO! should still check root.right
        #     return
        # if root.val > R:
        #     return 
        if L <= root.val <= R:
            res[0] += root.val
        self.helper(root.left, L, R, res)
        self.helper(root.right, L, R, res)
            
    def rangeSumBST_old(self, root: TreeNode, L: int, R: int) -> int:
        if not root: 
            return 0
        
        ret = self.rangeSumBST(root.left, L, R)
        if L <= root.val <= R:
            ret += root.val 
        ret += self.rangeSumBST(root.right, L, R)
    
        return ret        
# @lc code=end

