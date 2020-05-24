#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (38.61%)
# Likes:    4329
# Dislikes: 272
# Total Accepted:    611.5K
# Total Submissions: 1.6M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        # return self.pq_O_N_O_k(lists)
        # return self.merge_O_kN_O_1_BF(lists)
        # return self.O_MergeSort(lists)
        return self.O_MergeSort_O_1(lists)

    def O_MergeSort_O_1(self, lists):
        if not lists: return lists
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]      
     
    def O_MergeSort(self, lists):
        def helper(lists):
            n = len(lists)
            if n == 0: return []
            elif n == 1: return lists[0] 
            
            mid = n//2
            L = helper(lists[:mid])
            R = helper(lists[mid:])
            res = self.merge_2_lists(L, R)
            return res
        
        # def helper_index(lists, start, end):
        #     # n = len(lists)
        #     if start <= end: return []
        #     mid = start + (end-start)//2
        #     L = helper_index(lists, start, mid)
        #     R = helper_index(lists, mid+1, end)
        return helper(lists)
        # return helper(lists, 0, len(lists)-1)
        
    # recursion version as merge sort: https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-concise-divide-and-conquer-solution.    

    def merge_O_kN_O_1_BF(self, lists):        
        # Time: O(kxN); k:len(lists), N:len(l1)+len(l2)
        # Space: O(1)
        for i in range(1, len(lists)):
            lists[0] = self.merge_2_lists(lists[0], lists[i]) 
        
        return lists[0]

    
    def merge_2_lists(self, l1, l2):
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
    
    
    def pq_O_N_O_k(self, lists):
        m = len(lists)
        l = []
        for i in range(m):
            if lists[i]: # IMPORTANT
                heapq.heappush(l, (lists[i].val, i))
        
        dummy = ListNode(0)
        cur = dummy
        
        # Time: Nlog(k)
        # Space: O(N) for creating N nodes; O(k) for priority queue
        while l:
            val, i = heapq.heappop(l)
            cur.next = ListNode(val)    
            
            cur = cur.next

            lists[i] = lists[i].next
            if lists[i]:    # IMPORTANT
                heapq.heappush(l, (lists[i].val, i))
        # cur.next = None

        return dummy.next
# @lc code=end

