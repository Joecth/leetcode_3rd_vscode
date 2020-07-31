#
# @lc app=leetcode id=737 lang=python3
#
# [737] Sentence Similarity II
#
# https://leetcode.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (45.71%)
# Likes:    492
# Dislikes: 31
# Total Accepted:    41.2K
# Total Submissions: 90.1K
# Testcase Example:  '["great","acting","skills"]\n' +
  '["fine","drama","talent"]\n' +
  '[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are
# similar.
# 
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine",
# "drama", "talent"] are similar, if the similar word pairs are pairs =
# [["great", "good"], ["fine", "good"], ["acting","drama"],
# ["skills","talent"]].
# 
# Note that the similarity relation is transitive. For example, if "great" and
# "good" are similar, and "fine" and "good" are similar, then "great" and
# "fine" are similar.
# 
# Similarity is also symmetric. For example, "great" and "fine" being similar
# is the same as "fine" and "great" being similar.
# 
# Also, a word is always similar with itself. For example, the sentences words1
# = ["great"], words2 = ["great"], pairs = [] are similar, even though there
# are no specified similar word pairs.
# 
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 =
# ["doubleplus","good"].
# 
# Note:
# 
# 
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
# 
# 
# 
# 
#

# @lc code=start
class UF_w_rank(object):
    def __init__(self, n):
        self._parents = [idx for idx in range(n+1)]
        self._rank = [1 for idx in range(n+1)]
    def find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        # self._parents[pv] = pu
        # return True
        if self._rank[u] > self._rank[v]:
            self._parents[pv] = pu
        elif self._rank[u] < self._rank[v]:
            self._parents[pu] = pv
        else:
            self._parents[pv] = pu
            self._rank[pu] += 1
            self._rank[pv] += 1
        return True
    
class UF(object):
    def __init__(self, n):
        self._parents = [idx for idx in range(n+1)]
        # self._rank
    def find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self._parents[pv] = pu
        return True
        
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        m, n = len(words1), len(words2)
        if m != n or not pairs:
            return False
        uf = UF(len(pairs) * 2)
        # d = collections.defaultdict(int)
        d = {}
        for w1, w2 in pairs:
            # w1--> u
            # w2--> v
            # if w1 not in d:
            #     d[w1] = len(d)
            u = d[w1] = d.get(w1, len(d))
            v = d[w2] = d.get(w2, len(d))
            # print(w1,u,w2,v)
            uf.union(u, v)
            
        for i in range(m):
            w1, w2 = words1[i], words2[i]
            if w1 == w2:    # may both not in d, but are same
                continue
            # w1--> u
            # w2--> v
            if w1 not in d or w2 not in d:
                return False
            u, v = d[w1], d[w2]
            if uf.find(u) != uf.find(v):
                return False
        return True
        
        
    def BF():       # Not finished yet
        m, n = len(words1), len(words2)
        if m != n or not pairs:
            return False
        d = collections.defaultdict(set)
        for u, v in range(pairs):
            d[u].add(v)
            d[v].add(u)
            
        for i in range(m):
            if not self.is_similar(words1[i], words2[i], d):
                return False
        return True
    
    def is_similar(self, w1, w2, d):
        if w1 not in d and w2 not in d:
            return False
        if w1 in d:
            return self.is_similar( w2)
            # ==> many expansion!
        if w2 in d and w1 in d[w2]:
            return True
        
        
        
        
# @lc code=end

