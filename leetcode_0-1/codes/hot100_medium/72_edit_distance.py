# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 72. 编辑距离 (Edit Distance) | 难度: 中等 | 官方分组: 多维动态规划
# 题目链接: https://leetcode.cn/problems/edit-distance/
# 题意: 把 word1 变成 word2 的最少编辑次数（增删改）
# 考点: 编辑距离 DP：增/删/改三种转移 dp(i,j)=1+min(dp(i-1,j), dp(i,j-1), dp(i-1,j-1))
# 标签: 字符串,动态规划
# hello-algo: 第14章 动态规划 · 编辑距离问题
#   https://www.hello-algo.com/chapter_dynamic_programming/edit_distance_problem/
# 题解来源: @LeetCode-Solution《编辑距离》(LeetCode 题解)
#   https://leetcode.cn/problems/edit-distance/solutions/bian-ji-ju-chi-by-leetcode-solution/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [ [0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]