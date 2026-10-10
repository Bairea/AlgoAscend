# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 437. 路径总和 III (Path Sum III) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/path-sum-iii/
# 题意: 统计路径和等于 targetSum 的路径数（向下、不必到叶）
# 考点: 树上前缀和 + 回溯：prefix=根到当前路径和，查 prefix-target 计数；离开时撤销（回溯思想）
# 标签: 树,深度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# hello-algo: 第13章 回溯 · 回溯算法
#   https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
# 题解来源: @LeetCode-Solution《路径总和 III》(LeetCode 题解)
#   https://leetcode.cn/problems/path-sum-iii/solutions/lu-jing-zong-he-iii-by-leetcode-solution-z9td/

import collections

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)