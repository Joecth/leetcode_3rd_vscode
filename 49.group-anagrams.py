#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (53.31%)
# Likes:    2809
# Dislikes: 157
# Total Accepted:    537.4K
# Total Submissions: 997.8K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    # def __init__(self):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # write your code here
        # return self.helper(strs)
        return self.helper_better(strs)
    
    def helper_better(self, strs):
        d = {}
        for s in strs:
            tmp_s = ''.join(sorted(s))
            if tmp_s not in d:
                d[tmp_s] = [s]
            else:
                d[tmp_s] += [s]
        return [val for val in d.values()]
        
        
    def helper(self, strs):
        # map_s = {}
        # map_s for strs[0]
        # map_s_cand = []
        # str2anagrams = {}
        # for s in str[1] ==> str[-1]:
        #     for cand in map_s_cand
        #         if not is_anagram(cand, s):
        #             update map_s_cand
        #         else
        #             update str2anagrams
            
        # res = []        
        # for key in str2anagrams:
        #     append valu into res
            
        # return res
        
        map_s = {}  # represents strs[0]
        cur_str = strs[0]
        for i in range(len(cur_str)):
            map_s[cur_str[i]] = map_s.get(cur_str[i], 0) + 1
            
        # map_s_candidates = []
        # map_s_candidates.append(map_s)
        map_s_candidates = {cur_str: map_s}
        str2anagrams = {cur_str: [cur_str]}
        for i in range(1, len(strs)):
            cur_str = strs[i]
            # for key in map_s_candidates.keys():
            # map_tmp = {}
            group_key = None
            for key in map_s_candidates.keys():
                # print("cand: ",  map_s_candidates[key], "; cur_str: ", cur_str)
                if self.is_anagram(map_s_candidates[key].copy(), cur_str):
                    str2anagrams[key] += [cur_str]
                    group_key = key
                    break
                
            if group_key == None:
                map_tmp = {}
                for i in range(len(cur_str)):
                    map_tmp[cur_str[i]] = map_tmp.get(cur_str[i], 0) + 1
                    
                map_s_candidates[cur_str] = map_tmp
                str2anagrams[cur_str] = [cur_str]
        # print("map_s_candidates: \n", map_s_candidates)
        # print("str2anagrams: \n", str2anagrams)
        
        res = []
        for key in str2anagrams.keys():
            res.append(str2anagrams[key])
        return res
                
    def is_anagram(self, map_s, t):
        for i in range(len(t)):
            if t[i] not in map_s: 
                return False
            
            map_s[t[i]] -= 1
            if map_s[t[i]] == 0:
                del map_s[t[i]]
        
        for val in map_s.values():
            if val != 0:
                return False
        return True
    
    def old(self, strs):
        res = []
        d = defaultdict(list)
        for i in range(len(strs)):
            item = ''.join(sorted(strs[i]))
            # print(item)
            d[item].append(strs[i])   # {aet: [eat, ]}
        # print(d)
        return [l for l in d.values()]
        
        
        
    def groupAnagrams_old(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        # build a one-hot mapping 
        for s in strs:
            onehot = self.chars2onehot(s)
            # if onehot not in d: # unhashable type: 'list' CAUTIOUS! should turn into tuple for hashable
            if tuple(onehot) not in d:
                d[tuple(onehot)] = [s]  # [100101] ==> eat
            else:
                d[tuple(onehot)].append(s)
            # d[onehot] = d.get(onehot, 0) + 1
            # {[1 0 0 0 0 1 0 0 1 0 ]}
        
        ret = []
        for key in d.keys():
            ret.append(d[key])
        
        return ret
        
    def chars2onehot(self, s):
        onehot = [0] * 26
        for c in s:
            onehot[ord(c)-97] += 1  # 97 is ord('a') CAUTIOUS!!
        
        return onehot
# @lc code=end

