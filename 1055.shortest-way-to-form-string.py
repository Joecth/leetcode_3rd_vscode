#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#
# https://leetcode.com/problems/shortest-way-to-form-string/description/
#
# algorithms
# Medium (56.95%)
# Likes:    477
# Dislikes: 32
# Total Accepted:    32.8K
# Total Submissions: 57.6K
# Testcase Example:  '"abc"\n"abcbc"'
#
# From any string, we can form a subsequence of that string by deleting some
# number of characters (possibly no deletions).
# 
# Given two strings source and target, return the minimum number of
# subsequences of source such that their concatenation equals target. If the
# task is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
# subsequences of source "abc".
# 
# 
# Example 2:
# 
# 
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of
# source string due to the character "d" in target string.
# 
# 
# Example 3:
# 
# 
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" +
# "xz".
# 
# 
# Constraints:
# 
# 
# Both the source and target strings consist of only lowercase English letters
# from "a"-"z".
# The lengths of source and target string are between 1 and 1000.
# 
#

# @lc code=start
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if not source: return -1
        # return self.my_sol(source, target)
        return self.sol_sisi(source, target)
    
    def sol_sisi(self, source, target):
        map_s = collections.defaultdict(list)
        # map_s['#'].append(sys.maxsize)
        m, n = len(source), len(target)
        for i in range(len(source)):
            map_s[source[i]].append(i)
            
        idx = 0
        res = 0
        while idx < n:
            if target[idx] not in map_s: 
                return -1
            start = map_s[target[idx]][0]
            for j in range(start, m):
                if target[idx] == source[j]:
                    idx += 1
                if idx == n:
                    return res + 1
            res += 1
        return res
    
    def my_sol(self, source, target):
        # target = target + '#'
        if not source: return -1
        map_s = collections.defaultdict(list)
        # map_s['#'].append(sys.maxsize)
        for i in range(len(source)):
            map_s[source[i]].append(i)
        from bisect import bisect_left  # lower_bound
        count = 0
        prev = -1
        for j in range(len(target)):
            if target[j] not in map_s:
                return -1
            arr = map_s[target[j]]
            # prev + 1    <= search this target
            index = bisect_left(arr, prev+1)    # call module,  要找比 prev(在source中) 大的index
            # if index == len(source):
            if index == len(arr):# or arr[index] == len(source)-1:
                            # pass CASE: ["xyz" "xzyxz"]
                            # yet failed CASE: ["aaaaa", "aaaaaaaaaaaaa"]
                count += 1
                # prev = -1
                prev = arr[0]
            else:
                prev = arr[index]
        count += 1
        return count
            
#         lookup = set(list(source))
#         # if not target: return 
#         i = 0
#         count = 0
#         for j in range(len(target)):
#             t = target[j]
#             if t not in lookup:
#                 return -1
#             while i < len(source) and source[i] != t:
#                 i += 1
#             if i < len(source) and source[i] == t:
#                 i += 1
#             print(j, i, count)
#             if i == len(source):
#                 count += 1
#                 i = 0
            
#         if i != 0:              # for case: "aaaaa"
#                                 #           "aaaaaaaaaaaaa" 
#             count += 1
#         return count        
# @lc code=end

