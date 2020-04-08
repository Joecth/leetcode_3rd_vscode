/*
 * @lc app=leetcode id=18 lang=javascript
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (32.73%)
 * Likes:    1604
 * Dislikes: 301
 * Total Accepted:    306.4K
 * Total Submissions: 934.9K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate quadruplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    let res = [];
    nums.sort((a,b)=>a-b);
    console.log(nums);
    for (let i=0; i < nums.length-3; i++){
        if (i>0 && nums[i] == nums[i-1]){
            continue;
        }
        for (let j=i+1; j < nums.length-2; j++){
            if (j>i+1 && nums[j] == nums[j-1]){
                continue;
            }
            let l = j + 1;
            let r = nums.length-1;

            while (l < r){
                let arr = [nums[i], nums[j], nums[l], nums[r]];
                let total = arr.reduce((x, y) => x+y, 0);
                let diff = total - target;
                if (diff == 0){
                    res.push(arr);
                    while (l+1<r && nums[l] == nums[l+1]){
                        l += 1;
                    }
                    l += 1;
                    
                    while (l<r-1 && nums[r] == nums[r-1]){
                        r -= 1;
                    }
                    r -= 1;
                }
                else if (diff < 0){
                    l += 1;
                }
                else{
                    r -= 1;
                }
            }
        }
    }
    return res;
};
console.log(fourSum([-5, -4, -3,-2,-1,0,0,1,2,3, 4, 5], 0))
// console.log(fourSum([-2,-1,0,0,1,2], 0))
// console.log(fourSum([-3,-2,-1,0,0,1,2,3], 0))
// console.log(fourSum([0,0,0,0], 0))
// @lc code=end

