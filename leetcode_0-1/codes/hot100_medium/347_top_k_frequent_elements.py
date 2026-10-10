# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 347. 前 K 个高频元素 (Top K Frequent Elements) | 难度: 中等 | 官方分组: 堆
# 题目链接: https://leetcode.cn/problems/top-k-frequent-elements/
# 题意: 返回出现频率前 k 高的元素
# 考点: 哈希计数 + Top-K：小顶堆维护前 k 高频，或桶排序按频次分桶
# 标签: 数组,哈希表,分治,桶排序,计数,快速选择,排序,堆（优先队列）
# hello-algo: 第8章 堆 · Top-K 问题
#   https://www.hello-algo.com/chapter_heap/top_k/
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第11章 排序 · 桶排序
#   https://www.hello-algo.com/chapter_sorting/bucket_sort/
# 题解来源: @xxinjiee《python/c++ 自己实现堆，优先队列》(LeetCode 题解)
#   https://leetcode.cn/problems/top-k-frequent-elements/solutions/python-dui-pai-xu-by-xxinjiee/

from typing import List

import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1) 
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1) 
        return [item[0] for item in heap[1:]]