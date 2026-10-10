# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 139. 单词拆分 (Word Break) | 难度: 中等 | 官方分组: 动态规划
# 题目链接: https://leetcode.cn/problems/word-break/
# 题意: 判断字符串能否被字典单词完全切分
# 考点: DP：f(i)=存在 j<i 使 f(j) 且 s[j:i] 在字典；字典用哈希集合 O(1) 查
# 标签: 字典树,记忆化,数组,哈希表,字符串,动态规划,Brute-Force Search
# hello-algo: 第14章 动态规划 · 初探动态规划
#   https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @wu_yan_zu《动态规划+记忆化回溯 逐行解释 Python3》(LeetCode 题解)
#   https://leetcode.cn/problems/word-break/solutions/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/

from typing import List

import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    res=back_track(s[i:]) or res
            return res
        return back_track(s)