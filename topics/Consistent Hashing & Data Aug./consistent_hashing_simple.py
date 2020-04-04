# 519. 一致性哈希
# 中文English
# 一般的数据库进行horizontal shard的方法是指，把 id 对 数据库服务器总数 n 取模，然后来得到他在哪台机器上。这种方法的缺点是，当数据继续增加，我们需要增加数据库服务器，将 n 变为 n+1 时，几乎所有的数据都要移动，这就造成了不 consistent。为了减少这种 naive 的 hash方法(%n) 带来的缺陷，出现了一种新的hash算法：一致性哈希的算法——Consistent Hashing。这种算法有很多种实现方式，这里我们来实现一种简单的 Consistent Hashing。

# 将 id 对 360 取模，假如一开始有3台机器，那么让3台机器分别负责0~119, 120~239, 240~359 的三个部分。那么模出来是多少，查一下在哪个区间，就去哪台机器。
# 当机器从 n 台变为 n+1 台了以后，我们从n个区间中，找到最大的一个区间，然后一分为二，把一半给第n+1台机器。
# 比如从3台变4台的时候，我们找到了第3个区间0~119是当前最大的一个区间，那么我们把0~119分为0~59和60~119两个部分。0~59仍然给第1台机器，60~119给第4台机器。
# 然后接着从4台变5台，我们找到最大的区间是第3个区间120~239，一分为二之后，变为 120~179, 180~239。
# 假设一开始所有的数据都在一台机器上，请问加到第 n 台机器的时候，区间的分布情况和对应的机器编号分别是多少？

# Example
# 例1:

# 输入:
#  n = 1, 
# 输出:
# [
#   [0,359,1]
# ]
# 解释:
# 表示 0~359 属于机器 1.
# 例2:

# 输入:
#  n = 2,
# 输出:
# [
#   [0,179,1],
#   [180,359,2]
# ]
# 解释:
# 表示 0~179 属于机器 1.
# 表示 180~359 属于机器 2.
# 例3:

# 输入:
# n = 3,
# 输出:
# [
#   [0,89,1]
#   [90,179,3],
#   [180,359,2]
# ]
# Clarification
# 如果最大间隔是[x，y]，并且它属于机器id z，当你添加一个id为n的新机器时，你应该将[x，y，z]分成两个区间：

# [x，（x + y）/ 2，z]和[（x + y）/ 2 + 1，y，n]

# Notice
# 你可以假设 n <= 360. 同时我们约定，当最大区间出现多个时，我们拆分编号较小的那台机器。
# 比如0~119， 120~239区间的大小都是120，但是前一台机器的编号是1，后一台机器的编号是2, 所以我们拆分0~119这个区间。
from collections import deque
from math import ceil, log
class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        # write your code here
        Q = deque()
        v = [0, 359, 1]
        Q.append(v)
        res = Q
        for idx in range(1, n):
            cur = idx + 1
            low, high, idx = Q.popleft()

            Q.append([low , (low+high)//2, idx])
            new_v = [(low+high)//2+1 , high,cur]
            Q.append(new_v)
            res = Q
            
            ## Following makes system use smaller ID for same size segs, but still failed at 76, Anyway, sequence matters less
            if not self.is_power_of_two(cur):
                len_to_sort = 2**ceil(log(cur,2)) - cur
                tmp = sorted(list(Q)[:len_to_sort], key=lambda x: x[2])
                # print('tmp: ', tmp)
                tmp.extend(list(Q)[len_to_sort:])
                Q = deque(tmp)
                # print('Q: ', Q)

        return list(res)
    
    def is_power_of_two(self, n):
        return not (n & (n-1))

if __name__ == '__main__':
    sol = Solution()
    sol.consistentHashing(3)