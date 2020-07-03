#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (54.26%)
# Likes:    1322
# Dislikes: 54
# Total Accepted:    467.7K
# Total Submissions: 855K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        S = []
        S.append(root)
        while S:
            cur = S.pop()
            print(cur.val)
            res.append(cur.val)
            if cur.right:
                S.append(cur.right)
            if cur.left:
                S.append(cur.left)
        return res
        
    def preorderTraversal_old(self, root: TreeNode) -> List[int]:       
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            v = stack.pop()
            res.append(v.val)
            # if v.left:
            #     stack.append(v.left)
            # if v.right:
            #     stack.append(v.right)
            if v.right:
                stack.append(v.right)    
            if v.left:
                stack.append(v.left)
        return res
    
        # WRONG ! Following is BFS...
        # res = []
        # Q = deque()
        # Q.append(root)
        # while Q:
        #     v = Q.popleft()
        #     res.append(v.val)
        #     if v.left:
        #         Q.append(v.left)
        #     if v.right:
        #         Q.append(v.right)
        # return res
            
            
        ''' recursive solution
        self.res = []
        self.helper(root)
        return self.res
        
    def helper(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.helper(node.left)
        self.helper(node.right)
        '''
        # l = []
        # l.append(root.val)
        # l += self.preorderTraversal(root.left)
        # l += self.preorderTraversal(root.right) 
        # return l

    def preorderTraversal_oldold(self, root: TreeNode) -> List[int]:
        if not root: return root
        res = []
        # self.dfs(root, res)
        self.iterative(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return 
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

    def iterative(self, root, res):
        # Try to explain "WHY"?
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res # 根左右

        


# @lc code=end

