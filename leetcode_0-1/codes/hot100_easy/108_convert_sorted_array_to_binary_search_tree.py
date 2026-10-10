# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 简单题
# 108. 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree) | 难度: 简单 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# 题意: 把升序数组转换成高度平衡的二叉搜索树
# 考点: 分治：升序数组取中点为根，左右递归建子树；依赖 BST 左<根<右 性质保证平衡
# 标签: 树,二叉搜索树,数组,分治,二叉树
# hello-algo: 第7章 树 · 二叉搜索树
#   https://www.hello-algo.com/chapter_tree/binary_search_tree/
# hello-algo: 第12章 分治 · 分治算法
#   https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/
# 题解来源: @LeetCode-Solution《将有序数组转换为二叉搜索树（官方题解·方法一）》(LeetCode 题解)
#   https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solutions/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/

from typing import List

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)