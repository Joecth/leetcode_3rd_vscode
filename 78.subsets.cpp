/*
 * @lc app=leetcode id=78 lang=cpp
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
class Solution {
private:
    vector<vector<int>> result;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> item;
        helper(nums, 0, item);  // 呼叫時候不需要 this 加在前面
        return result;
    }

    void helper(vector<int>& nums, int idx, vector<int>& item){
        if (idx == nums.size()){
            result.push_back(item);
            return;
        }

        item.push_back(nums[idx]);
        helper(nums, idx+1, item);
        item.pop_back();
        helper(nums, idx+1, item);
    }
};
// @lc code=end

