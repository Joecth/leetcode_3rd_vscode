#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (53.89%)
# Likes:    1849
# Dislikes: 115
# Total Accepted:    117.2K
# Total Submissions: 213.7K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# Example:
# 
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:        
        # self.helper_local_var(root, 0)
        self.helper_BETTER(root, [0])
        return root

    def helper_local_var(self, root, val=0):
        """
                2
            0       3
        -4      1    
        """
        # if not root:
        if root == None:
            return val
        
        r_sum = self.helper_local_var(root.right, val)
        root.val += r_sum
        left = self.helper_local_var(root.left, root.val)
        return left
        
    def helper_BETTER(self, root, sum_=[]):
        """
                2
            0       3
        -4      1
        """
        if not root:
            return None
        
        self.helper_BETTER(root.right, sum_) 
        root.val += sum_[0]
        sum_[0] = root.val
        self.helper_BETTER(root.left, sum_)
        # return root        
# @lc code=end

