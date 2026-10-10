# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 279. 完全平方数 (Perfect Squares) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/perfect-squares/
# 题意: 和为 n 的最少完全平方数个数
# 考点: 完全背包：f[i]=min(f[i-平方数]+1)；也可 BFS 求最短步数
# 标签: 广度优先搜索,数学,动态规划,背包问题,完全背包
# hello-algo: 第14章 动态规划 · 完全背包问题
#   https://www.hello-algo.com/chapter_dynamic_programming/unbounded_knapsack_problem/
# hello-algo: 第9章 图 · 图遍历
#   https://www.hello-algo.com/chapter_graph/graph_traversal/
# 题解来源: @zi-lai-huo《python3 最基础的 BFS 套路代码，适合入门新手！》(LeetCode 题解)
#   https://leetcode.cn/problems/perfect-squares/solutions/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/

class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1