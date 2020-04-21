/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int ans = 101;
        for (int i=0; i<dim[0]; i++){
            int lo = b_left(binaryMatrix, i, dim[1]);
            if (lo != dim[1])
                ans = min(ans, lo);
        }
        
        if (ans == 101) return -1;
        return ans;
    }
    
    int b_left(BinaryMatrix &mat, int row, int col_len){
        int lo = 0;
        int hi = col_len;
        while (lo<hi){
            int mid = (lo+hi)>>1;
            if (mat.get(row, mid) == 1)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};