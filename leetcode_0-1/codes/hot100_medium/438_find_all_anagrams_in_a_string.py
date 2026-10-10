# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 438. 找到字符串中所有字母异位词 (Find All Anagrams in a String) | 难度: 中等 | 官方分组: 滑动窗口
# 题目链接: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 题意: 找出 s 中所有 p 的异位词子串的起始下标
# 考点: 定长滑动窗口：维护 26 长度计数数组，每步 O(1) 更新与比对
# 标签: 哈希表,字符串,滑动窗口
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @LeetCode-Solution《找到字符串中所有字母异位词》(LeetCode 题解)
#   https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            
            if differ == 0:
                ans.append(i + 1)

        return ans