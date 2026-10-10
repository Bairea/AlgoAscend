# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 152. 乘积最大子数组 (Maximum Product Subarray) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/maximum-product-subarray/
# 题意: 求乘积最大的非空连续子数组
# 考点: DP 双状态：同时维护以 i 结尾的最大积与最小积（负数乘负数翻转），fmax=max(三种来源)
# 标签: 数组,动态规划
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# 题解来源: @powcai《多种思路求解（乘积最大子数组·DP 版）》(LeetCode 题解)
#   https://leetcode.cn/problems/maximum-product-subarray/solutions/duo-chong-si-lu-qiu-jie-by-powcai-3/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res