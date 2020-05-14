#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (61.27%)
# Likes:    2772
# Dislikes: 118
# Total Accepted:    686.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        res = []
        S = []
        cur = root
        while True:
            while cur:
                S.append(cur)
                cur = cur.left
            
            if not S:
                return res
            cur = S.pop()
            res.append(cur.val)
            cur = cur.right

        return res
        
    def inorderTraversal_old(self, root):        
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right

        return ans
    
    ''' Recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return 
        self.helper(node.left)
        self.res.append(node.val)
        self.helper(node.right)
    '''                
# @lc code=end

