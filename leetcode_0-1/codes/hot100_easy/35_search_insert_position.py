# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 35. 搜索插入位置 (Search Insert Position) | 难度: 简单 | 官方分组: 二分查找
# 题目链接: https://leetcode.cn/problems/search-insert-position/
# 题意: 在升序数组中找 target 的插入下标（不存在则返回应插入位置）
# 考点: 二分查找插入点（lower_bound）模板：循环不变量 + 闭区间写法
# 标签: 数组,二分查找
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# hello-algo: 第10章 搜索 · 二分查找插入点
#   https://www.hello-algo.com/chapter_searching/binary_search_insertion/
# 题解来源: @endlesscheng《二分查找总是写不对？（lower_bound 模板）》(LeetCode 题解)
#   https://leetcode.cn/problems/search-insert-position/solutions/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-nq23/

from typing import List

# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 找到第一个大于或等于 target 的元素的下标，以及排除不可能是目标范围的区域

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)  # 选择其中一种写法即可


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)
