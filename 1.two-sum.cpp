/*
 * @lc app=leetcode id=1 lang=cpp
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
#include<unordered_map>
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> d;
        for (int i=0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (d.find(diff) != d.end()){
                return {d[diff], i};
            }
            d[nums[i]] = i;
            //cout << "=============" << endl;
            //for (auto tmp: d){
            //    cout << tmp.first << ": " << tmp.second << endl;
            //}
        }
        
        return {};
    }
};

int main_(){
    vector<int> a ={2,7,11,15};
    auto ans = Solution().twoSum(a, 9);
    cout  << ans.size() << endl;
    for (int i=0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
    //for (auto elem: ans){
    //    cout << elem << endl;
    //}
    return 0;
}

// @lc code=end

