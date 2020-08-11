#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (56.01%)
# Likes:    2631
# Dislikes: 274
# Total Accepted:    320.4K
# Total Submissions: 566.2K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
  '[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
                    7
        /                \            
    3                      15
  cur_min   5           9       20
          4     6
          cur
"""
class BSTIterator:
    def __init__(self, root: TreeNode):
        # Search LEFT sub-tree
        cur = root
        cur_min = cur      # used in iterator.next()
        # parent = cur
        """ 1. Find the cur_min node """
        # while cur.left:
        while cur and cur.left:
            cur = cur.left
        cur_min = cur
        
        """ 2. Find the successor of cur_min! """
        """ Dynamic update in next()"""
        # p = cur
        # successor = root
        # while cur:
        #     if cur.val == p.val:
        #         cur = cur.right
        #     # elif cur.val > p.val:
        #     else:# cur.val > p.val:
        #         successor = cur
        #         cur = cur.left
        #     # else:   # Impossible
        #     #     cur = cur.left                
        
        """ 3. Record cur_min & cur """
        self.root = root
        self.cur_min = cur_min
        # self.cur = cur
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        ret = self.cur_min
        # self.cur_min = self.cur
        # update for next round
        # if self.cur:
        self.cur_min = self.get_inorder_successor(self.root, ret)
            
        if ret:
            return ret.val
        else:
            return -1
    
    def get_inorder_successor(self, root, p):
        suc = None
        cur = root
        while cur:
            if p.val < cur.val:
                suc = cur
                cur = cur.left
            else:
                cur = cur.right
        return suc
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.cur_min:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


import heapq
class BSTIterator_Old:

    def __init__(self, root: TreeNode):
        self.l = []
        self.trvs(root)
        
    def trvs(self, root):
        
        if not root:
            return None
        
        # heapq.heappush(self.l, root.val)
        self.trvs(root.left)
        self.l.append(root.val)
        self.trvs(root.right)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # return heapq.heappop(self.l)
        return self.l.pop(0)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.l:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

