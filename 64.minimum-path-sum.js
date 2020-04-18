/*
 * @lc app=leetcode id=64 lang=javascript
 *
 * [64] Minimum Path Sum
 *
 * https://leetcode.com/problems/minimum-path-sum/description/
 *
 * algorithms
 * Medium (51.32%)
 * Likes:    2389
 * Dislikes: 52
 * Total Accepted:    340.6K
 * Total Submissions: 655.4K
 * Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
 *
 * Given a m x n grid filled with non-negative numbers, find a path from top
 * left to bottom right which minimizes the sum of all numbers along its path.
 * 
 * Note: You can only move either down or right at any point in time.
 * 
 * Example:
 * 
 * 
 * Input:
 * [
 * [1,3,1],
 * ⁠ [1,5,1],
 * ⁠ [4,2,1]
 * ]
 * Output: 7
 * Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
/*
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
 0 0 0.          0
 0 1 4           5
 0 2 min(2,4)+5  min(7,5)+1
 0 6 min(6,7)+2  min(8,6)+1

*/
var minPathSum = function(grid) {
    if ((grid.lenght == 0) || grid[0].length == 0) return 0;
    let dp = [];
    // Init dp
    for (let i=0; i<grid.length+1; i++){
        dp.push([]);
        for (let j=0; j<grid[0].length+1; j++){
            dp[i].push(0);
        }
    }

    for (let i=1; i<dp.length; i++){
        for (let j=1; j<dp[0].length; j++){
            if (i==1)
                dp[i][j] = dp[i][j-1] + grid[i-1][j-1];
            else if (j==1)
                dp[i][j] = dp[i-1][j] + grid[i-1][j-1];
            else
                dp[i][j] = Math.min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1];
        }   
    }

    return dp[dp.length-1][dp[0].length-1];
};
// @lc code=end

