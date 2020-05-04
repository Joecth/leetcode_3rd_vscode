/*
 * @lc app=leetcode id=476 lang=cpp
 *
 * [476] Number Complement
 *
 * https://leetcode.com/problems/number-complement/description/
 *
 * algorithms
 * Easy (63.35%)
 * Likes:    741
 * Dislikes: 77
 * Total Accepted:    141K
 * Total Submissions: 220.8K
 * Testcase Example:  '5'
 *
 * Given a positive integer, output its complement number. The complement
 * strategy is to flip the bits of its binary representation.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 5
 * Output: 2
 * Explanation: The binary representation of 5 is 101 (no leading zero bits),
 * and its complement is 010. So you need to output 2.
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 1
 * Output: 0
 * Explanation: The binary representation of 1 is 1 (no leading zero bits), and
 * its complement is 0. So you need to output 0.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The given integer is guaranteed to fit within the range of a 32-bit signed
 * integer.
 * You could assume no leading zero bit in the integer’s binary
 * representation.
 * This question is the same as 1009:
 * https://leetcode.com/problems/complement-of-base-10-integer/
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    int findComplement(int num) {
        int ans = 0;
        int i = 0;
        while (num!=0){
            if (num % 2 == 0){
                ans += 1 << i;
            }
            num >>= 1;
            i += 1;
        }
        return ans;
    }
};
// @lc code=end

