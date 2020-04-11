#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (48.34%)
# Likes:    2418
# Dislikes: 151
# Total Accepted:    240.1K
# Total Submissions: 496.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
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
           1(5)
         /    \
        2(2)    3(2)
       /  \        \
      4(0) 5(0)     6(1)
                    /
                  9(0)
      
Diameter: summation of left height and right height
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # self.ans = 0
        self.g_max = 0
        self.helper(root)
        return self.g_max
    
    def helper(self, root):
        if not root:
            return
        
        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            return max(height(root.left), height(root.right)) + 1
        """
        Diameter: summation of left height and right height
        """
        # if not root:
        if not root.left and not root.right:
            return 
        
        L_dia = height(root.left) + int(root.left is not None)
        R_dia = height(root.right) + int(root.right is not None)
        my_dia = L_dia + R_dia
        self.g_max = max(my_dia, self.g_max)
        self.helper(root.left)
        self.helper(root.right)
        
# @lc code=end

