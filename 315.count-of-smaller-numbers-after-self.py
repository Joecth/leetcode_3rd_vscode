#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (41.35%)
# Likes:    2351
# Dislikes: 83
# Total Accepted:    129.7K
# Total Submissions: 313.5K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
#

# @lc code=start
class FenwickTree:
    def __init__(self, n):
        self.nums = [0] * (n+1)
    
    def update(self, pos, delta):
        while pos < len(self.nums):
            self.nums[pos] += delta    
            pos += self._lowbit(pos)
    
    def query(self, pos):
        sum_ = 0
        while pos > 0:
            sum_ += self.nums[pos]
            pos -= self._lowbit(pos)
        return sum_
        
    def _lowbit(self, x):
        return x & -x
        

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Write your code here
        if not A:
            return 0
        # return self.M_sort_sol(nums)
        return self.BIT_sol(nums)   # TODO: fix
        return self.binary_sol(nums)
    
    def binary_sol(self, nums):
        order = []
        res = []
        from bisect import bisect_left, bisect_right, insort_left
        for i in range(len(nums)-1, -1, -1):
            pos = bisect_left(order, nums[i])
            res.append(pos)
            # order.insert(pos, nums[i])
            insort_left(order, nums[i])
            # print('pos: {}'.format(pos))
            # print('order: {}'.format(order))
        return res[::-1]
    
    def BIT_sol(self, nums):
        n = len(nums)
        order = [x for x in nums]
        order.sort()
        cnt = [0] * n
        # print(order)
        tree = FenwickTree(len(nums))
        from bisect import bisect_left, bisect_right
        for i in range(len(nums)-1, -1, -1):
            # print(order)
            idx = bisect_right(order, nums[i])
            # idx = bisect_left(order, nums[i])+1
            cnt[i] = tree.query(idx-1)
            tree.update(idx, 1)
        res = []
        for i in range(n):
            res.append(cnt[i])
        return res
        
    def M_sort_sol(self, nums):
        temp = [0] * len(nums)
        ans = [0] * len(nums)
        self.M_Sort(nums, 0, len(nums)-1, temp, ans)
        return ans
        
    def M_Sort(self, nums, left, right, temp, ans):
        if left >= right:
            return 0
            
        mid = left + (right - left)//2
        count = 0
        count += self.M_Sort(nums, left, mid, temp, ans)
        count += self.M_Sort(nums, mid+1, right, temp, ans)
        
        i, j = left, mid + 1
        k = left
        
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
            # if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
                count += mid + 1 - i
                ans[k] = count
            k += 1
        
        
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1
        for i in range(left, right+1):
            nums[i] = temp[i]    
        
        return count                
# @lc code=end

