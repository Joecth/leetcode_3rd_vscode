/*
 * @lc app=leetcode id=40 lang=javascript
 *
 * [40] Combination Sum II
 *
 * https://leetcode.com/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (46.06%)
 * Likes:    1451
 * Dislikes: 56
 * Total Accepted:    298K
 * Total Submissions: 645K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * Given a collection of candidate numbers (candidates) and a target number
 * (target), find all unique combinations in candidates where the candidate
 * numbers sums to target.
 * 
 * Each number in candidates may only be used once in the combination.
 * 
 * Note:
 * 
 * 
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: candidates = [10,1,2,7,6,1,5], target = 8,
 * A solution set is:
 * [
 * ⁠ [1, 7],
 * ⁠ [1, 2, 5],
 * ⁠ [2, 6],
 * ⁠ [1, 1, 6]
 * ]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: candidates = [2,5,2,1,2], target = 5,
 * A solution set is:
 * [
 * [1,2,2],
 * [5]
 * ]
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    // res = [];
    let res = new Set();
    candidates.sort((a,b)=>(a-b));
    helper(candidates, target, 0, [], 0);
    ans = [];
    for (let j of res){
        ans.push(j.split(','));
    }
    return ans;
    // return res;
    
    function helper(nums, target, idx, item, sum){
        if (sum == target){
            // res.push(item.slice(0, item.length));
            res.add(item.join());
            return ;
        }
        if(sum > target){
            return
        }
        for (let i=idx; i < nums.length; i++){
            item.push(nums[i]);
            helper(nums, target, i+1, item, sum+nums[i]);
            item.pop()
        }   
    };    
};
// console.log(combinationSum2([10,1,2,7,6,1,5], 8));
// @lc code=end

