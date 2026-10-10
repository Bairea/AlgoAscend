# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 198. 打家劫舍 (House Robber) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/house-robber/
# 题意: 不能偷相邻两家，求能偷到的最高金额
# 考点: 线性 DP：f(i)=max(f(i-1), f(i-2)+nums[i])（不偷相邻），滚动变量省空间
# 标签: 数组,动态规划
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @LeetCode-Solution《打家劫舍》(LeetCode 题解)
#   https://leetcode.cn/problems/house-robber/solutions/da-jia-jie-she-by-leetcode-solution/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second