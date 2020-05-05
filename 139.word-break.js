/*
 * @lc app=leetcode id=139 lang=javascript
 *
 * [139] Word Break
 *
 * https://leetcode.com/problems/word-break/description/
 *
 * algorithms
 * Medium (38.56%)
 * Likes:    3735
 * Dislikes: 203
 * Total Accepted:    498.7K
 * Total Submissions: 1.3M
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * Given a non-empty string s and a dictionary wordDict containing a list of
 * non-empty words, determine if s can be segmented into a space-separated
 * sequence of one or more dictionary words.
 * 
 * Note:
 * 
 * 
 * The same word in the dictionary may be reused multiple times in the
 * segmentation.
 * You may assume the dictionary does not contain duplicate words.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "leetcode", wordDict = ["leet", "code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet
 * code".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "applepenapple", wordDict = ["apple", "pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple
 * pen apple".
 * Note that you are allowed to reuse a dictionary word.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output: false
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    /*
    // dp[0] = c in ws? 
               s[0:1]

    // dp[1] = ca in ws? or 
               s[0:2]
    //         a in ws and dp[0]
               s[1:2]

    // dp[2] = cat in ws? or 
               s[0:3]
    //         ac in ws and dp[0] or 
               s[1:3]
    //         a in ws and dp[1]
               s[2:3]

    // return dp[-1]
    */
    let ws = new Set(wordDict);

    let dp = [];

    // const dp = new Array(s.length + 1).fill(false);
    for (let i=0; i < s.length; i++)
        dp.push(false);

    for (let i=0; i < s.length; i++){
        let token = s.slice(0, i+1); // s[0:i+1];
        // if (token in ws){ 
        if (ws.has(token)){
            dp[i] = true;
            continue;
        }

        let start = 1;
        while (start <= i){
            token = s.slice(start, i+1); // s[start:i+1];
            if (ws.has(token) && dp[start-1])
                dp[i] = true;
            start += 1;
        }
    }

    return dp[dp.length-1];
};
// function wordBreak_BFS(s, wordDict) {
//     const dict = new Set(wordDict);
//     const visited = new Set();
//     const q = [0];
  
//     while (q.length) {
//       const start = q.shift();
  
//       if (!visited.has(start)) {
//         for (let end = start + 1; end <= s.length; end++) {
//           if (dict.has(s.slice(start, end))) {
//             if (end === s.length) return true;
//             q.push(end);
//           }
//         }
//         visited.add(start);
//       }
//     }
//     return false;
//   }
// @lc code=end

