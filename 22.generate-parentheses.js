/*
 * @lc app=leetcode id=22 lang=javascript
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (60.35%)
 * Likes:    4396
 * Dislikes: 239
 * Total Accepted:    493.8K
 * Total Submissions: 816.4K
 * Testcase Example:  '3'
 *
 * 
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * 
 * For example, given n = 3, a solution set is:
 * 
 * 
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    
    var helper = function(n, l, r, item){
        if (item.length == n*2){
            res.push(item);
            return;
        }

        if (l > 0){
            helper(n, l-1, r, item+'(');
        }
        if (r > l){
            helper(n, l, r-1, item+')');
        }
    }
    // function helper(n){
    //     return n;
    // }

    res = [];
    helper(n, n, n, '');
    return res
};
console.log(generateParenthesis(3));
// TODO: Time - Catalan
// @lc code=end

