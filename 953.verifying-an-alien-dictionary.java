/*
 * @lc app=leetcode id=953 lang=java
 *
 * [953] Verifying an Alien Dictionary
 *
 * https://leetcode.com/problems/verifying-an-alien-dictionary/description/
 *
 * algorithms
 * Easy (54.36%)
 * Likes:    861
 * Dislikes: 347
 * Total Accepted:    118K
 * Total Submissions: 217.5K
 * Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
 *
 * In an alien language, surprisingly they also use english lowercase letters,
 * but possibly in a different order. The order of the alphabet is some
 * permutation of lowercase letters.
 * 
 * Given a sequence of words written in the alien language, and the order of
 * the alphabet, return true if and only if the given words are sorted
 * lexicographicaly in this alien language.
 * 
 * Example 1:
 * 
 * 
 * Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
 * Output: true
 * Explanation: As 'h' comes before 'l' in this language, then the sequence is
 * sorted.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
 * Output: false
 * Explanation: As 'd' comes after 'l' in this language, then words[0] >
 * words[1], hence the sequence is unsorted.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
 * Output: false
 * Explanation: The first three characters "app" match, and the second string
 * is shorter (in size.) According to lexicographical rules "apple" > "app",
 * because 'l' > '∅', where '∅' is defined as the blank character which is less
 * than any other character (More info).
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 20
 * order.length == 26
 * All characters in words[i] and order are English lowercase letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        if (words == null || order.length() == 0 || words.length == 0){
            // assert(0);
            return false;
        }
        HashMap<Character, Integer> map_order = new HashMap<>();
        for (int i=0; i < order.length(); i++){
            map_order.put(order.charAt(i), i);
        }
        
        int n = words.length;
        for (int i=0; i < n-1; i++){
            if (isBigger(words[i], words[i+1], map_order)){
                return false;
            }
        }
        return true;
    }
    
    private boolean isBigger(String word1, String word2, HashMap map_order){
        int m = word1.length();
        int n = word2.length();
        for (int i=0; i < Math.min(m, n); i++){
            int a = (int)map_order.get(word1.charAt(i));
            int b = (int)map_order.get(word2.charAt(i));
            if (a > b)
                return true;
            else if (a < b)
                return false;
        }
        if (m > n)
            return true;
        return false;
    }
}
// @lc code=end

