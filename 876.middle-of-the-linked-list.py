#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (66.49%)
# Likes:    1087
# Dislikes: 54
# Total Accepted:    174.5K
# Total Submissions: 254.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
# = NULL.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given list will be between 1 and 100.
# 
# 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1 2 3 4 5 
    s 
        f
        if not f.next, return s
        
1 2 3 4 5 6
    s
        f 
        if not f.next.next, return s.next
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1 2 3 4 5 
    s 
        f
        if not f.next, return s
        
1 2 3 4 5 6
    s
        f 
        if not f.next.next, return s.next
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1 2 3 4 5 
    s 
        f
        if not f.next, return s
        
1 2 3 4 5 6
    s
        f 
        if not f.next.next, return s.next
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # return self.helper(head)
        return self.helper_cleaner(head)
    
    def helper_cleaner(self, head):
        if not head: return head
        
        dummy = ListNode(0)
        fast = slow = dummy.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # if fast:   # count % 2 == 0
        #     return slow.next
        # else:
        #     return slow    
        return slow
    
    def helper(self, head: ListNode) -> ListNode:
        if not head: return head
        
        cur = dummy = ListNode(0)
        dummy.next = head
        slow = fast = cur
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:   # count % 2 == 0
            return slow.next
        else:
            return slow
        
    def middleNode_old(self, head: ListNode) -> ListNode:
        
        s = f = head
        while f:
            if not f.next:
                return s
            if not f.next.next:
                return s.next
            f = f.next.next
            s = s.next
# @lc code=end

