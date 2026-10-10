# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 48. 旋转图像 (Rotate Image) | 难度: 中等 | 官方分组: 矩阵
# 题目链接: https://leetcode.cn/problems/rotate-image/
# 题意: 原地顺时针旋转矩阵 90°
# 考点: 先水平翻转再主对角线转置 = 顺时针旋转 90°；数学关系 (i,j)→(j,n-1-i)
# 标签: 数组,数学,矩阵
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《旋转图像》(LeetCode 题解)
#   https://leetcode.cn/problems/rotate-image/solutions/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]