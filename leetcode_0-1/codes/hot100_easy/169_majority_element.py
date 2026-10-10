# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 169. 多数元素 (Majority Element) | 难度: 简单 | 官方分组: 技巧
# 题目链接: https://leetcode.cn/problems/majority-element/
# 题意: 找出出现次数超过 ⌊n/2⌋ 的多数元素
# 考点: 摩尔投票：候选数抵消不同的数，超过半数者必胜；也可哈希计数/排序取中位
# 标签: 数组,哈希表,分治,计数,排序
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第11章 排序
#   https://www.hello-algo.com/chapter_sorting/sorting_algorithm/
# 题解来源: @LeetCode-Solution《多数元素》(LeetCode 题解)
#   https://leetcode.cn/problems/majority-element/solutions/duo-shu-yuan-su-by-leetcode-solution/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate