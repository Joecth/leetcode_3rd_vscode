#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (40.04%)
# Likes:    1980
# Dislikes: 353
# Total Accepted:    255.7K
# Total Submissions: 626.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.helper(head, k)
    
    def helper(self, head, k):
        if not head or not head.next or k <= 1: return head
        
        dummy = ListNode(0)
        cur = dummy.next = head # dummy.next is not used 
        cur = head
        
        cur_head = head # the current head we're iterating
        pre_head = dummy # the cur_head's previous node
        i = 0
        while cur:
            i += 1
            if (i == k):
                tmp = cur.next
                cur.next = None
                reversed_head = self.reverse(cur_head)
                pre_head.next = reversed_head
                pre_head = cur_head # tail of reversed linkedlist
                
                cur_head.next = tmp
                cur_head = tmp
                i = 0
                cur = tmp
                continue
            
            cur = cur.next
            
        """ If reversed remaining part
        tail = thie.reverse(cur_head)
        pre_head.next = tail
        """
        return dummy.next
        # https://www.youtube.com/watch?v=QD9xEicaxxI
        
    def helper_failed(self, head):
        def getSize(head):
            counter = 0
            while(head is not None):
                counter +=1
                head = head.next
            return counter
         
    
        def split(head, step):
            i = 1
            while (i < step and head):
                head = head.next
                i += 1
                
            if head is None: return None
            #disconnect
            temp = head.next
            head.next = None
            return temp
        
        
        size = getSize(head)
        prev = dummy = ListNode(0)
        cur = dummy.next = head
        
        while k < size:
            r = split(cur, k)
            tmp = r.next
            reverse_head = reverse(cur)
            
            size -= k
            
        return dummy.next

    def reverse(self, head):
        prev, cur = None, head
        while cur:
            tmp, cur.next, prev = cur.next, prev, cur
            cur = tmp
        return prev
    
        
# @lc code=end

