# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 118. 杨辉三角 (Pascal's Triangle) | 难度: 简单 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/pascals-triangle/
# 题意: 生成杨辉三角的前 numRows 行
# 考点: 二维数组按行递推 f[i][j]=f[i-1][j-1]+f[i-1][j]，DP 递推的雏形
# 标签: 数组,动态规划
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @LeetCode-Solution《杨辉三角》(LeetCode 题解)
#   https://leetcode.cn/problems/pascals-triangle/solutions/yang-hui-san-jiao-by-leetcode-solution-lew9/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret