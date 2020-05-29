#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (41.10%)
# Likes:    3418
# Dislikes: 168
# Total Accepted:    374.1K
# Total Submissions: 894.2K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 1 <= numCourses <= 10^5
# 
# 
#

# @lc code=start
# exmample: 4, [[1,0],[2,0],[3,1],[3,2]]
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.helper_old(numCourses, prerequisites)
        return self.helper(numCourses, prerequisites)
    
    def helper(self, numCourses, prerequisites):
        n = numCourses
        in_degree = [0 for i in range(n)]
        outs = [[] for j in range(n)]
        
        for i in range(len(prerequisites)):
            prereq = prerequisites[i]
            in_degree[prereq[0]] += 1   # in_degree[prereq.end] += 1
            outs[prereq[1]].append(prereq[0])   # outs[prereq.start].append(prereq.end)
        # print(in_degree, outs)
        
        Q = deque()
        path = []
        for i in range(n):
            if in_degree[i] == 0:
                Q.append(i)
                # path.append(i)
        
        while Q:
            len_cur = len(Q)
            for i in range(len_cur):
                cur = Q.popleft()
                path.append(cur)
                for nbr in outs[cur]:
                    in_degree[nbr] -= 1
                    if in_degree[nbr] == 0:
                        Q.append(nbr)
                        # path.append(nbr)
        
        # print(len(path))    # 
        return len(path) == numCourses
                    
        
    def helper_old(self, numCourses, prerequisites):
        n = numCourses
        G = [[] for i in range(n)]
        degrees = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degrees[j] += 1    
    
        '''
        0 -> 1 ------> 3
          \        /
            -> 2 --
            idx    0 1 2 3
        degrees = [0 1 1 2]
        G = [[1,2], [3], [3], []]
        
        Q = [0]
            idx
        ''' 
        Q = deque([])
        [Q.append(idx) for idx, degree in enumerate(degrees) if degree == 0]        
        visited = []
        # result = [] # as a stack
        # [result.append(idx) for idx in Q]     # [0], result = Q.copy()
        while Q:
            v_idx = Q.popleft()    
            # visited.append[v_idx]
            for j in range(len(G[v_idx])):
                next_v_idx = G[v_idx][j] # 1, then 2
                degrees[next_v_idx] -= 1
                if degrees[next_v_idx] == 0:
                    Q.append(next_v_idx)
                    # result.append(next_v_idx)
        # return len(result) == numCourses
        # 3
        # [[1,0],[1,2],[0,1]]  should be False!
        
        return not any(degrees) # check whether any element in degrees is larger than 0              
# @lc code=end

