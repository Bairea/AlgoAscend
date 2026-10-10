# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 55. 跳跃游戏 (Jump Game) | 难度: 中等 | 官方分组: 堆
# 题目链接: https://leetcode.cn/problems/jump-game/
# 题意: 判断能否从第一个下标跳到最后一个下标
# 考点: 贪心维护「当前能到达的最远下标」rightmost，扫一遍判定
# 标签: 贪心,数组,动态规划
# hello-algo: 第15章 贪心算法 · 贪心算法
#   https://www.hello-algo.com/chapter_greedy/greedy_algorithm/
# 题解来源: @LeetCode-Solution《跳跃游戏》(LeetCode 题解)
#   https://leetcode.cn/problems/jump-game/solutions/tiao-yue-you-xi-by-leetcode-solution/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False