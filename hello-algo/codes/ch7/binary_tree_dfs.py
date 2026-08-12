from binary_tree import TreeNode

# 先按照顺序找到尽头的节点，然后才开始塞入节点值
# 前序 根左右
# 中序 左根右
# 后序 左右根


def pre_order(root: TreeNode | None, res: list[int]) -> None:
    """前序遍历：根 -> 左 -> 右"""
    if root is None:
        return
    res.append(root.val)
    pre_order(root.left, res)
    pre_order(root.right, res)


def in_order(root: TreeNode | None, res: list[int]) -> None:
    """中序遍历：左 -> 根 -> 右"""
    if root is None:
        return
    in_order(root.left, res)
    res.append(root.val)
    in_order(root.right, res)


def post_order(root: TreeNode | None, res: list[int]) -> None:
    """后序遍历：左 -> 右 -> 根"""
    if root is None:
        return
    post_order(root.left, res)
    post_order(root.right, res)
    res.append(root.val)


if __name__ == "__main__":
    # 构建测试二叉树：
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    res: list[int] = []
    pre_order(n1, res)
    print("前序遍历:", res)  # [1, 2, 4, 5, 3]

    res.clear()
    in_order(n1, res)
    print("中序遍历:", res)  # [4, 2, 5, 1, 3]

    res.clear()
    post_order(n1, res)
    print("后序遍历:", res)  # [4, 5, 2, 3, 1]
