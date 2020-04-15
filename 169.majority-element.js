/*
 * @lc app=leetcode id=169 lang=javascript
 *
 * [169] Majority Element
 *
 * https://leetcode.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (56.20%)
 * Likes:    2661
 * Dislikes: 208
 * Total Accepted:    534.6K
 * Total Submissions: 949K
 * Testcase Example:  '[3,2,3]'
 *
 * Given an array of size n, find the majority element. The majority element is
 * the element that appears more than ⌊ n/2 ⌋ times.
 * 
 * You may assume that the array is non-empty and the majority element always
 * exist in the array.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,2,3]
 * Output: 3
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,1,1,1,2,2]
 * Output: 2
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    d = {};
    for (let i=0; i < nums.length; i++){
        if (nums[i] in d){
            d[nums[i]] += 1;
        }
        else{
            d[nums[i]] = 0;
        }

        if (d[nums[i]] >= Math.floor(nums.length/2)){
            return nums[i];
        }
    }
};
// @lc code=end

