/*
 * @lc app=leetcode id=82 lang=javascript
 *
 * [82] Remove Duplicates from Sorted List II
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
 *
 * algorithms
 * Medium (35.57%)
 * Likes:    1363
 * Dislikes: 100
 * Total Accepted:    231.2K
 * Total Submissions: 648.3K
 * Testcase Example:  '[1,2,3,3,4,4,5]'
 *
 * Given a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list.
 * 
 * Return the linked list sorted as well.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2->3->3->4->4->5
 * Output: 1->2->5
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 1->1->1->2->3
 * Output: 2->3
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let prev = dummy = new ListNode(0);
    let cur = dummy.next = head;

    while (cur){
        while (cur.next && cur.next.val == cur.val){
            cur = cur.next;
        }
        if (prev.next == cur){
            prev = cur;
        }
        else{
            prev.next = cur.next;
        }
        cur = cur.next;
    }
    return dummy.next;
};
// @lc code=end

