#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (43.52%)
# Likes:    978
# Dislikes: 168
# Total Accepted:    114.4K
# Total Submissions: 256.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the vertical order traversal of its nodes'
# values. (ie, from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to
# right.
# 
# Examples 1:
# 
# 
# Input: [3,9,20,null,null,15,7]
# 
# ⁠  3
# ⁠ /\
# ⁠/  \
# ⁠9  20
# ⁠   /\
# ⁠  /  \
# ⁠ 15   7 
# 
# Output:
# 
# [
# ⁠ [9],
# ⁠ [3,15],
# ⁠ [20],
# ⁠ [7]
# ]
# 
# 
# Examples 2:
# 
# 
# Input: [3,9,8,4,0,1,7]
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7 
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9],
# ⁠ [3,0,1],
# ⁠ [8],
# ⁠ [7]
# ]
# 
# 
# Examples 3:
# 
# 
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
# child is 5)
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
# ⁠   /\
# ⁠  /  \
# ⁠  5   2
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9,5],
# ⁠ [3,0,1],
# ⁠ [8,2],
# ⁠ [7]
# ]
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Q = collections.deque()
        Q.append((root, 0))
        idx2nodes = {}
        while Q:
            node, idx = Q.popleft()
            if idx not in idx2nodes:
                idx2nodes[idx] = []
            idx2nodes[idx].append(node.val)
            
            if node.left:
                Q.append((node.left, idx-1))
            if node.right:
                Q.append((node.right, idx+1))
        res = []
        for key in sorted(idx2nodes.keys()):
            res.append(idx2nodes[key])
        return res
        
# @lc code=end

