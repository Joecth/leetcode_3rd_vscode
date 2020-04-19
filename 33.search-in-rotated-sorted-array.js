/*
 * @lc app=leetcode id=33 lang=javascript
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (33.68%)
 * Likes:    4045
 * Dislikes: 413
 * Total Accepted:    609.4K
 * Total Submissions: 1.8M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * 
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (null == nums || nums.length == 0) return -1;

    let lo = 0;
    let hi = nums.length - 1;
    while (lo <= hi){
        let mid = (lo + hi)>>1;
        let cur = nums[mid];
        if (cur == target) return mid;
        else if (nums[0] > cur){
            if (target > cur  && target <= nums[hi])
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        else {
            if (target < cur && target >= nums[lo])
                hi = mid - 1;
            else
                lo = mid + 1;
        }
    }
    return -1;

};
// @lc code=end

