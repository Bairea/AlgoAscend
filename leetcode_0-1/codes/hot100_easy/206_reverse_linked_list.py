# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 206. 反转链表 (Reverse Linked List) | 难度: 简单 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/reverse-linked-list/
# 题意: 反转单链表
# 考点: 链表引用操作基本功：迭代三指针（prev/cur/next）或递归反转
# 标签: 递归,链表
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @jyd《206. 反转链表（双指针，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/reverse-linked-list/solutions/206-fan-zhuan-lian-biao-shuang-zhi-zhen-r1jel/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回