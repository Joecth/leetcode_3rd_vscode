/*
 * @lc app=leetcode id=146 lang=cpp
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
#include <unordered_map>
class LRUCache {
    typedef pair<int, int> Node;
    typedef list<Node>::iterator ref;
    list<Node> db_ll;
    unordered_map<int, ref> d;
    int cap;
public:
    LRUCache(int capacity) {
        // https://www.tutorialspoint.com/cpp_standard_library/cpp_unordered_map_reserve.htm
        cap = capacity;
        d.reserve(capacity);
    }
    
    int get(int key) {
        if (d.find(key) != d.end()){
            int val = d[key]->second;
            put(key, val);
            return val;
        } 
        return -1;
    }
    
    void put(int key, int value) {
        if (d.find(key) != d.end()){
            db_ll.erase(d[key]);    // O(1)
            // d.erase(key);    // No need
            
            // db_ll.push_back(make_pair(key, value));
            db_ll.push_front(make_pair(key, value));
            d[key] = db_ll.begin();
            
            //TODO: splice() usage: https://blog.csdn.net/qq_41909314/article/details/90575034?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3 
            // thus,             db_ll.splice(db_ll.begin(), db_ll, d[key]); is also OK, P.S. d is the "Cache"
        }
        else {
            if (db_ll.size() >= cap){
                int key = db_ll.back().first;
                db_ll.pop_back();   // O(1)
                d.erase(key);   
            }
            db_ll.push_front(make_pair(key, value));
            d[key] = db_ll.begin();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

