#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (43.85%)
# Likes:    789
# Dislikes: 2254
# Total Accepted:    109.2K
# Total Submissions: 248.7K
# Testcase Example:  '["Solution","pickIndex"]\r\n[[[1]],[]]\r'
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i(0-indexed), write a function pickIndex which randomly picks an index
# in proportion to its weight.
# 
# For example, given an input list of values w = [2, 8], when we pick up a
# number out of it, the chance is that 8 times out of 10 we should pick the
# number 1 as the answer since it's the second element of the array (w[1] =
# 8).
# 
# 
# Example 1:
# 
# 
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]
# 
# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. Since there is only one single element on
# the array the only option is to return the first element.
# 
# 
# Example 2:
# 
# 
# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]
# 
# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It's returning the second element (index =
# 1) that has probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It's returning the first element (index =
# 0) that has probability of 1/4.
# 
# Since this is a randomization problem, multiple answers are allowed so the
# following outputs can be considered correct :
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# 
# 
#

# @lc code=start
from bisect import bisect_right
from random import random, randint

class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
class Solution_failedSomeHow:

    def __init__(self, w: List[int]):
        if not w:
            assert(0)
        self.pre_sum = [0] * len(w)
        self.pre_sum[0] = w[0]
        cur_sum = 0
        for i in range(1, len(w)):
            self.pre_sum[i] = self.pre_sum[i-1] + w[i]
        self.total_sum = self.pre_sum[-1]
        print(self.pre_sum)
        # print(self.pre_sum)
    """
    3 4 1 7
    3 7 8 15
    """ 
    def pickIndex(self) -> int:
        # target = self.total_sum * random()
        # target = randint(self.pre_sum[0], self.total_sum)
        target = randint(1, self.total_sum)
        start, end = 0, len(self.pre_sum)-1
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.pre_sum[mid] < target:
                start = mid
            else:
                end = mid
        
        if self.pre_sum[start] == target:
            print(target, start, end, 'return start: {}'.format(start))
            return start
        print(target, start, end, 'return end: {}'.format(end))
        return end
                
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

