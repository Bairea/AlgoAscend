# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 54. 螺旋矩阵 (Spiral Matrix) | 难度: 中等 | 官方分组: 矩阵
# 题目链接: https://leetcode.cn/problems/spiral-matrix/
# 题意: 按顺时针螺旋顺序返回矩阵所有元素
# 考点: 边界收缩模拟：按 左→右/上→下/右→左/下→上 四边遍历，逐层向内收缩
# 标签: 数组,矩阵,模拟
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《螺旋矩阵》(LeetCode 题解)
#   https://leetcode.cn/problems/spiral-matrix/solutions/luo-xuan-ju-zhen-by-leetcode-solution/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order