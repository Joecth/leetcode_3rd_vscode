/*
 * @lc app=leetcode id=543 lang=javascript
 *
 * [543] Diameter of Binary Tree
 *
 * https://leetcode.com/problems/diameter-of-binary-tree/description/
 *
 * algorithms
 * Easy (48.34%)
 * Likes:    2418
 * Dislikes: 151
 * Total Accepted:    240.1K
 * Total Submissions: 496.5K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 
 * Given a binary tree, you need to compute the length of the diameter of the
 * tree. The diameter of a binary tree is the length of the longest path
 * between any two nodes in a tree. This path may or may not pass through the
 * root.
 * 
 * 
 * 
 * Example:
 * Given a binary tree 
 * 
 * ⁠         1
 * ⁠        / \
 * ⁠       2   3
 * ⁠      / \     
 * ⁠     4   5    
 * 
 * 
 * 
 * Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
 * 
 * 
 * Note:
 * The length of path between two nodes is represented by the number of edges
 * between them.
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

// * ⁠         1
// * ⁠        / \
// * ⁠       2   3
// * ⁠      / \     
// * ⁠     4   5    
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    
    function height(root){
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 0;
        return Math.max(height(root.left), height(root.right)) + 1;
    };

    function helper(root){
        if (null==root) return 0;
        let L_height = height(root.left);
        let R_height = height(root.right);
        let L_dia = 0;
        if (root.left != null){
            L_dia = L_height + 1;
        }
        let R_dia = 0;
        if (root.right != null){
            R_dia = R_height + 1;
        }
        let my_dia = L_dia + R_dia;
        g_dia = Math.max(g_dia, my_dia);
        helper(root.left);
        helper(root.right);
    };
    let g_dia = 0;
    helper(root);
    return g_dia
};
// @lc code=end

