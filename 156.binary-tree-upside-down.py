#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#
# https://leetcode.com/problems/binary-tree-upside-down/description/
#
# algorithms
# Medium (54.21%)
# Likes:    278
# Dislikes: 870
# Total Accepted:    60.3K
# Total Submissions: 110.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree where all the right nodes are either leaf nodes with a
# sibling (a left node that shares the same parent node) or empty, flip it
# upside down and turn it into a tree where the original right nodes turned
# into left leaf nodes. Return the new root.
# 
# Example:
# 
# 
# Input: [1,2,3,4,5]
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \
# 4   5
# 
# Output: return the root of the binary tree [4,5,2,#,#,3,1]
# 
# ⁠  4
# ⁠ / \
# ⁠5   2
# ⁠   / \
# ⁠  3   1  
# 
# 
# Clarification:
# 
# Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is
# serialized on OJ.
# 
# The serialization of a binary tree follows a level order traversal, where '#'
# signifies a path terminator where no node exists below.
# 
# Here's an example:
# 
# 
# ⁠  1
# ⁠ / \
# ⁠2   3
# ⁠   /
# ⁠  4
# ⁠   \
# ⁠    5
# 
# 
# The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
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
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        return self.dfs(root)
    
    def dfs(self, root):
        if not root.left:
            return root
        new_root = self.dfs(root.left)
        # self.dfs(root.right)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return new_root
                
# @lc code=end

