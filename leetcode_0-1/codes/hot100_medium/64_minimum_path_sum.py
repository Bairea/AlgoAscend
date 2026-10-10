# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 64. 最小路径和 (Minimum Path Sum) | 难度: 中等 | 官方分组: 多维动态规划
# 题目链接: https://leetcode.cn/problems/minimum-path-sum/
# 题意: 网格从左上到右下的最小路径和（只能右/下）
# 考点: 网格 DP：f(i,j)=grid(i,j)+min(上, 左)，首行首列单独初始化
# 标签: 数组,动态规划,矩阵
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @LeetCode-Solution《最小路径和》(LeetCode 题解)
#   https://leetcode.cn/problems/minimum-path-sum/solutions/zui-xiao-lu-jing-he-by-leetcode-solution/

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]