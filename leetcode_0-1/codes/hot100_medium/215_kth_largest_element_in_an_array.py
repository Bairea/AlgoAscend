# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 215. 数组中的第K个最大元素 (Kth Largest Element in an Array) | 难度: 中等 | 官方分组: 堆
# 题目链接: https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 题意: 找无序数组中第 k 大的元素
# 考点: 快速选择（partition 缩小范围，均摊 O(n)）或大小为 k 的堆 O(n log k)
# 标签: 数组,分治,快速选择,排序,堆（优先队列）
# hello-algo: 第8章 堆 · Top-K 问题
#   https://www.hello-algo.com/chapter_heap/top_k/
# hello-algo: 第8章 堆 · 堆
#   https://www.hello-algo.com/chapter_heap/heap/
# hello-algo: 第11章 排序 · 快速排序
#   https://www.hello-algo.com/chapter_sorting/quick_sort/
# 题解来源: @jyd《215. 数组中的第 K 个最大元素（分治，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/215-shu-zu-zhong-de-di-k-ge-zui-da-yuan-d786p/

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)