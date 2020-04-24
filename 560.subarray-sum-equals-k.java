/*
 * @lc app=leetcode id=560 lang=java
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
class Solution {
    public int subarraySum(int[] nums, int k) {
        if (nums.length == 0) return 0;
        int prefix_sum = 0;
        int count = 0;
        // Map<int, int> d = new HashMap();
        Map<Integer, Integer> d = new HashMap();
        d.put(0, 1);
        for (int num: nums){
            prefix_sum += num;
            if (d.containsKey(prefix_sum-k))
                count += d.get(prefix_sum-k);
            
            if (!(d.containsKey(prefix_sum)))
                d.put(prefix_sum, 0);
            d.put(prefix_sum, d.get(prefix_sum)+1);
        }
        return count;
    }
}
// @lc code=end

