#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (32.53%)
# Likes:    3187
# Dislikes: 257
# Total Accepted:    335.8K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
"""
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        # self.max = 0
        self.ans = root.val
        self.dfs(root)
        return self.ans
    
    def maxPathSum_failed(self, root: TreeNode) -> int:
        # self.ans = float("-inf")
        if not root:return 0
        return self.helper(root)
        
    def dfs(self, node):
        if not node:
            return 0
        
        L_sum = max(self.dfs(node.left), 0)   # 要取max, 當下面如果是負數過來時把下面給割了！
        R_sum = max(self.dfs(node.right), 0)  # 42. 
        
        self.ans = max(self.ans, L_sum+R_sum+node.val)
        
        return max(L_sum, R_sum) + node.val
        # ref: https://www.bilibili.com/video/av92694072/

    def helper(self, root):
        if not root:
            return float('-inf')

        if not root.left and not root.right:
            return root.val
            
        L = self.helper(root.left)
        R = self.helper(root.right)
        cur_max = max(root.val, root.val+L, root.val+R, root.val+L+R, L, R)
        # if root.left and root.right:
        #     cur_max = max(root.val, root.val+L, root.val+R, root.val+L+R, L, R)
        # elif root.left:
        #     cur_max = max(root.val, root.val+L, L)
        # else:
        #     cur_max = max(root.val, root.val+R, R)

        return cur_max

# @lc code=end

