# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 560. 和为 K 的子数组 (Subarray Sum Equals K) | 难度: 中等 | 官方分组: 子串
# 题目链接: https://leetcode.cn/problems/subarray-sum-equals-k/
# 题意: 统计和恰好等于 k 的连续子数组的个数
# 考点: 前缀和 + 哈希计数：prefix[j]-prefix[i]=k 即子数组和为 k，边扫边查（前缀和属书外考点）
# 标签: 数组,哈希表,前缀和
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @endlesscheng《前缀和+哈希表：从两次遍历到一次遍历，附变形题（Python/Java/C++/Go/JS/Rust）》(LeetCode 题解)
#   https://leetcode.cn/problems/subarray-sum-equals-k/solutions/qian-zhui-he-ha-xi-biao-cong-liang-ci-bi-4mwr/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s - k]
        return ans