/*
 * @lc app=leetcode id=139 lang=cpp
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
#include <unordered_set>
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> ws;
        
        for (auto s: wordDict){
            ws.insert(s);
        }
        
        vector<bool> dp(s.length(), false); 
        
        for (int i=0; i < s.length(); i++){
            string token = s.substr(0, i+1);
            if (ws.find(token) != ws.end()){
                dp[i] = true;
                continue;
            }
            
            int start = 1;
            while (start <= i){
                // token = s.substr(start, i+1);
                token = s.substr(start, i-start+1);
                if (ws.find(token) != ws.end() && dp[start-1]){
                    dp[i] = true;
                    break;
                }
                start += 1;
            }
        }
        return dp[s.length()-1];
    }
};
// @lc code=end

