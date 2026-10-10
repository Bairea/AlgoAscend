# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 1143. 最长公共子序列 (Longest Common Subsequence) | 难度: 中等 | 官方分组: 多维动态规划
# 题目链接: https://leetcode.cn/problems/longest-common-subsequence/
# 题意: 求两字符串的最长公共子序列长度
# 考点: 经典二维 DP：相等则 dp(i,j)=dp(i-1,j-1)+1，否则取两侧最大
# 标签: 字符串,动态规划,最长公共子序列
# hello-algo: 第14章 动态规划 · 编辑距离问题
#   https://www.hello-algo.com/chapter_dynamic_programming/edit_distance_problem/
# hello-algo: 第14章 动态规划 · 动态规划问题特性
#   https://www.hello-algo.com/chapter_dynamic_programming/dp_problem_features/
# 题解来源: @LeetCode-Solution《最长公共子序列》(LeetCode 题解)
#   https://leetcode.cn/problems/longest-common-subsequence/solutions/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]