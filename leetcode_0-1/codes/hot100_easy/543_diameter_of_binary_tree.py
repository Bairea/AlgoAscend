# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 543. 二叉树的直径 (Diameter of Binary Tree) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/diameter-of-binary-tree/
# 题意: 求二叉树中任意两节点间路径的最大边数（直径）
# 考点: 后序遍历聚合：每个节点贡献 l+1 与 r+1，全局维护 l+r 的最大值（直径）
# 标签: 树,深度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# 题解来源: @LeetCode-Solution《二叉树的直径》(LeetCode 题解)
#   https://leetcode.cn/problems/diameter-of-binary-tree/solutions/er-cha-shu-de-zhi-jing-by-leetcode-solution/

from typing import Optional

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1