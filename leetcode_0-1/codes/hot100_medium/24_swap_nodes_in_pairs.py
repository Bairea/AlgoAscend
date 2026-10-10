# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 24. 两两交换链表中的节点 (Swap Nodes in Pairs) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/swap-nodes-in-pairs/
# 题意: 两两交换相邻节点（如 1↔2、3↔4）
# 考点: 迭代交换：哑结点 temp，每轮把 node1/node2 交换接回（注意指针顺序），或递归
# 标签: 递归,链表
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《两两交换链表中的节点》(LeetCode 题解)
#   https://leetcode.cn/problems/swap-nodes-in-pairs/solutions/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next