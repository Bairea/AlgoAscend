# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 131. 分割回文串 (Palindrome Partitioning) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/palindrome-partitioning/
# 题意: 把字符串分割成若干回文子串，返回所有方案
# 考点: 回溯 + 预处理：枚举每个切割点，回文判断用记忆化（DP 预计算）避免重复比较
# 标签: 字符串,动态规划,回溯
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @LeetCode-Solution《分割回文串》(LeetCode 题解)
#   https://leetcode.cn/problems/palindrome-partitioning/solutions/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret