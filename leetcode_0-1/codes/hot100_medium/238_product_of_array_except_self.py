# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 238. 除了自身以外数组的乘积 (Product of Array Except Self) | 难度: 中等 | 官方分组: 普通数组
# 题目链接: https://leetcode.cn/problems/product-of-array-except-self/
# 题意: 返回除自身外其余元素乘积的数组（禁用除法）
# 考点: 前缀乘积分解：answer[i]=左缀积×右缀积，两次遍历，不用除法
# 标签: 数组,前缀和
# hello-algo: 第4章 数组与链表 · 数组
#   https://www.hello-algo.com/chapter_array_and_linkedlist/array/
# 题解来源: @LeetCode-Solution《除自身以外数组的乘积》(LeetCode 题解)
#   https://leetcode.cn/problems/product-of-array-except-self/solutions/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]
        
        return answer