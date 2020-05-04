/*
 * @lc app=leetcode id=61 lang=cpp
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
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (nullptr == head) return head;

        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* tmp = head;
        int num = 1;
        while (tmp!=nullptr && tmp->next!=nullptr){
            num += 1;
            tmp = tmp->next;
        }
        ListNode* TAIL = tmp;
        int steps = num - k%num;
        ListNode* cur = dummy;
        while (steps > 0){
            cur = cur->next;
            steps -= 1;
        }

        TAIL->next = dummy->next;
        dummy->next = cur->next;
        cur->next = nullptr;

        return dummy->next;
    }
};
// @lc code=end

