# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 104. 二叉树的最大深度 (Maximum Depth of Binary Tree) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 题意: 求二叉树的最大深度
# 考点: 后序递归聚合子问题：max(左深度, 右深度) + 1
# 标签: 树,深度优先搜索,广度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# 题解来源: @LeetCode-Solution《二叉树的最大深度》(LeetCode 题解)
#   https://leetcode.cn/problems/maximum-depth-of-binary-tree/solutions/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/

class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1