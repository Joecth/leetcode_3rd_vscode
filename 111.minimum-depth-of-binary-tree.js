/*
 * @lc app=leetcode id=111 lang=javascript
 *
 * [111] Minimum Depth of Binary Tree
 *
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (36.73%)
 * Likes:    1145
 * Dislikes: 620
 * Total Accepted:    381.6K
 * Total Submissions: 1M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, find its minimum depth.
 * 
 * The minimum depth is the number of nodes along the shortest path from the
 * root node down to the nearest leaf node.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * return its minimum depth = 2.
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
 * @return {number}
 */
/*
    3
   / \
  9  20
    /  \
   15   7
       /
      8
*/
var minDepth = function(root) {
    if (null == root) return 0;
    return helper(root);
    
    function helper(root){
        if (null == root) return 0;
        if ((null == root.left) && (null == root.right)){
            return 1;   // CRUCIAL!!!, different from null == root
        }
        let L_mh = helper(root.left);
        let R_mh = helper(root.right);
        // console.log(L_mh, R_mh);
        if (root.left && root.right){
            return Math.min(L_mh, R_mh)+1;
        }
        return Math.max(L_mh, R_mh)+1;
    };
};
// @lc code=end

