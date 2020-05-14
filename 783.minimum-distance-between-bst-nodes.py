#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (51.70%)
# Likes:    593
# Dislikes: 176
# Total Accepted:    56.4K
# Total Submissions: 108.5K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
# This question is the same as 530:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def minDiffInBST(self, root: TreeNode) -> int:
        # return self.minDiffInBST_dfs(root)
        return self.iterative(root)
    
    def iterative(self, root):
        S = []
        cur = root
        prev = float('-inf')
        ans = float('inf')
        while True:
            while cur:
                S.append(cur)
                cur = cur.left
                
            if not S:
                break
                
            cur = S.pop()
            ans = min(cur.val-prev, ans)
            prev = cur.val
            cur = cur.right
        return ans
        
    def minDiffInBST_dfs(self, root: TreeNode) -> int:
        self.prev = float("-inf")
        self.ans = float("inf")
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 
        
        self.dfs(root.left)
        self.ans = min(root.val-self.prev, self.ans)
        self.prev = root.val
        self.dfs(root.right)
        
# Time Complexity: O(N), where NN is the number of nodes in the tree. We iterate over every node once.
# Space Complexity: O(H), where HH is the height of the tree. This is the space used by the implicit call stack when calling dfs.                
# @lc code=end

