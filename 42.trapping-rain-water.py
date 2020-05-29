#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.17%)
# Likes:    6553
# Dislikes: 114
# Total Accepted:    486.3K
# Total Submissions: 1M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        return self.dp_sol(height)
        return self.two_ptr(height) 
        # return self.mono_stack(height)
    
    def mono_stack(self, height):
        n = len(height)
        S = []
        res = 0
        for r in range(n):
            left = r
            while S and height[r] > height[S[-1]]: # height[i] is R_h
                valley_h = height[S.pop()]
                if not S: 
                    break
                nbr_h = min(height[S[-1]], height[r]) # OOR if height[0] < height[1], since no more elem in S
                        # min(L_h, R_h)
                res += (r-1-S[-1]) * (nbr_h - valley_h)
                left -= 1
            S.append(r)
        return res
    
    def two_ptr(self, height):
        l, r = 0, len(height)-1
        l_max, r_max = 0, 0
        count = 0
        while l < r:
            # if height[l] < height[r]:     # This should behind updates of l and r, or FAILED in VALLEY as [2 0 2]
            #     l += 1
            # else:
            #     r -= 1                
            if height[l] >= l_max:
                l_max = height[l]
            else:
                cur = max(min(l_max, r_max) * 1 - height[l], 0)
                count += cur
                # l += 1
            if height[r] >= r_max:
                r_max = height[r]
            else:
                cur = max(min(l_max, r_max) * 1 - height[r], 0)
                count += cur
                # r -= 1
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return count
        
    def dp_sol(self, height):   # max rectangle
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # l_max =  [0 0 1 1 2 2 2 2 3 3 3 3]
        # r_max =  [3 3 3 3 3 3 3 2 2 2 1 0]
        # min_nbr = min(l_max[i], r_max[i])
        # water[i] = height[i] < min_nbr ? (min_nbr-height[i]) * 1:0
        # return sum(water)        
        
        n = len(height)
        # l_max = [0] * n
        # cur_max = 0
        # for i in range(n):
        #     l_max[i] = cur_max
        #     cur_max = max(height[i], cur_max)
        """ DP also OK """
        l_max = [0] * n
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i])
            
        # r_max = [0] * n
        # cur_max = 0
        # for j in reversed(range(n)):
        #     r_max[j] = cur_max
        #     cur_max = max(height[j], cur_max)
        r_max = [0] * n
        r_max[n-1] = height[n-1]
        for i in reversed(range(0, n-1)):
            r_max[i] = max(r_max[i+1], height[i])
        
        res = 0
        for k in range(n):
            min_nbr = min(l_max[k], r_max[k])
            res += (min_nbr-height[k])*1 if height[k] < min_nbr else 0
            
        return res
# @lc code=end

