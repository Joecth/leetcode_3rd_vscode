#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.73%)
# Likes:    1145
# Dislikes: 620
# Total Accepted:    381.6K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
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
    3
   / \
  9  20
    /  \
   15   7

"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min_h = 0
        if not root:
            return 0
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        L_mh = self.helper(root.left)
        R_mh = self.helper(root.right)
        if root.left and root.right:
            return min(L_mh, R_mh) + 1
        return max(L_mh, R_mh) + 1

# @lc code=end

