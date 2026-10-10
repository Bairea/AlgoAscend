# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 34. 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array) | 难度: 中等 | 官方分组: 二分查找
# 题目链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 题意: 升序数组中 target 的首尾下标，O(log n)
# 考点: 二分查找边界：手写 lower_bound 找起点，再对 target+1 找终点（或右边界变体）
# 标签: 数组,二分查找
# hello-algo: 第10章 搜索 · 二分查找边界
#   https://www.hello-algo.com/chapter_searching/binary_search_edge/
# hello-algo: 第10章 搜索 · 二分查找插入点
#   https://www.hello-algo.com/chapter_searching/binary_search_insertion/
# 题解来源: @endlesscheng《二分查找总是写不对？（lower_bound 模板）》(LeetCode 题解)
#   https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-t9l9/

from typing import List

class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]