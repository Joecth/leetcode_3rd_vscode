#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        start, end = 0, num
        while start+1 < end:
            mid = start + (end-start)//2
            tmp = mid*mid
            if tmp == num:
                return True
            elif tmp > num:
                end = mid
            else:
                start = mid    
        return False

    def isPerfectSquare_old(self, num: int) -> bool:
        if num < 2:
            return True
        return self.helper(num)
        
        
    def helper(self, num):
        lo, hi = 0, num
        while lo < hi:
        # while lo <= hi:
            mid = lo + ((hi-lo)>>1)
            # print(lo, hi, mid)
            tmp = mid*mid
            if tmp <= num < (mid+1)*(mid+1):
                return tmp == num
            elif tmp > num:
                hi = mid
            else:# tmp < num:
                lo = mid+1
            # else:
            #     assert(0)
        return False
                        
# @lc code=end

