#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (46.92%)
# Likes:    2343
# Dislikes: 284
# Total Accepted:    316K
# Total Submissions: 669.2K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.helper(root)

    def helper(self, root):
        if not root:
            return None

        self.helper(root.right)
        self.helper(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        # return prev

# Time Complexity: O(n) since we must visit all nodes.
# Space Complexity: O(log n) on balanced tree. O(n) otherwise.
# @lc code=end

