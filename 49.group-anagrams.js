/*
 * @lc app=leetcode id=49 lang=javascript
 *
 * [49] Group Anagrams
 *
 * https://leetcode.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (53.31%)
 * Likes:    2809
 * Dislikes: 157
 * Total Accepted:    537.4K
 * Total Submissions: 997.8K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * Given an array of strings, group anagrams together.
 * 
 * Example:
 * 
 * 
 * Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
 * Output:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 * 
 * Note:
 * 
 * 
 * All inputs will be in lowercase.
 * The order of your output does not matter.
 * 
 * 
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let d = {};
    for (let i=0; i < strs.length; i++){
        let item = [...strs[i]].sort().join('');
        // d[item] = 'undefined' ? strs[i]:[...d[item], s[i]];
        if (d[item]){
            d[item].push(strs[i]);
        }else{
            d[item] = [strs[i]]
        }
    }
    // console.log(d);
    return Object.values(d);
};
groupAnagrams(["eat","tea","tan","ate","nat","bat"])
// @lc code=end

