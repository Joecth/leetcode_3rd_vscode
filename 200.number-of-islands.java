/*
 * @lc app=leetcode id=200 lang=java
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
class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length==0 || grid[0].length==0) return 0;
        int count = 0;
        for (int i=0; i<grid.length; i++){
            for (int j=0; j<grid[0].length; j++){
                if (grid[i][j] == '1'){
                    helper(i, j, grid);
                    count += 1;
                }
            }
        }
        return count;
    }
    
    private void helper(int r, int c, char[][] grid){
        if (r<0 || c<0 || r>grid.length-1 || c>grid[0].length-1 || grid[r][c]!='1')
            return;
        grid[r][c] = 'X';
        helper(r-1, c, grid);
        helper(r+1, c, grid);
        helper(r, c-1, grid);
        helper(r, c+1, grid);
    }
}

/**
 * Nice BFS in Java without using CONTAINER:
 * class Solution {
    public int numIslands(char[][] grid) {
        Queue<Integer> queue = new LinkedList<Integer>(); 
        int result =0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1'){
                    grid[i][j] = '0';
                    int code = i*grid[0].length+j;
                    queue.add(code);
                    result += bfs(grid,queue);
                }
            }
        }
        
        return result;
    }
    
    public int bfs(char[][] grid,Queue<Integer> queue){
        int[] dr = {-1,0,1,0};
        int[] dk = {0,-1,0,1};
        
        while(!queue.isEmpty()){
            int code = queue.poll();
            int r=code/grid[0].length;
            int c=code%grid[0].length;
            
            for(int i=0;i<=3;i++){
                int nr = r + dr[i];
                int nc = c + dk[i];
                if(nr>=0 && nr<grid.length && nc>=0 && nc<grid[0].length && grid[nr][nc]=='1'){
                    int ncode = nr*grid[0].length+nc;
                    grid[nr][nc] = '0';
                    queue.add(ncode);
                }
            }
        }
        
        return 1;
    }
}
 */

// @lc code=end

