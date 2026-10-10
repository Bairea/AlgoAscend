# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 148. 排序链表 (Sort List) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/sort-list/
# 题意: O(n log n) 时间排序链表（进阶：O(1) 空间）
# 考点: 归并排序：快慢指针找中点断开，递归排序两段，再合并（链表排序的标准解）
# 标签: 链表,双指针,分治,排序,归并排序
# hello-algo: 第11章 排序 · 归并排序
#   https://www.hello-algo.com/chapter_sorting/merge_sort/
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《排序链表》(LeetCode 题解)
#   https://leetcode.cn/problems/sort-list/solutions/pai-xu-lian-biao-by-leetcode-solution/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        if not head:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1
        
        return dummyHead.next