#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (56.44%)
# Likes:    2065
# Dislikes: 55
# Total Accepted:    333.9K
# Total Submissions: 583.6K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.iterative(root, k)
        
        res = []
        # self.dfs(root, res, k)
        # return res[k-1]
        self.k = k
        self.dfs2(root, res, k)
        return res[0]
    
    def iterative(self, root, k):
        ## TODO:
        res = 0 
        if not root:
            return res
        
        S = []
        cur = root
        while True:
            while cur:
                S.append(cur)
                cur = cur.left
            
            if not S:
                return -1
            
            cur = S.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        
    def dfs2(self, root, res, k):
        if not root:
            return
        self.dfs2(root.left, res, k)
        self.k -= 1
        if self.k == 0:
            res.append(root.val)
            return 
        self.dfs2(root.right, res, k)
    
    def dfs(self, root, res, k):
        if not root:
            return 
        self.dfs(root.left, res, k)
        res.append(root.val)
        if len(res) == k:
            return
        self.dfs(root.right, res, k)
        
# @lc code=end

