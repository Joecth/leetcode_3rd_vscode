#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (26.86%)
# Likes:    1048
# Dislikes: 2774
# Total Accepted:    176.2K
# Total Submissions: 654.4K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#

# @lc code=start
d = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 
         6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}   # EDGE CASE: 0:'' for 120
d10 = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',
           14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
           18:'Eighteen', 19:'Nineteen'}
d2 = {20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty',
          60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
class Solution:

    def numberToWords(self, num: int) -> str:
        # return self.name3digits(num)
        if num == 0: return 'Zero'
        res = []
        while num > 0:
            carry, three_digits = num//1000, num % 1000
            res.append(self.name3digits(three_digits))
            num = carry
                    
        # res = res[::-1]
        ans = ''
        unit = ['', 'Thousand', 'Million', 'Billion']
        for i in range(len(res)-1, -1, -1):
            ans += res[i]
            if res[i] != "":    # ==> for 1000000, One Million
                ans += " " + unit[i] + " "      #'a  b c' ==> [a, b, c]
        return ' '.join(ans.split())    # TODO: practice java 
    
    def name3digits(self, num):
        hundred, ten, digit = num//100, num%100, num%10
        s = 'N/A'
        if hundred == 0:
            if ten < 10:
                s = '{}'.format(d[digit])
            elif 10 <= ten < 20:
                s = '{}'.format(d10[ten])
            elif ten >= 20:
                s = '{} {}'.format(d2[ten//10*10], d[digit])
        else:
            if ten < 10:
                s = '{} Hundred {}'.format(d[hundred], d[digit])
            elif 10 <= ten < 20:
                s = '{} Hundred {}'.format(d[hundred], d10[ten])
            elif ten >= 20:
                s = '{} Hundred {} {}'.format(d[hundred], d2[ten//10*10], d[digit])
        return s
    # def name2digits(self, num):
        
# @lc code=end

