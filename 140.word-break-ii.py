#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (30.06%)
# Likes:    1630
# Dislikes: 351
# Total Accepted:    213.4K
# Total Submissions: 703.5K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper_MLE(s, wordDict)
        # return self.helper_TLE_idx_chain(s, wordDict)
    
    def helper_TLE_idx_chain(self, s, wordDict):
        dp_seq = self.helper_idx_chain(s, wordDict)
        if len(s)-1 not in dp_seq.keys():
            return []
        
        ans = []
        # print(list(dp_seq.values())[-1])
        for seq in list(dp_seq.values())[-1]:
            one = ''
            start = 0
            for idx in seq:
                one = one + s[start:idx+1] + " "
                start = idx+1
            ans.append(one[:-1])
        return ans
                
    
    def helper_idx_chain(self, s, wordDict):  
        """ build indexes chain, still TLE... """
        # dp = [[]] * len(s)  # [[], [], [], ....., []]
        dp = defaultdict(list)
        dp_seq = defaultdict(list)
        ws = set(wordDict)
        max_len = 0
        for word in ws:
            max_len = max(len(word), max_len)
        
        if s[0] in ws:
            # dp[0] += [s[0]]
            dp[0].append(s[0]+" ")
            dp_seq[0].append([0])
        # else:
        #     dp_seq[0].append([-1])
        # print(dp)
        # return []
        for i in range(1, len(s)):
            """ abcde   [b,c, d, e]
            dp[1] = s[1:1+1](s[1]) in ws  and  dp[0]==True(len(dp[0])>0)
                    or 
                    
                    s[0:1+1] in ws 
                    
            dp[2] = s[2:2+1](s[2]) in ws  and dp[1]==True(len(dp[1])>0)
                    or 
                    s[1:2+1] in ws and dp[0]==True(len(dp[0])>0)
                    or 
                    
                    s[0:2+1] in ws 
            """
            start = i
            # while start > 0: Optimization　↓↓
            while start > 0 and start > i-max_len:
                token = s[start:i+1] # the changing token as Sliding Windo0w
                # print(f"START: i:{i}, start:{start}, token:{token}, dp:{dp}")            
                if token in ws and len(dp[start-1]) > 0:
                    for st in dp[start-1]:
                        dp[i].append(st+token+" ")
                    for seq in dp_seq[start-1]:
                    # for seq in dp_seq.get(start-1):
                        # print (seq)
                        # print(seq)
                        dp_seq[i].append(seq+[i])   # seq.append(i)
                        # print(seq)
                start -= 1
            
            token = s[start:i+1]    # Now, start is 0 
            if token in ws:
                dp[i].append(s[start:i+1]+" ")
                dp_seq[i].append([i])
                
            # print(f"END: i:{i}, start:{start}, token:{token}, dp:{dp}")
        # print(dp_seq)
        for i in range(len(dp[len(s)-1])):
            dp[len(s)-1][i] = dp[len(s)-1][i].rstrip()
        return dp_seq
    
    def helper_MLE(self, s, wordDict):
        # dp = [[]] * len(s)  # [[], [], [], ....., []]
        dp = defaultdict(list)
        dp_seq = defaultdict(list)
        ws = set(wordDict)
        max_len = 0
        for word in ws:
            max_len = max(len(word), max_len)
            
        if s[0] in ws:
            # dp[0] += [s[0]]
            dp[0].append(s[0]+" ")
            dp_seq[0].append([0])
        # else:
        #     dp_seq[0].append([-1])
        # print(dp)
        # return []
        for i in range(1, len(s)):
            """ abcde   [b,c, d, e]
            dp[1] = s[1:1+1](s[1]) in ws  and  dp[0]==True(len(dp[0])>0)
                    or 
                    
                    s[0:1+1] in ws 
                    
            dp[2] = s[2:2+1](s[2]) in ws  and dp[1]==True(len(dp[1])>0)
                    or 
                    s[1:2+1] in ws and dp[0]==True(len(dp[0])>0)
                    or 
                    
                    s[0:2+1] in ws 
            """
            start = i
            while start > 0 and start > i-max_len:
                token = s[start:i+1] # the changing token as Sliding Windo0w
                # print(f"START: i:{i}, start:{start}, token:{token}, dp:{dp}")            
                if token in ws and len(dp[start-1]) > 0:
                    for st in dp[start-1]:
                        dp[i].append(st+token+" ")
                    for seq in dp_seq[start-1]:
                    # for seq in dp_seq.get(start-1):
                        # print(seq)
                        dp_seq[i].append(seq+[i])   # seq.append(i)
                        # print(seq)
                start -= 1
            
            token = s[start:i+1]    # Now, start is 0 
            if token in ws:
                dp[i].append(s[start:i+1]+" ")
                dp_seq[i].append([i])
                
            # print(f"END: i:{i}, start:{start}, token:{token}, dp:{dp}")
        # print(dp_seq)
        for i in range(len(dp[len(s)-1])):
            dp[len(s)-1][i] = dp[len(s)-1][i].rstrip()
        return dp[len(s)-1]
# @lc code=end

