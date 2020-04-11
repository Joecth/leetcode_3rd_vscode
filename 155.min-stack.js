/*
 * @lc app=leetcode id=155 lang=javascript
 *
 * [155] Min Stack
 *
 * https://leetcode.com/problems/min-stack/description/
 *
 * algorithms
 * Easy (41.42%)
 * Likes:    2844
 * Dislikes: 285
 * Total Accepted:    451.3K
 * Total Submissions: 1.1M
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 * 
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 * 
 * 
 * 
 * 
 * Example:
 * 
 * 
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> Returns -3.
 * minStack.pop();
 * minStack.top();      --> Returns 0.
 * minStack.getMin();   --> Returns -2.
 * 
 * 
 * 
 * 
 */

// @lc code=start
/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.s = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    let cur_min = x;
    if (this.s.length != 0){
        // console.log(this.s);
        cur_min = Math.min(this.s[this.s.length-1][1], x);
    }
    this.s.push([x, cur_min]);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    v = this.s.pop();
    return v[0];
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if (this.s.length == 0) return 0;
    return this.s[this.s.length-1][0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    // return Math.min(...this.s)
    if (this.s.length == 0) return 0;
    return this.s[this.s.length-1][1];
};
var obj = new MinStack()
obj.push(3)
obj.pop()
var param_3 = obj.top()
var param_4 = obj.getMin()
/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @lc code=end

