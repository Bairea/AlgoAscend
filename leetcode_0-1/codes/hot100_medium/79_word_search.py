# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 79. 单词搜索 (Word Search) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/word-search/
# 题意: 判断二维网格中是否存在上下左右相邻拼接的单词路径
# 考点: 网格 DFS + 回溯：visited 标记进入/撤销，四方向探索匹配单词
# 标签: 深度优先搜索,数组,字符串,回溯,矩阵
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# hello-algo: 第9章 图 · 图遍历
#   https://www.hello-algo.com/chapter_graph/graph_traversal/
# 题解来源: @LeetCode-Solution《单词搜索》(LeetCode 题解)
#   https://leetcode.cn/problems/word-search/solutions/dan-ci-sou-suo-by-leetcode-solution/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False