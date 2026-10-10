# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 189. 轮转数组 (Rotate Array) | 难度: 中等 | 官方分组: 普通数组
# 题目链接: https://leetcode.cn/problems/rotate-array/
# 题意: 数组向右轮转 k 个位置（原地）
# 考点: 三次反转技巧：整体反转→反转前 k 个→反转剩余，原地 O(1) 空间轮转
# 标签: 数组,数学,双指针
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @endlesscheng《【图解】负负得正，一图秒懂！（Python/Java/C++/C/Go/JS/Rust）》(LeetCode 题解)
#   https://leetcode.cn/problems/rotate-array/solutions/tu-jie-yuan-di-zuo-fa-yi-tu-miao-dong-py-ryfv/

from typing import List

# 注：请勿使用切片，会产生额外空间
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等同于轮转 k % n 次
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)