# 1469. Longest Path On The Tree
# 中文English
# Given a tree consisting of n nodes, n-1 edges. Output the distance between the two nodes with the furthest distance on this tree.
# Given three arrays of size n-1, starts, ends, and lens, indicating that the i-th edge is from starts[i] to ends[i] and the length is lens[i].

# Example
# Example 1:

# Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[1,2,5,6]
# Output：11
# Explanation:
# (3→2→4)the length of this path is `11`,as well as(4→2→3)。
# Example 2:

# Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[5,2,5,6]
# Output：13
# Explanation:
# (1→0→2→4)the length of this path is`13`,as well as(4→2→0→1)。
# Notice
# Return the farthest distance between any two nodes on the tree, not the depth of the tree. Note that the given edges are undirected edge.
# It is guaranteed that the given edges are able to constitute a tree.

# 1 \leq n \leq 1* 10^51≤n≤1∗10
# ​5
# ​​ 
# 1 \leq lens[i] \leq 1* 10^31≤lens[i]≤1∗10
# ​3
# ​​

class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        # Write your code here
        """
        Input： n=5,
        starts= [0,0,2,2],
        ends=   [1,2,3,4],
        lens=   [1,2,5,6]
        
         0 1 2 3 4 5
         (0) --1-- (1)
             \
              --2-- (2)  --5-- (3)
                         \
                          --6-- (4)
        """        
        # return self.mine(n, starts, ends, lens)
        # return self.teacher_RE(n, starts, ends, lens)
        return self.teacher_bfs(n, starts, ends, lens)
        return self.practice(self, starts, ends, lens)
    
    def practice(self, n, starts, ends, lens):
        neighbors = {}
        for i in range(n-1):
            if starts[i] not in neighbors:
                neighbors[starts[i]] = []
            if ends[i] not in neighbors:
                neighbors[ends[i]] = []
        
        for i in range(n-1):
            neighbors[starts[i]].append((ends[i], lens[i]))
            neighbors[ends[i]].append((starts[i], lens[i]))
        
        start, _ = self.bfs_practice(starts[0], neighbors)
        end, answer = self.bfs_practice(start, neighbors)
        return answer
            
    def bfs_practice(self, root, neighbors):
        Q = collections.deque()
        distance_to_root = {}
        
        Q.append(root)
        distance_to_root[root] = 0
        max_dist = 0
        max_node = None
        while Q:
            now = Q.popleft()
            if distance_to_root[now] > max_dist:
                max_dist = distance_to_root[now]
                max_node = now
            for nbr, edge_dist in neighbors[now]:
                if nbr in distance_to_root:
                    continue
                # Q.append((nbr, distance_to_root[now] + edge_dist))
                Q.append(nbr)
                distance_to_root[nbr] = distance_to_root[now] + edge_dist
        return (max_node, max_dist)
                
    
    def teacher_bfs(self, n, starts, ends, lens):
        neighbors = {}
        
        for i in range(n-1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]
            
            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []
            
            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))
        
        # return 離root最遠的點，該點離root的距離
        start, _ = self.bfs(0, neighbors)   # 從任意點開始
        # print(start)
        end, answer = self.bfs(start, neighbors)
        # print(end, answer)
        return answer
        
    def bfs(self, root, neighbors):
        Q = collections.deque()
        distance_to_root = {}
        
        Q.append(root)
        distance_to_root[root] = 0
        maximum_distance = 0
        maximum_node = -1
        
        while Q:
            now = Q.popleft()
            if maximum_distance < distance_to_root[now]:
                maximum_distance = distance_to_root[now]
                maximum_node = now
            
            for neighbor, edge_length in neighbors[now]:
                if neighbor in distance_to_root:
                    continue
                
                Q.append(neighbor)
                distance_to_root[neighbor] = distance_to_root[now] + edge_length
        
        return (maximum_node, maximum_distance)
        
        
    # 爆棧了。。RecursionError
    def teacher_RE(self, n, starts, ends, lens):
        # 不能快速找到neighbor
        # 建圖
        neighbors = {}
        for i in range(n-1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]
            
            # Build graph
            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []
            
            # 為何雙向邊
            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))
        
        # root, parent, neighbors, 
        # return maximum_chain, maximum_path
        chain, path = self.dfs(0, -1, neighbors)
                             # 這邊這個0換成什麼都可以, 代表從哪個開始只要在0~n-1都可以
        return path
    
    # 爆棧了。。RecursionError: maximum recursion depth exceeded in comparison
    def dfs(self, root, parent, neighbors):
        longest_chain = 0
        longest_path = 0
        
        child_longest_chain = 0
        child_second_longest_chain = 0
        
        for neighbor, dist in neighbors[root]:
            if neighbor == parent:
                continue
            
            child_chain, child_path = self.dfs(neighbor, root, neighbors)
            child_chain += dist
            
            longest_path = max(child_path, longest_path)
            longest_chain = max(longest_chain, child_chain)
            
            _, child_second_longest_chain, child_longest_chain = \
            sorted([child_longest_chain, child_second_longest_chain, child_chain])
            # sorted([child_longest_chain, child_second_longest_chain, longest_chain])
            
        longest_path = max(child_longest_chain + child_second_longest_chain, longest_path)
        # print(root, longest_chain, longest_path)
        return [longest_chain, longest_path]
        
    def mine(self, n, starts, ends, lens):
        # 0. collect all nodes
        # 1. build graph for topological sort
        # 2. trvs
        
        # 0. 
        all_nodes = set()
        for node in starts:
            all_nodes.add(node)
        for node in ends:
            all_nodes.add(node)
        
        # 1.
        in_degrees = {}
        out_edges = {}
        for node in all_nodes:
            in_degrees[node] = 0
            out_edges[node] = set()
            
        for i in range(len(starts)):
            # in_degrees[ends[i]] += 1
            in_degrees[ends[i]] += lens[i]
            out_edges[starts[i]].add(ends[i])
        # print(in_degrees, out_edges)
        
        # Q = collections.deque()
        S = []
        for k in in_degrees:
            if in_degrees[k] == 0:
                S.append(k)

        max_len = 0
        return self.dfs_mine_failed(S[0], in_degrees, out_edges, lens)[0]
        
    # can only pass first case
    def dfs_mine_failed(self, node, in_degrees, out_edges, lens):
        if out_edges[node] == 0:
            return [0, 0]
        now_node = node
        max_dia = 0
        # prev_max_dia = 0
        max_chain = 0
        prev_max_chain = 0
        for next_node in out_edges[now_node]:
            
            # out_edges[now_node].remove(next_node)
            # if not out_edges[next_node]:
            #     return [max_dia, max_chain]
                
            # S.append(next_node)
            nbr_dia, nbr_chain = self.dfs_mine_failed(next_node, in_degrees, out_edges, lens)
            max_dia = max(max_dia, nbr_chain + prev_max_chain)
            prev_max_chain = nbr_chain
            # max_chain = max(max_chain, nbr_chain) + 1
            max_chain = max(max_chain, nbr_chain) + in_degrees[next_node]
        print( [max_dia, max_chain])
        return [max_dia, max_chain]