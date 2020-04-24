/*
 * @lc app=leetcode id=560 lang=cpp
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
/*
  1 1 -1 1 1,    2

0 1 2  1 2 3    prefix_sum
    i    i 
                ==> 4 combinations 
*/
#include <unordered_map>
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if (!nums.size()) return 0;

        auto prefix_sum = 0;
        int ans = 0;
        unordered_map<int, int> d;
        d[0] = 1;
        // for (auto n: nums){
        for (int i=0; i < nums.size(); i++){
            prefix_sum += nums[i];
            if (d.find(prefix_sum - k) != d.end()){
                ans += d[prefix_sum - k]; 
            }

            // if (d.find(prefix_sum) == d.end())
            //     d[prefix_sum] = 0;
            d[prefix_sum] += 1;
        }
        return ans;
    }
};
// @lc code=end

