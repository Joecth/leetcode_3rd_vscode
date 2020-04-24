/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 *
 * https://leetcode.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (30.43%)
 * Likes:    5008
 * Dislikes: 222
 * Total Accepted:    469.7K
 * Total Submissions: 1.5M
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * Design and implement a data structure for Least Recently Used (LRU) cache.
 * It should support the following operations: get and put.
 * 
 * get(key) - Get the value (will always be positive) of the key if the key
 * exists in the cache, otherwise return -1.
 * put(key, value) - Set or insert the value if the key is not already present.
 * When the cache reached its capacity, it should invalidate the least recently
 * used item before inserting a new item.
 * 
 * The cache is initialized with a positive capacity.
 * 
 * Follow up:
 * Could you do both operations in O(1) time complexity?
 * 
 * Example:
 * 
 * 
 * LRUCache cache = new LRUCache( 2 /* capacity */ );
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // returns 1
 * cache.put(3, 3);    // evicts key 2
 * cache.get(2);       // returns -1 (not found)
 * cache.put(4, 4);    // evicts key 1
 * cache.get(1);       // returns -1 (not found)
 * cache.get(3);       // returns 3
 * cache.get(4);       // returns 4
 * 
 * 
 * 
 * 
 */

// @lc code=start
class LRUCache {
    LinkedHashMap<Integer, Integer> d;
    int cap;
    public LRUCache(int capacity) {
        // Map<Integer, Integer> this.d = new LinkedHashMap<>();
        // int this.cap = capacity;
        this.d = new LinkedHashMap<>();
        this.cap = capacity;
    }
    
    public int get(int key) {
        if (this.d.containsKey(key)){
            int val = this.d.get(key);
            this.d.remove(key);
            this.d.put(key, val);
            return val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (this.d.containsKey(key)){
            this.d.remove(key);
            this.d.put(key, value);
        }
        else {
            if (this.d.size() == this.cap){
                // this.d.pop_front();
                // Integer first = this.d.entrySet().iterator().next();
                Integer first = this.d.keySet().iterator().next();
                this.d.remove(first);
            }
            this.d.put(key, value);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

