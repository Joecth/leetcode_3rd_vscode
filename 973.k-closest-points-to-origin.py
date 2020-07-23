#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (63.60%)
# Likes:    1862
# Dislikes: 114
# Total Accepted:    297.3K
# Total Submissions: 466.9K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
import math
import heapq
from collections import deque 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # return self.helper_heap_KlgK(points, K)
        # return self.helper_Q_select(points, K)    # Iterative 
        """ 0720 """
        # return self.helper_Q_Select_recursive(points, K)    # Recursive
        """ 0722 """ # TODO: practice Java's heapq
        # return self.helper_Q_Select_recursive2(points, K)
        # return self.helper_Heap(points, K)  # O(N + KxLg(N))
        return self.helper_Heap2(points, K)
    
    # O(N + K + N x Lg(K))
    def helper_Heap2(self, points, K):
        dist = [self.get_distance(point) for point in points]   # O(N)
        l = []
        for i in range(len(points)):    # O(N x Lg(K))
            heapq.heappush(l, (-dist[i], i))
            # if len(l) == K+1:
            if len(l) > K:
                heapq.heappop(l)
        
        res = []
        for i in range(K):  # K
            idx = l[i][1]
            res.append(points[idx])
        return res
        
    
    # O(3N + KxLg(N))
    def helper_Heap(self, points, K):
        dist = [self.get_distance(point) for point in points]   # O(N)
        l = []
        for i in range(len(dist)):  # O(N)
            l.append((dist[i], i))
            
        # O(N)
        heapq.heapify(l)
        res = []
        
        for j in range(K):  # O(K x Lg(N))
            _, idx = heapq.heappop(l)
            res.append(points[idx])
        return res
        
    # O(N)
    def helper_Q_Select_recursive2(self, points, K):
        dist = [self.get_distance(point) for point in points]
        pos = self.Q_Select2(dist, points, 0, len(points)-1, K)
        return points[:pos+1]
    
    def Q_Select2(self, dist, points, left, right, K):
        pivot = dist[left]
        i, j = left, right
        while i <= j:
            while i <= j and dist[i] < pivot:
                i += 1
            while i <= j and dist[j] > pivot:
                j -= 1
            if i <= j:
                dist[i], dist[j] = dist[j], dist[i]
                points[i], points[j] = points[j], points[i]
                i += 1
                j -= 1
        offset = left + K -1
        if offset <= j:
            return self.Q_Select2(dist, points, left, j, K)
        if offset >= i:
            return self.Q_Select2(dist, points, i, right, K-(i-left))
        return j+1
    
    def helper_Q_Select_recursive(self, points, K):
        #       PLAN. A
        # 1. calc distance for each point, N
        # 2. heapify , N
        # 3. heappop, KlogK
        
        #       PLAN. B
        # 1. calc distance for each point, N
        # 2. Q-Select, and not only shift points arr
        dist = [self.get_distance(point) for point in points]
        # print(dist)
        # return self.Q_select(0, len(points)-1, points, dist, K)
        pos = self.Q_select(0, len(points)-1, points, dist, K)
        # print(pos, points)
        return points[:pos+1]
    
    def Q_select(self, left, right, points, dist, K):
        pivot = dist[left]
        i, j = left, right
        while i <= j: 
            while i <= j and dist[i] < pivot:
                i += 1
            # while i <= j and dist[i] > pivot: # prev BUG!
            while i <= j and dist[j] > pivot:
                j -= 1
            if i <= j:
                points[i], points[j] = points[j], points[i]
                dist[i], dist[j] = dist[j], dist[i]
                i += 1
                j -= 1
        # print(left, right, i, j, dist)
        # j X i
        offset = left + K -1
        # if K <= j:
        # from copy import deepcopy
        if offset <= j:
            return self.Q_select(left, j, points, dist, K)  # No need to deepcopy dist
        # if K >= i:
        if offset >= i:
            return self.Q_select(i, right, points, dist, K - (i-left))
        # return points[:K]
        return j+1
        # return points[:j+2]   # ALSO OK
    
    
    def get_distance(self, point):
        return point[0] * point[0] + point[1] * point[1]
    
    
#     def helper_Q_select(self, points, K):
#         dis = []
#         for pt in points:
#             dis.append(self.distance(pt, [0,0]))
        
#         self.Q_select(dis, K, points) # 0, len(dis)-1, K)
#         return points[:K]
        
#     def Q_select(self, dis, K, points):
#         l, r = 0, len(dis)-1
#         while l < r:
#             meetup = self.partition(dis, l, r, points)
            
#             # if meetup == K:
#             if meetup == K-1:
#                 return 
#             # elif meetup < K:
#             elif meetup < K-1:
#                 l = meetup + 1
#             else:
#                 r = meetup - 1        
                
#     def partition(self, arr, low, high, points):
#         # def swap(x, y):
#         #     x, y = y, x
            
#         i = low - 1
#         pvt = arr[high]      
#         '''
#               3    0 5 4 1 8 2 2
#         low              high 
#         X    X X 2 Y Y Y Y 
#                i         4   
#         # 0 1 2 2
#         '''
#         for j in range(low, high):
#             if arr[j] <= pvt:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#                 points[i], points[j] = points[j], points[i]
#                 # swap(arr[j], arr[i])      # NO USE
#                 # swap(points[j], points[i])
            
#         # swap(arr[i+1], arr[high])
#         # swap(points[i+1], points[high])
#         arr[i+1], arr[high] = arr[high], arr[i+1]
#         points[i+1], points[high] = points[high], points[i+1]
#         return i+1
    
#     def partitionX(self, arr, l, r, points): # 18, 26, 20
#         pvt = arr[l]
#         pvt_point = points[l]
#         i = l+1
#         j = r
                    
#         while i < j:
#             '''
#                3 2 1 5 0 8 7 4   
#              pvt i i i
#                        j, 

#                3 2 1 0
#              pvt  
#                      i
#             '''            
#             while arr[i] < pvt and i < j:
#                 i += 1
#             while arr[j] > pvt and i < j:
#                 j -= 1
#             # if i < j:
#             if True:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 points[i], points[j] = points[j], points[i]
#                 # i += 1
#                 # j -= 1
#         # arr[l], arr[i] = arr[i], pvt   # arr[l] WRONG!
#         # points[l], points[i] = points[i], pvt_point   # arr[l] WRONG!
#         return j
        
        
    
#     def helper_heap_KlgK(self, points, K):  # should use max-heap since we pop out unwanted ones   
#         l = []
#         for pt in points:   # O(N*lg(K))
#             # heapq._heappush_max(l, (self.distance(pt, [0,0]), pt))
#             heapq.heappush(l, (-1*self.distance(pt, [0,0]), pt))
#             if len(l) == K+1:
#                 heapq.heappop(l)
        
#         Q = deque()
#         for j in range(len(l)):
#             _, pt = heapq.heappop(l)
#             Q.appendleft(pt)
            
#         return Q
    
#     def helper_heap_NlgN(self, points, K):
        
#         l = []
#         for pt in points:   # O(N*lg(N))
#             # l.append(self.distance(pt, [0,0]), pt)
#             heapq.heappush(l, (self.distance(pt, [0,0]), pt))
            
#         ans = []
#         for j in range(K):
#             _, pt = heapq.heappop(l)
#             ans.append(pt)
            
#         return ans
    
#     def kClosest_old(self, points: List[List[int]], K: int) -> List[List[int]]:
#         ''' N*log(N)
#         # Q-sort tech
#         # [dis1, dis2, dis3]
#         if not points or not K:
#             return 0
#         l = []
#         for xy in points:
#             heapq.heappush(l, (self.distance(xy), xy[0], xy[1]))  # n*log(n)
#             # if len(l) > K:
#             #     heapq._heappop_max(l)

#         # map(points, self.distance)
#         # for point in points:
#         #     self.distance(point)
        
#         res = []
#         for i in range(K):
#             dis, x, y = heapq.heappop(l)
#             res.append([x,y])
            
#         return res
#         '''
#         l = []
#         for xy in points:
#             dist = self.distance(xy)
#             dist = -1*dist
#             if len(l) <= K-1:
#                 heapq.heappush(l, (dist, xy))
#             else:
#                 # print('---', dist)
#                 if dist > l[0][0]:
#                     heapq.heappop(l)
#                     heapq.heappush(l, (dist, xy))
                    
#         res = []
#         # for i in range(len(l)):
#         for i in range(K):
#             res.append(heapq.heappop(l)[1])
#         return res
            
#     def distance(self, xy, xy2=[0,0]):
#         return math.sqrt((xy[0]-xy2[0])**2 + (xy[1]-xy2[1])**2)#, xy[0], xy[1]
# @lc code=end

