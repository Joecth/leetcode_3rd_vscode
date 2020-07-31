#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.96%)
# Likes:    3167
# Dislikes: 764
# Total Accepted:    317.2K
# Total Submissions: 1M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        # return self.BF(nums)
        # return self.helper_FAILED(nums)   # FAILED w/ N space
        # return self.helper_cyclic_sort(nums)    # STILL BUGGY, fixed.... ><
        # return self.O_1_Hashing(nums)
        # return self.sol_magic(nums)
        return self.sol_guoguo(nums)  # BEST
        return self.sol_wu(nums)
    
    def sol_wu(self, nums):
        return self.sol_magic(nums)
    
    def sol_guoguo(self, nums):
        # [-1 -2 INF]
        # [-3 4 -INF -1]
        # [INF INF INF INf INF INF]
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n: # 因為負的index不能算，如-1不該讓第一個值也變成負的以為有1
                nums[i] = sys.maxsize
                # continue
        # print(nums)
        
        for i in range(n):
            if abs(nums[i]) == sys.maxsize:
                continue
            pos = abs(nums[i])-1
            nums[pos] = -abs(nums[pos])
        # print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
    
    def sol_magic(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
            # nums[nums[i]]+=n
        for i in range(1,len(nums)):
            # if nums[i]/n==0:
            if nums[i] < n:
                return i
        # print(n)
        return n

    def helper_cyclic_sort(self, nums):  # 原地一直换直到找到自己
        """
        1 2 0 
            i = 0: 2 1 0 => 0 1 2, j=0
            i = 1: 0 1 2, j=1
            i = 2: 0 1 2, j=2
                        return j + 1 == 3
            
        3 4 -1 1 
            i = 0: 1 4 -1 3 => 4 1 -1 3 ==> OOR, j stand still
            i = 1: 4 1 -1 3, j=1
            i = 2: 4 1 -1 3, j stand still
            i = 3: 4 1 -1 3            
                        ==> X! nums[] == -1, return 2  
                        return j + 1 == 2
                    
        7 8 9 11 12 
            i = 0: 7 8 9 11 12 => OOR, so, j stand still
            i = 1: 7 8 9 11 12 => OOR, so, j stand still
            i = 2: 7 8 9 11 12 => OOR, so, j stand still
            i = 3: 7 8 9 11 12 => OOR, so, j stand still
            i = 4: 7 8 9 11 12 => OOR, so, j stand still
                        return j + 1 == 1
        """
        n = len(nums)
        j = 0
        for i in range(1, n):
            if nums[i] < 0 or nums[i] > n:
                continue
            end = nums[i]-1
            
            # while nums[i] != nums[end]: #==> TLE
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[end]:
                # swap(nums, to, i)
                nums[end], nums[i] = nums[i], nums[end]
                end = nums[i] - 1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
#             while i != nums[i-1]:
#                 pos = nums[i-1]
#                 nums[i-1], nums[pos] = nums[pos], nums[i-1]

#             # if i == nums[i-1]:
#             #     nums[i-1] = -1
#         i = 0
#         for i in range(0, n):
#             # if i != nums[i-1]:
#             if i+1 != nums[i]:
#                 return i+1 # if nums[i] != 1 else 2
#         return i + 1 if len(nums) > 1 else 2
    
    def O_1_Hashing(self, nums):
        """
        3,4,-1,1    2
        1,-1,3,4
        
        f==hash : "nums[i]"" ==> should be at pos of "nums[i]-1"
                    1               0
                    3               2
                    4               3
        """
        n = len(nums)
        for i in range(n):
            # idx = nums[i]-1  BUGGY!!! INFINITE LOOP
            # while nums[i] > 0 and nums[i] <= n and nums[i] != nums[idx]:
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:            
                # print(nums)
                self.swap(nums, nums[i]-1, i) # stores nums[i] to nums[idx]
        
        for i in range(n):
            if nums[i] != i+1:  # 3 should be at pos 2
                return i+1
        return n+1  # also satisfy []
    
    def swap(self, nums, to, fr):
        nums[to], nums[fr] = nums[fr], nums[to]
    
        
    def helper_FAILED(self, nums):  # FAILED w/ N space
        """
        1 2 0 => 2 1 0 memo[2] => 2 1 0 memo[2]
              => 0 1 2 memo[2]
              => since 2 in memo, thus return i+1 == 3
                        
        3 4 -1 1 ==> 1 4 -1 3 memo [1]
                 ==> when i == 1, notice 4 OOR
                 ==> check 1 in memo (start fr cur i)
                 ==> check 2 not in memo
                                ==> return 2
                    
        7 8 9 11 12 
                ==> when i == 0, notcie 7 OOR
                ==> check 0 not in memo (start fr cur i)
                    is 0 valiid? No!
                ==> check 1 not in memo
                                ==> return 1
                WRONG!
                FAILED if 7 8 9 1 12
        """
        memo = set(nums)    # ==> O(N) space for checking!
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] < n:
                    nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                    memo.add(nums[i])
                else:   # OOR
                    j = i
                    # if j in memo:
                    #     j += 1
                    while j in memo:
                        j += 1
                    return j+1
        return nums[i] + 1
                    
        
    def BF(self, nums):
        nums.sort()     # NxLog(N)
        max_ = nums[-1]
        prev = 0
        for n in nums:
            if n <= 0:
                continue
            if n - prev > 1:
                return prev + 1
            else:
                prev = n
        return prev+1
# @lc code=end

