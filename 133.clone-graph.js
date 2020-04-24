/*
 * @lc app=leetcode id=133 lang=javascript
 *
 * [133] Clone Graph
 *
 * https://leetcode.com/problems/clone-graph/description/
 *
 * algorithms
 * Medium (32.07%)
 * Likes:    1443
 * Dislikes: 1261
 * Total Accepted:    306.1K
 * Total Submissions: 941.9K
 * Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
 *
 * Given a reference of a node in a connected undirected graph.
 * 
 * Return a deep copy (clone) of the graph.
 * 
 * Each node in the graph contains a val (int) and a list (List[Node]) of its
 * neighbors.
 * 
 * 
 * class Node {
 * ⁠   public int val;
 * ⁠   public List<Node> neighbors;
 * }
 * 
 * 
 * 
 * 
 * Test case format:
 * 
 * For simplicity sake, each node's value is the same as the node's index
 * (1-indexed). For example, the first node with val = 1, the second node with
 * val = 2, and so on. The graph is represented in the test case using an
 * adjacency list.
 * 
 * Adjacency list is a collection of unordered lists used to represent a finite
 * graph. Each list describes the set of neighbors of a node in the graph.
 * 
 * The given node will always be the first node with val = 1. You must return
 * the copy of the given node as a reference to the cloned graph.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
 * Output: [[2,4],[1,3],[2,4],[1,3]]
 * Explanation: There are 4 nodes in the graph.
 * 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val =
 * 4).
 * 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val =
 * 3).
 * 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val =
 * 4).
 * 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
 * 3).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: adjList = [[]]
 * Output: [[]]
 * Explanation: Note that the input contains one empty list. The graph consists
 * of only one node with val = 1 and it does not have any neighbors.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: adjList = []
 * Output: []
 * Explanation: This an empty graph, it does not have any nodes.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: adjList = [[2],[1]]
 * Output: [[2],[1]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= Node.val <= 100
 * Node.val is unique for each node.
 * Number of Nodes will not exceed 100.
 * There is no repeated edges and no self-loops in the graph.
 * The Graph is connected and all nodes can be visited starting from the given
 * node.
 * 
 * 
 */

// @lc code=start
/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    if (null == node) return node;
    return bfs(node);

    function bfs(node){
        let Q = [];
        Q.push(node);
        let node_N = new Node(node.val);
        let visited = {};
        visited[node.val] = node_N;

        while (Q.length != 0){
            let cur_O = Q.shift();
            for (let i=0; i < cur_O.neighbors.length; i++){
                let nbr_O = cur_O.neighbors[i];
                // console.log(cur_O.neighbors[i].val);
                if (!(nbr_O.val in visited)){
                    let nbr_N = new Node(nbr_O.val);
                    // console.log("INININ", nbr_N.val);
                    visited[nbr_O.val] = nbr_N;
                    Q.push(nbr_O);
                }            
                visited[cur_O.val].neighbors.push(visited[nbr_O.val]);
            }
        }

        return node_N;
    }
};

// @lc code=end

