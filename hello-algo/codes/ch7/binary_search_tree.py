from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self):
        """构造方法"""
        # 初始化空树
        self._root = None

    def get_root(self) -> TreeNode | None:
        """获取二叉树根节点"""
        return self._root

    def search(self, num: int):
        cur = self._root
        while cur is not None:
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
            else:
                break

        return cur


    def insert(self, num: int):
        if self._root is None:
            self._root = TreeNode(num)
            return

        # 找末端节点
        cur, pre = self._root, None
        while cur is not None:
            if cur.val == num:
                return
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left

        # 插入节点
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node

    def remove(self, num: int):
        if self._root is None:
            return
        cur, pre = self._root, None
        # 找相等的就break，没找到就是None
        while cur is not None:
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left

        # cur是None，没找到就结束
        if cur is None:
            return

        # 找子节点(可能为None)，直接把子节点交给父节点
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                self._root = child
        else:
            # 度为2，即有两个子节点，找右子树的最小的节点(一直左走)
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            self.remove(tmp.val)
            cur.val = tmp.val


def print_tree(root: TreeNode | None):
    """层序遍历打印二叉树(空节点用 None 占位)"""
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
    # 去掉末尾的 None,使输出更简洁
    while res and res[-1] is None:
        res.pop()
    print(res)


"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉搜索树
    bst = BinarySearchTree()
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # 请注意，不同的插入顺序会生成不同的二叉树，该序列可以生成一个完美二叉树
    for num in nums:
        bst.insert(num)
    print("\n初始化的二叉树为\n")
    print_tree(bst.get_root())

    # 查找节点
    node = bst.search(7)
    print("\n查找到的节点对象为: {}，节点值 = {}".format(node, node.val))

    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后，二叉树为\n")
    print_tree(bst.get_root())

    # 删除节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(2)
    print("\n删除节点 2 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(4)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.get_root())
