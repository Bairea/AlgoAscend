# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 19. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# 题意: 删除链表倒数第 n 个节点（一趟扫描）
# 考点: 哑结点 + 快慢指针：快指针先走 n 步，快慢同走到快指针到尾，慢指针下一个即待删
# 标签: 链表,双指针
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《删除链表的倒数第N个节点》(LeetCode 题解)
#   https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next