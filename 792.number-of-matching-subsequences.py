#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (47.35%)
# Likes:    940
# Dislikes: 66
# Total Accepted:    41.4K
# Total Submissions: 87.3K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#

# @lc code=start
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S or not words: return 0
        # return self.BF(S, words)
        # return self.sol_hash_counting(S, words) # Sequence cannot be guaranteed
        # return self.word_by_word_TLE(S, words)
        # return self.char_by_char_TLE(S, words)
        # return self.sol_mine(S, words)
        # return self.my_again(S, words)    # SAME as above line
        # return self.sol_special(S, words)
        return self.hash_next_chars(S, words)
    
    # But seems like the time complexity is O(S + W * L) # 50*5000 + 500000
    # ref: https://leetcode.com/problems/number-of-matching-subsequences/discuss/117598/Java-solution-using-HashMap-and-Queue
    def hash_next_chars(self, S, words):
        # map_w = collections.defaultdict(set)
        map_w = collections.defaultdict(collections.deque)
        for i in range(len(words)):
            word = words[i]
            # if word[0] not in map_w:
            #     map_w[word[0]] = deque([])
            map_w[word[0]].append([word, 0])
        # print(map_w)
        count = 0
        for i in range(len(S)):
            ref_char = S[i]
            # if ref_char not in map_w:     # NOT NECESSARY
            #     continue
            Q = map_w[ref_char]
            for j in range(len(Q)):     #sigma(len(word[idx]))   
                # now_word, now_idx = Q[j]   # FAILED, combined w/ Line44, 'cause of Line41!! 直接被消失掉了!!!
                now_word, now_idx = Q.popleft()   #OK!
                now_idx += 1
                if now_idx == len(now_word):
                    count += 1
                else:
                    map_w[now_word[now_idx]].append([now_word, now_idx])
                # print(now_word, now_idx)
            # del map_w[ref_char]     # FAILED, combined w/ Line36
        return count   
        
    from bisect import bisect_left
    def my_again(self, S, words):
        def is_subsq(map_S, word):
            prev = -1
            for i in range(len(word)):
                arr = map_S[word[i]]
                target = prev + 1
                index = bisect_left(arr, target)                     
                if index == len(word):
                    return True
                    # return False
                # prev = index  ==> prev should be related to idx in S, not idx in arr
                print(word, arr, index)
                prev = arr[index]
            return False
                
        map_S = collections.defaultdict(list)
        for i in range(len(S)):
            map_S[S[i]].append(i)
        count = 0
        for word in words:
            if is_subsq(map_S, word):
                count += 1
        return count
        
    def BF(self, S, words):
        def is_subsq(S, word):
            target_idx = 0
            for i, ch in enumerate(S):
                if ch == word[target_idx]:
                    target_idx += 1
                if target_idx == len(word):
                    return True
            return False
                    
        count = 0
        for word in words:
            if is_subsq(S, word):
                count += 1
        return count
            
    
    from copy import deepcopy
    def sol_hash_counting(self, S, words):
        # map_S = collections.defaultdict(int)
        def is_subsequence_hash_counting(map_S, word):
            for ch in word:
                if ch not in map_S:
                    return False
                map_S[ch] -= 1
                if map_S[ch] == 0:
                    del map_S[ch]
            return True
        map_S = {}
        for ch in S:
            map_S[ch] = map_S.get(ch, 0) + 1
        count = 0
        for word in words:
            if is_subsequence_hash_counting(deepcopy(map_S), word):
                count += 1
        return count
    
        # A[10000000]
        # new A(1000000000)
    def sol_special(self, S, words):
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return count        
        # ref: https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation

    # This one in the worst case:
    # O(len(S) + O(numbers of letters in all words)*log(len(S)))   
    # ref: https://leetcode.com/problems/number-of-matching-subsequences/discuss/117578/Simple-Python-solution
    def sol_mine(self, S, words):
        map_S = collections.defaultdict(list)
        for i, ch in enumerate(S):
            map_S[ch].append(i)
        count = 0
        for word in words:
            if self.is_subsequence_binary(map_S, word):
                count += 1
        return count
        
    from bisect import bisect_left
    def is_subsequence_binary(self, map_S, word):
        prev = -1
        for i in range(len(word)):
            ch = word[i]
            if ch not in map_S:
                return False
            
            arr = map_S[ch]
            target = prev+1
            """ Method 1: # binary search get first index larger than "pos" """
            index = bisect_left(arr, target)
            if index == len(arr):
                return False
            prev = arr[index]
            
            """ Method 2: B Search, implementation"""
            start, end = 0, len(arr)-1     
            while start + 1 < end:
                mid = start + (end - start)//2
                if arr[mid] >= target:
                    end = mid
                else:
                    start = mid
            if arr[start] >= target:
                prev = arr[start]
            elif arr[end] >= target:
                prev = arr[end]
            else:
                return False            
        return True
    # https://www.youtube.com/watch?v=l8_vcmjQA4g&feature=youtu.be        
        
        
    def char_by_char_TLE(self, S, words):
        pos = [0] * len(words)
        count = 0
        for i in range(len(S)):
            for j in range(len(words)):
                word = words[j]
                if pos[j] == -1:
                    continue
                # print(word, j, pos, S[i])
                if word[pos[j]] == S[i]:
                    pos[j] += 1
                if pos[j] == len(word):
                    pos[j] = -1    # prevent OOR in next round
                    count += 1
        # count = 0
        # for n in pos:
        #     if n == -1:
        #         count += 1
        return count
    
    def word_by_word_TLE(self, S, words):
        count = 0
        for word in words:
            if self.is_subsequence(S, word):
                count += 1
        return count

    def is_subsequence(self, S, word):
        j = 0
        for i in range(len(S)):
            if S[i] == word[j]:
                j += 1
            if j == len(word):
                return True
        return False
            
# @lc code=end

