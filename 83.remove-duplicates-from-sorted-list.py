#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.51%)
# Likes:    1248
# Dislikes: 100
# Total Accepted:    426.9K
# Total Submissions: 957.9K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
1 1 2 3 3
j 
  cur
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Same idea as leetcode 26
        if not head:
            return None
        j = cur = head
        while cur:
            if j.val != cur.val:
                j = j.next
            j.val = cur.val
            cur = cur.next
        j.next = None
        return head

# @lc code=end