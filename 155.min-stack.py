#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (41.42%)
# Likes:    2844
# Dislikes: 285
# Total Accepted:    451.3K
# Total Submissions: 1.1M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
# '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
# 
# 
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.dq = deque()   # deque: 
                            #    1:3  2:2  3:1
        # self.
        self.s = []

    def push(self, x: int) -> None:
        # self.cur_min = min(self.cur_min, x)
        if not self.s:
            cur_min = x
        else:
            cur_min = min(self.s[-1][1], x) # CAUTIOUS!
        self.s += [(x, cur_min)]

    def pop(self) -> None:
        v, cur_min = self.s[-1]
        self.s.pop()
        return v

    def top(self) -> int: # TODO: should also check is self.s empty like js's implementation
        return self.s[-1][0]

    def getMin(self) -> int: # TODO: should also check is self.s empty like js's implementation
        return self.s[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

