/*
 * @lc app=leetcode id=387 lang=java
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
class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> d = new HashMap();

        for (int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            // if (d.containsLey(s[i]))
            if (d.containsKey(ch))
                d.put(ch, d.get(ch)+1);
            else
                d.put(ch, 1);
        }

        for (int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if (d.get(ch) == 1)
                return i;
        }
        return -1;
    }
}
// @lc code=end

