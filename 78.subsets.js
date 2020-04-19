/*
 * @lc app=leetcode id=78 lang=javascript
 *
 * [78] Subsets
 *
 * https://leetcode.com/problems/subsets/description/
 *
 * algorithms
 * Medium (58.50%)
 * Likes:    3130
 * Dislikes: 73
 * Total Accepted:    511.6K
 * Total Submissions: 869.2K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a set of distinct integers, nums, return all possible subsets (the
 * power set).
 * 
 * Note: The solution set must not contain duplicate subsets.
 * 
 * Example:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if (nums.length == 0) return [];
    res = [];
    helper(nums, 0, []);
    return res;

    function helper(nums, idx, item){
        if (idx == nums.length){
            res.push([...item]);
            return;
        }

        item.push(nums[idx]);
        helper(nums, idx+1, item);
        item.pop();
        helper(nums, idx+1, item);
    }
};
// @lc code=end

