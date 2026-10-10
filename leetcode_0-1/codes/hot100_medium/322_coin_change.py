# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 322. 零钱兑换 (Coin Change) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/coin-change/
# 题意: 凑出 amount 的最少硬币数（每种面额无限）
# 考点: 完全背包：f[x]=min over coins(f[x-coin]+1)，f[0]=0
# 标签: 广度优先搜索,数组,动态规划,背包问题,完全背包
# hello-algo: 第14章 动态规划 · 完全背包问题
#   https://www.hello-algo.com/chapter_dynamic_programming/unbounded_knapsack_problem/
# 题解来源: @LeetCode-Solution《零钱兑换》(LeetCode 题解)
#   https://leetcode.cn/problems/coin-change/solutions/322-ling-qian-dui-huan-by-leetcode-solution/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1