# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 15. 三数之和 (3Sum) | 难度: 中等 | 官方分组: 双指针
# 题目链接: https://leetcode.cn/problems/3sum/
# 题意: 找出数组中所有和为 0 且不重复的三元组
# 考点: 排序后固定最小数，双指针夹逼找另两数；相邻跳过重复值去重
# 标签: 数组,双指针,排序
# hello-algo: 第11章 排序 · 快速排序
#   https://www.hello-algo.com/chapter_sorting/quick_sort/
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《三数之和》(LeetCode 题解)
#   https://leetcode.cn/problems/3sum/solutions/san-shu-zhi-he-by-leetcode-solution/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans