# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 739. 每日温度 (Daily Temperatures) | 难度: 中等 | 官方分组: 栈
# 题目链接: https://leetcode.cn/problems/daily-temperatures/
# 题意: 求每天等到一个更高温度所需的天数
# 考点: 单调栈（递减栈）：温度更高时弹栈结算天数差（hello-algo 无单调栈专章，属书外考点）
# 标签: 栈,数组,单调栈
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @LeetCode-Solution《每日温度》(LeetCode 题解)
#   https://leetcode.cn/problems/daily-temperatures/solutions/mei-ri-wen-du-by-leetcode-solution/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans