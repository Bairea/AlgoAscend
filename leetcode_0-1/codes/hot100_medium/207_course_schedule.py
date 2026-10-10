# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 207. 课程表 (Course Schedule) | 难度: 中等 | 官方分组: 图论
# 题目链接: https://leetcode.cn/problems/course-schedule/
# 题意: 判断先修课依赖关系（有向图）是否存在环
# 考点: 拓扑排序（Kahn）：建邻接表 + 入度表，入度 0 者入队，能出队数 = 课程数则无环
# 标签: 深度优先搜索,广度优先搜索,图,拓扑排序,有向无环图
# hello-algo: 第9章 图 · 图遍历
#   https://www.hello-algo.com/chapter_graph/graph_traversal/
# hello-algo: 第9章 图 · 图
#   https://www.hello-algo.com/chapter_graph/graph/
# 题解来源: @LeetCode-Solution《课程表》(LeetCode 题解)
#   https://leetcode.cn/problems/course-schedule/solutions/ke-cheng-biao-by-leetcode-solution/

from typing import List

import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses