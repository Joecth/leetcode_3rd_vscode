/*
 * @lc app=leetcode id=67 lang=javascript
 *
 * [67] Add Binary
 *
 * https://leetcode.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (42.68%)
 * Likes:    1487
 * Dislikes: 254
 * Total Accepted:    404.3K
 * Total Submissions: 946.7K
 * Testcase Example:  '"11"\n"1"'
 *
 * Given two binary strings, return their sum (also a binary string).
 * 
 * The input strings are both non-empty and contains only characters 1 or 0.
 * 
 * Example 1:
 * 
 * 
 * Input: a = "11", b = "1"
 * Output: "100"
 * 
 * Example 2:
 * 
 * 
 * Input: a = "1010", b = "1011"
 * Output: "10101"
 * 
 * 
 * Constraints:
 * 
 * 
 * Each string consists only of '0' or '1' characters.
 * 1 <= a.length, b.length <= 10^4
 * Each string is either "0" or doesn't contain any leading zero.
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    function reverseString(str){ 
        return str.split("").reverse().join("");
    }
    if (a == 0){return b;}
    if (b == 0){return a;}
    if (a.length < b.length){
        [a, b] = [b, a]
    }
    a = reverseString(a);
    b = reverseString(b);
    let res = '';
    let carry = 0;
    let i = 0;
    while (i < a.length){
        let m = parseInt(a[i]);
        let n = 0;
        if (i < b.length){
            n = parseInt(b[i]);
        }
        let total = m+n+carry;
        
        // carry, digit = Math.floor(total/2), total%2;
        carry = Math.floor(total/2);
        let digit = total%2;
        // console.log(m, n, total, carry, digit);
        res += digit.toString();
        i += 1;
    }
    
    if (carry == 1){
        res += '1';
    }
    return reverseString(res);    
};
// addBinary('1010', '1111');
// @lc code=end

