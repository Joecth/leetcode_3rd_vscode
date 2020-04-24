/*
 * @lc app=leetcode id=146 lang=javascript
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
/**
 * @param {number} capacity
 */
/**
 * 34

JavaScript in 2016, specifically EcmaScript 6, 
supports the Map built-in class.
A Map object iterates its elements in insertion order — a for...of loop returns an array of [key, value] for each iteration.
That's what you need. 
(I wonder why that is the first info in the description of this data structure, though.)

For example,
m = new Map()
m.set(3,'three')
m.set(1,'one')
m.set(2,'two')

m // Map { 3 => 'three', 1 => 'one', 2 => 'two' }

[...m.keys()] // [ 3, 1, 2 ]

var myMap = new Map();
myMap.set(0, 'zero');
myMap.set(1, 'one');

myMap // Map { 0 => 'zero', 1 => 'one' }

for (var [key, value] of myMap) {
  console.log(key + " = " + value);
}

for (var key of myMap.keys()) {
  console.log(key);
}
 */
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.d = new Map();
    this.cap = capacity;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (this.d.has(key)){
        let val = this.d.get(key);
        this.d.delete(key); // this.d.remove(key);
        this.d.set(key, val); // this.d.put(key, val);
        return val;
    }
    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.d.has(key)){
        this.d.delete(key); // this.d.remove(key);
        this.d.set(key, value); // this.d.put(key, value);
        return;
    }
    else{
        if (this.d.size == this.cap){   // size, not size()
            // let first = this.d.next().keys();
            let first = this.d.keys().next().value;
            this.d.delete(first); // this.d.remove(first);
        }
        this.d.set(key, value); // this.d.put(key, val);
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end

