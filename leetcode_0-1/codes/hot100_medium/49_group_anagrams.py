# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 49. 字母异位词分组 (Group Anagrams) | 难度: 中等 | 官方分组: 哈希
# 题目链接: https://leetcode.cn/problems/group-anagrams/
# 题意: 把字母异位词（字母相同顺序不同）分到同一组
# 考点: 哈希表分组：对每个词做 26 字母计数，计数元组作 key 归组（异序词计数相同）
# 标签: 数组,哈希表,字符串,排序
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第11章 排序 · 计数排序
#   https://www.hello-algo.com/chapter_sorting/counting_sort/
# 题解来源: @LeetCode-Solution《字母异位词分组》(LeetCode 题解)
#   https://leetcode.cn/problems/group-anagrams/solutions/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/

from typing import List

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())