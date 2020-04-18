/*
 * @lc app=leetcode id=678 lang=java
 *
 * [678] Valid Parenthesis String
 *
 * https://leetcode.com/problems/valid-parenthesis-string/description/
 *
 * algorithms
 * Medium (34.00%)
 * Likes:    1384
 * Dislikes: 43
 * Total Accepted:    76.4K
 * Total Submissions: 243.4K
 * Testcase Example:  '"()"'
 *
 * 
 * Given a string containing only three types of characters: '(', ')' and '*',
 * write a function to check whether this string is valid. We define the
 * validity of a string by these rules:
 * 
 * Any left parenthesis '(' must have a corresponding right parenthesis ')'.
 * Any right parenthesis ')' must have a corresponding left parenthesis '('.
 * Left parenthesis '(' must go before the corresponding right parenthesis ')'.
 * '*' could be treated as a single right parenthesis ')' or a single left
 * parenthesis '(' or an empty string.
 * An empty string is also valid.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: "()"
 * Output: True
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: "(*)"
 * Output: True
 * 
 * 
 * 
 * Example 3:
 * 
 * Input: "(*))"
 * Output: True
 * 
 * 
 * 
 * Note:
 * 
 * The string size will be in the range [1, 100].
 * 
 * 
 */

// @lc code=start
/* Different from other languages:
    1. Stack<Integer> S = new Stack<Integer>();
    2. S.get(int i)
 */
class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> left = new Stack<Integer>();
        Stack<Integer> star = new Stack<Integer>();

        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == '(') left.push(i);
            else if (s.charAt(i) == '*') star.push(i);
            else{
                if (left.size() != 0) left.pop();
                else if (star.size() != 0) star.pop();
                else {
                    return false;
                }
            }
        }
        
        if (left.size() == 0) return true;

        while (left.size() != 0){
            if (star.size() == 0) return false;
            else if (star.get(star.size()-1) < left.get(left.size()-1)) return false;
            else {
                left.pop();
                star.pop();
            }
        }
        return true;
    }
}
// @lc code=end