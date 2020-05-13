#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (43.09%)
# Likes:    3264
# Dislikes: 166
# Total Accepted:    431.1K
# Total Submissions: 981.7K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        return self.helper(root, p.val, q.val)
        
    def helper(self, root, p, q):
        if not root:
            return None    
        if root.val == p or root.val == q:
            return root

        L = self.helper(root.left, p, q)
        R = self.helper(root.right, p, q)

        if L and R: 
            return root
        if L:
            return L
        if R:
            return R
        if not L and not R:
            return None
        # Time: H, with worst N
        # Space: H, with worst N

    # 2). def backtracking and then compare 2 lists

    # 3). def helper_parent_ptr(self, root):
    # ref: https://books.google.com.tw/books?id=eErBDwAAQBAJ&pg=PA123&lpg=PA123&dq=lca+with+parent+pointer+python&source=bl&ots=Fosnvv7wZ1&sig=ACfU3U0sUS-TM7669O6HTYISkm4-WkI2tw&hl=en&sa=X&ved=2ahUKEwjugY720rDpAhW7xIsBHQrFCPUQ6AEwDnoECAkQAQ#v=onepage&q=lca%20with%20parent%20pointer%20python&f=false
    



# @lc code=end

