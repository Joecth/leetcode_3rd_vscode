/*
 * @lc app=leetcode id=61 lang=java
 *
 * [61] Rotate List
 *
 * https://leetcode.com/problems/rotate-list/description/
 *
 * algorithms
 * Medium (29.09%)
 * Likes:    1023
 * Dislikes: 969
 * Total Accepted:    254.1K
 * Total Submissions: 868.2K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, rotate the list to the right by k places, where k is
 * non-negative.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2->3->4->5->NULL, k = 2
 * Output: 4->5->1->2->3->NULL
 * Explanation:
 * rotate 1 steps to the right: 5->1->2->3->4->NULL
 * rotate 2 steps to the right: 4->5->1->2->3->NULL
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 0->1->2->NULL, k = 4
 * Output: 2->0->1->NULL
 * Explanation:
 * rotate 1 steps to the right: 2->0->1->NULL
 * rotate 2 steps to the right: 1->2->0->NULL
 * rotate 3 steps to the right: 0->1->2->NULL
 * rotate 4 steps to the right: 2->0->1->NULL
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // if (!head) return head;
        if (head == null) return head;

        ListNode dummy = new ListNode(0);
        ListNode tmp = dummy.next = head;
        int count = 1;
        while ((tmp != null) && (tmp.next != null)){
            count += 1;
            tmp = tmp.next;
        }
        ListNode TAIL = tmp;

        int steps = count - k%count;
        ListNode cur = dummy;
        while (steps > 0){
            steps -= 1;
            cur = cur.next;
        }

        TAIL.next = dummy.next;
        dummy.next = cur.next;
        cur.next = null;

        return dummy.next;
    }
}
// @lc code=end

