# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 22. 括号生成 (Generate Parentheses) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/generate-parentheses/
# 题意: 生成所有合法的 n 对括号组合
# 考点: 回溯 + 约束剪枝：左括号剩余可填条件 left<n，右括号条件 right<left
# 标签: 字符串,动态规划,回溯,括号序列
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# 题解来源: @LeetCode-Solution《括号生成（官方题解·方法二 回溯）》(LeetCode 题解)
#   https://leetcode.cn/problems/generate-parentheses/solutions/gua-hao-sheng-cheng-by-leetcode-solution/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans