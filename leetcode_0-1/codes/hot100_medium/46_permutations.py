# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 46. 全排列 (Permutations) | 难度: 中等 | 官方分组: 回溯
# 题目链接: https://leetcode.cn/problems/permutations/
# 题意: 返回不含重复数字的数组的所有全排列
# 考点: 回溯模板：选一个未用的数填入→递归→撤销；或原地交换法省 visited
# 标签: 数组,回溯
# hello-algo: 第13章 回溯 · 全排列问题
#   https://www.hello-algo.com/chapter_backtracking/permutations_problem/
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# 题解来源: @LeetCode-Solution《全排列》(LeetCode 题解)
#   https://leetcode.cn/problems/permutations/solutions/quan-pai-lie-by-leetcode-solution-2/

from typing import List

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res