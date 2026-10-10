# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 62. 不同路径 (Unique Paths) | 难度: 中等 | 官方分组: 多维动态规划
# 题目链接: https://leetcode.cn/problems/unique-paths/
# 题意: m×n 网格从左上到右下的路径数（只能右/下）
# 考点: 网格计数 DP：f(i,j)=f(i-1,j)+f(i,j-1)，边界为 1
# 标签: 数学,动态规划,组合数学
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @LeetCode-Solution《不同路径（官方题解·动态规划）》(LeetCode 题解)
#   https://leetcode.cn/problems/unique-paths/solutions/bu-tong-lu-jing-by-leetcode-solution-hzjf/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]