# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 416. 分割等和子集 (Partition Equal Subset Sum) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/partition-equal-subset-sum/
# 题意: 能否把数组分成两个元素和相等的子集
# 考点: 0-1 背包判定：总和一半为容量，dp[j] |= dp[j-num] 倒序遍历
# 标签: 数组,动态规划,背包问题,0-1 背包
# hello-algo: 第14章 动态规划 · 0-1 背包问题
#   https://www.hello-algo.com/chapter_dynamic_programming/knapsack_problem/
# 题解来源: @LeetCode-Solution《分割等和子集》(LeetCode 题解)
#   https://leetcode.cn/problems/partition-equal-subset-sum/solutions/fen-ge-deng-he-zi-ji-by-leetcode-solution/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]