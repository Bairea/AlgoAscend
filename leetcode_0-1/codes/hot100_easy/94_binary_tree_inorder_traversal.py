# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 94. 二叉树的中序遍历 (Binary Tree Inorder Traversal) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/binary-tree-inorder-traversal/
# 题意: 返回二叉树的中序遍历序列
# 考点: 递归遍历（左→根→右）；迭代写法需用栈模拟（白灰标记法）
# 标签: 栈,树,深度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# hello-algo: 第5章 栈与队列 · 栈
#   https://www.hello-algo.com/chapter_stack_and_queue/stack/
# 题解来源: @hzhu212《颜色标记法，一种通用且简明的树遍历方法》(LeetCode 题解)
#   https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/

from typing import List

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res