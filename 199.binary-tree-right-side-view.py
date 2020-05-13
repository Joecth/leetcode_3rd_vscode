#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (52.05%)
# Likes:    1933
# Dislikes: 116
# Total Accepted:    262.4K
# Total Submissions: 497.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        
        Q = deque()
        Q.append(root)
        ans = []

        while Q:    
            # level_Q = d
            level_len = len(Q)
            for i in range(level_len):
                node = Q.popleft()
                if node.left:
                    # level_Q.append(node.left)
                    Q.append(node.left)
                if node.right:
                    # level_Q.append(node.right)
                    Q.append(node.right)
                
                if i == level_len-1:
                    ans.append(node.val)
            # Q = level_Q
        return ans      
# @lc code=end

