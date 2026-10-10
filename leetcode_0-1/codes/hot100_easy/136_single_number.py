# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 136. 只出现一次的数字 (Single Number) | 难度: 简单 | 官方分组: 技巧
# 题目链接: https://leetcode.cn/problems/single-number/
# 题意: 除一个元素出现一次外其余都出现两次，找出那个元素
# 考点: 异或的「消除重复」性质：a^a=0, a^0=a，全部异或后剩下单独的数（位运算，与 389 题同款技巧）
# 标签: 位运算,数组
# hello-algo: （位运算为 hello-algo 书外考点；位表示基础见）第3章 数据结构 · 数字编码
#   https://www.hello-algo.com/chapter_data_structure/number_encoding/
# 题解来源: @LeetCode-Solution《只出现一次的数字》(LeetCode 题解)
#   https://leetcode.cn/problems/single-number/solutions/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)