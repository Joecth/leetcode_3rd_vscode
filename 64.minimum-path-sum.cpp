/*
 * @lc app=leetcode id=64 lang=cpp
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
// @lc code=start
#include<vector>
#include<cmath>
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if ((grid.size()==0) || (grid[0].size()==0)) return 0;
        vector<vector<int>> dp;
        for (int i=0; i<grid.size()+1; i++){
            vector<int> tmp;
            dp.push_back(tmp);
            for (int j=0; j<grid[0].size()+1; j++){
                dp[i].push_back(0);
                // cout << i << " " << j << " " << dp[i][j];
            }
        }


        for (int i=1; i<dp.size(); i++){
            for (int j=1; j<dp[0].size(); j++){
                int val = grid[i-1][j-1];
                if (i==1)
                    dp[i][j] = dp[i][j-1] + val;
                else if (j==1)
                    dp[i][j] = dp[i-1][j] + val;
                else
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + val;
            }
        }
        // return 0;
        return dp[dp.size()-1][dp[0].size()-1];
    }
};
// @lc code=end

