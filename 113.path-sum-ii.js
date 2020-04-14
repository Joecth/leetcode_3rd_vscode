/*
 * @lc app=leetcode id=113 lang=javascript
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
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    if (null == root) return [];
    let res = [];
    helper(root, sum, []);
    return res;

    function helper(root, val, item){
        if (null == root) return null;
        item.push(root.val);
        // console.log(item, root.val);

        if (null == root.left && null == root.right){
            if (val-root.val == 0){
                res.push([...item]); // TODO:! copy!!!
            }
            item.pop();     // CRUCIAL!!!
            return null;
        }
        
        L = helper(root.left, val-root.val, item);
        R = helper(root.right, val-root.val, item);
        item.pop()
    }    
};
console.log(pathSum([5,4,8,11,null]), 22)
// @lc code=end

