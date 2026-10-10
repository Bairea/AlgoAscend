# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 45. 跳跃游戏 II (Jump Game II) | 难度: 中等 | 官方分组: 堆
# 题目链接: https://leetcode.cn/problems/jump-game-ii/
# 题意: 求跳到最后一个下标的最少跳跃次数（保证可达）
# 考点: 贪心分层：当前层末端 end 与可达最远 maxPos，越过 end 步数 +1 并更新
# 标签: 贪心,数组,动态规划
# hello-algo: 第15章 贪心算法 · 贪心算法
#   https://www.hello-algo.com/chapter_greedy/greedy_algorithm/
# 题解来源: @LeetCode-Solution《跳跃游戏 II》(LeetCode 题解)
#   https://leetcode.cn/problems/jump-game-ii/solutions/tiao-yue-you-xi-ii-by-leetcode-solution/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step