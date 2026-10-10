# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 17. 电话号码的字母组合 (Letter Combinations of a Phone Number) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
# 题意: 电话按键数字串对应的所有字母组合
# 考点: 回溯模板：按数字逐位枚举字母，index 到尾收集结果
# 标签: 哈希表,字符串,回溯
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @LeetCode-Solution《电话号码的字母组合（官方题解·方法一 回溯）》(LeetCode 题解)
#   https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations