/*
 * @lc app=leetcode id=560 lang=javascript
 *
 * [560] Subarray Sum Equals K
 *
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (43.53%)
 * Likes:    3959
 * Dislikes: 124
 * Total Accepted:    262K
 * Total Submissions: 595.4K
 * Testcase Example:  '[1,1,1]\n2'
 *
 * Given an array of integers and an integer k, you need to find the total
 * number of continuous subarrays whose sum equals to k.
 * 
 * Example 1:
 * 
 * Input:nums = [1,1,1], k = 2
 * Output: 2
 * 
 * 
 * 
 * Note:
 * 
 * The length of the array is in range [1, 20,000].
 * The range of numbers in the array is [-1000, 1000] and the range of the
 * integer k is [-1e7, 1e7].
 * 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    if (nums.length == 0) return 0;
    let ans = 0;
    let prefix_sum = 0;
    d = {};
    d[0] = 1;
    for (let i=0; i<nums.length; i++){
        prefix_sum += nums[i];
        if (prefix_sum - k in d)
            ans += d[prefix_sum-k];
        
        if (!(prefix_sum in d))
            d[prefix_sum] = 0;
        d[prefix_sum] += 1;
    }
    return ans;

};
// @lc code=end

