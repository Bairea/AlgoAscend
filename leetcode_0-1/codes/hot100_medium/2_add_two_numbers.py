# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 2. 两数相加 (Add Two Numbers) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/add-two-numbers/
# 题意: 两个非负整数按逆序存于链表，求和返回同格式链表
# 考点: 链表模拟加法：逐位相加 + 进位标志，注意最后残留进位
# 标签: 递归,链表,数学
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《两数相加》(LeetCode 题解)
#   https://leetcode.cn/problems/add-two-numbers/solutions/liang-shu-xiang-jia-by-leetcode-solution/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val+l2.val >= 10:
            i = 1
        else:
            i = 0
        node1 = ListNode((l1.val+l2.val)%10)
        node = node1
        if l1.next!=None and l2.next!=None:
            while l1.next and l2.next:
                node.next = ListNode((l1.next.val+l2.next.val+i)%10)
                if l1.next.val+l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                l2 = l2.next
                node = node.next
        if l1.next != None:
            while l1.next:
                node.next = ListNode((l1.next.val+i)%10)
                if l1.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                node = node.next
        if l2.next != None:
            while l2.next:
                node.next = ListNode((l2.next.val+i)%10)
                if l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l2 = l2.next
                node = node.next
        if i == 1:
            node.next = ListNode(1)
        return node1