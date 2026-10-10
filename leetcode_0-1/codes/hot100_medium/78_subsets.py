# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 78. 子集 (Subsets) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/subsets/
# 题意: 返回数组的所有子集（幂集）
# 考点: 子集回溯：每个元素「选/不选」二叉决策；或枚举起点按长度收集
# 标签: 位运算,数组,回溯
# hello-algo: 第13章 回溯 · 子集和问题
#   https://www.hello-algo.com/chapter_backtracking/subset_sum_problem/
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# 题解来源: @powcai《回溯算法（子集·DFS 版）》(LeetCode 题解)
#   https://leetcode.cn/problems/subsets/solutions/hui-su-suan-fa-by-powcai-5/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res