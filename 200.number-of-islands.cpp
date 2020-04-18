/*
 * @lc app=leetcode id=200 lang=cpp
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
#include<vector>
#include <deque> 

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (!grid.size() || !grid[0].size()) return 0;
        int count = 0;
        for (int i=0; i < grid.size(); i++){
            for (int j=0; j < grid[0].size(); j++){
                if (grid[i][j] == '1'){
                    helper(i, j, grid);
                    count += 1;
                }
            }
        }
        return count;
    }

    void helper(int r, int  c, vector<vector<char>>& grid){
        deque<vector<int>> Q;
        vector<int> v;
        v.push_back(r); v.push_back(c);
        Q.push_back(v);
        
        int dr[] = {-1, 0, 1, 0};
        int dc[] = {0, 1, 0, -1}; 
        
        while (Q.size() != 0){
            v = Q.front(); Q.pop_front();
            int I, J;
            I = v.front(); J = v.back();

            for (int idx=0; idx < 4; idx++){
                int i = I + dr[idx];
                int j = J + dc[idx];
                if (i<0 || j<0 || i>grid.size()-1 || j>grid[0].size()-1 || grid[i][j] != '1'){
                    continue;
                }
                vector<int> v;
                v.push_back(i); v.push_back(j);
                Q.push_back(v);
                grid[i][j] = 'X';
            }
        }
    }
};

/* BETTER DS:
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = m ? grid[0].size() : 0, islands = 0, offsets[] = {0, 1, 0, -1, 0};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    islands++;
                    grid[i][j] = '0';
                    queue<pair<int, int>> todo;
                    todo.push({i, j});
                    while (!todo.empty()) {
                        pair<int, int> p = todo.front();
                        todo.pop();
                        for (int k = 0; k < 4; k++) {
                            int r = p.first + offsets[k], c = p.second + offsets[k + 1];
                            if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == '1') {
                                grid[r][c] = '0';
                                todo.push({r, c});
                            }
                        }
                    }
                }
            }
        }
        return islands;
    }
};

*/
// @lc code=end

