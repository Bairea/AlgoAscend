# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 33. 搜索旋转排序数组 (Search in Rotated Sorted Array) | 难度: 中等 | 官方分组: 二分查找
# 题目链接: https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 题意: 在旋转过的升序数组中 O(log n) 查找 target
# 考点: 旋转数组二分：mid 把数组切成一半有序一半无序，先判哪半有序再判 target 在不在其中
# 标签: 数组,二分查找
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# 题解来源: @LeetCode-Solution《搜索旋转排序数组》(LeetCode 题解)
#   https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1