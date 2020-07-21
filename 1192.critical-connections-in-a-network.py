#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (48.66%)
# Likes:    1177
# Dislikes: 82
# Total Accepted:    59.6K
# Total Submissions: 122.7K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # [node for node who has only one nbr]
        if not connections:
            return []
    #     return self.helper(n, connections)
    # def helper(self, n, connections):
        g = defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
        jump = [-1] * n
        """
        starting fr the cur node, explore all the node connecting to this node except for it's parent, and return the minimum value node
        """
        res = []
        self.dfs(0, -1, 0, jump, res, g)
        return res
    
    def dfs(self, v:int, par:int, lvl:int, jump:list, res:list, g) -> int:
        # return minimum steps
        jump[v] = lvl + 1   # distance!
        for child in g[v]:
            if child == par:
                continue
            elif jump[child] == -1:
                jump[v] = min(jump[v], 
                              self.dfs(child, v, lvl+1, jump, res, g)
                             )
            else:
                jump[v] = min(jump[v], jump[child])
            
        if jump[v] == lvl + 1 and v != 0:
            res.append([par, v])
        # print(jump)
        return jump[v]
    
    def failed():
        neighbors = defaultdict(list)
        for connection in connections:
            a, b = connection
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        """ Following cannot solve 2 rings with 1 connection """
        # res = []
        # for k, v in neighbors.items():
        #     if len(v) <= 1:
        #         res.append([k, v[0]])
        
        return res        
# @lc code=end

