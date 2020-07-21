#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (60.51%)
# Likes:    479
# Dislikes: 15
# Total Accepted:    40K
# Total Submissions: 65.8K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters. 
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# 
# 
# Example 3:
# 
# 
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# 
# 
# Example 4:
# 
# 
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        return self.helper(s)
    
    def helper(self, s):
        rm_list = []
        """
        #  1. record invalid positions 
        #      A. forward 
        # if ( 
        #     score += 1
        # elif )
        #     if score > 0:
        #         score -= 1
        #     else:
        #         rm.append(i)     
        #      B. backward 
        #  2. post-process   
        # strBuilder to build a valid answer
        """
        """ Forward """
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                score += 1
            elif s[i] == ')':
                if score > 0:
                    score -= 1
                else:
                    rm_list.append(i)
                    
        """ Backward """
        score = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                score += 1
            elif s[i] == '(':
                if score > 0:
                    score -= 1
                else:
                    rm_list.append(i)
        # print(rm_list)
        """ Post Process """
        res = ""
        rm_list = set(rm_list)
        # prev_pos = -1
        # for pos in rm_list:
        #     res += s[prev_pos:pos]
        #     prev_pos = pos
        for j in range(len(s)):
            if j not in rm_list:
                res += s[j]
        return res
#         return self.helper_old(s)   # two pass filtering
    
#     def helper_old(self, s):
#         li = []
#         balance = 0
#         for i in range(len(s)):
#             ch = s[i]
#             if ch == '(':
#                 balance += 1
#                 li.append(ch)
#             elif ch == ")":
#                 if balance == 0:
#                     continue
#                 balance -= 1
#                 li.append(ch)
#             else:
#                 li.append(ch)
#         # print(li)
        
#         # return li
#         ans = []
#         balance = 0
#         for j in reversed(range(len(li))):
#             ch = li[j]
#             if ch == ')':
#                 balance += 1
#                 ans.append(ch)
#             elif ch == '(':
#                 if balance == 0:
#                     continue
#                 balance -= 1
#                 ans.append(ch)
#             else:
#                 ans.append(ch)
#         return ''.join(ans[::-1])
    
                
            
            
#     def helper_failed(self, s):
#         pos = []
#         left = []
#         for i in range(len(s)):
#             if s[i] == '(':
#                 left.append(i)
#             elif s[i] == ')':
#                 if left:
#                     left.pop()
#                 else:
#                     pos.append(i)
                    
#         ''' 處理多餘 ) '''
#         # print(pos)
#         if pos:
#             ans = s[:pos[0]] 
#             for j in range(1, len(pos)-1):
#                 if pos[j]+1 != pos[j+1]:
#                     ans =  ans + s[pos[j]+1:]
#             ans += s[pos[-1]+1:]
#         else:
#             ans = s
#         if not left:
#             return ans
        
#         # print(ans)
#         ''' 處理多餘 ( '''
#         if left:
#             ret = ans[left[-1]+1:]
#             print('left:', left)
#             print('ans:', ans, ' ret: ',  ret)
#             for k in reversed(range(1, len(left)-1)):
#                 if left[k]-1 != left[k-1]:
#                     ret = ans[k+1:] + ret
#             ## till now , Pass all tests, but Failed at "()()((("
#             ## Thus, we need the following line
#             ret = ans[:max(0, left[0])] + ret
#         return ret
# @lc code=end

