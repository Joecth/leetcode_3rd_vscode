/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 *
 * https://leetcode.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (56.20%)
 * Likes:    2661
 * Dislikes: 208
 * Total Accepted:    534.6K
 * Total Submissions: 949K
 * Testcase Example:  '[3,2,3]'
 *
 * Given an array of size n, find the majority element. The majority element is
 * the element that appears more than ⌊ n/2 ⌋ times.
 * 
 * You may assume that the array is non-empty and the majority element always
 * exist in the array.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,2,3]
 * Output: 3
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,1,1,1,2,2]
 * Output: 2
 * 
 * 
 */

// @lc code=start
#include<unordered_map>
#include<vector>
#include<cmath>
using namespace std;
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> d;
        int n = 0;
        for (auto num: nums){
            if (d.find(num) != d.end()){
                d[num] += 1;
            }
            else{
                d[num] = 0;
            }

            if (d[num] >= floor(nums.size()/2)){
                n = num;
                break;
            }
        }
        return n;
    }
};
// @lc code=end

