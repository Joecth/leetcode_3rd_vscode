/*
 * @lc app=leetcode id=387 lang=cpp
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
#include <unordered_map>
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> d;

        for (auto ch: s){
            if (d.find(ch) == d.end())
                d[ch] = 1;
            else
                d[ch] += 1;
        }

        for (int i=0; i<s.length(); i++){
            if (d[s[i]] == 1)
                return i;
        }
        return -1;
    }
    
    // OR int firstUniqChar(string s) {
    //     vector<int> v(26,0);
	// 	for(char c : s) v[c - 'a']++;
	// 	for(int i = 0; i < s.length(); i++){
	// 		if(v[s[i] - 'a'] == 1) return i;
	// 	}
	// 	return -1;
    // }    
};
// @lc code=end

