#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (52.58%)
# Likes:    758
# Dislikes: 62
# Total Accepted:    83.3K
# Total Submissions: 157.5K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note:
# 
# 
# There are at least two nodes in this BST.
# This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # return self.dfs_main(root)
        return self.iterative(root)
    
    def iterative(self, root):
        S = []
        prev = float('-inf')
        ans = float('inf')
        cur = root
        while True:
            while cur:
                S.append(cur)
                cur = cur.left
            if not S:
                break
            cur = S.pop()
            ans = min(ans, cur.val - prev)
            prev = cur.val
            cur = cur.right
        return ans
    
    def dfs_main(self, root):
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
                
# @lc code=end

