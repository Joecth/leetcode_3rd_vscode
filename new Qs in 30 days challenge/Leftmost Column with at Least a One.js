/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * function BinaryMatrix() {
 *     @param {integer} x, y
 *     @return {integer}
 *     this.get = function(x, y) {
 *         ...
 *     };
 *
 *     @return {[integer, integer]}
 *     this.dimensions = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {BinaryMatrix} binaryMatrix
 * @return {number}
 */
var leftMostColumnWithOne = function(binaryMatrix) {
    
    let [n, m] = binaryMatrix.dimensions();
    let ans = 101
    for (let i=0; i<n; i++){
        let lo = b_left(binaryMatrix, i, m);
        if (lo != m)
            ans = Math.min(ans, lo);
    }
    
    if (ans == 101) return -1; 
    return ans;
    
    function b_left(mat, row, col_len){
        let l = 0;
        let r = col_len;
        while (l < r){
            let mid = (l+r)>>1;
            if (mat.get(row, mid) == 1)
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
};