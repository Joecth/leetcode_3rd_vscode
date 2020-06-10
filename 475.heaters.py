#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (32.65%)
# Likes:    688
# Dislikes: 778
# Total Accepted:    63.2K
# Total Submissions: 192K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        return self.house_oriented(houses, heaters)
        return self.heaters_oriented(houses, heaters)

    def heaters_oriented(self, houses, heaters):
        min_r = max(
                    abs(houses[0] - heaters[-1]),
                    abs(houses[-1] - heaters[-1])
                )
        start, end = 0, min_r
        start, end = 0, 10**9
        
        while start+1 < end:
            mid = start + (end - start)//2
            if self.is_valid_radius(mid, houses, heaters):
                end = mid
            else:
                start = mid
        
        if self.is_valid_radius(start, houses, heaters):
            return start
        return end

    def is_valid_radius(self, r, houses, heaters):
        n, m = len(houses), len(heaters)
        now_heater = 0
        for house_pos in houses:
            while now_heater != m and abs(house_pos - heaters[now_heater]) > r:
                now_heater += 1
            if now_heater == m:
                return False
        return True    
    
    def is_valid_radius_my_TLE(self, r, houses, heaters):
        for house in houses:
            not_ok = 0
            for heater in heaters:
                if abs(house - heater) <= r:
                    break
                else:
                    not_ok += 1
                    
                if not_ok == len(heaters):
                    return False
        return True
        
    
    
        
    def house_oriented(self, houses, heaters):
        
        # min_r = sys.maxsize
        min_r = -sys.maxsize
        for house in houses:
            cur_r = self.get_min_radius(house, heaters)
            min_r = max(min_r, cur_r)
        
        return min_r
    
    def get_min_radius(self, house, heaters):
        start, end = 0, len(heaters)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if heaters[mid] > house:
                end = mid
            else:
                start = mid
            
        if abs(heaters[start] - house) <= abs(heaters[end] - house):
            return abs(heaters[start] - house)
        return abs(heaters[end] - house)
            
        
# @lc code=end

