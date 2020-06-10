#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (40.87%)
# Likes:    2950
# Dislikes: 169
# Total Accepted:    257.5K
# Total Submissions: 603.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        # return self.TLE(s, p)
        # return self.findAnagrams_Counter(s, p)
        # return self.findAnagrams_old(s, p)
        return self.helper_new(s, p)
    
    def helper_new(self, s, p):
        map_p = {}
        for ch in p:
            map_p[ch] = map_p.get(ch, 0) + 1
        
        start = 0
        matched = 0
        res = []
        map_s = {}
        for end in range(len(s)):
            ch = s[end]
            map_s[ch] = map_s.get(ch, 0) + 1
                
            
            # if end - start + 1 == len(p):
            if end >= len(p):
                """
                # map_s[s[end-len(p)]] -= 1
                # if map_s[s[end-len(p)]] == 0:
                #     del map_s[s[end-len(p)]]
                """ 
                """ SAME AS ABOVE 3 LINES ↑↓ """
                map_s[s[start]] -= 1
                if map_s[s[start]] == 0:
                    del map_s[s[start]]
                start += 1
                
            if map_p == map_s:
            # if self.is_anagram() ==> VERY SLOW when p is very LONG
            # map comparison is more efficient
                res.append(end-len(p)+1)
                
        return res
                    
                
    def TLE(self, s, p):
        # write your code here
        # ==> Sliding Wind
        # fixed length sliding window
        # res = []
        # for i 
        #     pat = s[i:i+leng(p)]
        #     if self.is_anagram(p, pat):
        #         res.append(i)
        # return res
        res = []
        for i in range(len(s)-len(p)+1):
            pat = s[i:i+len(p)]
            if self.is_anagram(p, pat):
                res.append(i)
        return res

    def is_anagram(self, p, pat):
        # return sorted(p) == sorted(pat)  
        # BAD       ↑
        
        # BETTER    ↓
        map_s = {}
        for i in range(len(p)):
            map_s[p[i]] = map_s.get(p[i], 0) + 1
        
        for i in range(len(pat)):
            if pat[i] not in map_s:
                return False
            map_s[pat[i]] -= 1
            if map_s[pat[i]] == 0:
                del map_s[pat[i]]
        return True
            

    def findAnagrams_old2(self, s: str, p: str) -> List[int]:    # 100 ms
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        # enc_s = self.encoder(s[:win])
        
        offset = win-1
        res = []
        '''Dynamically update pattern in s'''
        # for i in range(offset, len(s)):
        enc_c = [0] * 26
        j = 0
        for i in range(len(s)):
            enc_c[ord(s[i]) - ord('a')] += 1
            if i - j >= win:
                enc_c[ord(s[j]) - ord('a')] -= 1
                j += 1
            if enc_c == enc_p:
                res.append(j)
        return res
        
    def findAnagrams_TLE(self, s: str, p: str) -> List[int]:    # TLE
        ''' TLE, SHOULD Dynamically  Update enc_tmp'''
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        
        offset = win-1
        res = []
        for i in range(offset, len(s)):
            start = i - win + 1
            sub_s = s[start:i+1]
            # print(sub_s)
            enc_tmp = self.encoder(sub_s)  # 2 - (3-1) : 3  # No OOR
            
            if enc_tmp == enc_p:
                res.append(start)
        return res
        
    def encoder(self, s):
        enc = [0] * 26   
        for i in range(len(s)):
            enc[ord(s[i]) - ord('a')] += 1
            
        return enc
        
        
    def findAnagrams_old(self, s: str, p: str) -> List[int]:
        '''
        p ==> onehot arr
        a b c , [1,1,1,0 0 0... 0], len == 26
        b a c 
        
        
        trvs string s w/ sliding window
        fr idx 0 to idx len(s)-1-len(p) to check
        '''
        
        window = len(p)
        # d = {}  # {[1 1 1 0 0 0 ]:
                #     ['abc', 'cba'...]
                # }
        onehot_p = self.onehot2encode(p)
        
        onehot_s = [0] * 26
        ans = []
        for k in range(len(s)):
            onehot_s[ord(s[k])-ord('a')] += 1
            if k >= window:
                onehot_s[ord(s[k-window])-ord('a')] -= 1
                
            if onehot_s == onehot_p:
                ans.append(k-window+1)
                       
        return ans
        
    def onehot2encode(self, p):  # bucket sort
        onehot = [0] * 26
        for i in range(len(p)):
            onehot[ord(p[i]) - ord('a')] += 1 
        return onehot
         # [1,1,1,0 0 0... 0]
        
# @lc code=end

