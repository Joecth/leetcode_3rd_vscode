#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (39.98%)
# Likes:    2434
# Dislikes: 120
# Total Accepted:    251K
# Total Submissions: 615K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
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

import heapq
from collections import defaultdict
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.hq_O_N(head)
        # return self.hq_O_1(head)  # TODO: add capacity to heap?!

    def hq_O_1(self, head): # TODO: add capacity to heap?!
        l = []  # 
        d = defaultdict(int) # O(k)
        cur = head
        while cur:
            heapq.heappush(l, (cur.val, d[cur.val], cur))
            d[cur.val] += 1
            cur = cur.next
            
            
        cur = dummy = ListNode(0)
        while l:
            val, _, node = heapq.heappop(l)
            # print(val)
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next
    
            
    def hq_O_N(self, head):
        l = []
        d = defaultdict(int)
        cur = head
        while cur:
            heapq.heappush(l, (cur.val, d[cur.val], cur))
            d[cur.val] += 1
            cur = cur.next
            
            
        cur = dummy = ListNode(0)
        while l:
            val, _, node = heapq.heappop(l)
            # print(val)
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next
            
# @lc code=end

