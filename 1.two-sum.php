/*
 * @lc app=leetcode id=1 lang=php
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
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $tempArray = array();
        foreach($nums as $key=>$num){
            if(isset($tempArray[$target - $num]) && $tempArray[$target - $num] != $key){
                return [$tempArray[$target - $num], $key];
            }
            $tempArray[$num] = $key;
        }
    }
}
// @lc code=end

