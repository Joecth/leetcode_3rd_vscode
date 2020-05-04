/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
 *
 * https://leetcode.com/problems/ransom-note/description/
 *
 * algorithms
 * Easy (51.65%)
 * Likes:    547
 * Dislikes: 187
 * Total Accepted:    193.6K
 * Total Submissions: 362.8K
 * Testcase Example:  '"a"\n"b"'
 *
 * 
 * Given an arbitrary ransom note string and another string containing letters
 * from all the magazines, write a function that will return true if the
 * ransom 
 * note can be constructed from the magazines ; otherwise, it will return
 * false. 
 * 
 * 
 * Each letter in the magazine string can only be used once in your ransom
 * note.
 * 
 * 
 * Note:
 * You may assume that both strings contain only lowercase letters.
 * 
 * 
 * 
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 * 
 * 
 */

// @lc code=start
#include<unordered_map>
using namespace std;
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> r_map;
        for (auto ch: ransomNote){
            if (r_map.find(ch) == r_map.end())
                r_map[ch] = 1;
            else
                r_map[ch] += 1;
        }

        for (auto ch: magazine){
            if (r_map.find(ch) == r_map.end())
                continue;
            else {
                r_map[ch] -= 1;
                if (r_map[ch] == 0)
                    r_map.erase(ch);
            }
        }
        // cout << r_map.size() << endl;
        return r_map.empty();
    }
};
// @lc code=end

