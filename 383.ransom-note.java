/*
 * @lc app=leetcode id=383 lang=java
 *
 * [383] Ransom Note
 *
 * https://leetcode.com/problems/ransom-note/description/
 *
 * algorithms
 * Easy (51.65%)
 * Likes:    547
 * Dislikes: 187
 * Total Accepted:    193.6K
 * Total Submissions: 362.8K
 * Testcase Example:  '"a"\n"b"'
 *
 * 
 * Given an arbitrary ransom note string and another string containing letters
 * from all the magazines, write a function that will return true if the
 * ransom 
 * note can be constructed from the magazines ; otherwise, it will return
 * false. 
 * 
 * 
 * Each letter in the magazine string can only be used once in your ransom
 * note.
 * 
 * 
 * Note:
 * You may assume that both strings contain only lowercase letters.
 * 
 * 
 * 
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 * 
 * 
 */

// @lc code=start

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> m_map = new HashMap();
        for (char ch: magazine.toCharArray()){
            if (m_map.containsKey(ch))
                // m_map[ch] += 1;
                m_map.put(ch, m_map.get(ch)+1);
            else
                // m_map[ch] = 1;
                m_map.put(ch, 1);
        }

        for (char ch: ransomNote.toCharArray()){
            if (m_map.containsKey(ch)){
                m_map.put(ch, m_map.get(ch)-1);
                if (m_map.get(ch) == 0)
                    m_map.remove(ch);
            }
            else
                return false;  
        }
        return true;
    }
}
// @lc code=end

