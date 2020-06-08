#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.97%)
# Likes:    7409
# Dislikes: 1916
# Total Accepted:    1.3M
# Total Submissions: 3.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return l1
        if not l1: return l2
        if not l2: return l1
        return self.helper_clean(l1, l2)

    # update again
    def helper_clean(self, l1, l2):
        cur = dummy = ListNode(0)
        carry = 0
        while l1 or l2:
            # # m = l1.val if l1 else 0
            # n = l2.val if l2 else 0
            m = 0
            if l1:
                m = l1.val
                l1 = l1.next
            n = 0
            if l2:
                n = l2.val
                l2 = l2.next
            total = m+n+carry
            carry, digit = total//10, total%10
            cur.next = ListNode(digit)
            cur = cur.next
            # l1, l2 = l1.next, l2.next   # BUGGY!
        
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
        

    def helper(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2: #or carry:
            m, n = 0, 0
            if l1: m = l1.val
            if l2: n = l2.val
            # total = l1.val + l2.val + carry
            total = m + n + carry
            carry, digit = total//10, total%10
            cur.next = ListNode(digit)
            cur = cur.next
            # res = res*10 + digit
            l1, l2 = l1.next, l2.next

        if l2: l1 = l2
        while l1:# or carry:
            total = l1.val + 0 + carry
            carry, digit = total//10, total%10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next

        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next
# @lc code=end

