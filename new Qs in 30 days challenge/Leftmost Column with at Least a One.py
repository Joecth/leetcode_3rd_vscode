# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        mat = binaryMatrix
        
        ans = float('inf')
        n, m = mat.dimensions()
        for i in range(n):
            lo = self.b_left(i, m, mat)
            if lo != m: # "lo==m" means NOT FOUND 
                ans = min(lo, ans)
            
        return ans if ans != float('inf') else -1
    
    def b_left(self, row, col_len, mat):
        lo, hi = 0, col_len
        
        while lo < hi:
            mid = (lo+hi) >> 1
            if mat.get(row, mid) == 1:
                hi = mid
            else:
                lo = mid + 1
        return lo