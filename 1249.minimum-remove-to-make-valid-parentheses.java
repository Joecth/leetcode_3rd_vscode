/*
 * @lc app=leetcode id=1249 lang=java
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 *
 * https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
 *
 * algorithms
 * Medium (62.34%)
 * Likes:    864
 * Dislikes: 25
 * Total Accepted:    74.5K
 * Total Submissions: 119.3K
 * Testcase Example:  '"lee(t(c)o)de)"'
 *
 * Given a string s of '(' , ')' and lowercase English characters. 
 * 
 * Your task is to remove the minimum number of parentheses ( '(' or ')', in
 * any positions ) so that the resulting parentheses string is valid and return
 * any valid string.
 * 
 * Formally, a parentheses string is valid if and only if:
 * 
 * 
 * It is the empty string, contains only lowercase characters, or
 * It can be written as AB (A concatenated with B), where A and B are valid
 * strings, or
 * It can be written as (A), where A is a valid string.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "lee(t(c)o)de)"
 * Output: "lee(t(c)o)de"
 * Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "a)b(c)d"
 * Output: "ab(c)d"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "))(("
 * Output: ""
 * Explanation: An empty string is also valid.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "(a(b(c)d)"
 * Output: "a(b(c)d)"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s[i] is one of  '(' , ')' and lowercase English letters.
 * 
 */

// @lc code=start
class Solution {
    public String minRemoveToMakeValid(String s) {
        if (s.length() == 0)
            return s;
        
        int n = s.length();
        /* L --> R */
        HashSet<Integer> rm_list = new HashSet<>();
        int score = 0;
        for (int i=0; i < n; i++){
            // rm_list.add
            if (s.charAt(i) == '('){
                score += 1;
            }
            else if (s.charAt(i) == ')'){
                if (score > 0){
                    score -= 1;
                }
                else {
                    rm_list.add(i);
                }
            }
        }
        
        /* L <-- R*/
        score = 0;
        for (int i=n-1; i > -1; i--){
            // rm_list.add
            if (s.charAt(i) == ')'){
                score += 1;
            }
            else if (s.charAt(i) == '('){
                if (score > 0){
                    score -= 1;
                }
                else {
                    rm_list.add(i);
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++){
            if (!rm_list.contains(i))
                sb.append(s.charAt(i));
        }
        
        // return (String)sb;
        return sb.toString();
    }
}
// @lc code=end
