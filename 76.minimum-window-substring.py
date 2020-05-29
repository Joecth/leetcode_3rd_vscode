#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.59%)
# Likes:    4126
# Dislikes: 292
# Total Accepted:    376.8K
# Total Submissions: 1.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
'''
A D O B E C O D E B A N C
     i,        j 

T ==> d{A:1, B:1, C:1}
'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str: # compare with leetcode.3
        # return self.minWindow_FASTER(s, t)
    
        map_t = Counter(t)
        map_s = {}
        start = 0
        min_len = sys.maxsize
        res = ""
        res_start, res_end = 0, 0
        for end in range(0, len(s)):
            ch = s[end]
            map_s[ch] = map_s.get(ch, 0) + 1
            
            while self.is_all_chars_included(map_s, map_t):
                count = end - start + 1
                if count < min_len:
                    res = s[start: end+1]
                    res_start, res_end = start, end+1
                    min_len = min(min_len, count)
                    print(res_start, res_end)
                # print(start)
                if map_s[s[start]] == 1:
                    del map_s[s[start]]
                else:
                    map_s[s[start]] -= 1
                    
                start += 1
        # print(res_start, min_len)
        return s[res_start:res_end]
        return res      # THIS ALSO OK, but personally, res_start and res_end provide more information!
                
    def is_all_chars_included(self, map_s, map_t):
        if len(map_t) > len(map_s):
            return False
        for key in map_t.keys():
            if map_t[key] > map_s.get(key, 0):
                return False
        return True
        
    
    def minWindow_FASTER(self, s: str, t: str) -> str: # compare with leetcode.3
        # def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        map_t, len_t = collections.Counter(t), len(t)
        for i, c in enumerate(s):
            map_t[c] -= 1
            if map_t[c] >= 0:
                cnt += 1
            while cnt == len_t:
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left : i + 1]
                map_t[s[left]] += 1
                if map_t[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res
