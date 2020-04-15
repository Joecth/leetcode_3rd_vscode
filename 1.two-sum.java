/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (45.19%)
 * Likes:    14097
 * Dislikes: 513
 * Total Accepted:    2.7M
 * Total Submissions: 6M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 */

// @lc code=start
// Java中有四种常见的Map实现，HashMap，TreeMap，HashTable和LinkedHashMap，我们可以使用一句话来描述各个Map，如下：

// HashMap：基于散列表实现，是无序的；
// TreeMap：基于红黑树实现，按Key排序；
// LinkedHashMap：保存了插入顺序；
// Hashtable：是同步的，与HashMap类似；
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> d = new HashMap<Integer, Integer>();

        for (int i=0; i < nums.length; i++){
            int diff = target - nums[i];
            if (d.containsKey(diff)){
                return new int[]{d.get(diff), i};
            }
            d.put(nums[i], i);
        }
        return new int[2];
    }
}
// @lc code=end

