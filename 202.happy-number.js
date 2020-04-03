/*
 * @lc app=leetcode id=202 lang=javascript
 *
 * [202] Happy Number
 *
 * https://leetcode.com/problems/happy-number/description/
 *
 * algorithms
 * Easy (48.83%)
 * Likes:    1758
 * Dislikes: 378
 * Total Accepted:    418.9K
 * Total Submissions: 836.8K
 * Testcase Example:  '19'
 *
 * Write an algorithm to determine if a number is "happy".
 * 
 * A happy number is a number defined by the following process: Starting with
 * any positive integer, replace the number by the sum of the squares of its
 * digits, and repeat the process until the number equals 1 (where it will
 * stay), or it loops endlessly in a cycle which does not include 1. Those
 * numbers for which this process ends in 1 are happy numbers.
 * 
 * Example: 
 * 
 * 
 * Input: 19
 * Output: true
 * Explanation: 
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let hash = new Map()
    let res = 0;
    while (n > 0){
        let carry = Math.floor(n/10);
        let digit = n%10;
        res += Math.pow(digit, 2);
        n = carry;
        // hash.set(res, '')

        if (carry == 0){
            if (res == 1){
                break;
            }
            if (hash.has(res)){
                return false;
            }
            hash.set(res, '');
            n = res;
            res = 0;
        }
    }
    return true;
};
// isHappy(1);
// @lc code=end

