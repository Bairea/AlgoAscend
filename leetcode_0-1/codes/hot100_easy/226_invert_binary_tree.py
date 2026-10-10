# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 226. 翻转二叉树 (Invert Binary Tree) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/invert-binary-tree/
# 题意: 把每个节点的左右子树交换（镜像）
# 考点: 递归：先翻转左右子树，再交换 root 的左右引用
# 标签: 树,深度优先搜索,广度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树
#   https://www.hello-algo.com/chapter_tree/binary_tree/
# 题解来源: @LeetCode-Solution《翻转二叉树》(LeetCode 题解)
#   https://leetcode.cn/problems/invert-binary-tree/solutions/fan-zhuan-er-cha-shu-by-leetcode-solution/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root