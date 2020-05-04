# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
# Problem from: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root and not arr:
            return True
        if not root:
            return False
        if not arr:
            return True
        return self.helper(root, arr, 0)
        
        
    def helper(self, root, arr, idx):
        if not root:
            return False
        if idx >= len(arr):
            return False
        if arr[idx] != root.val:
            return False
        else:
            if idx == len(arr)-1:
                if not root.left and not root.right:
                    return True
            
        L = self.helper(root.left, arr, idx+1)
        R = self.helper(root.right, arr, idx+1)
        return L or R