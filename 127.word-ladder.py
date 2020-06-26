#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (27.97%)
# Likes:    2857
# Dislikes: 1115
# Total Accepted:    404.1K
# Total Submissions: 1.4M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
from collections import deque
import string
class Solution:
# class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        return self.my_again2(beginWord, endWord, wordList)
        return self.my_BiBFS2(beginWord, endWord, wordList)
        # return self.my_graph_sol_TLE(beginWord, endWord, wordList)
        # return self.my_bfs(beginWord, endWord, wordList)
        # return self.my_bibfs(beginWord, endWord, wordList) # 標記顏色法，沒絲絲的方法好
        # return self.sisi_bibfs(beginWord, endWord, wordList)    # 1) Faster whan one side is much wider; 2) Doesn't depend on ascii_lowercase
    
    def my_again2(self, beginWord, endWord, wordList):
        # https://leetcode-cn.com/problems/word-ladder-ii/solution/ru-guo-ni-fa-xian-kan-bie-ren-de-ti-jie-kan-bu-don/
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        level_map = {}
        word_map = {}
        Q = collections.deque([beginWord])
        visited = set()
        found = False
        level = 0
        
        level_map[beginWord] = 0
        visited.add(beginWord)
        
        while Q:
            level_size = len(Q)
            
            for _ in range(level_size):
                word = Q.popleft()
                if word == endWord:
                    return level+1  # 30% IMPROVEMENT
                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word not in word_set:
                            continue
                        
                        if new_word in word_map:    # parent跟之前的不同；還是幫它建圖，只是不再入隊
                            word_map[new_word].append(word)
                        else:
                            word_map[new_word] = []
                            word_map[new_word].append(word)
                        
                        if new_word in visited:
                            continue
                        if new_word == endWord:
                            found = True
                            
                            
                        level_map[new_word] = level + 1
                        Q.append(new_word)
                        visited.add(new_word)
            level += 1
        
        return 0
        # if not found:
        #     return 0        
        # return level_map[endWord] + 1
    
    def my_BiBFS2(self, beginWord, endWord, wordList):
        """ VERSION 0625, SAME as sisi_bibfs """
        if not beginWord or not endWord:
            return []
        
        """
        hit --> h*t 
                    ==> hot --> *ot
                                    ==> dot --> do*
                                                    ==> dog --> *og
                                                                    ==> cog
                                    ==> lot --> lo*
                                                    ==> log --> *og
                                                                    ==> cog
        """

        word_set = set(wordList)    # for Quick Access later on
        if endWord not in word_set:
            return 0
        # Build Graph
        map_d = {}  # edges
        for i in range(len(word_set)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                map_d[pattern] = map_d.get(pattern, []) + [word]
                

        Q = collections.deque()
        end_Q = collections.deque()
        distance = {}
        end_distance = {}
        
        Q.append((beginWord, 1))
        end_Q.append((endWord, 1))
        distance[beginWord] = 1
        end_distance[endWord] = 1
        while Q and end_Q:
            res = self.bfs2(Q, distance, end_distance, map_d)
            if res >= 0:
                # TODO:
                # pass
                print('distance: ', distance)
                print('end_distance: ', end_distance)
                return res
            res = self.bfs2(end_Q, end_distance, distance, map_d)
            if res >= 0:
                # pass
                print('distance: ', distance)
                print('end_distance: ', end_distance)
                return res
            print('distance: ', distance)
            print('end_distance: ', end_distance)
        return 0
    
    
    def bfs2(self, Q, distance, other_distance, map_d):
        now_word, now_depth = Q.popleft()
        for i in range(len(now_word)):
            pattern = now_word[:i] + "*" + now_word[i+1:]
            for next_word in map_d.get(pattern, []):
                if next_word in other_distance:
                    return now_depth + other_distance[next_word]
                
                if next_word not in distance:
                    Q.append((next_word, now_depth+1))
                    distance[next_word] = now_depth + 1
                    
        return -1
    
    def sisi_bibfs(self, beginWord, endWord, wordList):
        ws = set(wordList)
        if endWord not in ws:
            return 0
        
        map_star = {}
        """ Build Graph """
        for word in wordList:
            arr = []
            for i in range(len(word)):
                arr.append(word[:i] + '*' + word[i+1:])
            for pat in arr:
                map_star[pat] = map_star.get(pat, []) + [word]
        # print(map_star)
        
        Q, end_Q = deque(), deque()
        Q.append((beginWord, 1))
        end_Q.append((endWord, 1))
        visited, end_visited = {beginWord:1}, {endWord:1}
        res = -1
        '''
            "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                          \    |        |      /
                           -- "lot" -- "log" --
            1). Is length of each string the same?  == >Yes
        '''
        while Q and end_Q:
            res = self.visitNode(Q, visited, end_visited, map_star)
            if res >= 0:
                return res
            res = self.visitNode(end_Q, end_visited, visited, map_star)
            if res >= 0:
                return res
        return 0
            
    def visitNode(self, Q, visited, other_visited, map_star):
        cur_w, depth = Q.popleft()
        arr = [cur_w[:i] + '*' + cur_w[i+1:] for i in range(len(cur_w))]
        for pattern in arr:
            if pattern in map_star:
                for next_w in map_star[pattern]:
                    if next_w in other_visited:
                        return depth + other_visited[next_w]

                    if next_w not in visited:
                        visited[next_w] = depth+1
                        Q.append((next_w, depth+1))
        return -1
        
            # cur_w, depth = end_Q.popleft()
            
        
    '''
            "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                          \    |        |      /
                           -- "lot" -- "log" --
            1). Is length of each string the same?  == >Yes
    '''
    def my_bibfs(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList: return 0
        ws = set(wordList)
        if endWord not in ws: return 0
        Q = deque()
        Q.append((beginWord, 'H', 1))
        visited = {beginWord: ('H', 1)}
        
        Q.append((endWord, 'T', 1))
        visited[endWord] = ('T', 1)
        while Q:
            for _ in range(len(Q)):
                cur, color, steps = Q.popleft()
                # print(cur, color)
                for j in range(len(cur)):
                    for ch in string.ascii_lowercase:
                        next_word = cur[:j] + ch + cur[j+1:]
                        if next_word in ws:
                            if next_word not in visited:
                                Q.append((next_word, color, steps+1))
                                visited[next_word] = (color, steps+1)
                            else:
                                # if cur.color != visited[next_word].color
                                if color != visited[next_word][0]:
                                    # print(cur, next_word, ', ', visited[next_word][0])
                                    # print(f"cur:{cur}, color:{color}, next_word:{next_word}, next_color:{visited[next_word][0]}")           
                                    return steps + visited[next_word][1]
                                    """ Following No Work, since it finds PARENT... and it's related to enque sequence btw startWord and endWord"""
                                    # if color == 'H':
                                    #     print(color, level)
                                    #     return level*2
                                    # else:
                                    #     print(color, level)
                                    #     return level+1
            # level += 1
            # step += 1
        return 0
                            
                
    
    def my_bfs(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList: return 0
        ws = set(wordList)
        Q = deque()
        Q.append(beginWord)
        visited = set([beginWord])
        level = 0
        while Q:
            for _ in range(len(Q)):
                cur = Q.popleft()
                print(cur)
                if cur == endWord: return level + 1
                for i in range(len(beginWord)):
                    for ch in string.ascii_lowercase:
                        next_word = cur[:i] + ch + cur[i+1:]
                        if next_word in ws and next_word not in visited:
                            Q.append(next_word)
                            visited.add(next_word)
            level += 1
        return 0
    
    def others_bfs(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            for i in range(len(queue)): # NOT NECESSARY, just for clear logics
                word, length = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':  # how if we don't know this?
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            wordList.remove(next_word)
                            queue.append([next_word, length + 1])
        return 0      
        # Time: O(L * 26 * n), Space: O(n)
        # https://youtu.be/hB_nYXFtwP0?t=274
        # https://leetcode.com/problems/word-ladder/discuss/40810/Python-BFS-solution         
        
    def others_BiBFS(self, beginWord, endWord, wordList):
        words = set(wordList)
        
        # Early exit
        if endWord not in words:
            return 0
        
        m = len(wordList[0])
            
        # A generator that returns the list of all adjacent words/nodes, possibly with some duplicates
        def neighbours(word):
            for i in range(m):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    adj = word[:i] + c + word[i+1:]
                    
                    if adj in words:
                        yield adj
        
        # Expands all nodes in a given queue <q> (i.e. all nodes at the same level)
        # <q_visited>: set of nodes already visited by <q>
        # <other_visited>: set of nodes already visited by the other BFS queue
        def expand(q, q_visited, other_visited):            
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                
                for adj in neighbours(word):
                    if adj in q_visited:
                        continue
                    
                    if adj in other_visited:
                        return True
                    
                    q.append(adj)
                    q_visited.add(adj)
                    
            return False
        
        
        head = deque() # queue for BFS starting from beginWord
        tail = deque() # queue for BFS starting from endWord        
        head_visited = set() # set of visited nodes for head BFS
        tail_visited = set() # set of visited nodes for tail BFS
        
        head.append(beginWord)
        tail.append(endWord)
        head_visited.add(beginWord) # add in case beginWord is in wordList
        tail_visited.add(endWord)
        
        # Two-ended BFS, always choose the queue of smaller size
        # to minimise the number of nodes to expand per level,
        # i.e. maximise efficiency!
        dist = 2
        while head and tail:
            if len(head) <= len(tail):            
                if expand(head, head_visited, tail_visited):
                    return dist
            else:
                if expand(tail, tail_visited, head_visited):
                    return dist
            dist += 1
        return 0


    '''
            "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                          \    |        |      /
                           -- "lot" -- "log" --
            1). Is length of each string the same?  == >Yes
    '''
    def my_graph_sol_TLE(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # treat each string as vertex, and then BFS to find min path 
        # return self.helper_TLE(beginWord, endWord, wordList)
        return self.helper_TLE(beginWord, endWord, wordList)
    
    def helper(self, beginWord, endWord, wordList):
        pass    

        
    
    def helper_TLE(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        # should add beginWord into WordList at the beginning
        wordList.append(beginWord)
        # '''TLE　HERE ?!
        map_nbr = self.build_adjacent(wordList)
        
        Q = deque()
        Q.append((beginWord, 1, 'blue'))  # BFS from begin  # so, if end ifs just his adjacent, ans would be 2
        Q.append((endWord, 1, 'red'))   # Bi-direction BFS
        
        visited = dict()
        visited[beginWord] = (1, 'blue')
        visited[endWord] = (1, 'red')

        # '''     TLE, so I try bi-directional BFS first, then try to build adjacent table dynamically
        # begin end 1 2 -1 -2 3 4 -3 -4(in set! then return i+1)
        while Q:
            len_Q = len(Q)
            for i in range(len_Q):
                cur, i, color = Q.popleft()   # i means Nth node in path
                # visited[node]
                nbrs = map_nbr[cur]
                '''
                "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                              \    |        |      /
                               -- "lot" -- "log" --
                1). Is length of each string the same?  == >Yes
                '''
                for j in range(len(nbrs)):
                    # if nbrs[j] == endWord:
                    #     return i+1      # return RIGHT ans here
                    # set visit
                    if nbrs[j] not in visited:
                        # visited.add(nbrs[j])
                        visited[nbrs[j]] = (i+1, color)
                        Q.append((nbrs[j], i+1, color))
                    else:
                        m, color_m = visited[nbrs[j]]
                        if color != color_m:
                            return i+m #+1
        return 0
        
    def build_adjacent(self, wordList):# Adj table
        map_nbr = defaultdict(list)
        leng = len(wordList[0])
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.is_connected(wordList[i], wordList[j]):
                    map_nbr[wordList[i]] += [wordList[j]]  # k:hot, v:[dot, lot]  # since it's  Bi-Directional
                    map_nbr[wordList[j]] += [wordList[i]]
        return map_nbr
                        
    def is_connected(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
            if count > 1:
                return False
        return True
            
    def helper_FAILED(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        map_nbr = self.build_adjacent(wordList)
        print(map_nbr)
        # TODO: use in_degree to earlier prune unavailable cases?
        Q = deque()
        # BFS from begin
        Q.append((beginWord, 'blue'))    # so, if end ifs just his adjacent, ans would be 2
        # Bi-direction BFS
        Q.append((endWord, 'red'))
        
        visited = dict()
        visited[beginWord] = 'blue'
        visited[endWord] = 'red'
        
        step = 1
        # '''     TLE, so I try bi-directional BFS first, then try to build adjacent table dynamically
        # begin end 1 2 -1 -2 3 4 -3 -4(in set! then return i+1)
        while Q:
            len_Q = len(Q)
            step += 1
            for i in range(len_Q):
                cur, color = Q.popleft()   # i means Nth node in path
                '''
                "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                              \    |        |      /
                               -- "lot" -- "log" --
                1). Is length of each string the same?  == >Yes
                '''
                # for j in range(len(nbrs)):
                for nbr in map_nbr[cur]:
                    if nbr not in visited:
                        visited[nbr] = color
                        Q.append((nbr, color))
                    else:
                        color_m = visited[nbr]
                        if color != color_m:
                            # return i+m #+1
                            return 2*step + 1
        return 0
# @lc code=end

