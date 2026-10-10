# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 21. 合并两个有序链表 (Merge Two Sorted Lists) | 难度: 简单 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/merge-two-sorted-lists/
# 题意: 把两个升序链表合并成一个升序链表
# 考点: 哑结点 + 逐节点比较拼接；与归并排序的 merge 步骤同构
# 标签: 递归,链表
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# hello-algo: 第11章 排序 · 归并排序
#   https://www.hello-algo.com/chapter_sorting/merge_sort/
# 题解来源: @LeetCode-Solution《合并两个有序链表》(LeetCode 题解)
#   https://leetcode.cn/problems/merge-two-sorted-lists/solutions/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

# 加一个哑节点
