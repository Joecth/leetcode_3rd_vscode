/*
 * @lc app=leetcode id=387 lang=javascript
 *
 * [387] First Unique Character in a String
 *
 * https://leetcode.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (51.66%)
 * Likes:    1686
 * Dislikes: 112
 * Total Accepted:    448.3K
 * Total Submissions: 857.4K
 * Testcase Example:  '"leetcode"'
 *
 * 
 * Given a string, find the first non-repeating character in it and return it's
 * index. If it doesn't exist, return -1.
 * 
 * Examples:
 * 
 * s = "leetcode"
 * return 0.
 * 
 * s = "loveleetcode",
 * return 2.
 * 
 * 
 * 
 * 
 * Note: You may assume the string contain only lowercase letters.
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    d = _.countBy(s);

    for (let i=0; i<s.length; i++){
        if (d[s[i]] == 1)
            return i;
    }
    return -1;
};
// Time complexity : O(N) since we go through the string of length N two times.
// Space complexity : O(N) since we have to keep a hash map with N elements.
// @lc code=end

