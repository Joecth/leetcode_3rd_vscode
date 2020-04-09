/*
 * @lc app=leetcode id=844 lang=javascript
 *
 * [844] Backspace String Compare
 *
 * https://leetcode.com/problems/backspace-string-compare/description/
 *
 * algorithms
 * Easy (47.22%)
 * Likes:    1174
 * Dislikes: 65
 * Total Accepted:    121.7K
 * Total Submissions: 256.4K
 * Testcase Example:  '"ab#c"\n"ad#c"'
 *
 * Given two strings S and T, return if they are equal when both are typed into
 * empty text editors. # means a backspace character.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: S = "ab#c", T = "ad#c"
 * Output: true
 * Explanation: Both S and T become "ac".
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: S = "ab##", T = "c#d#"
 * Output: true
 * Explanation: Both S and T become "".
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: S = "a##c", T = "#a#c"
 * Output: true
 * Explanation: Both S and T become "c".
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: S = "a#c", T = "b"
 * Output: false
 * Explanation: S becomes "c" while T becomes "b".
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= S.length <= 200
 * 1 <= T.length <= 200
 * S and T only contain lowercase letters and '#' characters.
 * 
 * 
 * Follow up:
 * 
 * 
 * Can you solve it in O(N) time and O(1) space?
 * 
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function(S, T) {
    const helper = function(st){
        let stack = '';
        for (let i=0; i < st.length; i++){
            if (st[i] == '#'){
                if (stack.length == 0){
                    let xx = 1;
                }
                else {
                    // stack.pop()
                    stack = stack.slice(0, stack.length-1);
                }
            }
            else {
                // stack.push(S[i]);
                stack += st[i];
            }
        }
        return stack;
    }
    let a = helper(S);
    let b = helper(T);
    return a == b;
};
// console.log(backspaceCompare("ab#c", "ad#c"));
// console.log(backspaceCompare("a#c", "b"));
// @lc code=end

