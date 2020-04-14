#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (44.73%)
# Likes:    1456
# Dislikes: 51
# Total Accepted:    304.7K
# Total Submissions: 678.3K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
"""
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return root
        self.res = []
        self.helper(root, sum, [])
        return self.res

    def helper(self, root, val, item):
        if not root:
            return None
        if not root.left and not root.right:
            if val - root.val == 0:
                self.res.append(item + [root.val])
            return None     # CRUCIAL or Memory Limit Exceeded
                
        L = self.helper(root.left, val-root.val, item + [root.val])
        R = self.helper(root.right, val-root.val, item + [root.val])

# @lc code=end

