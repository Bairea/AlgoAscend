# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 234. 回文链表 (Palindrome Linked List) | 难度: 简单 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/palindrome-linked-list/
# 题意: 判断链表的值序列是否为回文
# 考点: 快慢指针找中点 + 反转后半段逐一比对（综合 206 与 141 的技巧）；也可用栈
# 标签: 栈,递归,链表,双指针
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @LeetCode-Solution《回文链表》(LeetCode 题解)
#   https://leetcode.cn/problems/palindrome-linked-list/solutions/hui-wen-lian-biao-by-leetcode-solution/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous