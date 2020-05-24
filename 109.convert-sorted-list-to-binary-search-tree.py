#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (45.45%)
# Likes:    1798
# Dislikes: 86
# Total Accepted:    233.7K
# Total Submissions: 504.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# LeetCode 109

# 1. Sorted Array + Divide Conquer Time O(N) Space O(N)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        values = self.list_to_array(head)
        return self.list_to_bst(values, 0, len(values) - 1)
    
    def list_to_array(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values
    
    def list_to_bst(self, values, left, right):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        node = TreeNode(values[mid])
        node.left = self.list_to_bst(values, left, mid - 1)
        node.right = self.list_to_bst(values, mid + 1, right)
        return node
      
# 2. Inorder Time O(nlogn) Space O(logn)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        mid = self.find_middle(head)
        
        node = TreeNode(mid.val)
        
        if head == mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
    
    def find_middle(self, head):
        # The pointer used to disconnect the left half from the mid node.
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head
        
        # Iterate until fast_ptr doesn't reach the end of the linked list.
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # Handling the case when slow_ptr was equal to head.
        if prev_ptr:
            prev_ptr.next = None
        
        return slow_ptr




# Time Complexity O(N), Space Complexity O(logN)

# Python Solution 1: Inorder

# Version 1: Without Global Variable
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        length = self.find_length(head)
        return self.convert_to_bst([head], 0, length - 1)
    
    def find_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def convert_to_bst(self, head, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) // 2
        left = self.convert_to_bst(head, start, mid - 1)
        
        node = TreeNode(head[0].val)
        node.left = left
        
        head[0] = head[0].next
        node.right = self.convert_to_bst(head, mid + 1, end)
        return node

# Version 2: With Global Vairable
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        length = self.find_length(head)
        self.node = head
        return self.convert_to_bst(0, length - 1)
    
    def find_length(self, head):
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1
        return length
    
    def convert_to_bst(self, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) // 2
        left = self.convert_to_bst(start, mid - 1)
        
        root = TreeNode(self.node.val)
        root.left = left
        
        self.node = self.node.next
        root.right = self.convert_to_bst(mid + 1, end)
        return root

  # 1 2 3 4
  # node: 1 end = 3, start 0;
  # node:1 end = 1, start 1 left(1,null, null); right(3, null, null); root(2, left,right)
  # start : 0, end: 9
  # root: (idx: 4).  [0,3]. [5,9]
  # ju
 # arr[0, ..., n] mid = 0 + (n - 0) /2;
 # left++ until mid.
 # right++ until n

# Python Solution 2: Imporved Divide Conquer (Reference: https://www.jiuzhang.com/solution/convert-sorted-list-to-binary-search-tree/)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        length = self.find_length(head)
        tree_root, next_list_node = self.convert_to_bst(head, length)
        return tree_root

    def find_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def convert_to_bst(self, head, length):
         # Convert head -> head.next ....       head.next.next... -> next
         #           |_______________________________|
         #                        length
         # to a Balanced-BST and return the root of the BST and the
         # (length + 1)th node from head.

        if length == 0:
            return None, head
# 5: left : 2 mid :1 right:2
# 4/2 =2 left: 2 mid:1 right:1
          
        # convert the first length // 2 nodes to a left child tree node.
        left_tree_root, mid = self.convert_to_bst(head, length // 2)
        # convert linked list from (length // 2 + 2)th node as head to a right child tree node
        right_tree_root, next_list_node = self.convert_to_bst(mid.next, length - length // 2 - 1)

        # so the (length // 2 + 1)th node will be directly converted to the root node.
        #           root
        #     /              \
        # left_tree_root  right_tree_root
        root = TreeNode(mid.val)
        root.left = left_tree_root
        root.right = right_tree_root
				# array:
        # root: arr[mid], left: arr[mid/2], right[mid + mid/2]
        return root, next_list_node        
# @lc code=end

