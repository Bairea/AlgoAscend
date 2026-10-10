# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 102. 二叉树的层序遍历 (Binary Tree Level Order Traversal) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/binary-tree-level-order-traversal/
# 题意: 层序遍历（每层输出一个列表）
# 考点: BFS 逐层：队列按层处理，每轮循环次数 = 当前层节点数
# 标签: 树,广度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# hello-algo: 第5章 栈与队列 · 队列
#   https://www.hello-algo.com/chapter_stack_and_queue/queue/
# 题解来源: @jyd《102. 二叉树的层序遍历（广度优先遍历，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/102-er-cha-shu-de-ceng-xu-bian-li-yan-du-dyf7/

from typing import List, Optional

import collections

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res