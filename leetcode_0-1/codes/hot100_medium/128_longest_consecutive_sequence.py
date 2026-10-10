# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 128. 最长连续序列 (Longest Consecutive Sequence) | 难度: 中等 | 官方分组: 哈希
# 题目链接: https://leetcode.cn/problems/longest-consecutive-sequence/
# 题意: 求无序数组中最长连续数字序列的长度
# 考点: 哈希集合 O(n)：只从「无左邻居」的数起数连续段，每个数至多访问两次
# 标签: 并查集,数组,哈希表
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @LeetCode-Solution《最长连续序列》(LeetCode 题解)
#   https://leetcode.cn/problems/longest-consecutive-sequence/solutions/zui-chang-lian-xu-xu-lie-by-leetcode-solution/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak