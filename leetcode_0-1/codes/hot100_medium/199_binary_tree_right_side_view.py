# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 199. 二叉树的右视图 (Binary Tree Right Side View) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/binary-tree-right-side-view/
# 题意: 从右侧看二叉树，返回每层最右节点值
# 考点: BFS 每层最后一个节点即右视图；或 DFS 根-右-左首个到达者
# 标签: 树,深度优先搜索,广度优先搜索,二叉树
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# hello-algo: 第5章 栈与队列 · 队列
#   https://www.hello-algo.com/chapter_stack_and_queue/queue/
# 题解来源: @LeetCode-Solution《二叉树的右视图》(LeetCode 题解)
#   https://leetcode.cn/problems/binary-tree-right-side-view/solutions/er-cha-shu-de-you-shi-tu-by-leetcode-solution/

from typing import List

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]