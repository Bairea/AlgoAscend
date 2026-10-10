# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 994. 腐烂的橘子 (Rotting Oranges) | 难度: 中等 | 官方分组: 图论
# 题目链接: https://leetcode.cn/problems/rotting-oranges/
# 题意: 新鲜橘子每分钟被相邻烂橘子传染，求全部腐烂时间
# 考点: 多源 BFS：所有烂橘子同时入队作为第 0 层，扩散层数即分钟数
# 标签: 广度优先搜索,数组,矩阵
# hello-algo: 第9章 图 · 图遍历
#   https://www.hello-algo.com/chapter_graph/graph_traversal/
# 题解来源: @LeetCode-Solution《腐烂的橘子》(LeetCode 题解)
#   https://leetcode.cn/problems/rotting-oranges/solutions/fu-lan-de-ju-zi-by-leetcode-solution/

from typing import List

import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d