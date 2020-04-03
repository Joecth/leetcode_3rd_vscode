/*
 * @lc app=leetcode id=16 lang=javascript
 *
 * [16] 3Sum Closest
 *
 * https://leetcode.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (45.73%)
 * Likes:    1732
 * Dislikes: 123
 * Total Accepted:    436K
 * Total Submissions: 953.4K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * Given an array nums of n integers and an integer target, find three integers
 * in nums such that the sum is closest to target. Return the sum of the three
 * integers. You may assume that each input would have exactly one solution.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 2, 1, -4], and target = 1.
 * 
 * The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    if (nums.length == 0)
        return [];

    function abs(a){
        // console.log('in abs' + Math.abs(a));
        return Math.abs(a);
    }
    const sum = arr => arr.reduce((a,b) => a + b, 0);
    
    nums.sort((a,b)=>a-b);
    // console.log(nums);
    let res = [9999999999999999];
    for (let i=0; i <= nums.length; i++){
        let l = i + 1;
        let r = nums.length - 1;
        while (l < r){
            arr = [nums[i], nums[l], nums[r]];
            // console.log(sum(arr)-target);
            // console.log(sum(res)-target);
            // if (abs(sum(arr)-target) < abs(sum(res)-target)){
            let a = abs(sum(arr)-target);
            let b = abs(sum(res)-target);

            if (a < b){
                // console.log(abs(sum(arr)-target));
                // console.log(abs(sum(res)-target));
                // console.log('aaaaaa ' + arr);
                res = arr;
                // console.log(res);
            }
            if (sum(arr) == target){
                // break;
                return target
            }
            else if(sum(arr) < target){
                l += 1;
            }
            else {
                r -= 1;
            }
        }
    }
    return sum(res);    
};
// @lc code=end

