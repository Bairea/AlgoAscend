# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 105. 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 题意: 由前序与中序遍历序列构造二叉树
# 考点: 分治建树：前序首元素为根，哈希定位根在中序的位置，切分左右递归
# 标签: 树,数组,哈希表,分治,二叉树
# hello-algo: 第12章 分治 · 分治构建二叉树问题
#   https://www.hello-algo.com/chapter_divide_and_conquer/build_binary_tree_problem/
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# 题解来源: @jalan《Python 递归详解》(LeetCode 题解)
#   https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/python-di-gui-xiang-jie-by-jalan/

from typing import List

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root