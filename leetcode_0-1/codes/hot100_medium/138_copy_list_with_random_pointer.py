# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 138. 随机链表的复制 (Copy List with Random Pointer) | 难度: 中等 | 官方分组: 链表
# 题目链接: https://leetcode.cn/problems/copy-list-with-random-pointer/
# 题意: 深拷贝带 random 指针的链表
# 考点: 哈希表存「旧节点→新节点」两遍扫描建立 next/random；或拼接-拆分法 O(1) 空间
# 标签: 哈希表,链表
# hello-algo: 第6章 哈希表 · 哈希表
#   https://www.hello-algo.com/chapter_hashing/hash_map/
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @jyd《138. 复制带随机指针的链表（清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/copy-list-with-random-pointer/solutions/138-fu-zhi-dai-sui-ji-zhi-zhen-de-lian-b-6jeo/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点