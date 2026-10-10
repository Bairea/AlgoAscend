# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 160. 相交链表 (Intersection of Two Linked Lists) | 难度: 简单 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/intersection-of-two-linked-lists/
# 题意: 求两个单链表相交的起始节点
# 考点: 双指针互换轨道（A 走完走 B）：两指针走过相同总长度后同步到达交点
# 标签: 哈希表,链表,双指针
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @jyd《相交链表（双指针）》(LeetCode 题解)
#   https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/intersection-of-two-linked-lists-shuang-zhi-zhen-l/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A