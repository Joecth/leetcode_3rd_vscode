/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 *
 * https://leetcode.com/problems/maximum-subarray/description/
 *
 * algorithms
 * Easy (45.86%)
 * Likes:    6730
 * Dislikes: 303
 * Total Accepted:    833.5K
 * Total Submissions: 1.8M
 * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
 *
 * Given an integer array nums, find the contiguous subarray (containing at
 * least one number) which has the largest sum and return its sum.
 * 
 * Example:
 * 
 * 
 * Input: [-2,1,-3,4,-1,2,1,-5,4],
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 * 
 * 
 * Follow up:
 * 
 * If you have figured out the O(n) solution, try coding another solution using
 * the divide and conquer approach, which is more subtle.
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    function max(a,b ){
        return Math.max(a,b);
    }
    let dp0 = nums[0];
    let g_max = nums[0]
    for (let i = 1; i < nums.length; i++){
        dp0 = max(dp0+nums[i], nums[i]);
        g_max = max(dp0, g_max);
    }
    return g_max;
};
maxSubArray([-2,1,-3,4,-1,2,1,-5,4]);
// @lc code=end

