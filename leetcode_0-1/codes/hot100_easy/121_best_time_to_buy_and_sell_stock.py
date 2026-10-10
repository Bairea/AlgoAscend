# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 121. 买卖股票的最佳时机 (Best Time to Buy and Sell Stock) | 难度: 简单 | 官方分组: 贪心算法
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# 题意: 一天买一天卖（先买后卖），求最大利润
# 考点: 一次遍历维护历史最低价 minprice，当天卖出的利润取最大（贪心）
# 标签: 数组,动态规划
# hello-algo: 第15章 贪心算法 · 贪心算法
#   https://www.hello-algo.com/chapter_greedy/greedy_algorithm/
# 题解来源: @LeetCode-Solution《买卖股票的最佳时机》(LeetCode 题解)
#   https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit