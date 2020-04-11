/*
 * @lc app=leetcode id=39 lang=javascript
 *
 * [39] Combination Sum
 *
 * https://leetcode.com/problems/combination-sum/description/
 *
 * algorithms
 * Medium (53.82%)
 * Likes:    3202
 * Dislikes: 101
 * Total Accepted:    487.8K
 * Total Submissions: 903.6K
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * Given a set of candidate numbers (candidates) (without duplicates) and a
 * target number (target), find all unique combinations in candidates where the
 * candidate numbers sums to target.
 * 
 * The same repeated number may be chosen from candidates unlimited number of
 * times.
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
 * Input: candidates = [2,3,6,7], target = 7,
 * A solution set is:
 * [
 * ⁠ [7],
 * ⁠ [2,2,3]
 * ]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: candidates = [2,3,5], target = 8,
 * A solution set is:
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
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
var combinationSum = function(candidates, target) {
    res = [];
    candidates.sort((a,b)=>(a-b));
    helper(candidates, target, 0, 0, []);
    return res;
    
    function helper(nums, target, idx, sum, item){
        if (target == sum){
            res.push([...item]);
            return;
        }
        if (target < sum){
            return;
        }
        for (let i=idx; i< nums.length; i++){
            item.push(nums[i])
            helper(nums, target, i, sum+nums[i], item);
            item.pop()
        }
    };
};
console.log(combinationSum([2,3,6,7], 7));
// @lc code=end

