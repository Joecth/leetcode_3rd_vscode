#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (69.51%)
# Likes:    996
# Dislikes: 16
# Total Accepted:    69.9K
# Total Submissions: 99.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
# 
# 
# 
# Example:
# 
# 
# Input: [1,2,3,4,5]
# 
# 1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# Output: [[4,5,3],[2],[1]]
# 
# 
# 
# 
# Explanation:
# 
# 1. Removing the leaves [4,5,3] would result in this tree:
# 
# 
# ⁠         1
# ⁠        / 
# ⁠       2          
# 
# 
# 
# 
# 2. Now removing the leaf [2] would result in this tree:
# 
# 
# ⁠         1          
# 
# 
# 
# 
# 3. Now removing the leaf [1] would result in the empty tree:
# 
# 
# ⁠         []         
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
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """ method 1 """
        # self.d = defaultdict(list)
        # return self.helper_g_variable(root)
        
        """ method 2 """
        # d = defaultdict(list)
        # self.helper_local_variable(root, d)
        # return [d[k] for k in sorted(d)]
    
        """ method 3 """
        return self.helper_closure(root)    
    
    def helper_closure(self, root):
        def dfs(node):
            if not node:
                return -1
            i = 1 + max(dfs(node.left), dfs(node.right))
            if i == len(out):
                out.append([])
            out[i].append(node.val)
            return i
        out = []
        dfs(root)
        return out
    # https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/83778/10-lines-simple-Java-solution-using-recursion-with-explanation
        
    def helper_local_variable(self, root, d):
        if not root:
            return 0
        if not root.left and not root.right:
            d[0] += [root.val]
            return 0
        
        left = self.helper_local_variable(root.left, d)
        right = self.helper_local_variable(root.right, d)
        my_h = max(left, right) + 1
        d[my_h] += [root.val]
        return my_h
        
        
    def helper_g_variable(self, root):
        self.helper(root)
        return [self.d[h] for h in sorted(self.d)]
        
    def helper(self, root):
        if not root:
            return 0
    
        if not root.left and not root.right:
            self.d[0] += [root.val]
            return 0
        
        left_h = self.helper(root.left)
        right_h = self.helper(root.right)
        
        my_h = max(left_h, right_h)+1
        self.d[my_h] += [root.val]
        return my_h        
# @lc code=end

