# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 155. 最小栈 (Min Stack) | 难度: 中等 | 官方分组: 栈
# 题目链接: https://leetcode.cn/problems/min-stack/
# 题意: 设计支持 push/pop/top/getMin 均 O(1) 的栈
# 考点: 辅助栈同步维护当前最小值（或存差值省空间）
# 标签: 栈,设计
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @LeetCode-Solution《最小栈》(LeetCode 题解)
#   https://leetcode.cn/problems/min-stack/solutions/zui-xiao-zhan-by-leetcode-solution/

import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]