# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 300. 最长递增子序列 (Longest Increasing Subsequence) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/longest-increasing-subsequence/
# 题意: 求最长严格递增子序列的长度
# 考点: LIS：f(i)=以 i 结尾的最长上升子序列，O(n²) DP；进阶 O(n log n) 贪心+二分
# 标签: 数组,二分查找,动态规划,最长上升子序列
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# hello-algo: 第10章 搜索 · 二分查找插入点
#   https://www.hello-algo.com/chapter_searching/binary_search_insertion/
# 题解来源: @LeetCode-Solution《最长递增子序列（官方题解·动态规划）》(LeetCode 题解)
#   https://leetcode.cn/problems/longest-increasing-subsequence/solutions/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)