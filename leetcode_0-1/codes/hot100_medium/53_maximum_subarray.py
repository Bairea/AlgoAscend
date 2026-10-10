# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 53. 最大子数组和 (Maximum Subarray) | 难度: 中等 | 官方分组: 普通数组
# 题目链接: https://leetcode.cn/problems/maximum-subarray/
# 题意: 求连续子数组的最大和
# 考点: DP：f(i)=max(nums[i], f(i-1)+nums[i])，「以 i 结尾的最大子数组和」；也可分治
# 标签: 数组,分治,动态规划
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# hello-algo: 第12章 分治 · 分治算法
#   https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/
# 题解来源: @liweiwei1419《最大子序和（动态规划+分治）》(LeetCode 题解)
#   https://leetcode.cn/problems/maximum-subarray/solutions/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-jav/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)