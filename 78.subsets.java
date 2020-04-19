/*
 * @lc app=leetcode id=78 lang=java
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
/*
語言知識點：
● Line 2: error: List is abstract; cannot be instantiated
● 要用 ArrayList，不能用 List,  不然就找不到 clone method
*/

class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>();

    public List<List<Integer>> subsets(int[] nums) {
        if (nums.length == 0) return res;
        ArrayList<Integer> item = new ArrayList<Integer>();   // Line 2: error: List is abstract; cannot be instantiated ..
        helper(nums, 0, item);
        return res;
    }

    private void helper(int[] nums, int idx, ArrayList<Integer> item){
        if (idx == nums.length){
            // System.out.println(item);
            res.add((ArrayList<Integer>) item.clone());
            return;
        }
        item.add(nums[idx]);
        helper(nums, idx+1, item);
        item.remove(item.size()-1);
        helper(nums, idx+1, item);
    }
}

// @lc code=end

