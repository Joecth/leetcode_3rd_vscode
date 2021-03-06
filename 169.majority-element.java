/*
 * @lc app=leetcode id=169 lang=java
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
class Solution {
    public int majorityElement(int[] nums) {
        // Arrays.sort(nums);
        HashMap<Integer, Integer> d = new HashMap<Integer, Integer>();
        // Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();
        // //Hashtable<Integer, Integer> myMap = new Hashtable<Integer, Integer>();

        
        int ans = 0;
        for (int i=0; i<nums.length; i++){
        // for (int num: nums) {
            if (d.containsKey(nums[i])){
                d.put(nums[i], d.get(nums[i])+1);
            }
            else{
                d.put(nums[i], 0);
            }

            if (Math.floor(d.get(nums[i])) >= nums.length/2){
                ans = nums[i];
                break;
            }
        }
        return ans;
    }        
}
// @lc code=end

