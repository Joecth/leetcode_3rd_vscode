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
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        
        /* 1. L->R */
        int l[] = new int[n];
        l[0] = 1;
        // for (int i=0; i < n; i++){
        //     l[i] = 1;
        // }
        
        for (int i=1; i < n; i++){
            l[i] = l[i-1] * nums[i-1];
        }
        
        /* 2. L<-R */
        int r[] = new int[n];
        // for (int i=0; i < n; i++){
        //     r[i] = 1;
        // }
        r[n-1] = 1;
        for (int i=n-2; i >= 0; i--){
            r[i] = r[i+1] * nums[i+1];
        }
        
        /* 3 merge */
        for(int i=0; i < n; i++){
            l[i] *= r[i];
        }
            
        return l;
    }

//     public int[] productExceptSelf_old(int[] nums) {
//         int[] l = initialize_array(nums.length);
//         for (int i=1; i < nums.length; i++){
//             l[i] = l[i-1] * nums[i-1];
//         }

//         int[] r = initialize_array(nums.length);
//         for (int j=nums.length-1-1; j >= 0; j--){
//             r[j] = r[j+1] * nums[j+1];
//         }

//         int[] res = initialize_array(nums.length);
//         for (int k=0; k < nums.length; k++){
//             res[k] = l[k] * r[k];
//         }
//         return res;
//     }

}
// @lc code=end

