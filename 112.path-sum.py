#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (40.09%)
# Likes:    1554
# Dislikes: 447
# Total Accepted:    429.6K
# Total Submissions: 1.1M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
# ⁠         5
# ⁠    /        \
# ⁠   4         8
# ⁠  /          / \
# ⁠ 11          13  4
# ⁠/    \             \
# 7(F)   2(T)          1
5 4 11 2

"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return  False # problem requires; NOT sum == 0

        return self.helper(root, sum)

    def helper(self, root, val):
        if not root: return False   # since this is not a leaf
        if not root.left and not root.right:
            return val-root.val == 0
        
        L = self.helper(root.left, val-root.val)
        R = self.helper(root.right, val-root.val)
        return L or R
# @lc code=end

