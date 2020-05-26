#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (38.18%)
# Likes:    3809
# Dislikes: 270
# Total Accepted:    563.6K
# Total Submissions: 1.5M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
  *---*
 cur_i cur_j
    *-------*
    tmp_i   cur_j
                   *---*
               tmp_i   tmp_j
                                    *--------*
start i to end j
push (i,j) into priority que, so that the min-heap use i as key
    
while min-heap:
    pop the (i, j) pair and if curr j > than next i of pop() from min-heap, keep poping()
    if j <= next i:
        count += 1
'''
import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        # return self.helper(intervals)
        return self.helper2(intervals)
    
    def helper2(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            print(res)
        return res
        
    
    def helper(self, intervals):
        if not intervals:
            return intervals
        result = []
        intervals_s = sorted(intervals, key=lambda x: x[0])
        prev_start, prev_end = intervals_s[0][0], intervals_s[0][1]
        for i in range(1, len(intervals)):
            # cur_end_time 
            if intervals_s[i][0] <= prev_end:
                prev_end = max(prev_end, intervals_s[i][1])
                # result.append([prev_start, intervals_s[i][1]])
            else:   # not able to merge
                result.append([prev_start, prev_end])
                prev_start = intervals_s[i][0]
                prev_end = intervals_s[i][1]
        result.append([prev_start, prev_end])
        
        return result
            
# @lc code=end

