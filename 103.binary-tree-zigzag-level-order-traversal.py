#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (45.61%)
# Likes:    1922
# Dislikes: 99
# Total Accepted:    347.8K
# Total Submissions: 745.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Q = collections.deque()
        Q.append(root)
        res = []
        n = 0
        while Q:
            level_res = []
            for _ in range(len(Q)):
                node = Q.popleft()
                level_res.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            if n % 2 == 1:
                level_res = level_res[::-1]
            res.append(level_res)
            n += 1
        return res        
# @lc code=end

