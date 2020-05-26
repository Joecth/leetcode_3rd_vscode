#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.73%)
# Likes:    1471
# Dislikes: 172
# Total Accepted:    238.6K
# Total Submissions: 721.7K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # return self.O_NlogN(intervals, newInterval)
        return self.O_N(intervals, newInterval)
    
    def O_N(self, intervals, newInterval):
        # TODO:
        # pass
        if not intervals: return [newInterval]
        if not newInterval: return [intervals]
        
        n = len(intervals)
        
        i = 0
        res = []
        # while newInterval.start > intervals[i].start:
        while i < n and newInterval[0] >= intervals[i][0]:  
                                        # "equals" for [[1,5]], [1,7]
            res.append(intervals[i])
            i += 1
        
        # if newInterval.start > res[-1].end:
        if not res:     # for [[1,5]], [0, 3]
            res.append(newInterval) 
        else:
            if newInterval[0] > res[-1][1]:
                res.append(newInterval)
            else:
                res[-1][1] = max(res[-1][1], newInterval[1])
        
        # print(res)
        for j in range(i, n):
            if intervals[j][0] > res[-1][1]:
                res.append(intervals[j])
            else:
                res[-1][1] = max(res[-1][1], intervals[j][1])
        return res
        
        
        
    def O_NlogN(self, intervals, newInterval):  # same as merge Interval
        intervals.append(newInterval)
        arr = sorted(intervals, key=lambda interval: interval[0])
        res = []
        for i in range(len(arr)):
            if not res or res[-1][1] < arr[i][0]:
                res.append(arr[i])
            else:
                res[-1][1] = max(res[-1][1], arr[i][1])
        return res
        
# @lc code=end

