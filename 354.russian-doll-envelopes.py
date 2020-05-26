#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (34.98%)
# Likes:    981
# Dislikes: 37
# Total Accepted:    62.8K
# Total Submissions: 178.5K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
# 
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
# 
# Note:
# Rotation is not allowed.
# 
# Example:
# 
# 
# 
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        elif len(envelopes) == 1: return 1
        arr = sorted(envelopes, key=lambda envelope: (envelope[0], -envelope[1]))
        # return self.helper_FAILED(arr)
        # return self.O_NxN(arr)
        return self.O_NxlogN(arr)

    def O_NxlogN(self, envelopes):
        dp = []
        
        for i in range(len(envelopes)):
            if not dp:
                dp.append(envelopes[i][1])
                continue

            # if envelopes[i][0] > dp[-1] and envelopes[i][1] > dp[-1][1]:
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                target = envelopes[i][1]
                start, end = 0, len(dp)
                # To find elem >= envelopes[i][1]
                while start + 1 < end:
                    mid = start + (end-start)//2
                    if dp[mid] >= target:
                        end = mid
                    else:
                        start = mid
                if dp[start] >= target:
                    dp[start] = target
                elif dp[end] >= target:
                    dp[end] = target
                
            # print(dp)
        return len(dp)    
    
    def O_NxN(self, envelopes):
        dp = []
        
        for i in range(len(envelopes)):
            if not dp:
                dp.append(envelopes[i][1])
                continue

            # if envelopes[i][0] > dp[-1] and envelopes[i][1] > dp[-1][1]:
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                for j in range(len(dp)):
                    if envelopes[i][1] <= dp[j]:
                        dp[j] = envelopes[i][1]
                        break
            # print(dp)
        return len(dp)
    
    def helper_FAILED(self, envelopes):
        dp = []
        for envelope in envelopes:
            if not dp:
                dp.append(envelope)
                continue
                
            if envelope[0] > dp[-1][0] and envelope[1] > dp[-1][1] :
                dp.append(envelope) 
            else:
                for j in range(len(dp)):
                    # NO USE
                    # if envelope[0] <= dp[j][0] and envelope[1] > dp[j][1]:
                    #     break
                    # elif envelope[0] > dp[j][0] and envelope[1] <= dp[j][1]:
                    #     break
                    if envelope[0] <= dp[j][0] and envelope[1] <= dp[j][1]:
                        dp[j] = envelope
                        break
            print(dp)
        return len(dp)        
# @lc code=end

