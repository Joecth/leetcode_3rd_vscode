#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (30.43%)
# Likes:    5008
# Dislikes: 222
# Total Accepted:    469.7K
# Total Submissions: 1.5M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int: # CAUTIOUS! remember to set the key to the tail of self.od
        # print(self.od, ', asked k: ', key)
        if key in self.od:
            val = self.od[key]
            del self.od[key]
            self.od[key] = val
            return  self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            # tmp = self.od[key]
            del self.od[key]
            self.od[key] = value
        else:
            if len(self.od) < self.capacity:
                self.od[key] = value
            else:                
                # del self.od[next(iter(self.od))]
                self.od.popitem(last=False)
                self.od[key] = value        
# 如果是OD或deque+dict的實現，在del時就是O(N)…

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

