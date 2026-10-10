# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 394. 字符串解码 (Decode String) | 难度: 中等 | 官方分组: 栈
# 题目链接: https://leetcode.cn/problems/decode-string/
# 题意: 解码 k[encoded_string] 形式的字符串（嵌套）
# 考点: 栈解码：遇 '[' 压入当前串与倍数，遇 ']' 弹出拼接；或递归处理嵌套
# 标签: 栈,递归,字符串
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @jyd《字符串解码（辅助栈法）》(LeetCode 题解)
#   https://leetcode.cn/problems/decode-string/solutions/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res