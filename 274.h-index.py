#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (35.23%)
# Likes:    541
# Dislikes: 913
# Total Accepted:    144.6K
# Total Submissions: 409.7K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return self.helper(citations)
        
    def helper(self, citations):
        n = len(citations)
        bucket = [0 for _ in range(n+1)]
        
        for citation in citations:
            if citation > n:
                bucket[n] += 1
            else:
                bucket[citation] += 1
        print(bucket)
        
        carry = 0
        for j in reversed(range(n+1)):
            if carry + bucket[j] >= j:
                return j
            else:
                carry += bucket[j]
        return 1
            
        

    """
    6 5 3 1 0
    0 1 2 3 4
    """
    def old():
        citations.sort(reverse=True)
        count = 0
        for i in range(len(citations)):
            if i < citations[i]:
                count += 1
            else: break
        return count
        
        # return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
        
# @lc code=end

