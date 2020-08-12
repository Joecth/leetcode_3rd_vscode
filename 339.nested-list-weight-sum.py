#
# @lc app=leetcode id=339 lang=python3
#
# [339] Nested List Weight Sum
#
# https://leetcode.com/problems/nested-list-weight-sum/description/
#
# algorithms
# Easy (73.57%)
# Likes:    569
# Dislikes: 140
# Total Accepted:    93.1K
# Total Submissions: 125.9K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, return the sum of all integers in the list
# weighted by their depth.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: 10 
# Explanation: Four 1's at depth 2, one 2 at depth 1.
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: 27 
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 +
# 4*2 + 6*3 = 27.
# 
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
[[1,1],2,[1,1]]
  
"""
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # res = [0]
        # self.helper(nestedList, 0, res)
        # return res[0]
        
        return self.dfs_WRONG(nestedList, 1)  # also OK!
        """ 
        [obj1, obj2, obj3, obj4, ....]
            V.S.
        [[1,1],2,[1,1]]
        """
    
        n = len(nestedList)
        if n == 0: 
            return 0
        res = 0
        for i in range(n):
            if nestedList[i].isInteger():
                res += nestedList[i].getInteger() * 1
            else:
                res += self.dfs_WRONG(nestedList[i].getList(), 1+1)
        return res
        # Try Iterative solution!
        # TODO: DISCUSS BFS sol
    
    def dfs_WRONG(self, arr, depth):
        # if idx == len(arr):
        #     return 0
        
        level_sum = 0
        for i in range(len(arr)):
            if arr[i].isInteger():
                level_sum += arr[i].getInteger() * depth
            else:
                level_sum += self.dfs_WRONG(arr[i].getList(), depth+1)
        return level_sum

            
        
        
# @lc code=end

