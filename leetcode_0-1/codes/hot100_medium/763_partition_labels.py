# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 763. 划分字母区间 (Partition Labels) | 难度: 中等 | 官方分组: 堆
# 题目链接: https://leetcode.cn/problems/partition-labels/
# 题意: 把字符串切成尽量多的段，使每段字母不跨段出现
# 考点: 贪心：记录每字符最后出现位置，当前段延伸到 end=max(end, last[c])，到达即切分
# 标签: 贪心,哈希表,双指针,字符串
# hello-algo: 第15章 贪心算法 · 贪心算法
#   https://www.hello-algo.com/chapter_greedy/greedy_algorithm/
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @LeetCode-Solution《划分字母区间》(LeetCode 题解)
#   https://leetcode.cn/problems/partition-labels/solutions/hua-fen-zi-mu-qu-jian-by-leetcode-solution/

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition