# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 114. 二叉树展开为链表 (Flatten Binary Tree to Linked List) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
# 题意: 把二叉树原地展开为「右指针串联」的链表（前序顺序）
# 考点: 前序展开：对每个节点找左子树的最右节点（前序前驱），把右子树接到前驱上，类似 Morris 遍历
# 标签: 栈,树,深度优先搜索,链表,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# hello-algo: 第4章 数组与链表 · 链表
#   https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/
# 题解来源: @LeetCode-Solution《二叉树展开为链表》(LeetCode 题解)
#   https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right