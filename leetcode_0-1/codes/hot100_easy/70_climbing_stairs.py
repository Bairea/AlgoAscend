# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 70. 爬楼梯 (Climbing Stairs) | 难度: 简单 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/climbing-stairs/
# 题意: 每次爬 1 或 2 阶，求爬到第 n 阶的方案数
# 考点: DP 入门：状态定义 → 转移方程 f(i)=f(i-1)+f(i-2) → 初始值；即斐波那契
# 标签: 记忆化,数学,动态规划
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @jyd《70. 爬楼梯（动态规划，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/climbing-stairs/solutions/70-pa-lou-ti-dong-tai-gui-hua-qing-xi-tu-ruwa/

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b