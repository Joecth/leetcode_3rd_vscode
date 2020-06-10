# There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

# The goal is to merge the stones in one pile observing the following rules:

# At each step of the game,the player can merge two adjacent piles to a new pile.
# The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.

# Example
# Example 1:

# Input: [3, 4, 3]
# Output: 17
# Example 2:

# Input: [4, 1, 1, 4]
# Output: 18
# Explanation:
#   1. Merge second and third piles => [4, 2, 4], score = 2
#   2. Merge the first two piles => [6, 4]，score = 8
#   3. Merge the last two
import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # return self.memo_search(A, 0, len(A) - 1, {})
        return self.greedy_as_leetcode_1130(A)

    def greedy_as_leetcode_1130(self, A):
        if not A: 
            return 0
        
        B = A.copy()
        res = 0
        nbr = 0
        while len(B) > 1:
            n = len(B)
            idx = B.index(min(B))
            # print(idx)
            if 0 < idx < n-1:
                cur = B[idx] + min(B[idx-1], B[idx+1])
                # nbr = B.index(min(B[idx-1], B[idx+1]))
                nbr = idx - 1 if B[idx-1] < B[idx+1] else idx + 1
            else:
                cur = B[idx] + B[1 if idx == 0 else idx-1]
                nbr = 1 if idx == 0 else idx-1
                
            res += cur
            B[nbr] = cur
            # print(cur, nbr, res)
            B.pop(idx)
            # print(B)
        return res


    def memo_search(self, A, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
            
        if start >= end:
            return 0
            
        cost = sum(A[start:end + 1])
        minimum = sys.maxsize
        for mid in range(start, end):
            left = self.memo_search(A, start, mid, memo)
            right = self.memo_search(A, mid + 1, end, memo)
            print(start, end, left, right, minimum, left+right+cost)
            minimum = min(minimum, left+right+cost)
        
        memo[(start, end)] = minimum
        print("MEMO: ",  memo)
        return minimum
print(Solution().stoneGame([1, 1, 1, 1]))