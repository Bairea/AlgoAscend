# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 5. 最长回文子串 (Longest Palindromic Substring) | 难度: 中等 | 官方分组: 多维动态规划
# 题目链接: https://leetcode.cn/problems/longest-palindromic-substring/
# 题意: 求字符串中的最长回文子串
# 考点: 中心扩展法：枚举 2n-1 个中心向两侧扩；或区间 DP f(i,j)=回文且内层回文
# 标签: 双指针,字符串,动态规划,Manacher 算法
# hello-algo: 第14章 动态规划 · 动态规划问题特性
#   https://www.hello-algo.com/chapter_dynamic_programming/dp_problem_features/
# hello-algo: 第12章 分治 · 分治算法
#   https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/
# 题解来源: @LeetCode-Solution《最长回文子串》(LeetCode 题解)
#   https://leetcode.cn/problems/longest-palindromic-substring/solutions/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/

class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]