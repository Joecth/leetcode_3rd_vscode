/*
 * @lc app=leetcode id=14 lang=javascript
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (34.80%)
 * Likes:    2186
 * Dislikes: 1723
 * Total Accepted:    676.8K
 * Total Submissions: 1.9M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0){
        return '';
    }
    
    let res = strs[0];
    for (let i=1; i < strs.length; i++){
        s = strs[i];
        let count = 0;
        for (let j=0; j < Math.min(s.length, res.length); j++){
            if (s[j] != res[j]){
                break;
            }
            count += 1;
        }
        
        // res = res[:count]
        res = res.slice(0, count);
    }
    return res;    
};
// @lc code=end

