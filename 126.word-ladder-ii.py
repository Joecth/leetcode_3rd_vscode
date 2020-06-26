#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (20.79%)
# Likes:    1701
# Dislikes: 243
# Total Accepted:    181.4K
# Total Submissions: 834.8K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
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
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
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
# Output: []
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
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:    
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        return self.my_again2(beginWord, endWord, wordList)
        # return self.my_again_one_directional(beginWord, endWord, wordList)
        # return self.my_again_bi_directional(beginWord, endWord, wordList)   
        """ https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/ """
        # return self.my_buggy_FAILED(beginWord, endWord, wordList)
        # return self.findLadders_others_bibfs(beginWord, endWord, wordList)
        # return self.other_python_clear(beginWord, endWord, wordList)
        # return self.my_bfs(beginWord, endWord, wordList)        
        # wordSet = set(wordList)
        # if endWord not in wordSet:
        #     return []
        # return self.teacher(beginWord, endWord, wordSet)
        
        
    def my_again2(self, beginWord, endWord, wordList):
        # https://leetcode-cn.com/problems/word-ladder-ii/solution/ru-guo-ni-fa-xian-kan-bie-ren-de-ti-jie-kan-bu-don/  , SIMILAR TO self.other_python_clear
        # BTW, level ISSUE in https://leetcode.com/problems/word-ladder-ii/discuss/487138/Python-Easy-Clean-Readable-Code
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
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
            
        if not found:
            return []
        # print(level_map)
        # print(word_map)
        
        res = []
        def dfs(res, path, begin_word, word, word_map, level_map):
            if word == begin_word:
                tmp = [begin_word]
                tmp.extend(path)
                res.append(tmp[:])
                return 
            
            path.insert(0, word)
            if word in word_map:
                for parent in word_map[word]:
                    if level_map[parent] + 1 == level_map[word]:
                        dfs(res, path, begin_word, parent, word_map, level_map)
            path.pop(0)
        dfs(res, [], beginWord, endWord, word_map, level_map)
        return res
    
    # def is_valid(self, word, visited):
        # if 
    
    def my_again_bi_directional(self, beginWord, endWord, wordList):
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表
        found = self.__bidirectional_bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bidirectional_bfs(self, beginWord, endWord, word_set, successors):
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        found = False
        forward = True
        word_len = len(beginWord)
        while begin_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited
                forward = not forward

            next_level_visited = set()
            for current_word in begin_visited:
                word_list = list(current_word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                found = True
                                # 在另一侧找到单词以后，还需把这一层关系添加到「后继结点列表」
                                self.__add_to_successors(successors, forward, current_word, next_word)
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                self.__add_to_successors(successors, forward, current_word, next_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            if found:
                break
        return found

    def __add_to_successors(self, successors, forward, current_word, next_word):
        if forward:
            successors[current_word].add(next_word)
        else:
            successors[next_word].add(current_word)

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


    def my_again_one_directional(self, beginWord, endWord, wordList):
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表

        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True

                                # 避免下层元素重复加入队列，这里感谢 https://leetcode-cn.com/u/zhao-da-ming/ 优化了这个逻辑
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)

                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()

        
        
    
    def other_python_clear(self, beginWord, endWord, wordList):
        def dfs(word):
            tmp.append(word)
            if word == endWord:
                res.append(list(tmp))
                tmp.pop()
                return 
            if word in graph:
                for nei in graph[word]:
                    if dist[nei] == dist[word]+1:
                        dfs(nei)
            tmp.pop()

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        q = collections.deque([(beginWord, 0)])
        dist = {}
        graph = collections.defaultdict(set)
        seen = set([beginWord])
        while q:
            u, d = q.popleft()
            dist[u] = d
            for i in range(len(u)):
                for alph in alphabets:
                    if alph != u[i]:
                        new = u[:i]+alph+u[i+1:]
                        if new in wordSet:
                            graph[u].add(new)
                            graph[new].add(u)
                            if new not in seen:
                                q.append((new, d+1))
                                seen.add(new)
        if endWord not in dist:
            return []
        res = []
        tmp = []
        dfs(beginWord)
        return res 
        # https://leetcode.com/problems/word-ladder-ii/discuss/241584/Python-solution
    
    def findLadders_others_bibfs(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for i in range(n):
                    first, second = x[:i], x[i+1:]
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        y = first + c + second
                        if y in words:
                            if y in eq: 
                                found = True
                            else: 
                                nq.add(y)
                            tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq): 
                bq, eq, rev = eq, bq, not rev
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord) 
        # https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS
        
    
    def my_bfs(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # stores current word and all possible sequences how we got to it

        while layer:
            # print(layer)    
            newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                for i in range(len(word)): # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []
    # https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
        
    '''
            "hit -- "["hot"-- "dot" -- "dog" --- "cog"]
                          \    |        |      /
                           -- "lot" -- "log" --
            1). Is length of each string the same?  == >Yes
    '''    
    
    def teacher(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, distance, dict)
        
        results = []
        self.dfs(start, end, distance, dict, [start], results)
        
        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
                        
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return
        
        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
        
    
    def my_buggy_FAILED(self, beginWord, endWord, wordList):
        # ISSUES:
        # 1. early return and the not complete distance dict...
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
            return []
        # if beginWord in word_set:
        #     word_set.remove(beginWord)
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
        
        path = defaultdict(set)
        end_path = defaultdict(set)
        meetup_depth = sys.maxsize
        while Q and end_Q:
            begin_meetup_depth = self.bfs2(Q, distance, end_distance, map_d, path)
            meetup_depth = min(meetup_depth, begin_meetup_depth)
            if meetup_depth != sys.maxsize:
                break
            end_meetup_depth = self.bfs2(end_Q, end_distance, distance, map_d, end_path)
            meetup_depth = min(meetup_depth, end_meetup_depth)
            if meetup_depth != sys.maxsize:
                break
        print(meetup_depth)
        # print('path: ', path)
        # print('end_path: ', end_path)
        
        if meetup_depth == sys.maxsize:
            return []
        
        end_path_reversed = {}
        for key, val in end_path.items():
            for word in val:
                end_path_reversed[word] = end_path_reversed.get(word, []) + [key]

        end_res = []
        end_path_reversed.update(path)
        print('end_path_reversd: ', end_path_reversed)
        self.dfs_mine(endWord, end_path_reversed, [endWord], end_res, meetup_depth)
        return end_res
        
    def dfs_mine(self, end, end_path, item, res, meetup_depth):
        # if end not in end_path:
        
        if len(item) == meetup_depth:
            res.append(item[::-1].copy())
            return
        
        if end not in end_path:
            return 
        
        for word in end_path[end]:
            item.append(word)
            self.dfs_mine(word, end_path, item, res, meetup_depth)
            item.pop()
        
    def bfs2(self, Q, distance, other_distance, map_d, path):
        meetup_depth = sys.maxsize
        # for _ in range(len(Q)):
        len_Q = len(Q)
        for _ in range(len_Q):
            now_word, now_depth = Q.popleft()
            for i in range(len(now_word)):
                pattern = now_word[:i] + "*" + now_word[i+1:]
                for next_word in map_d.get(pattern, []):
                    if next_word in other_distance:
                        # path[next_word] = path.get(next_word, []) + [now_word]
                        path[next_word].add(now_word)
                        meetup_depth = now_depth + other_distance[next_word]

                    if next_word not in distance:
                        Q.append((next_word, now_depth+1))
                        distance[next_word] = now_depth + 1
                        # path[next_word] = path.get(next_word, []) + [now_word]
                        path[next_word].add(now_word)
        return meetup_depth    # -1 means not meetup yet
        # return -1
# @lc code=end

