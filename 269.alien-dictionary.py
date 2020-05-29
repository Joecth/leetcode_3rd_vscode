#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (33.76%)
# Likes:    1607
# Dislikes: 317
# Total Accepted:    135.1K
# Total Submissions: 405.9K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
# 
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
# 
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ] 
# 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
# 
# 
# Note:
# 
# 
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
# 
# 
#

# @lc code=start
"""
    e -- ------- - -- 
        \             \
         v              v
    w --> r --> ------ --> t(self points)
           \         /
            --> f --
            
    {'r': 2, 'w': 0, 't': 3, 'f': 1, 'e': 0}
    {'w': ['r'], 'r': ['t', 'f'], 't': [], 'f': ['t'], 'e': ['r', 't']}
    
    t > f ? or t < f ?
"""        
from collections import deque
import random
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # return self.helper_MISUNDERSTANDING(words)
        # return 'wertf'
        return self.helper(words)
    
    def helper(self, words):
        res = ''
        outs = {}   # {t:[f], w:[e], r:[t], e:[r]}
        in_degree = {}  # {w:0, f:1, e:1, t:1, r:1}
        
        # Put SEEDs
        for word in words:
            for j in range(len(word)):
                if word[j] not in outs:
                    outs[word[j]] = []
                    in_degree[word[j]] = 0
        
        for i in range(1, len(words)):
            prev, cur = words[i-1], words[i]
            # if len(prev) > len(cur) and prev.startswith(cur): return ""   # 
            for j in range(min(len(prev), len(cur))):
                if prev[j] != cur[j]:
                    if cur[j] not in outs[prev[j]]:
                        outs[prev[j]] += [cur[j]] 
                        in_degree[cur[j]] += 1
                    break   # !!! for CRUTIAL, ["za","zb","ca","cb"], or zb, ca ends up with z->c and b->a(INVALID)
                else:   # for ['abc', ab] case, SAME as line36
                    if j == min(len(prev), len(cur)) - 1 and len(prev) > len(cur): return ""
                    
        Q = deque()
        path = ""
        for key in outs.keys():
            if in_degree[key] == 0:
                Q.append(key)
                # path += key
        
        while Q:
            for i in range(len(Q)):
                cur = Q.popleft()
                path += cur

                for nbr in outs[cur]:
                    in_degree[nbr] -= 1
                    if in_degree[nbr] == 0:
                        Q.append(nbr)
                        # path += key

        return "" if len(path) != len(outs) else path
        # return path
        
    def helper_MISUNDERSTANDING(self, words):
        # CHALLENGE: BUILD GRAPH: USE 953 to build GRAPH
        # in_degree = {} # {e:0, w:0, r:2 ...}
        # outs = {} # {e: [w, r], ...}
        in_degree = defaultdict(int)
        outs = defaultdict(list)
        for i in range(0, len(words)-1):
            word = words[i]
            # TODO: cmp words[i] and words[i+1]
            for j in range(0, len(word)-1):
                # word[j] --> word[j+1]
                start, end = word[j], word[j+1]
                if start == end: 
                    continue
                if end not in outs.get(start, []):
                    outs[start] = outs.get(start, []) + [end]
                    in_degree[end] = in_degree.get(end, 0) + 1
                
                """ Edge case Init """
                outs[end] = outs.get(end, [])
                in_degree[start] = in_degree.get(start, 0)       
                
                # w-->r-->t
        print(in_degree, outs)    # CANNOT get t --> f... how?!
        
        Q = deque()
        path = []
        for key in in_degree.keys():
            if in_degree[key] == 0:
                Q.append(key)
                path.append(key)
        
        # random.shuffle(path)
        print(Q, path)
        while Q:            
            len_Q = len(Q)
            for i in range(len_Q):
                cur = Q.popleft()
                # random.shuffle(outs[cur])
                # random.shuffle(outs[cur])
                print(outs[cur])
                for nbr in outs[cur]:
                    in_degree[nbr] -= 1
                    if in_degree[nbr] == 0:
                        path.append(nbr)
                        Q.append(nbr)
        # return "wertf"
        return ''.join(path)   # werft
                