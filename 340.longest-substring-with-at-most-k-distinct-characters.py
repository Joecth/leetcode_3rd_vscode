#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (42.92%)
# Likes:    1012
# Dislikes: 36
# Total Accepted:    126.8K
# Total Submissions: 291.7K
# Testcase Example:  '"eceba"\n2'
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
# 
# Example 1:
# 
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:    
        # return self.helper_maxlen(s, k)
        return self.helper_res_end(s, k)
    
    def helper_res_end(self, s, k):
        map_s = {}
        start = 0
        
        # res = ''
        res_start = 0
        res_end = 0
        max_len = 0
        for end in range(len(s)):
            ch = s[end]
            map_s[ch] = map_s.get(ch, 0) + 1
            if len(map_s) > k:
                # max_len = max(max_len, end-start)
                # if end-start+1 > res_end-res_start+1:
                #     res_start = start
                #     res_end = end
                #     max_len = end-start
                
                if map_s[s[start]] == 1:
                    del map_s[s[start]]
                else:
                    map_s[s[start]] -= 1
                start += 1
            max_len = max(max_len, end-start+1)
        # return res_end-res_start
        return max_len
        
        
        
    def helper_maxlen(self, s, k):
        map_s = {}
        start = 0
        max_len = 0
        
        # res = ''
        res_start = 0
        res_end = 0
        max_len = 0
        for end in range(len(s)):
            ch = s[end]
            map_s[ch] = map_s.get(ch, 0) + 1
            
            if len(map_s) > k:
                # max_len = max(max_len, end-start+1)
                if end-start+1 > res_end-res_start+1:
                    res_start = start
                    res_end = end    
                
                if map_s[s[start]] == 1:
                    del map_s[s[start]]
                else:
                    map_s[s[start]] -= 1
                start += 1
                
            # res_end = max(res_end, end-start+1)
            max_len = max(max_len, end-start+1)
            # print(end, max_len)
        return max_len
        # return res_end-res_start
        # return s[res_start:res_end]
        
    def lengthOfLongestSubstringKDistinct_old(self, s: str, k: int) -> int:
        # {e:[0, 2], c:[1]}   l=0 r=r2 len=3
        # or
        # {e:2, c:1}
        if k == 0:
            return 0
        
        d = defaultdict(int)   
        j = 0
        max_len = 0
        for idx in range(len(s)):
            if s[idx] not in d:
                d[s[idx]] = 0
            else:
                d[s[idx]] += 1
            while len(d) > k and j < idx:
                if d[s[j]] > 0:
                    d[s[j]] -= 1
                else:
                    del d[s[j]]
                j += 1
            max_len = max(max_len, idx - (j-1))        
        return max_len
            
        
                
# @lc code=end

