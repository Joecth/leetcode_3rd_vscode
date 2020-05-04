// # Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 
// # We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
// # Problem from: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} arr
 * @return {boolean}
 */
var isValidSequence = function(root, arr) {
    // console.log('aaaaa ', arr.length);
    if (!root) 
        return arr.size == 0;
    if (!arr)
        return true;
    
    return helper(root, arr, 0);
    
    function helper(root, arr, idx){
        if (root == null || idx >= arr.length)
            return false;
        if (arr[idx] != root.val)
            return false;
        else{
            // console.log(arr.size)
            if (idx == arr.length-1){
                // console.log(idx);
                if (!root.left && !root.right)
                    return true;
            }
        }
        let L = helper(root.left, arr, idx+1);
        let R = helper(root.right, arr, idx+1);
        return L || R;
    }
};