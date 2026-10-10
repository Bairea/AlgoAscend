# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 153. 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array) | 难度: 中等 | 官方分组: 二分查找
# 题目链接: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
# 题意: 找旋转升序数组中的最小值，O(log n)
# 考点: 二分找旋转点：mid 与右端比较，nums[mid]>右端 说明最小值在右半
# 标签: 数组,二分查找
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# 题解来源: @LeetCode-Solution《寻找旋转排序数组中的最小值》(LeetCode 题解)
#   https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]