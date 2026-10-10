from __future__ import annotations


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

n1 = TreeNode(val=1)
n2 = TreeNode(val=4)
n3 = TreeNode(val=2)
n4 = TreeNode(val=3)
n5 = TreeNode(val=5)
n6 = TreeNode(val=6)

n1.left = n2
n1.right = n4
n2.left = n5
n2.right = n3
n5.left = n6

# 构造一个函数，打印节点间联系
#   1
# /  \
# 2   3
def display_tree(node: TreeNode, prefix: str = "", is_left: bool = True):
    if node is None:
        return
    connector = "├── " if is_left else "└── "
    if prefix == "":
        print(node.val)
    else:
        print(f"{prefix}{connector}{node.val}")
    new_prefix = prefix + ("│   " if is_left else "    ")
    has_left = node.left is not None
    has_right = node.right is not None
    if has_left:
        display_tree(node.left, new_prefix, is_left=has_right)
    if has_right:
        display_tree(node.right, new_prefix, is_left=False)


if __name__ == "__main__":
    display_tree(n1)
