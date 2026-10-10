# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 39. 组合总和 (Combination Sum) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/combination-sum/
# 题意: 找出所有使数字和为 target 的组合（数字可重复选用）
# 考点: 组合回溯：可重复选当前数（递归传 i 而非 i+1），排序后剪枝（超 target 即 break）
# 标签: 数组,回溯
# hello-algo: 第13章 回溯 · 子集和问题
#   https://www.hello-algo.com/chapter_backtracking/subset_sum_problem/
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# 题解来源: @jyd《39. 组合总和（回溯，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/combination-sum/solutions/39-zu-he-zong-he-hui-su-qing-xi-tu-jie-b-9zx7/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(
            state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
        ):
            """回溯算法：子集和 I"""
            # 子集和等于 target 时，记录解
            if target == 0:
                res.append(list(state))
                return
            # 遍历所有选择
            # 剪枝二：从 start 开始遍历，避免生成重复子集
            for i in range(start, len(choices)):
                # 剪枝一：若子集和超过 target ，则直接结束循环
                # 这是因为数组已排序，后边元素更大，子集和一定超过 target
                if target - choices[i] < 0:
                    break
                # 尝试：做出选择，更新 target, start
                state.append(choices[i])
                # 进行下一轮选择
                backtrack(state, target - choices[i], choices, i, res)
                # 回退：撤销选择，恢复到之前的状态
                state.pop()

        state = []  # 状态（子集）
        candidates.sort()  # 对 candidates 进行排序
        start = 0  # 遍历起始点
        res = []  # 结果列表（子集列表）
        backtrack(state, target, candidates, start, res)
        return res