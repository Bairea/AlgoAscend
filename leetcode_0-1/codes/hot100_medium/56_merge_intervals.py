# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 56. 合并区间 (Merge Intervals) | 难度: 中等 | 官方分组: 普通数组
# 题目链接: https://leetcode.cn/problems/merge-intervals/
# 题意: 合并所有重叠的区间
# 考点: 按左端点排序后扫描：当前区间与上一结果重叠则合并（右端点取 max）
# 标签: 数组,排序,快速排序
# hello-algo: 第11章 排序 · 排序算法
#   https://www.hello-algo.com/chapter_sorting/sorting_algorithm/
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《合并区间》(LeetCode 题解)
#   https://leetcode.cn/problems/merge-intervals/solutions/he-bing-qu-jian-by-leetcode-solution/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged