#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (33.35%)
# Likes:    3615
# Dislikes: 305
# Total Accepted:    425.8K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False        
            reachable = max(reachable, i+nums[i])
        return True
        # ref: https://www.youtube.com/watch?v=muDPTDrpS28    

# Greedy: 
# public class Solution {
#     public boolean canJump(int[] nums) {
#         int lastPos = nums.length - 1;
#         for (int i = nums.length - 1; i >= 0; i--) {
#             if (i + nums[i] >= lastPos) {
#                 lastPos = i;
#             }
#         }
#         return lastPos == 0;
#     }
# }
    
# @lc code=end

