#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (48.34%)
# Likes:    2418
# Dislikes: 151
# Total Accepted:    240.1K
# Total Submissions: 496.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
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
           1(5)
         /    \
        2(2)    3(2)
       /  \        \
      4(0) 5(0)     6(1)
                    /
                  9(0)
      
Diameter: summation of left height and right height
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # method 1.
        self.g_max = 0
        # self.dfs(root)
        # return self.g_max
        return self.helper9(root)[0]
        
    def helper9(self, root):
        if not root:
            return [0, 0]
        max_dia_left, max_chain_left = self.helper9(root.left)
        max_dia_right, max_chain_right = self.helper9(root.right)
        
        max_dia = max(max_dia_left, max_dia_right, max_chain_left+max_chain_right)
        max_chain = max(max_chain_left, max_chain_right) + 1
        
        return max_dia, max_chain
    
    def dfs(self, root):
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 0

        L_dia = self.dfs(root.left)
        R_dia = self.dfs(root.right)
        self.g_max = max(self.g_max, L_dia+R_dia)
        return max(L_dia, R_dia) + 1    # CAUTIOUS! 這個不是答案，上一行才是
    
    def helper(self, root):
        if not root:
            return
        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            return max(height(root.left), height(root.right)) + 1
        """
        Diameter: summation of left height and right height
        """
        # if not root:
        if not root.left and not root.right:
            return 
        
        L_dia = height(root.left) + int(root.left is not None)
        R_dia = height(root.right) + int(root.right is not None)
        my_dia = L_dia + R_dia
        self.g_max = max(my_dia, self.g_max)
        self.helper(root.left)
        self.helper(root.right)
        
#         self.g_max = 0
#         self.helper(root)
        
#         return self.g_max
        
        
#     def helper(self, root):
#         if not root:
#             return 0
        
        
#         L_height = self.height(root.left)
#         R_height = self.height(root.right)
#         diameter = L_height + R_height
        
#         L_sub_diameter = self.helper(root.left)
#         R_sub_diameter = self.helper(root.right)
        
#         cur_max = max(diameter, L_sub_diameter, R_sub_diameter) # shouldn't be passed to ROOT
#         self.g_max = max(self.g_max, cur_max)
        
#         return max(L_sub_diameter, R_sub_diameter)
        
        
        
        
        
    
#     def diameterOfBinaryTree_old(self, root: TreeNode) -> int:            
#         self.g_max = 0
#         self.helper(root)
#         return self.g_max
#     # return height and calculate dia at root
#     def helper_old(self, root):
#         # if not root:
#         if not root:
#             return 0
        
#         # L_diameter = self.helper(root.left)
#         # R_diameter = self.helper(root.right)
        
#         L_height = self.height(root.left)
#         R_height = self.height(root.right)
#         # diameter = L_height + R_height + 1
#         diameter = L_height + R_height
#         # self.g_max = max(self.g_max, diameter)
        
#         L = self.helper(root.left)
#         R = self.helper(root.right)
#         self.g_max = max(self.g_max, diameter, L, R)
#         # return 1 + max(L_height, R_height)        
#         return diameter
        
#     def height(self, root):
#         if not root:
#             return 0
#         L = self.height(root.left)  
#         R = self.height(root.right)
#         return 1 + max(L, R)
        
    
#     # Wrong !!!
# #     def diameterOfBinaryTree(self, root: TreeNode) -> int:
# #         if not root:
# #             return 0
# #         res = 0
        
# #         if root.left:
# #             self.g_max = 0
# #             self.helper(root.left, 0)
# #             res += 1
# #             res += self.g_max
# #         if root.right:
# #             self.g_max = 0
# #             self.helper(root.right, 0)
# #             res += 1
# #             res += self.g_max
        
# #         return res
        
# #     def helper(self, root, dmtr=0):
# #         # dmtr = 0
# #         if not root.left and not root.right:
# #             if dmtr > self.g_max:
# #                 self.g_max = dmtr
        
        
# #         if root.left:
# #             dmtr += 1
# #             self.helper(root.left, dmtr)    # 2 
# #             dmtr -= 1   # 1
            
# #         if root.right:
# #             dmtr += 1   # 1+1
# #             self.helper(root.right, dmtr)   # 2 
# #             dmtr -= 1
                    
# @lc code=end

