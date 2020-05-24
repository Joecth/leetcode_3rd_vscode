#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.74%)
# Likes:    3882
# Dislikes: 567
# Total Accepted:    953.5K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
'''
    1 2 4 
    i
    1 3 4 
cur -> smaller one
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # return l2 if not l1
        # return l1 if not l2
        return self.helper3(l1, l2)
    
        # if not l1: return l2
        # if not l2: return l1
        # dummy = cur = ListNode(0)
        # # dummy.next = 
        # self.helper2(cur, l1, l2)
        # return dummy.next
    
    def helper3(self, l1, l2):
        cur = dummy = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
                
            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next
        
# @lc code=end

