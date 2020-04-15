/*
 * @lc app=leetcode id=238 lang=cpp
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
#include <vector>
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> l = init_arr(nums.size());
        for (int i=1; i < nums.size(); i++){
            l[i] = nums[i-1] * l[i-1];
        }

        vector<int> r = init_arr(nums.size());
        for (int j=nums.size()-1-1; j >= 0; j--){
            r[j] = nums[j+1] * r[j+1];
        }

        vector<int> res = init_arr(nums.size());
        for (int k=0; k < nums.size(); k++){
            res[k] = l[k] * r[k];
        }
        return res;
    }

    vector<int> init_arr(int n){
        vector<int> ret;
        for (int i=0; i<n; i++){
            ret.push_back(1);
        }
        return ret;
    }
};
// @lc code=end

