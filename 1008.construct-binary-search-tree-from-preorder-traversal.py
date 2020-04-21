#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (75.32%)
# Likes:    745
# Dislikes: 23
# Total Accepted:    58.7K
# Total Submissions: 76.9K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for idx in range(1, len(preorder)):
            self.helper(root, preorder[idx])
            
        return root
        
    def helper(self, root, val):
        if not root:
            return
        
        if val < root.val:
            if root.left:
                self.helper(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.helper(root.right, val)
            else:
                root.right = TreeNode(val)        
# @lc code=end

