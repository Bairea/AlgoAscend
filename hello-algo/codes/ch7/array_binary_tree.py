r"""
数组表示法存储二叉树（完全二叉树编号法）

核心笔记：
- 节点按下标存储，下标 0 是根节点，空位用 None 占位
- 索引关键规则（由下标推算亲戚下标）：
    left   = 2 * i + 1      左孩子下标
    right  = 2 * i + 2      右孩子下标
    parent = (i - 1) // 2   父节点下标
- 数组本身就是层序遍历的顺序（从上到下、从左到右）
- 越界下标与 None 统一视为"无节点"，递归可安全终止

示例：tree = [1,2,3,4,None,6,7,8,9,None,None,12,None,None,15]

下标: 0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
值:   1    2    3    4  None  6    7    8    9  None None 12  None None  15

                   1 (0)
                 /     \
            2 (1)       3 (2)
            / \         / \
        4 (3)  X     6 (5) 7 (6)
        /  \         /  \     \
     8 (7) 9(8)   12(11)    15(14)
"""

tree = [1,2,3,4,None,6,7,8,9,None,None,12,None,None,15]

class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        # 拷贝一份数组，避免外部修改影响内部结构
        self._tree = list(arr)

    def size(self):
        return len(self._tree)

    def val(self, i: int) -> int | None:
        # 越界或空位都返回 None，统一表示"该位置没有节点"
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    # 索引规则：算出的是【下标】而不是值，取值需要再套 val()
    def left(self, i: int) -> int | None:
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        # 数组天然就是层序排列，线性扫一遍、跳过 None 即可
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        # 递归出口：空节点（含越界）直接返回
        if self.val(i) is None:
            return

        # 访问顺序固定为 root -> left -> right
        # 前/中/后序的区别只在"什么时候记录值"

        # 前序 = root 之后立即记录
        if order == "pre":
            self.res.append(self.val(i))

        # left：深入左子树
        self.dfs(self.left(i), order)
        # 中序 = left 回来之后、right 出发之前记录
        if order == "in":
            self.res.append(self.val(i))

        # right：深入右子树
        self.dfs(self.right(i), order)
        # 后序 = right 也回来之后记录
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="post")
        return self.res
