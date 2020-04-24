#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (32.07%)
# Likes:    1443
# Dislikes: 1261
# Total Accepted:    306.1K
# Total Submissions: 941.9K
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 
# Test case format:
# 
# For simplicity sake, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val = 1, the second node with
# val = 2, and so on. The graph is represented in the test case using an
# adjacency list.
# 
# Adjacency list is a collection of unordered lists used to represent a finite
# graph. Each list describes the set of neighbors of a node in the graph.
# 
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
# 
# 
# Example 1:
# 
# 
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
# 
# 
# Example 2:
# 
# 
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
# 
# 
# Example 3:
# 
# 
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# 
# 
# Example 4:
# 
# 
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque, OrderedDict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return node
        self.visited = {}
        return self.helper(node)
        # return self.dfs(node)
    
    def dfs(self, root):
        if root not in self.visited:
            root_N = Node(root.val)
            
            self.visited[root] = root_N
    
    def helper(self, root):
        Q = deque()
        Q.append(root)
        
        root_N = Node(root.val)
        visited = {root : root_N} 
        
        while Q:
            node = Q.popleft()
            for nbr_O in node.neighbors: 
                """
                if nbr_O not in visited:
                    # For NEW
                    clone_N = Node(nbr_O.val)
                    visited[node].neighbors.append(clone_N)
                    
                    # For OLD
                    Q.append(nbr_O)
                    visited[nbr_O] = clone_N
                else:   # the clone_N already created before
                    visited[node].neighbors.append(visited[nbr_O])
                """                    
                
                if nbr_O not in visited:
                    nbr_N = Node(nbr_O.val)
                    visited[nbr_O] = nbr_N
                    Q.append(nbr_O)
                visited[node].neighbors.append(visited[nbr_O])
        return root_N        
# @lc code=end

