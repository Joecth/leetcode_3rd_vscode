/*
 * @lc app=leetcode id=127 lang=java
 *
 * [127] Word Ladder
 *
 * https://leetcode.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (27.97%)
 * Likes:    2857
 * Dislikes: 1115
 * Total Accepted:    404.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * Given two words (beginWord and endWord), and a dictionary's word list, find
 * the length of shortest transformation sequence from beginWord to endWord,
 * such that:
 * 
 * 
 * Only one letter can be changed at a time.
 * Each transformed word must exist in the word list.
 * 
 * 
 * Note:
 * 
 * 
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * Output: 5
 * 
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
 * "dog" -> "cog",
 * return its length 5.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * Output: 0
 * 
 * Explanation: The endWord "cog" is not in wordList, therefore no possible
 * transformation.
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    int practice(String beginWord, String endWord, List<String> wordList)
    {
        // if(wordList.contains(endWord))
        //     return 0;
        Set<String> dict=new HashSet<>(wordList);
        Map<String,List<String>> star=new HashMap<>();
        ////build graph
        for(String word:wordList)
        {
            List<String> arr=convert(word);
            for(String tp:arr)
            {
                List<String> list=star.getOrDefault(tp, new ArrayList<>());
                list.add(word);
                star.put(tp, list);
            }
        }

        Queue<String> que=new LinkedList<>();
        Set<String> seen=new HashSet<>();
        que.add(beginWord);
        seen.add(beginWord);
        int depth=1;
        while(!que.isEmpty())
        {
            int size=que.size();
            for(int i=0; i<size;i++)
            {
                String top=que.poll();
                System.out.println(top);
                for(String word:convert(top))
                    if(star.containsKey(word))
                        for(String next:star.get(word))
                        {
                            if(seen.contains(next))
                                continue;
                            if(next.equals(endWord))
                                return depth+1;
                            seen.add(next);
                            que.add(next);
                        }
            }
            depth++;
        }
        return 0;
    }   
    
    List<String> convert(String word){
            List<String> res=new ArrayList<>();
            char[] ch=word.toCharArray();
            for(int i=0; i<ch.length; i++)
            {
                char tp=ch[i];
                ch[i]='*';
                res.add(new String(ch));
                ch[i]=tp;  
            }
            return res; 
    }    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
////the weighted graph use dijsktra
        return practice(beginWord, endWord, wordList);
    }
}
// @lc code=end

