/*
 * @lc app=leetcode id=34 lang=javascript
 *
 * [34] Find First and Last Position of Element in Sorted Array
 *
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (35.27%)
 * Likes:    2850
 * Dislikes: 127
 * Total Accepted:    448.4K
 * Total Submissions: 1.3M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * Given an array of integers nums sorted in ascending order, find the starting
 * and ending position of a given target value.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * If the target is not found in the array, return [-1, -1].
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    // return helper_O_N(nums, target);
    return helper_O_lgN(nums, target);

    function helper_O_lgN(nums, target){
        if (nums.length == 0)
            return [-1, -1];
        
        let l = b_left(nums, target);
        let has_l = false
        if (l < nums.length && nums[l] == target){ // [2,2], 3   issue
            has_l = true
        }
        if (false == has_l)
            return [-1, -1]

        // find r_bound with binary search
        let r = b_right(nums, target);
        return [l, r-1];
    }

    function b_right(nums, target){
        let l = 0;
        let r = nums.length;
        while (l < r){
            let mid = (l+r) >> 1;
            if (nums[mid] > target)
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }

    function helper_O_N(nums, target){
        if (nums.length == 0)
            return [-1, -1];

        let l = b_left(nums, target);
        let has_l = false
        if (l < nums.length && nums[l] == target){
            has_l = true;
        }
        if (has_l == false) return [-1, -1]; 

        // find right bound 
        let r = l;
        while (r < nums.length && nums[r] == target){
            r += 1;
        }
        return [l, r-1]
    }

    function b_left(nums, target){
        let l = 0;
        let r = nums.length;
        while (l < r){
            mid = (l+r) >> 1; // floor((l+r)/2)
            if (nums[mid] >= target){
                r = mid;
            }
            else {
                l = mid+1;
            }
        }
        return l;
    }
    
};
// @lc code=end

