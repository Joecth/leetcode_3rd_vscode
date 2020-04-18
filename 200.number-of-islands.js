/*
 * @lc app=leetcode id=200 lang=javascript
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (45.10%)
 * Likes:    4620
 * Dislikes: 173
 * Total Accepted:    609.1K
 * Total Submissions: 1.3M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges of
 * the grid are all surrounded by water.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * Output: 3
 * 
 */

// @lc code=start
/**
 * @param {character[][]} grid
 * @return {number}
 */
/* Different from other langs:
    for [], 
    unshift: insert from head
    shift: pop_left()
    ref: https://medium.com/@realdennis/%E4%BD%A0%E5%85%B6%E5%AF%A6%E4%B8%8D%E7%94%A8%E5%9C%A8-javascript-%E5%AF%A6%E4%BD%9C%E4%B8%80%E5%80%8B-queue-b4e788e23bc7
*/
var numIslands = function(grid) {
    if (!grid.length || !grid[0].length) return 0;
    let count = 0;
    for (let i=0; i<grid.length; i++){
        for (let j=0; j<grid[0].length; j++){
            if (grid[i][j] == '1'){
                helper(i, j, grid);
                count += 1
            }
        }
    }
    return count;
    
    function helper(r, c, grid){
        // let Q = deque();
        let dr = [-1, 0, 1, 0];
        let dc = [0, 1, 0, -1];
        let Q = [[r,c]];
        // let Q = new TinyQueue();
        
        while (Q.length != 0){
            // let I, J = Q.pop_front();
            let v = Q.shift(); 
            let I = v[0];
            let J = v[1];
            for (let idx=0; idx<4; idx++){
                let i = I + dr[idx];
                let j = J + dc[idx];
                
                if (i<0 || j<0 || i>grid.length-1 || j>grid[0].length-1 || grid[i][j]!='1'){
                    continue;
                }
                Q.push([i, j]);
                grid[i][j] = 'X';
            }
        }
    }
};
// @lc code=end

