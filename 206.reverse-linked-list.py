#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (60.23%)
# Likes:    4079
# Dislikes: 84
# Total Accepted:    931.1K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return self.iterative(head)
 
        return self.recursive(head)
        return self.recursive_fr_tail(head)

    def iterative(self, root):
        cur = root
        prev = None
        while cur:
            tmp = cur.next 
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def recursive_fr_tail(self, root):
        def helper(root):
            if not root or not root.next:
                return root
            head = helper(root.next)
            root.next.next = root
            root.next = None

            return head

        return helper(root)

    def recursive(self, root):
        # dummy = ListNode(0)
        # dummy.next = root
        def helper(cur, prev):
            if not cur:
                return prev
            next_ = cur.next
            cur.next = prev
            return helper(next_, cur)

        return helper(root, None)
# @lc code=end

