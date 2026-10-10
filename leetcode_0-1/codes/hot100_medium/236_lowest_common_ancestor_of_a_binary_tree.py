# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 236. 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# 题意: 求二叉树中两节点的最近公共祖先
# 考点: 后序分治：左右子树分别找 p/q，两边都命中则当前节点即 LCA，否则上交非空一侧
# 标签: 树,深度优先搜索,二叉树,最近公共祖先,Binary Lifting
# hello-algo: 第7章 树 · 二叉树
#   https://www.hello-algo.com/chapter_tree/binary_tree/
# hello-algo: 第12章 分治 · 分治算法
#   https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/
# 题解来源: @jyd《236. 二叉树的最近公共祖先（DFS ，清晰图解）》(LeetCode 题解)
#   https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right: