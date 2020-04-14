/*
 * @lc app=leetcode id=113 lang=cpp
 *
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (44.73%)
 * Likes:    1456
 * Dislikes: 51
 * Total Accepted:    304.7K
 * Total Submissions: 678.3K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given a binary tree and a sum, find all root-to-leaf paths where each path's
 * sum equals the given sum.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given the below binary tree and sum = 22,
 * 
 * 
 * ⁠     5
 * ⁠    / \
 * ⁠   4   8
 * ⁠  /   / \
 * ⁠ 11  13  4
 * ⁠/  \    / \
 * 7    2  5   1
 * 
 * 
 * Return:
 * 
 * 
 * [
 * ⁠  [5,4,11,2],
 * ⁠  [5,8,4,5]
 * ]
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    vector<vector<int>> result;

public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> item;
        helper(root, sum, item);
        return result;
    }

    // vector<vector<int>>
    void helper(TreeNode* root, int sum, vector<int> item) {
        if (!root){
            return ;
        }

        item.push_back(root->val);
        if (!root->left && !root->right){
            if (sum - root->val == 0){
                result.push_back(item);
            }
            item.pop_back();
            return;
        }
        
        helper(root->left, sum - root->val, item);
        helper(root->right, sum - root->val, item);
        item.pop_back();
    }

};
// @lc code=end

