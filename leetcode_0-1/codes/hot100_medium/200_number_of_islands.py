# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 200. 岛屿数量 (Number of Islands) | 难度: 中等 | 官方分组: 图论
# 题目链接: https://leetcode.cn/problems/number-of-islands/
# 题意: 统计矩阵中岛屿（相连的 '1'）的数量
# 考点: 网格 DFS「沉岛」：遍历到 '1' 计数 +1 并把连通陆地全部改 '0'
# 标签: 深度优先搜索,广度优先搜索,并查集,数组,矩阵
# hello-algo: 第9章 图 · 图遍历
#   https://www.hello-algo.com/chapter_graph/graph_traversal/
# hello-algo: 第9章 图 · 图
#   https://www.hello-algo.com/chapter_graph/graph/
# 题解来源: @LeetCode《岛屿数量（官方题解·DFS）》(LeetCode 题解)
#   https://leetcode.cn/problems/number-of-islands/solutions/dao-yu-shu-liang-by-leetcode/

from typing import List

class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands