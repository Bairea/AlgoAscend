# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 142. 环形链表 II (Linked List Cycle II) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/linked-list-cycle-ii/
# 题意: 返回链表入环的第一个节点（无环返回 null）
# 考点: Floyd 判圈第二阶段：相遇后把一个指针放回头部，同速再走，再次相遇即入环口
# 标签: 哈希表,链表,双指针,Floyd 判圈算法
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @jyd《环形链表 II（双指针，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/linked-list-cycle-ii/solutions/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast