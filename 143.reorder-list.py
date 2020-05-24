#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (34.87%)
# Likes:    1652
# Dislikes: 108
# Total Accepted:    218.3K
# Total Submissions: 611.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return head
        # return self.O_N(head)
        return self.O_1(head)
    
    def O_1(self, head):
        # pass
        def find_middle(head):    
            dummy = ListNode(0)
            fast = slow = dummy.next = head
            prev = None
            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next
                
            # if fast: # count % 2 == 0
            #     return slow
            return prev, slow # SAME as leetcode.876
        
        def reverse(root):
            prev = None
            cur = root
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
            
        def merge_2_lists(l1, l2):  # similar to leetcode.21
            cur = dummy = ListNode(0)
            
            while l1 and l2:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                
            if l1:
                cur.next = l1
            else:
                cur.next = l2
                    
            return dummy.next
                
        def merge_2_lists_clever(l1, l2):
            dummy = ListNode(0)
            dummy.next = l1
            
            # while l1:     # FAILED when [1,2] vs [5,4,3], 3 will be left
            while l2:
                tmp = l1.next
                l1.next = l2
                l1 = l2
                l2 = tmp
            
            return dummy.next
            
        cur = dummy = ListNode(0)
        dummy.next = head
        # // step 1. cut the list to two halves
        # // prev will be the tail of 1st half
        # // slow will be the head of 2nd half        
        prev, middle = find_middle(head)
        # ref: https://leetcode.com/problems/reorder-list/discuss/45147/Java-solution-with-3-steps
        prev.next = None    # Handle prev==None issue at beginning as "if not head.next: return head"
        
        reverse_head = reverse(middle)    

        # return merge_2_lists(head, reverse_head)
        return merge_2_lists_clever(head, reverse_head)
        
    
    def O_N(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        Q = deque()
        cur = head
        count = 1
        while cur:
            # if count % 2 == 1:
            Q.append(cur)
            cur = cur.next
            count += 1
        
        i = 1
        dummy = ListNode(0)
        cur = dummy
        while Q:
            if i % 2 == 1:
                v = Q.popleft()
            else:
                v = Q.pop()
            print(v.val)
            cur.next = v
            cur = cur.next
            # cur.next = v
            # cur = cur.next
            i += 1
        cur.next = None     # CRUCIAL!!! or Cycle LinkedList
            
        return dummy.next
# @lc code=end

