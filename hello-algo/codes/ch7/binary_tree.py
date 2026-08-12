class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# 插入与删除
p = TreeNode(0)
n1.left = p
p.left = n2
n1.left = n2
# 删除节点通常意味着删除该节点及其所有子树

print(n1)
