#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (34.30%)
# Likes:    2083
# Dislikes: 115
# Total Accepted:    133.7K
# Total Submissions: 388K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Now suppose you are given
# the locations and height of all the buildings as shown on a cityscape photo
# (Figure A), write a program to output the skyline formed by these buildings
# collectively (Figure B).
# ⁠   
# 
# The geometric information of each building is represented by a triplet of
# integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
# right edge of the ith building, respectively, and Hi is its height. It is
# guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
# may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
# point is the left endpoint of a horizontal line segment. Note that the last
# key point, where the rightmost building ends, is merely used to mark the
# termination of the skyline, and always has zero height. Also, the ground in
# between any two adjacent buildings should be considered part of the skyline
# contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3
# 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# 
# The number of buildings in any input list is guaranteed to be in the range
# [0, 10000].
# The input list is already sorted in ascending order by the left x position
# Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
# acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...[2 3], [4 5], [12 7], ...]
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        # return self.all_comments(buildings)  # fr. Discussion
        # return self.sol_w_dict(buildings)
        # return self.sol_fr_TLE(buildings)
        # return self.sol_fr_TLE_TLE(buildings)
        # return self.helper_mock(buildings)
        return self.helper_again(buildings)
    
    def helper_again(self, buildings):
        # count from 0, thus, sorting
        points = []
        for l, r, h in buildings:
            # points.append([l, r, h])    # 同個點高的要先進來，所以h應該要在r的前面
            # points.append([r, -999, h])
            points.append([l, -h, r])   # 進來時高的先進來
            points.append([r, h, 999])    # 出去時矮的先出去
        
        points.sort()
        hp = [[0, sys.maxsize]]
        res = [[0, 0]]
        for l, h, r in points:
            while hp[0][1] <= l:
                heapq.heappop(hp)
            heapq.heappush(hp, [h, r])
            # if res[-1][1] != -hp[0][1]: # BUG
            if res[-1][1] != -hp[0][0]: # BUG
                res.append([l, -hp[0][0]])
        return res[1:]
    
    def helper_mock(self, buildings):
        # count from 0, thus, sorting
        points = []
        for l, r, h in buildings:
            # points.append([l, r, h])    # 同個點高的要先進來，所以h應該要在r的前面
            # points.append([r, -999, h])
            points.append([l, -h, r])   # 進來時高的先進來
            points.append([r, h, r])    # 出去時矮的先出去
        
        points.sort()
        res = [[0,  0]] # 
        # prev_highest = 0  # 但解決不了還要後續的很多個高的，所以要heapq
        hp = [[0, sys.maxsize]]
        for l, h, r in points:
            # if h < 0:
            # if h > prev_highest:    # 但解決不了還要後續的很多個高的，所以要heapq
                # if abs(h) > abs(hp[0][0]):    # cur h is taller than existing highest
                                    # 為了不多判斷第一棟進來時的case, 替hp加上 初始高度為 0           
            while l >= hp[0][1]:
                heapq.heappop(hp)
            heapq.heappush(hp, [h, r])   # 會需要右邊界的info嗎？==> 需要，這樣上上一行才有辦法作彈出
            if res[-1][1] != -hp[0][0]:     # 預先塞一個0作初始化
                res.append([l, -hp[0][0]])
        return res[1:]
            
              
        
    
    
    def sol_fr_TLE_TLE(buildings):
        q = []
        res = []
        i, j, cur_height = 0, 0, 0
        m = len(buildings)
        points = []
        for k in buildings:
            if k[0] not in points:
                points.append(k[0])
            if k[1] not in points:
                points.append(k[1])
        points.sort()
        while True:
            # 添加新来的建筑
            while j != m and buildings[j][0] == points[i]:
                q.append(buildings[j])
                j += 1

            # 判断是否结束
            if j == m and not q:
                break
            
            temp = 0
            # 清除已经过去的建筑
            q = list(filter(lambda x: x[1] > points[i], q))
            # 检测当前点最高的建筑
            for build in q:
                temp = max(temp, build[2])
            if temp != cur_height:
                cur_height = temp
                res.append([points[i], temp])
            i += 1
        return res
        # 链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/jie-ti-si-lu-by-xerrors/
    
    def sol_fr_TLE(self, buildings):
        points = []
        for build in buildings:
            points.append((build[0], -build[2]))
            points.append((build[1],  build[2]))
        points.sort(key=lambda x: (x[0], x[1]))

        heights = []
        res = []
        should_del = {} # 因为在堆里面删除元素需要更多的时间开销，所以先把需要删除的元素保存起来

        cur_height = 0

        for point in points:
            if point[1] < 0: heapq.heappush(heights, point[1])
            elif should_del.get(point[1]): 
                should_del[point[1]] += 1 # 保存需要删除的次数，删除的时候，删除一次
            else:
                should_del[point[1]] = 1

            # 如果当前堆顶元素是应该删除的元素就先删除掉
            while heights and -heights[0] in should_del:
                temp = -heights[0]
                heapq.heappop(heights)
                should_del[temp] -= 1
                if should_del[temp] == 0:
                    should_del.pop(temp)
            
            maxH = -heights[0] if heights else 0
            if maxH != cur_height:
                cur_height = maxH
                res.append([point[0], cur_height])

        return res
        # 作者：xerrors
        # 链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/jie-ti-si-lu-by-xerrors/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


    def sol_w_dict(self, buildings):
        ans = {}
        dic = {}
        points = []
        for L,R,H in buildings: #初始化所有关键点
            points.append((L,'left',H,R))
            points.append((R,'right',0,0))
        points.sort()
        dic[0] = 0
        cur = 0
        for x,s,H,R in points:
            if s =='left': #这个关键点是左端 
                if R in dic.keys(): #把其右端点和高度存入高度字典
                    dic[R] = max(dic[R],H)
                else:
                    dic[R] = H
                new = max(dic.values()) #如果高度改变，这就是天际线点
                if new != cur:
                    if x in ans.keys(): ans[x] =  max(ans[x],H)
                    else: ans[x] = H                   
                    cur = new
            else: #这个关键点是右端 
                if x not in dic.keys():  #前面已经被删除了，所有没有，跳过
                    continue
                del dic[x] #删除右端点及其高度，检查高度是否改变
                new = max(dic.values())
                if new != cur:
                    ans[x] = new
                    cur = new                
        return ans.items()
        # https://leetcode-cn.com/problems/the-skyline-problem/solution/chu-xue-zhe-bu-yong-dui-yong-zi-dian-de-fang-fa-by/
# 作者：cvcv2525
# 链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/chu-xue-zhe-bu-yong-dui-yong-zi-dian-de-fang-fa-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """import heapq
    heapq.heappop(l)
    heapq.heappush(l, elem)"""
    def all_comments(self, buildings: List[List[int]]) -> List[List[int]]:
        #思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings:return []
        points = []
        heap = [[0, float('inf')]]      # ==> list
        res = [[0, 0]]

        #1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r)) #这里负号将最小堆，变成了最大堆
            points.append((r, h, 99999999)) #r的右端点为0 ==> 用不到

        #2.将端点从小到大排序
        points.sort() #如果当前点相等，则按照高度升序, N x Lg(N)

        #3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:  # N x Lg(N)
            while l >= heap[0][1]: #EXPIRE?! 出堆：保证当前堆顶为去除之前建筑物右端点的最大值。過期的也不見得都會被刪了!
                heapq.heappop(heap) # ==> 
            if h < 0: #進高度; 入堆：所有左端点都要入堆 
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]: #查高度有無變化; 关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
        return res[1:]  # 去 0
        # 链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/python3-sao-miao-xian-zui-da-dui-wan-zheng-zhu-shi/        
# @lc code=end

