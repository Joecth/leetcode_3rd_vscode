/*
 * @lc app=leetcode id=1008 lang=javascript
 *
 * [1008] Construct Binary Search Tree from Preorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
 *
 * algorithms
 * Medium (75.32%)
 * Likes:    745
 * Dislikes: 23
 * Total Accepted:    58.7K
 * Total Submissions: 76.9K
 * Testcase Example:  '[8,5,1,7,10,12]'
 *
 * Return the root node of a binary search tree that matches the given preorder
 * traversal.
 * 
 * (Recall that a binary search tree is a binary tree where for every node, any
 * descendant of node.left has a value < node.val, and any descendant of
 * node.right has a value > node.val.  Also recall that a preorder traversal
 * displays the value of the node first, then traverses node.left, then
 * traverses node.right.)
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [8,5,1,7,10,12]
 * Output: [8,5,10,1,7,null,12]
 * 
 * 
 * 
 * 
 * 
 * Note: 
 * 
 * 
 * 1 <= preorder.length <= 100
 * The values of preorder are distinct.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
/*
 * 跟 java 一樣，需要 new 以返回 pointer
*/

var bstFromPreorder = function(preorder) {
    let root = new TreeNode(preorder[0]);
    for (let i=1; i < preorder.length; i++){
        helper(root, preorder[i]);
    }
    return root;

    function helper(root, val){

        if (val < root.val){
            if (null == root.left)
                root.left = new TreeNode(val);
            else
                helper(root.left, val);
        }
        else{
            if (null == root.right)
                root.right = new TreeNode(val);
            else
                helper(root.right, val);
        }
    }
};

// Time complexity : O(N) since we visit each node exactly once.
// Space complexity : O(N) to keep the entire tree.

// console.log(bstFromPreorder([8,5,1,7,10,12]));
// @lc code=end