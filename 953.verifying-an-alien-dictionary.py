#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (54.94%)
# Likes:    721
# Dislikes: 282
# Total Accepted:    99.7K
# Total Submissions: 182.5K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.
# 
# Example 1:
# 
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
# 
# 
# Example 2:
# 
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
# 
# 
# Example 3:
# 
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
# 
# 
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # return self.helper_old(words, order)
        # return self.helper_vertical(words, order) # any intuition that this failed?
        # return self.helper_wordbyword(words, order)
        return self.helper_4rd(words, order)
    
    def helper_4rd(self, words, order):
        map_order = {}
        for i in range(len(order)):
            map_order[order[i]] = i
        for i in range(len(words)-1):
            if self.is_Bigger(words[i], words[i+1], map_order):
                return False
        return True
    def is_Bigger(self, word1, word2, map_order):
        for i in range(min(len(word1), len(word2))):
            # if order.index(word1[i]) > order.index(words2[i]):
            if map_order[word1[i]] > map_order[word2[i]]:
                return True
            elif map_order[word1[i]] < map_order[word2[i]]:
                return False
            else:
                pass
        if len(word1) > len(word2):
            return True
        return False
        
    def helper_wordbyword(self, words, order):
        # map_o = {}
        map_o = {order[i]:i for i in range(len(order))}
        # print (map_o)
        
        for i in range(len(words)-1):
            if self.is_bigger(words[i], words[i+1], map_o):
                return False
        return True
    
    def is_bigger(self, w1, w2, map_o):
        for i in range(min(len(w1), len(w2))):
            if map_o[w1[i]] > map_o[w2[i]]:
                return True
            if map_o[w1[i]] < map_o[w2[i]]:
                return False
            
        if len(w1) > len(w2):   # case like ["apple", "app"]
            return True
        return False
    
    def helper_vertical_FAILED(self, words, order):
        
        max_len = max(len(word) for word in words)
        # words_set = set(words)
        
        map_o = {}
        for i in range(len(order)):
            ch = order[i]
            map_o[ch] = i
        
        dont_check = set()
        for i in range(max_len):
            min_idx = map_o[words[0][i]]
            for j in range(1, len(words)):
                if j in dont_check:
                    continue
                    
                ch = words[j][i]
                if map_o[ch] < min_idx:
                    return False
                elif map_o[ch] > min_idx:
                    dont_check.add(j)       # don't check this word at next index
                    min_idx = map_o[ch]
                else:
                    pass
        return True
        
    def helper_old(self, words, order):
        # 1. build mapping score for each c in order str
        # 2. assign pointer at head of each of the word in words and check the mapping score relationship
        # 3. empty hel'' < hel'l'
        
        if not words or not order: return False
        score = {'':0}
        for idx in range(len(order)):
            score[order[idx]] = idx+1
            
        n = len(words)
        
        for i in range(len(words)-1):
            # compare word by word
            a, b = words[i], words[i+1]
            _len = min(len(a), len(b))
            for k in range(_len):
                if score[a[k]] < score[b[k]]:
                    break
                elif score[a[k]] == score[b[k]]:
                    continue
                if score[a[k]] > score[b[k]]:    # SERIOUSLY WRONG!!! NOT EACH CHAR, ONLY FIRST CHAR to be compared!!!
                    # print(a[k], b[k])
                    return False
                
            # if len(a) > len(b):   # for [apple, app], but failed when [kuvp, q]
                # return False
            if len(a) > len(b) and a[:_len] == b:
                return False
        return True
# @lc code=end

