# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 74. 搜索二维矩阵 (Search a 2D Matrix) | 难度: 中等 | 官方分组: 二分查找
# 题目链接: https://leetcode.cn/problems/search-a-2d-matrix/
# 题意: 每行升序且行首大于上行行尾的矩阵中查找 target
# 考点: 二维升序矩阵按行拼接为一维有序数组：mid 映射到 (row, col) 做标准二分
# 标签: 数组,二分查找,矩阵
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# 题解来源: @infallible-napieror1《【暴力】【二分查找】【矩阵】》(LeetCode 题解)
#   https://leetcode.cn/problems/search-a-2d-matrix/solutions/bao-li-er-fen-cha-zhao-ju-zhen-by-infall-4zd6/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        # 需要将一维数组的索引转换为二维矩阵的行和列索引。

        # 获取矩阵维度
        m = len(matrix)     # 行
        n = len(matrix[0])  # 列
        # 定义一维数组的左右指针
        left = 0
        right = m * n -1

        # 闭区间形式
        while left <= right:
            mid = (left + right) // 2
            # 将一维数组的索引转换为二维矩阵的行列
            mid_value = matrix[mid // n][mid % n]
            
            # 注意！！！
            # mid 是 一维索引
            # mid_value 是根据一维索引找到的二维数组对应的值！
            # 用mid_value 跟 target对比
            # 根据结果改边界应该是mid！！！


            if mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
            else:
                return True
        return False