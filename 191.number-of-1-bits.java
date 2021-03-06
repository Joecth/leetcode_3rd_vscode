/*
 * @lc app=leetcode id=191 lang=java
 *
 * [191] Number of 1 Bits
 *
 * https://leetcode.com/problems/number-of-1-bits/description/
 *
 * algorithms
 * Easy (47.44%)
 * Likes:    702
 * Dislikes: 483
 * Total Accepted:    330.1K
 * Total Submissions: 691.8K
 * Testcase Example:  '00000000000000000000000000001011'
 *
 * Write a function that takes an unsigned integer and return the number of '1'
 * bits it has (also known as the Hamming weight).
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 00000000000000000000000000001011
 * Output: 3
 * Explanation: The input binary string 00000000000000000000000000001011 has a
 * total of three '1' bits.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 00000000000000000000000010000000
 * Output: 1
 * Explanation: The input binary string 00000000000000000000000010000000 has a
 * total of one '1' bit.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 11111111111111111111111111111101
 * Output: 31
 * Explanation: The input binary string 11111111111111111111111111111101 has a
 * total of thirty one '1' bits.
 * 
 * 
 * 
 * Note:
 * 
 * 
 * Note that in some languages such as Java, there is no unsigned integer type.
 * In this case, the input will be given as signed integer type and should not
 * affect your implementation, as the internal binary representation of the
 * integer is the same whether it is signed or unsigned.
 * In Java, the compiler represents the signed integers using 2's complement
 * notation. Therefore, in Example 3 above the input represents the signed
 * integer -3.
 * 
 * 
 * 
 * 
 * Follow up:
 * 
 * If this function is called many times, how would you optimize it?
 * 
 */

// @lc code=start

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        int mask = 1;
        while (n != 0){  // CRUCIAL, better than n > 0, 'cause the SIGN(+/- 1) issue, 
                         // for 11111111111111111111111111111101, 
                         // it would be -3 at the beginning, and not able to enter while loop.. 
                         // (2's complement, from 011(+3) to 1...1101(-3))
            if ((n & mask) == 1){
                count += 1;
            }
            n = n >>> 1; // CRUCIAL
            /*
            >> is arithmetic shift right, >>> is logical shift right.
            ● In an arithmetic shift, the sign bit is extended to preserve the signedness of the number.
                For example: -2 represented in 8 bits would be 11111110 
                (because the most significant bit has negative weight). 
                Shifting it right one bit using arithmetic shift would give you 11111111, or -1. 
            ● Logical right shift, however, does not care that the value could possibly represent a signed number; 
                it simply moves everything to the right and fills in from the left with 0s. 
                Shifting our -2 right one bit using logical shift would give 01111111.
            */
        }
        return count;
    }
}


/*
Wrong Answer
315/601 cases passed (N/A)
Testcase
11111111111111111111111111111101
Answer
0
Expected Answer
31
*/

// @lc code=end

