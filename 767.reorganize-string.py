#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (48.29%)
# Likes:    1723
# Dislikes: 83
# Total Accepted:    87.2K
# Total Submissions: 179.1K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        1. backtracking?  ==> No, since S in range [1, 500]
        2. counting by GREEDY pickup?
        """
        # return self.sol1_FAILED(S)
        # return self.sol2(S) 
        return self.sol3(S)
                
    def sol3(self, S):
        if not S:
            return ''
        n = len(S)
        d = {}
        for i in range(len(S)):
            d[S[i]] = d.get(S[i], 0) + 1
        # keys, counts = d.keys(), d.values()
        if len(d.keys()) == 1:
            return ""
        l = []
        for ch, v in d.items():
            heapq.heappush(l, (-v, ch))
            
        res = []
        res = ''
        max_count = 0
        for _ in range(n):
            if res and l[0][1] == res[-1]:
                max_count, max_ch = heapq.heappop(l)    # Inorder to get key w/ 2nd large count
            if len(l) == 0: # means not 2nd large to pop(); 事後加上的限制
                return ''
            
            count, ch = heapq.heappop(l)
            # res.append(ch)
            res += ch
            
            """ push back """
            if abs(count)-1 > 0:
                heapq.heappush(l, (-(abs(count)-1), ch))
            # if len(l) == 1:
            #     return ''
            
            if abs(max_count) > 0:  # 第30行, 取了出來要放回去
                heapq.heappush(l, (max_count, max_ch))
                max_count = 0
            
        return res
        # return ''.join(res)
#     def sol2_FAILED(self, S):  # 雙向指針，FAILED    
#         n = len(S)
#         start, end = 0, n-1
#         prev = ""
#         next_ = ""
#         while start < end:
#             if S[start] == prev:
            
#             if S[end] == next_:
                
#             prev = S[tart]    
#             start += 1
#             end -= 1
            

    
    def sol1_FAILED(self, S):  # counting & GREEDY
                                # FAILED in "baaba", 因为我把res第一個固定住了…如果從counts最大的開始就可以… 但有「最大」的就有「第二大」。。。的問題。。
        # a a a a b c c
        # c_map = collections.Counter(S)
        # keys, counts = list(c_map.keys()), list(c_map.values())
        if not S:
            return ''
        d = {}
        for i in range(len(S)):
            d[S[i]] = d.get(S[i], 0) + 1
        # keys, counts = d.keys(), d.values()
        if len(d.keys()) == 1:
            return ""
        
        n = len(S)
        prev_ch = S[0]
        d[prev_ch] -= 1
        res = [S[0]]
        for _ in range(1, n):
            # for j in range(len(keys)):
            for k in d.keys():
                if prev_ch != k:
                    res.append(k)
                    d[k] -= 1
                    prev_ch = k
                    if d[k] == 0:
                        del d[k]
                    break
                if len(d.keys()) == 1:
                    return ""
        return ''.join(res)
        
# @lc code=end

