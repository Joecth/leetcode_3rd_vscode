#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (29.09%)
# Likes:    1023
# Dislikes: 969
# Total Accepted:    254.1K
# Total Submissions: 868.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        dummy = ListNode(0)
        tmp = dummy.next = head
        
        num = 1
        while tmp and tmp.next:
            num += 1
            tmp = tmp.next
            
        TAIL = tmp
        
        shift = num - k % num
        cur = dummy
        while shift > 0:
            cur = cur.next
            shift -= 1
        
        TAIL.next = dummy.next
        dummy.next = cur.next
        cur.next = None
        
        
        return dummy.next
            
# @lc code=end

