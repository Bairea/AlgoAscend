# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 98. 验证二叉搜索树 (Validate Binary Search Tree) | 难度: 中等 | 官方分组: 二叉树
# 题目链接: https://leetcode.cn/problems/validate-binary-search-tree/
# 题意: 判断二叉树是否为合法二叉搜索树
# 考点: BST 性质验证：中序遍历严格递增，或递归传递 (下界, 上界)
# 标签: 树,深度优先搜索,二叉搜索树,二叉树
# hello-algo: 第7章 树 · 二叉搜索树
#   https://www.hello-algo.com/chapter_tree/binary_search_tree/
# hello-algo: 第7章 树 · 二叉树遍历
#   https://www.hello-algo.com/chapter_tree/binary_tree_traversal/
# 题解来源: @LeetCode-Solution《验证二叉搜索树》(LeetCode 题解)
#   https://leetcode.cn/problems/validate-binary-search-tree/solutions/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/

# 本地运行用最小节点定义（LeetCode 提交时无需）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True