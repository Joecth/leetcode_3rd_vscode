/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int x, int y) {}
 *     public List<Integer> dimensions {}
 * };
 */

class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> dim = binaryMatrix.dimensions();
        int ans = 101;
        // System.out.println(dim.get(0));
        // System.out.println(dim.get(1));
        // System.out.println("START");
        for (int i=0; i<dim.get(0); i++){
            int lo = b_left(binaryMatrix, i, dim.get(1));
            System.out.println(lo);
            if (lo != dim.get(1))
                ans = Math.min(ans, lo);
        }
        
        if (ans == 101) return -1;
        return ans;
    }
    
    private int b_left(BinaryMatrix mat, int row, int col_len){
        int lo = 0;
        int hi = col_len;
        while (lo < hi){
            int mid = (lo+hi)>>1;
            if (mat.get(row, mid)==1)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
}