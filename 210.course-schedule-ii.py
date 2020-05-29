#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (38.37%)
# Likes:    1898
# Dislikes: 126
# Total Accepted:    241.7K
# Total Submissions: 619K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return self.helper_old(numCourses, prerequisites)
        return self.helper(numCourses, prerequisites)
    
    def helper(self, numCourses, prerequisites):    # cannot handle duplicate inputs
        n = numCourses
        """
        0   -->  1  --> 
            \           \
             --> 2  --> --> 3
        """
        
        in_degree = [0 for j in range(n)]
        outs = [[] for j in range(n)]
        Q = deque()        
            
        for j in range(len(prerequisites)):
            prerequisite = prerequisites[j] 
            in_degree[prerequisite[0]] += 1
            outs[prerequisite[1]].append(prerequisite[0]) # outs[prerequisites[i].start] += prerequisites[i].end
        # print(in_degree, outs)   
        # """ in_degree: [0, 1, 1, 2], 
        #     outs: [[1, 2], [3], [3], []] 
        # """
            
        Q = deque()
        path = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                Q.append(i) # AS START POINTs
                # path.append(i)
                
        # print(path)
        random.shuffle(path)
        while Q:
            len_cur = len(Q)
            for i in range(len_cur):
                cur = Q.popleft()
                path.append(cur)
                random.shuffle(outs[cur])  #    [1,2]
                for nbr in outs[cur]:
                    in_degree[nbr] -= 1
                    # Q.append(nbr)            # shouldn't be here
                    if in_degree[nbr] == 0:    # Discuss: how about set() as used for visited?!
                        Q.append(nbr)
                        # path.append(nbr)
        if len(path) != numCourses: # for cyclic case, e.g. 3, [[1,0],[1,2],[0,1]], path == [2], not the answer
            return []
        return path
        # FOLLOW UP: find all path?!        
# @lc code=end

