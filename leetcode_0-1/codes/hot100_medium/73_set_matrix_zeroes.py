# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 73. 矩阵置零 (Set Matrix Zeroes) | 难度: 中等 | 官方分组: 矩阵
# 题目链接: https://leetcode.cn/problems/set-matrix-zeroes/
# 题意: 把含 0 的行列全部置 0（原地）
# 考点: 原地标记：用第一行/第一列充当标记数组，空间 O(1)
# 标签: 数组,哈希表,矩阵
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《矩阵置零》(LeetCode 题解)
#   https://leetcode.cn/problems/set-matrix-zeroes/solutions/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0