# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 141. 环形链表 (Linked List Cycle) | 难度: 简单 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/linked-list-cycle/
# 题意: 判断链表中是否存在环
# 考点: 快慢指针（Floyd 判圈）：快指针每次走 2 步，若相遇则有环
# 标签: 哈希表,链表,双指针
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《环形链表》(LeetCode 题解)
#   https://leetcode.cn/problems/linked-list-cycle/solutions/huan-xing-lian-biao-by-leetcode-solution/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True