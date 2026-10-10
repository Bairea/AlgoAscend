# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 287. 寻找重复数 (Find the Duplicate Number) | 难度: 中等 | 官方分组: 技巧
# 题目链接: https://leetcode.cn/problems/find-the-duplicate-number/
# 题意: n+1 个数在 [1,n] 内找唯一重复数（不改数组 O(1) 空间）
# 考点: Floyd 判圈（快慢指针）把 nums 看作 i→nums[i] 的链表，重复值即环入口；或二分抽屉原理
# 标签: 位运算,数组,双指针,二分查找,Floyd 判圈算法,抽屉原理
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# hello-algo: 第10章 搜索 · 二分查找
#   https://www.hello-algo.com/chapter_searching/binary_search/
# 题解来源: @endlesscheng《用基环树理解，做法同 142. 环形链表 II》(LeetCode 题解)
#   https://leetcode.cn/problems/find-the-duplicate-number/solutions/yong-ji-huan-shu-li-jie-zuo-fa-tong-142-tkoc2/

from typing import List

# 代码逻辑同 142. 环形链表 II
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0  # 0 一定不在环上，适合作为起点
        while True:
            slow = nums[slow]  # 等价于 slow = slow.next
            fast = nums[nums[fast]]  # 等价于 fast = fast.next.next
            if fast == slow:  # 快慢指针移动到同一个节点
                break

        head = 0  # 再用一个指针，从起点出发
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        return slow  # 入环口即重复元素