# 291. Second Diameter
# 中文English
# Given a tree consisting of n nodes, n-1 edges. Output the second diameter of a tree, namely, the second largest value of distance between pairs of nodes.
# Given an array edge of size (n-1) \times 3(n−1)×3, and edge[i][0], edge[i][1] and edge[i][2] indicate that the i-th undirected edge is from edge[i][0] to edge[i][1] and the length is edge[i][2].

# Example
# Input:[[0,1,4],[0,2,7]]
# Output:7
# Explanation: The second largest value of distance is 7 between node 0 and node 2.

# Clarification
# If there are more than one max distance, you just need to return the max distance

# Notice
# 2 \leq n \leq 10^52≤n≤10
# ​5
# ​​ 

# 1 \leq edge[i][2] \leq 10^51≤edge[i][2]≤10
# ​5
# ​​ 

# Using DFS(Depth-First-Search) is easy to cause stack overflow, so please use BFS(Breadth First Search) to finish the task.
class Solution:
    """
    @param edge: edge[i][0] [1] [2]  start point,end point,value
    @return: return the second diameter length of the tree
    """
    def getSecondDiameter(self, edge):
        # write your code here
        neighbors = {}
        m = len(edge)   # m = n-1
        for i in range(m):
            if edge[i][0] not in neighbors:
                neighbors[edge[i][0]] = []
            if edge[i][1] not in neighbors:
                neighbors[edge[i][1]] = []
                
        for i in range(m):
            start, end, dist = edge[i]
            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))
        
        # start, _ = self.bfs(0, neighbors)
        start, _ = self.bfs(edge[0][0], neighbors, None)
        end, max_dist = self.bfs(start, neighbors, None)
        _, dist_no_start = self.bfs(end, neighbors, start)
        _, dist_no_end = self.bfs(start, neighbors, end)
        return max(dist_no_start,dist_no_end)
        
    def bfs(self, root, neighbors, ban_node):
        Q = collections.deque()
        Q.append(root)
        distance_to_root = {}
        distance_to_root[root] = 0
        max_node, max_dist = None, 0
        while Q:
            now = Q.popleft()
            if distance_to_root[now] > max_dist:
                max_node = now
                max_dist = distance_to_root[now]
            for nbr, edge_len in neighbors[now]:
                if nbr == ban_node:
                    continue
                if nbr in distance_to_root:
                    continue
                Q.append(nbr)
                distance_to_root[nbr] = distance_to_root[now] + edge_len
        return max_node, max_dist
        