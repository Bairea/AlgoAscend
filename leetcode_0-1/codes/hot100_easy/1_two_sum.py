# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 1. 两数之和 (Two Sum) | 难度: 简单 | 官方分组: 哈希
# 题目链接: https://leetcode.cn/problems/two-sum/
# 题意: 在数组中找出和为 target 的两个数，返回下标
# 考点: 哈希表把内层「查找 target-x」从 O(n) 降到 O(1)，整体 O(n)
# 标签: 数组,哈希表
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第2章 复杂度分析 · 时间复杂度
#   https://www.hello-algo.com/chapter_computational_complexity/time_complexity/
# 题解来源: @LeetCode-Solution《两数之和》(LeetCode 题解)
#   https://leetcode.cn/problems/two-sum/solutions/liang-shu-zhi-he-by-leetcode-solution/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

# 哈希表的存储功能，减少遍历
