from collections import deque


class TreeNode:
    """AVL 树节点"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.height: int = 0  # 节点高度（叶节点高度为 0）
        self.left: TreeNode | None = None  # 左子节点
        self.right: TreeNode | None = None  # 右子节点


class AVLTree:
    """AVL 树：任意节点的左右子树高度差不超过 1 的二叉搜索树"""

    def __init__(self):
        """构造方法：初始化空树"""
        self._root: TreeNode | None = None

    def get_root(self) -> TreeNode | None:
        """获取根节点"""
        return self._root

    def height(self, node: TreeNode | None) -> int:
        """获取节点高度。空节点高度记为 -1，这样叶节点的高度正好是 0"""
        if node is not None:
            return node.height
        return -1

    def update_height(self, node: TreeNode):
        """更新节点高度 = 左右子树高度的最大值 + 1"""
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: TreeNode | None) -> int:
        """平衡因子 = 左子树高度 - 右子树高度，绝对值不超过 1 即平衡"""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode) -> TreeNode:
        """右旋：以 node 的左孩子为轴心，把 node 转到右下"""
        child = node.left
        grand_child = child.right
        child.right = node  # node 变成 child 的右孩子
        node.left = grand_child  # child 原来的右子树挂到 node 左边
        # 旋转改变了节点位置，先更新下面的 node，再更新上面的 child
        self.update_height(node)
        self.update_height(child)
        return child  # child 成为新的子树根节点

    def left_rotate(self, node: TreeNode) -> TreeNode:
        """左旋：以 node 的右孩子为轴心，把 node 转到左下"""
        child = node.right
        grand_child = child.left
        child.left = node
        node.right = grand_child
        self.update_height(node)
        self.update_height(child)
        return child

    def rotate(self, node: TreeNode) -> TreeNode:
        """执行旋转操作，使该子树重新恢复平衡"""
        balance_factor = self.balance_factor(node)
        # 左偏树：左子树过高
        if balance_factor > 1:
            if self.balance_factor(node.left) >= 0:
                # LL 型：直接右旋
                return self.right_rotate(node)
            else:
                # LR 型：先左旋左孩子，再右旋
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 右偏树：右子树过高
        elif balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                # RR 型：直接左旋
                return self.left_rotate(node)
            else:
                # RL 型：先右旋右孩子，再左旋
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # 已经平衡，无须旋转
        return node

    def search(self, val: int) -> TreeNode | None:
        """查找节点：比当前节点小走左子树，大走右子树，相等即找到"""
        cur = self._root
        while cur is not None:
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
            else:
                break
        return cur

    def insert(self, val: int):
        """插入节点"""
        self._root = self.insert_helper(self._root, val)

    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        """递归插入节点（辅助方法）"""
        if node is None:
            return TreeNode(val)
        # 1. 按二叉搜索树规则查找插入位置并插入节点
        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)
        else:
            # 重复节点不插入，直接返回
            return node
        # 2. 递归回溯时更新节点高度
        self.update_height(node)
        # 3. 检查平衡，失衡则旋转
        return self.rotate(node)

    def remove(self, val: int):
        """删除节点"""
        self._root = self.remove_helper(self._root, val)

    def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
        """递归删除节点（辅助方法）"""
        if node is None:
            return None
        # 1. 查找节点并删除
        if val < node.val:
            node.left = self.remove_helper(node.left, val)
        elif val > node.val:
            node.right = self.remove_helper(node.right, val)
        else:
            if node.left is None or node.right is None:
                child = node.left or node.right
                # 子节点数量 = 0，直接删除 node 并返回
                if child is None:
                    return None
                # 子节点数量 = 1，直接用子节点替换 node
                else:
                    node = child
            else:
                # 子节点数量 = 2，用右子树中的最小节点（中序后继）替换当前节点
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.right = self.remove_helper(node.right, temp.val)
                node.val = temp.val
        # 2. 更新节点高度
        self.update_height(node)
        # 3. 执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)


def print_tree(root: TreeNode | None):
    """层序遍历打印二叉树（空节点用 None 占位）"""
    if root is None:
        print("空树")
        return
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
        else:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    # 去掉末尾的 None，使输出更简洁
    while res and res[-1] is None:
        res.pop()
    print(res)


def in_order(node: TreeNode | None, res: list[int]):
    """中序遍历：结果必然是升序，用来验证树仍是合法的二叉搜索树"""
    if node is None:
        return
    in_order(node.left, res)
    res.append(node.val)
    in_order(node.right, res)


def is_balanced(tree: AVLTree, node: TreeNode | None) -> bool:
    """校验 AVL 性质：每个节点的平衡因子绝对值不超过 1"""
    if node is None:
        return True
    return (
        abs(tree.balance_factor(node)) <= 1
        and is_balanced(tree, node.left)
        and is_balanced(tree, node.right)
    )


"""Driver Code"""
if __name__ == "__main__":
    avl_tree = AVLTree()

    # 插入节点 1~15：顺序插入会让普通二叉搜索树退化成链表，
    # AVL 树会自动旋转，始终保持平衡
    print("依次插入节点 1~15")
    for i in range(1, 16):
        avl_tree.insert(i)
    print("层序遍历（None 表示空位）：")
    print_tree(avl_tree.get_root())
    res = []
    in_order(avl_tree.get_root(), res)
    print("中序遍历：", res)
    print("AVL 平衡校验：", "通过" if is_balanced(avl_tree, avl_tree.get_root()) else "失衡")
    print()

    # 查找节点
    node = avl_tree.search(7)
    print("查找 7：", "找到节点，节点值 = {}".format(node.val) if node else "未找到")
    node = avl_tree.search(100)
    print("查找 100：", "找到节点，节点值 = {}".format(node.val) if node else "未找到（返回 None）")
    print()

    # 删除节点（每次删除后都会自动重新平衡）
    for num in [1, 2, 4]:
        avl_tree.remove(num)
        print("删除 {} 后，层序遍历：".format(num))
        print_tree(avl_tree.get_root())
        res = []
        in_order(avl_tree.get_root(), res)
        print("中序遍历：", res)
        print("AVL 平衡校验：", "通过" if is_balanced(avl_tree, avl_tree.get_root()) else "失衡")
        print()
