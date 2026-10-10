# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 75. 颜色分类 (Sort Colors) | 难度: 中等 | 官方分组: 技巧
# 题目链接: https://leetcode.cn/problems/sort-colors/
# 题意: 原地把 0/1/2 三色数组排序（单遍扫描）
# 考点: 三指针一次遍历（荷兰国旗）：p0/p2 分界，i 扫描交换，快排三向切分思想
# 标签: 数组,双指针,冒泡排序,排序,快速排序
# hello-algo: 第11章 排序 · 快速排序
#   https://www.hello-algo.com/chapter_sorting/quick_sort/
# hello-algo: 第11章 排序 · 排序算法
#   https://www.hello-algo.com/chapter_sorting/sorting_algorithm/
# 题解来源: @LeetCode-Solution《颜色分类》(LeetCode 题解)
#   https://leetcode.cn/problems/sort-colors/solutions/yan-se-fen-lei-by-leetcode-solution/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1