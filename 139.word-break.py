#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (38.56%)
# Likes:    3735
# Dislikes: 203
# Total Accepted:    498.7K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
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
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
'''
     a b c d e       [ b, c, de]
dp 1 0 0 0 0 0
'''
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        
        max_len = 0
        for word in ws:
            max_len = max(max_len, len(word))
        
        dp = [False] * (len(s)+1)
        
        dp[0] = True
        for end in range(1, len(dp)):
            start = end-1
            # while start >=0: OPTIMIZATION↓↓　
            while start >=0 and start >= end-max_len:
                if s[start:end] in ws and dp[start]:
                    dp[end] = True
                    break
                start -= 1
        print(dp)
        return dp[-1]
        
    def wordBreak_old(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
        
        ws = set(wordDict) # wordSet
        dp = [False] * len(s)   # means states
        # abcde
        dp[0] = s[0] in ws

        for i in range(1, len(dp)):
            # print(i)
            
            if s[:i+1] in ws:
                dp[i] = True
                continue 
            # print(dp)            
            start = i
            
            """
            dp[1] =     s[1:1+1] in ws and dp[0]    # s[1] in ws and dp[0]  
                        or 
                        s[0:1+1] in ws                     
            

            dp[2] =     s[2:2+1] in ws and dp[1]    ## s[2]
                        or 
                        s[1:2+1] in ws and dp[0] 
                        or 
                        s[0:2+1] in ws
            """
            while start >= 0:
                # if s[start:i+1] in ws and dp[start-1]:
                if dp[start-1] and s[start:i+1] in ws:
                    dp[i] = True
                    break
                start -= 1
                
        return dp[-1]
# Time complexity : O(n^2). Two loops are their to fill \text{dp}dp array.
# Space complexity : O(n). Length of pp array is n+1n+1.            
# @lc code=end

