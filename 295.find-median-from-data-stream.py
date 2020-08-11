#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (43.84%)
# Likes:    2785
# Dislikes: 51
# Total Accepted:    214.6K
# Total Submissions: 484.4K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#

# @lc code=start
import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))  # so that every elem in max_heap < min_heap
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                           
    def findMedian(self) -> float:
        m, n = len(self.min_heap), len(self.max_heap)
        # print(self.min_heap, self.max_heap)
        if (m + n) % 2 == 1:
            return self.min_heap[0]
        else:   
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
                           
                           

from bisect import bisect_left
class MedianFinder_py:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.l = [0] * 100
        # self.sum = 0
        self.l = []
        
    def addNum(self, num: int) -> None:
        # self.l[num] += 1
        # self.sum += num
        idx = bisect_left(self.l, num)
        self.l = self.l[:idx] + [num] + self.l[idx:]
        
    def findMedian(self) -> float:
        l = self.l
        n = len(l)
        if n % 2 == 1:
            return l[n//2]
        else:
            return (l[n//2-1] + l[n//2])/2


class MedianFinder_TLE:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        
    def addNum(self, num: int) -> None:
        self.l.append(num)        
        
    def findMedian(self) -> float:
        l = sorted(self.l)
        n = len(l)
        if n % 2 == 1:
            return l[n//2]
        else:
            return (l[n//2-1] + l[n//2])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

