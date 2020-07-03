#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (52.86%)
# Likes:    1537
# Dislikes: 81
# Total Accepted:    356.8K
# Total Submissions: 666.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return root
        return self.iter_2_stack(root)
        # return self.iterative(root, res)
        # self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)

    def iterative(self, root, res):
        res = []
        S = []
        S.append(root)
        while S:
            v = S.pop()
            # res.append(v.val)
            res.insert(0, v.val)    # X first position, so constant!

            if v.left:
                S.append(v.left)
            if v.right:
                S.append(v.right) 
        
        return res
        # return res[::-1] 
    
    def iter_2_stack(self, root):
        s1 = []
        s2 = []
        s1.append(root)
        while s1:
            cur = s1.pop()
            s2.append(cur)
            
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s1.append(cur.right)
        res = []
        while s2:
            cur = s2.pop()
            res.append(cur.val)
        return res

#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         self.result = []
#         self.helper(root)
#         return self.result
    
#     def helper(self, node):
#         if not node:
#             return 
        
#         self.helper(node.left)
#         self.helper(node.right)
#         self.result.append(node.val)
        
        
        
        
        
        
#         if not root:
#             return []
        
#         l = self.postorderTraversal(root.left)
#         l += self.postorderTraversal(root.right)
#         l += [root.val]
        
#         return l    
    def postorderTraversal_oldold(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return root
        return self.iter_2_stack(root)
        return self.iterative(root, res)
        # self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)

    def iterative(self, root, res):
        # TODO: ... reversed preorder 
        # root => root.right => root.left, 
        # then reverse answer
        res = []
        S = []
        S.append(root)
        while S:
            v = S.pop()
            # res.insert(0, v.val)    # first position, others should be shifted, so O(N)
            res.append(v.val)
            if v.left:
                S.append(v.left)
            if v.right:
                S.append(v.right) 
        
        # return res
        return res[::-1] # 根右左 ==> 左右根


    def iter_2_stack(self, root):
        # also O(N), though 2 stacks, not O(2N) for Space Complexity
        s1 = []
        s2 = []
        s1.append(root)
        while s1:
            cur = s1.pop()
            s2.append(cur)
            
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s1.append(cur.right)
        res = []
        while s2:
            cur = s2.pop()
            res.append(cur.val)
        return res        
# @lc code=end

