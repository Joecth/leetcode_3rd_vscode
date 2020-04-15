/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (58.98%)
 * Likes:    4030
 * Dislikes: 345
 * Total Accepted:    431K
 * Total Submissions: 729.2K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array nums of n integers where n > 1,  return an array output such
 * that output[i] is equal to the product of all the elements of nums except
 * nums[i].
 * 
 * Example:
 * 
 * 
 * Input:  [1,2,3,4]
 * Output: [24,12,8,6]
 * 
 * 
 * Constraint: It's guaranteed that the product of the elements of any prefix
 * or suffix of the array (including the whole array) fits in a 32 bit
 * integer.
 * 
 * Note: Please solve it without division and in O(n).
 * 
 * Follow up:
 * Could you solve it with constant space complexity? (The output array does
 * not count as extra space for the purpose of space complexity analysis.)
 * 
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] l = initializeArray(nums.length);
        for (int i=1; i < nums.length; i++){
            l[i] = l[i-1] * nums[i-1];
        }

        int[] r = initializeArray(nums.length);
        for (int j=nums.length-1-1; j >= 0; j--){
            r[j] = r[j+1] * nums[j+1];
        }

        int[] res = initializeArray(nums.length);
        for (int k=0; k < nums.length; k++){
            res[k] = l[k] * r[k];
        }
        return res;
    }

    private int[] initializeArray(int n){
        int[] l = new int[n];
        Arrays.fill(l, 1);
        return l;
    }
}
// @lc code=end

