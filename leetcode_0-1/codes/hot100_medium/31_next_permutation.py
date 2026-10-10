# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 31. 下一个排列 (Next Permutation) | 难度: 中等 | 官方分组: 技巧
# 题目链接: https://leetcode.cn/problems/next-permutation/
# 题意: 把数组原地重排为字典序的下一个排列
# 考点: 固定套路：从右找第一个升序对 i，再找右边最后一个大于 nums[i] 的 j，交换后反转后缀
# 标签: 数组,双指针
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《下一个排列》(LeetCode 题解)
#   https://leetcode.cn/problems/next-permutation/solutions/xia-yi-ge-pai-lie-by-leetcode-solution/

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1