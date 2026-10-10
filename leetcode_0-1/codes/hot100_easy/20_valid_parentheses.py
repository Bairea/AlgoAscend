# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 20. 有效的括号 (Valid Parentheses) | 难度: 简单 | 官方分组: 栈
# 题目链接: https://leetcode.cn/problems/valid-parentheses/
# 题意: 判断括号字符串 s 是否完全匹配闭合
# 考点: 栈的 LIFO：左括号入栈，右括号必须与栈顶配对
# 标签: 栈,字符串
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @LeetCode-Solution《有效的括号》(LeetCode 题解)
#   https://leetcode.cn/problems/valid-parentheses/solutions/you-xiao-de-gua-hao-by-leetcode-solution/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

# 栈的进和出，false条件是右括号先出现或者括号不直接匹配，如(]
