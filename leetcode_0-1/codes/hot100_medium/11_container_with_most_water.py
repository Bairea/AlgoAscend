# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 11. 盛最多水的容器 (Container With Most Water) | 难度: 中等 | 官方分组: 双指针
# 题目链接: https://leetcode.cn/problems/container-with-most-water/
# 题意: 选两条竖线与 x 轴围成容器，求能装最多的水量
# 考点: 贪心 + 双指针夹逼：每次移动较短的一侧（移长侧不可能变优），面积取最大
# 标签: 贪心,数组,双指针
# hello-algo: 第15章 贪心算法 · 最大容量问题
#   https://www.hello-algo.com/chapter_greedy/max_capacity_problem/
# hello-algo: 第15章 贪心算法 · 贪心算法
#   https://www.hello-algo.com/chapter_greedy/greedy_algorithm/
# 题解来源: @LeetCode-Solution《盛最多水的容器》(LeetCode 题解)
#   https://leetcode.cn/problems/container-with-most-water/solutions/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans