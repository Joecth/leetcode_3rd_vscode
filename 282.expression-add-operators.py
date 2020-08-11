#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (35.41%)
# Likes:    1282
# Dislikes: 208
# Total Accepted:    105.9K
# Total Submissions: 298.5K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# Example 1:
# 
# 
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# 
# 
# Example 2:
# 
# 
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# 
# Example 3:
# 
# 
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# 
# Example 4:
# 
# 
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# 
# 
# Example 5:
# 
# 
# Input: num = "3456237490", target = 9191
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num.length <= 10
# num only contain digits.
# 
# 
#

# @lc code=start
# OPs = {'+':add, '-':sub, 'mult':mult, 'div':div}
# def add(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def mult(a, b):
#     return a*b

# def div(a, b):
#     return a/b
    
OPS = {'+': lambda a, b: a+b,
       '-': lambda a, b: a-b, 
       '*': lambda a, b: a*b, 
       '/': lambda a, b: a/b}
    
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        # return self.sol_others(num, target)
        res = []
        # self.helper_FAILED(num, 0, '', 0, target, res)
        self.helper(num, 0, 0, '', 0, target, res)
        # print(OPS['*'](3, 7))
        return res

    def helper(self, num, cur_res, mul, cur_path, idx, target, res):
        if idx == len(num):
            if cur_res == target:
                res.append(cur_path[:])
            return 
        
        for i in range(idx, len(num)):
            # 第一個所有的運算都是有問題的
            # n = int(num[idx:i+1]) ==> bug for [1 05, 5], for the 'leading zeroes'
            # if pat[0] == '0':   # ==> WRONG, since single '0' should be OK
            if i != idx and num[idx] == '0':
                break   # 结束這層的 backtracking
            n = int(num[idx:i+1])
            if idx == 0:
                self.helper(num, n, n, str(n), i+1, target, res)
            # 4 operations as following
            else:
                new_mul = cur_res - mul + mul*n
                self.helper(num, new_mul, mul*n, cur_path+'*'+str(n), i+1, target, res)
                self.helper(num, cur_res+n, n, cur_path+'+'+str(n), i+1, target, res)                
                self.helper(num, cur_res-n, -n, cur_path+'-'+str(n), i+1, target, res)
                
                # for op, func in OPS.items():
                #     path = cur_path + op + str(n)
                #     tmp = func(cur_res, n)
                #     self.helper(num, tmp, path, i+1, target, res)
    
    
    def helper_FAILE(self, num, cur_res, cur_path, idx, target, res):
        if idx == len(num) and cur_res == target:
            res.append(cur_path[:])
            # print(idx, target, res)
            return 
        
        for i in range(idx, len(num)):
            # 第一個所有的運算都是有問題的
            # 4 operations as following
            n = int(num[idx:i+1])
            for op, func in OPS.items():
                path = cur_path + op + str(n)
                tmp = func(cur_res, n)
                if cur_res == target:
                    self.helper(num, tmp, path, i+1, target, res)
                elif cur_res < target:
                    if op == '+' or op == '*':
                        self.helper(num, tmp, path, i+1, target, res)
                else:
                    if op == '-' or op == '/':
                        self.helper(num, tmp, path, i+1, target, res)
                
            # path = op + cur_path + str(n)
            # self.helper(num, cur_res+n, path, idx+1, target, res)
            # self.helper(num, cur_res*n, path, idx+1, target, res)
            # self.helper(num, cur_res-n, path, idx+1, target, res)
            # self.helper(num, cur_res/n, path, idx+1, target, res)
            
    def sol_others(self, num: 'str', target: 'int') -> 'List[str]':
        print("idx\t\tpath\t\tvalue\t\tprev")

        def backtracking(idx=0, path='', value=0, prev=None):
            print("{0}\t\t{1}\t\t{2}\t\t{3}".format(idx, path, value, prev))
            if idx == len(num) and value == target:
                rtn.append(path)
                print('Found')
                return

            for i in range(idx+1, len(num) + 1):
                tmp = int(num[i-1: i])
                if i == idx + 1 or (i > idx + 1 and num[i-1] != '0'):
                    if prev is None :
                        backtracking(i, num[i-1: i], tmp, tmp)
                    else:
                        backtracking(i, path+'+'+num[i-1: i], value + tmp, tmp)
                        backtracking(i, path+'*'+num[i-1: i], value - prev + prev*tmp, prev*tmp)

        rtn = []
        backtracking()
        return rtn          
# @lc code=end

