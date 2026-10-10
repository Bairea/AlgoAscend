# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 283. 移动零 (Move Zeroes) | 难度: 简单 | 官方分组: 双指针
# 题目链接: https://leetcode.cn/problems/move-zeroes/
# 题意: 把数组中所有 0 移到末尾，保持非零元素相对顺序（原地）
# 考点: 快慢双指针原地 partition：慢指针指向下一个非零应放的位置，同快排 partition 思想
# 标签: 数组,双指针
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# hello-algo: 第11章 排序 · 快速排序
#   https://www.hello-algo.com/chapter_sorting/quick_sort/
# 题解来源: @LeetCode-Solution《移动零》(LeetCode 题解)
#   https://leetcode.cn/problems/move-zeroes/solutions/yi-dong-ling-by-leetcode-solution/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1