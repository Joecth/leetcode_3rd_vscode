#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (60.91%)
# Likes:    3596
# Dislikes: 102
# Total Accepted:    578.1K
# Total Submissions: 930.1K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
# a a b c 
# a:2
# b:1
# c:1

from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        # return self.permute_by_bucket(nums)
        # return self.permute_by_putting(nums)
        return self.permute_by_swapping(nums)
    
    def permute_by_swapping(self, nums):
        ans = []
        self.bt(nums, nums.copy(), 0, ans)
        return ans
    
    def bt(self, nums, item, idx, ans):
        if idx == len(item):
            ans.append(item.copy())
            return 
        
        for i in range(idx, len(item)):
            self.swap(item, i, idx)
            self.bt(nums, item, idx+1, ans)
            self.swap(item, i, idx)
            
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
        
    def permute_by_putting(self, nums):
        self.ans = []
        self.dfs(nums, [])
        return self.ans
        
    def dfs(self, nums, item):
        if len(nums) == len(item):
            self.ans.append(item.copy())
            return
        
        for i in range(len(nums)):
            if nums[i] in item:
                continue
            item.append(nums[i])
            self.dfs(nums, item)
            item.pop()
            
    def permute_by_bucket(self, nums, item):
        c_map = Counter(nums)
        keys, values = c_map.keys(), c_map.values()
        sorted_keys = sorted(list(keys), key=lambda x: x)  # sequence should be garanteed during each backtracking
        counts = [0 for _ in range(len(sorted_keys))]
        
        for i in range(len(sorted_keys)):
            counts[i] = c_map[sorted_keys[i]]
            
        self.res = []
        self.helper(sorted_keys, counts, 0, [])
        
        return self.res
        
    def helper(self, sorted_keys, counts, idx, item):
        # for k in c_map.keys():    sequence should be garanteed
            # if c_map[k] == 0:
        if len(sorted_keys) == idx:
            self.res.append(item.copy())
            return 
        
        for i in range(len(sorted_keys)):
            key = sorted_keys[i]
            if counts[i] > 0:
                counts[i] -= 1
                item.append(key)
                self.helper(sorted_keys, counts, idx+1, item)
                item.pop()
                counts[i] += 1
        
        
    def permute_old(self, nums: List[int]) -> List[List[int]]:
        c_map = Counter(nums) # a a b c
        keys = sorted(c_map)    # a b c 
        
        arr = []
        counts = []
        for k in keys:
            arr.append(k)  # a b c 
            counts.append(c_map[k]) # 2 1 1
        item = [0 for tmp in range(len(nums))] # 0 0 0 0
        
        self.result = [] #set([])
        self.helper(arr, counts, 0, item.copy())
        
        return self.result
    
    def helper_old(self, arr, counts, level, item):
        if level == len(item):
            if item not in self.result:
                self.result.append(item.copy())
            return 
        
        # item[idx] = 
        # counts[idx] -= 1
        for j in range(len(arr)):   # a b c 
            if counts[j] == 0:       # 2 1 1
                continue
            item[level] = arr[j]    # [a a]
            counts[j] -= 1
            self.helper_old(arr, counts.copy(), level+1, item.copy())
            counts[j] += 1
                    
# @lc code=end

