#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (58.50%)
# Likes:    3130
# Dislikes: 73
# Total Accepted:    511.6K
# Total Submissions: 869.2K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.res = []
        self.helper_bt(nums, 0, [])
        # self.helper_BF_bt(nums, 0, [])
        return self.res
        return self.helper_BF(nums)
        
        
    # def helper_BF_bt_FAILED(self, nums, idx, item):
    #     if idx == len(nums):
    #         self.res.append(item.copy())
    #         return 
    #     for i in range(idx, len(nums)):
    #         # self.helper_BF_bt(idx+1, item + [nums[i]])     # NOT to write in this way
    #         item.append(nums[i])
    #         self.helper_BF_bt(nums, i+1, item)
    #         item.pop()
        
        
    def helper_BF(self, nums):
        res = [[]]
        for num in nums:
            new_subset = []
            for j in range(len(res)):
                cur = res[j].copy() # [] or [1] ... 
                cur.append(num)     # [2] or [1,2]
                new_subset.append(cur)
                # print(new_add)
            
            res.extend(new_subset)
        return res
    
    
    def helper_bt(self, nums, idx, item):
        if idx == len(nums):
            self.res.append(item.copy())
            return
        
        self.helper_bt(nums, idx+1, item+[nums[idx]])
        self.helper_bt(nums, idx+1, item)

    

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return nums
        
#         self.result = [[]]
#         item = []
#         self.helper(0, nums, item)
        
#         return self.result
        
#     def helper(self, level, nums, item):
#         if level == len(nums):
#             # self.result.append(item.copy())
#             return
        
#         item.append(nums[level])     # [1,2,3] # prevent the OOR here  
#         self.result.append(item.copy())
#         self.helper(level+1, nums, item.copy())
#         item.pop()  # no 2 
#         self.helper(level+1, nums, item.copy()) # level 3  eturn 
# @lc code=end

