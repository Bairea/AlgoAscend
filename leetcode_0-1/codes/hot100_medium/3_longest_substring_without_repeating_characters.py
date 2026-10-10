# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters) | 难度: 中等 | 官方分组: 滑动窗口
# 题目链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 题意: 求不含重复字符的最长子串长度
# 考点: 滑动窗口：右指针扩张、左指针收缩，哈希集合判断窗口内字符是否重复（hello-algo 无滑动窗口专章，属书外考点）
# 标签: 哈希表,字符串,滑动窗口
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# 题解来源: @LeetCode-Solution《无重复字符的最长子串》(LeetCode 题解)
#   https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans