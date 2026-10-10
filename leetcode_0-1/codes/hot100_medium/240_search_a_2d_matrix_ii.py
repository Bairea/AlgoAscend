# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 240. 搜索二维矩阵 II (Search a 2D Matrix II) | 难度: 中等 | 官方分组: 矩阵
# 题目链接: https://leetcode.cn/problems/search-a-2d-matrix-ii/
# 题意: 在每行每列均升序的矩阵中判断 target 是否存在
# 考点: 从右上角出发搜索：比目标小向下、比目标大向左，本质像在 BST 上走（每步排除一行或一列）
# 标签: 数组,二分查找,分治,矩阵
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# hello-algo: 第7章 树 · 二叉搜索树
#   https://www.hello-algo.com/chapter_tree/binary_search_tree/
# 题解来源: @LeetCode-Solution《搜索二维矩阵 II》(LeetCode 题解)
#   https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/sou-suo-er-wei-ju-zhen-ii-by-leetcode-so-9hcx/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False