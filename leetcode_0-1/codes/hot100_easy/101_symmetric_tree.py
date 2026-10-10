# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 101. 对称二叉树 (Symmetric Tree) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/symmetric-tree/
# 题意: 判断二叉树是否轴对称
# 考点: 递归同时比较两棵子树：左的左 vs 右的右（镜像比较）
# 标签: 树,深度优先搜索,广度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树
#   https://www.hello-algo.com/chapter_tree/binary_tree/
# 题解来源: @jyd《101. 对称二叉树（深度优先搜索，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/symmetric-tree/solutions/101-dui-cheng-er-cha-shu-fen-zhi-qing-xi-8oba/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)