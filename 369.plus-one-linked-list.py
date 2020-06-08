#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (57.80%)
# Likes:    440
# Dislikes: 24
# Total Accepted:    45.3K
# Total Submissions: 78.1K
# Testcase Example:  '[1,2,3]'
#
# Given a non-negative integer represented as non-empty a singly linked list of
# digits, plus one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
# 
# 
# Example :
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        last_nine = None
        not_nine = cur = dummy = ListNode(0)
        dummy.next = head
        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next
        
        not_nine.val += 1
        cur = not_nine.next
        while cur:
            # not_nine = not_nine.next
            cur.val = 0
            cur = cur.next
        
        return dummy.next if not_nine != dummy else dummy
        
        
# @lc code=end

