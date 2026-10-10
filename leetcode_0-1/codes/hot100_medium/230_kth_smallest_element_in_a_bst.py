# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 230. 二叉搜索树中第 K 小的元素 (Kth Smallest Element in a BST) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
# 题意: 求 BST 中第 k 小的元素
# 考点: BST 中序遍历有序：第 k 个访问的节点即第 k 小
# 标签: 树,深度优先搜索,二叉搜索树,二叉树
# hello-algo: 第7章 树 · 二叉搜索树
#   https://www.hello-algo.com/chapter_tree/binary_search_tree/
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# 题解来源: @LeetCode-Solution《二叉搜索树中第K小的元素（官方题解·中序遍历）》(LeetCode 题解)
#   https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solutions/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right