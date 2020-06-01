#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (45.23%)
# Likes:    1674
# Dislikes: 61
# Total Accepted:    219K
# Total Submissions: 473.9K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.helper(s, [], 0)
        # return self.bt_sol(s)
        return self.res
        # https://youtu.be/YN0mGjMX8Bo?t=281    O(N*2^N)
    
    def bt_sol(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
                return
            
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans
    
    
    def helper(self, s, item, idx):
        if idx == len(s):
            self.res.append(item.copy())
            return
        
        for end in range(idx, len(s)):
            cur = s[idx:end+1]
            """
            if cur == cur[::-1]:
            """
            # if self.isPalindrome(s, idx, end+1):
            if self.isPalindrome(s, idx, end):
                item.append(cur)
                self.helper(s, item, end+1)
                item.pop()
            
    def isPalindrome(self, s: str, a=0, b=0) -> bool:
        start, end = a, min(len(s)-1, b)
        # start, end = 0, len(s)-1
        # while start + 1< end:  # side by side if even, and same one if odd, for pure string
        while start < end:
            # left, right = s[start], s[end]
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
                
            if s[start].lower() != s[end].lower():
                return False
                
            start += 1
            end -= 1
        return True        
# @lc code=end

