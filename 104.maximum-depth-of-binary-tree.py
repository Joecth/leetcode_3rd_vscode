#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (64.39%)
# Likes:    2419
# Dislikes: 72
# Total Accepted:    805.6K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
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
# return its depth = 3.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''    
    3
   / \
  9  20
    /  \
   15   7
     \
     40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''    
    3
   / \
  9  20
    /  \
   15   7
     \
     40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # return self.helper(root)
        return self.helper2(root)
    
    def helper2(self, root):
        if not root:
            return 0
        return max(self.helper2(root.left), self.helper2(root.right)) + 1
    
    def helper(self, node):
        if not node:
            return 0
        
        if not node.left and not node.right:    # unnecessary in this case
            return 1
        
        L_depth = self.helper(node.left)
        R_depth = self.helper(node.right)
        
        return 1 + max(L_depth, R_depth)
# @lc code=end

