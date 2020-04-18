/*
 * @lc app=leetcode id=64 lang=java
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
/*
Java Equivalent to C++ std::vector
The nearly exact Java equivalent to the C++ std::vector collection is the Java ArrayList collection.
C++	
#include <vector>

virtual void Vector()
{
    std::vector<int> myList;
    myList.push_back(1);
    int i = 1;
    myList[0] = i;
    i = myList[0];
}	void Vector()

JAVA
{
    java.util.ArrayList<Integer> myList = new java.util.ArrayList<Integer>();
    myList.add(1);
    int i = 1;
    myList.set(0, i);
    i = myList.get(0);
}

要記得加 new 關鍵字
    int[][] dp = new int[grid.length+1][grid[0].length+1];
*/
class Solution {
    public int minPathSum(int[][] grid) {
        if (grid.length == 0  || grid[0].length == 0) return 0;
        // ArrayList<ArrayList<Integer>> dp = new ArrayList<ArrayList<Integer>>();
        int[][] dp = new int[grid.length+1][grid[0].length+1];
        for (int i=0; i < grid.length + 1; i++){
            for (int j=0; j < grid[0].length + 1; j++){
                // dp.get(i).set(j, 0
                dp[i][j] = 0;
            }
        }

        for (int i=1; i<dp.length; i++){
            for (int j=1; j<dp[0].length; j++){
                int val = grid[i-1][j-1];
                if (i==1)
                    dp[i][j] = dp[i][j-1] + val;
                else if (j==1)
                    dp[i][j] = dp[i-1][j] + val;
                else
                    dp[i][j] = Math.min(dp[i][j-1], dp[i-1][j]) + val;
            }
        }

        return dp[dp.length-1][dp[0].length-1];
        // return 0;
    }
}
// @lc code=end

