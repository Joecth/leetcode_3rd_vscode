#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (40.15%)
# Likes:    841
# Dislikes: 21
# Total Accepted:    76.8K
# Total Submissions: 191.4K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col)
# into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
# 
# Example:
# 
# 
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# 
# 
# Explanation:
# 
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
# 
# 
# 0 0 0
# 0 0 0
# 0 0 0
# 
# 
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 
# 
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 
# 
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# 
# 
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# 
# 
# Follow up:
# 
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
# 
#

# @lc code=start
class UF_w_rank(object):
    def __init__(self, n):
        self._parents = [idx for idx in range(n+1)]
        self._rank = [1 for idx in range(n+1)]
    def find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        # self._parents[pv] = pu
        # return True
        if self._rank[u] > self._rank[v]:
            self._parents[pv] = pu
        elif self._rank[u] < self._rank[v]:
            self._parents[pu] = pv
        else:
            self._parents[pv] = pu
            self._rank[pu] += 1
            self._rank[pv] += 1
        return True
    
class UF(object):
    def __init__(self, n):
        self._parents = [idx for idx in range(n+1)]
        # self._rank
    def find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self._parents[pv] = pu
        return True
        
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        m, n = len(words1), len(words2)
        if m != n or not pairs:
            return False
        uf = UF(len(pairs) * 2)
        # d = collections.defaultdict(int)
        d = {}
        for w1, w2 in pairs:
            # w1--> u
            # w2--> v
            # if w1 not in d:
            #     d[w1] = len(d)
            u = d[w1] = d.get(w1, len(d))
            v = d[w2] = d.get(w2, len(d))
            # print(w1,u,w2,v)
            uf.union(u, v)
            
        for i in range(m):
            w1, w2 = words1[i], words2[i]
            if w1 == w2:    # may both not in d, but are same
                continue
            # w1--> u
            # w2--> v
            if w1 not in d or w2 not in d:
                return False
            u, v = d[w1], d[w2]
            if uf.find(u) != uf.find(v):
                return False
        return True
        
        
    def BF():       # Not finished yet
        m, n = len(words1), len(words2)
        if m != n or not pairs:
            return False
        d = collections.defaultdict(set)
        for u, v in range(pairs):
            d[u].add(v)
            d[v].add(u)
            
        for i in range(m):
            if not self.is_similar(words1[i], words2[i], d):
                return False
        return True
    
    def is_similar(self, w1, w2, d):
        if w1 not in d and w2 not in d:
            return False
        if w1 in d:
            return self.is_similar( w2)
            # ==> many expansion!
        if w2 in d and w1 in d[w2]:
            return True
        
        
                
# @lc code=end

