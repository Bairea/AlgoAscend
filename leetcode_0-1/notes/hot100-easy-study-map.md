# LeetCode 热题 100 · 简单题 → hello-algo 学习地图

> 抓取时间：2026-10-09。题目清单与「官方知识点分组」取自力扣学习计划页《LeetCode 热题 100》（leetcode.cn/studyplan/top-100-liked/），每题的 Python 题解取自力扣题解区（优先官方题解 `@LeetCode-Solution`，无官方 Python 代码的题目用高赞社区题解兜底，详见第 7 节）。hello-algo 章节编号已对照 hello-algo.com 当前在线版本（含第 3 章「数据结构」的新版编号）。
>
> 配套文件：`notes/hot100-easy-map.csv`（本地图的表格版，Excel 可直接打开）；`codes/hot100_easy/`（20 个可独立运行的 Python 题解文件，文件名与本文一致）。

## TL;DR

Hot 100 共 100 题，其中简单题 20 道（中等 69、困难 11）。这 20 道简单题的分布非常集中：**链表 5 道 + 二叉树 6 道，合计 55%**，剩下的零散分布在哈希、栈、二分、贪心、动态规划入门和位运算技巧里。

因此你在 hello-algo 里要看的重点是：**第 4 章「数组与链表」和第 7 章「树」**，其次是第 5 章「栈」、第 6 章「哈希表」、第 10 章「搜索」（二分）、第 14 章「动态规划」（入门小节即可）、第 15 章「贪心」，以及读题解必备的第 2 章「复杂度分析」。有 4 个考点在 hello-algo 中没有专章（异或、摩尔投票、Floyd 判圈、换轨双指针），第 6 节单独补讲。

## 1. Hot 100 官方知识分组全景

力扣把热题 100 按知识点分了 16 组。下表是每个组的题量和其中的简单题（简单题按题号列出）：

| 官方分组 | 组内题数 | 组内简单题 |
| --- | --- | --- |
| 哈希 | 3 | 1 两数之和 |
| 双指针 | 4 | 283 移动零 |
| 链表 | 14 | 160 相交链表、206 反转链表、234 回文链表、141 环形链表、21 合并两个有序链表 |
| 二叉树 | 15 | 94 中序遍历、104 最大深度、226 翻转二叉树、101 对称二叉树、543 直径、108 有序数组转 BST |
| 二分查找 | 6 | 35 搜索插入位置 |
| 栈 | 5 | 20 有效的括号 |
| 贪心算法 | 4 | 121 买卖股票的最佳时机 |
| 动态规划 | 10 | 70 爬楼梯、118 杨辉三角 |
| 技巧 | 5 | 136 只出现一次的数字、169 多数元素 |
| 滑动窗口 | 2 | — |
| 子串 | 3 | — |
| 普通数组 | 5 | — |
| 矩阵 | 4 | — |
| 图论 | 4 | — |
| 回溯 | 8 | — |
| 堆 | 3 | — |
| 多维动态规划 | 5 | — |
| **合计** | **100** | **20** |

一句话解读：简单题基本是「数据结构操作 + 单层思想」的入口题；滑动窗口、回溯、堆、图论这些组完全没有简单题，它们的第一道题就是中等难度。所以先把链表和二叉树的简单题刷扎实，是后面中档题的地基。

## 2. 知识点 → hello-algo 阅读地图

| Hot 100 分组 | 对应 hello-algo 章节（当前在线版编号） | 覆盖度说明 |
| --- | --- | --- |
| 链表（5 题） | [第 4 章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/) | 节点定义、引用赋值、增删操作讲得完整；但 Floyd 判圈（141）和换轨双指针（160）这两个技巧书里没有 |
| 二叉树（6 题） | [第 7 章 树 · 二叉树](https://www.hello-algo.com/chapter_tree/binary_tree/)、[二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)、[二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree/) | 6 道题全部覆盖：遍历对应 94，递归对应 101/104/226/543，BST + 分治对应 108 |
| 哈希 | [第 6 章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/) | 完整覆盖，dict 的用法和 O(1) 查找原理都在 |
| 双指针 | [第 4 章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/) + [第 11 章 排序 · 快速排序](https://www.hello-algo.com/chapter_sorting/quick_sort/) | 书里没有「双指针」专章，但快排的哨兵划分（partition）就是最典型的双指针应用，283 移动零同款思想 |
| 二分查找 | [第 10 章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)、[二分查找插入点](https://www.hello-algo.com/chapter_searching/binary_search_insertion/) | 完整覆盖，而且比题目更细：35 题考的「插入点」在书里有独立小节 |
| 栈 | [第 5 章 栈与队列 · 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/) | 完整覆盖，20 有效的括号就是栈的教科书式应用 |
| 动态规划 | [第 14 章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/) | 完整覆盖，而且书里用来引入 DP 的例题就是爬楼梯（70） |
| 贪心算法 | [第 15 章 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/) | 思想覆盖，121 的「维护历史最低价」是典型贪心 |
| 技巧 | [第 6 章 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/) + [第 11 章 排序](https://www.hello-algo.com/chapter_sorting/sorting_algorithm/) + [第 3 章 数据结构 · 数字编码](https://www.hello-algo.com/chapter_data_structure/number_encoding/) | 部分覆盖：169 可用哈希/排序解；136 的异或、169 的摩尔投票是书外技巧 |

另外，**第 2 章[复杂度分析](https://www.hello-algo.com/chapter_computational_complexity/time_complexity/)建议最先读**：每道题的题解都会用 O 记号分析时间/空间开销，这一章是读懂题解讨论区的前提。

## 3. 建议阅读顺序（每章配练习题）

按依赖关系排序：先会读复杂度，再学链表（操作最基础、后续题依赖它），然后栈/哈希，接着树，最后是思想类的 DP 和贪心。

| 顺序 | hello-algo 章节 | 读完后练这些题 |
| --- | --- | --- |
| 1 | 第 2 章 复杂度分析（[时间](https://www.hello-algo.com/chapter_computational_complexity/time_complexity/)） | ——（无对应简单题，纯铺垫） |
| 2 | 第 4 章 数组与链表（[链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)） | 206 反转链表 → 283 移动零 → 21 合并两个有序链表 → 141 环形链表 → 160 相交链表 → 234 回文链表 |
| 3 | 第 5 章 栈与队列（[栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)） | 20 有效的括号 |
| 4 | 第 6 章 哈希表（[哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)） | 1 两数之和 → 169 多数元素（哈希解法） |
| 5 | 第 7 章 树（[遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)） | 94 中序遍历 → 104 最大深度 → 226 翻转二叉树 → 101 对称二叉树 → 543 直径 → 108 有序数组转 BST |
| 6 | 第 10 章 搜索（[二分查找插入点](https://www.hello-algo.com/chapter_searching/binary_search_insertion/)） | 35 搜索插入位置 |
| 7 | 第 14 章 动态规划（[初探](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)） | 70 爬楼梯 → 118 杨辉三角 |
| 8 | 第 15 章 贪心算法（[贪心](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)） | 121 买卖股票的最佳时机 |

顺序里有两个刻意的安排：234 回文链表放在链表组最后，因为它综合了 206 的「反转」和 141 的「快慢指针」；108 放在二叉树组最后，因为它需要 BST 性质（第 7 章）加上分治思想（第 12 章[分治](https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/)，可选读）。

## 4. 逐题总表

| # | 题目 | 分组 | 核心考点 | hello-algo 对应 | 本地题解文件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 两数之和 | 哈希 | 哈希表 O(1) 查找 | 第 6 章 哈希表 | [1_two_sum.py](../codes/hot100_easy/1_two_sum.py) |
| 20 | 有效的括号 | 栈 | 栈的 LIFO 配对 | 第 5 章 栈 | [20_valid_parentheses.py](../codes/hot100_easy/20_valid_parentheses.py) |
| 21 | 合并两个有序链表 | 链表 | 哑结点 + 归并 | 第 4 章 链表 / 第 11 章 归并排序 | [21_merge_two_sorted_lists.py](../codes/hot100_easy/21_merge_two_sorted_lists.py) |
| 35 | 搜索插入位置 | 二分查找 | lower_bound 模板 | 第 10 章 二分查找插入点 | [35_search_insert_position.py](../codes/hot100_easy/35_search_insert_position.py) |
| 70 | 爬楼梯 | 动态规划 | DP 状态转移（斐波那契） | 第 14 章 初探动态规划 | [70_climbing_stairs.py](../codes/hot100_easy/70_climbing_stairs.py) |
| 94 | 二叉树的中序遍历 | 二叉树 | 递归/栈迭代遍历 | 第 7 章 二叉树遍历 | [94_binary_tree_inorder_traversal.py](../codes/hot100_easy/94_binary_tree_inorder_traversal.py) |
| 101 | 对称二叉树 | 二叉树 | 镜像递归比较 | 第 7 章 二叉树 | [101_symmetric_tree.py](../codes/hot100_easy/101_symmetric_tree.py) |
| 104 | 二叉树的最大深度 | 二叉树 | 后序递归聚合 | 第 7 章 二叉树遍历 | [104_maximum_depth_of_binary_tree.py](../codes/hot100_easy/104_maximum_depth_of_binary_tree.py) |
| 108 | 将有序数组转换为二叉搜索树 | 二叉树 | 分治 + BST 性质 | 第 7 章 BST / 第 12 章 分治 | [108_convert_sorted_array_to_binary_search_tree.py](../codes/hot100_easy/108_convert_sorted_array_to_binary_search_tree.py) |
| 118 | 杨辉三角 | 动态规划 | 二维递推 | 第 4 章 数组 / 第 14 章 DP | [118_pascals_triangle.py](../codes/hot100_easy/118_pascals_triangle.py) |
| 121 | 买卖股票的最佳时机 | 贪心算法 | 维护历史最低价 | 第 15 章 贪心算法 | [121_best_time_to_buy_and_sell_stock.py](../codes/hot100_easy/121_best_time_to_buy_and_sell_stock.py) |
| 136 | 只出现一次的数字 | 技巧 | 异或消除重复 | 书外（位表示见第 3 章数字编码） | [136_single_number.py](../codes/hot100_easy/136_single_number.py) |
| 141 | 环形链表 | 链表 | 快慢指针判圈 | 第 4 章 链表 | [141_linked_list_cycle.py](../codes/hot100_easy/141_linked_list_cycle.py) |
| 160 | 相交链表 | 链表 | 换轨双指针 | 第 4 章 链表 | [160_intersection_of_two_linked_lists.py](../codes/hot100_easy/160_intersection_of_two_linked_lists.py) |
| 169 | 多数元素 | 技巧 | 摩尔投票/哈希计数 | 第 6 章 哈希表 / 第 11 章 排序 | [169_majority_element.py](../codes/hot100_easy/169_majority_element.py) |
| 206 | 反转链表 | 链表 | 迭代三指针/递归 | 第 4 章 链表 | [206_reverse_linked_list.py](../codes/hot100_easy/206_reverse_linked_list.py) |
| 226 | 翻转二叉树 | 二叉树 | 递归交换子树 | 第 7 章 二叉树 | [226_invert_binary_tree.py](../codes/hot100_easy/226_invert_binary_tree.py) |
| 234 | 回文链表 | 链表 | 快慢指针 + 反转 | 第 4 章 链表 / 第 5 章 栈 | [234_palindrome_linked_list.py](../codes/hot100_easy/234_palindrome_linked_list.py) |
| 283 | 移动零 | 双指针 | 原地 partition | 第 4 章 数组 / 第 11 章 快排 | [283_move_zeroes.py](../codes/hot100_easy/283_move_zeroes.py) |
| 543 | 二叉树的直径 | 二叉树 | 后序遍历维护全局最大 | 第 7 章 二叉树遍历 | [543_diameter_of_binary_tree.py](../codes/hot100_easy/543_diameter_of_binary_tree.py) |

## 5. 逐题详解

每题给出：题意（用完整句子说明要做什么）、考点（这道题真正在考什么）、hello-algo 对应章节、题解来源，以及从力扣题解区抓取的 Python 代码（与 `codes/hot100_easy/` 下的文件内容一致）。

### 1. 两数之和（哈希）

- **题意**：给定一个整数数组 `nums` 和目标值 `target`，找出和为目标值的两个整数的下标。
- **考点**：暴力法是两层循环 O(n²)；用哈希表把内层「查找 target−x 是否出现过」从 O(n) 降到 O(1)，整体降到 O(n)。这是哈希表「空间换时间」的最经典入门。
- **hello-algo**：[第 6 章 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；复杂度分析见[第 2 章](https://www.hello-algo.com/chapter_computational_complexity/time_complexity/)。
- **题解**：官方题解（方法二：哈希表）@[LeetCode-Solution](https://leetcode.cn/problems/two-sum/solutions/liang-shu-zhi-he-by-leetcode-solution/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
```

### 20. 有效的括号（栈）

- **题意**：给定一个只含 `()[]{}` 的字符串，判断它是否是合法的括号序列（每个左括号都必须被同类型的右括号正确闭合）。
- **考点**：栈的后进先出（LIFO）特性天然匹配「最近未闭合的左括号最先被闭合」：左括号入栈，右括号必须与栈顶配对，最后栈要为空。
- **hello-algo**：[第 5 章 栈与队列 · 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/valid-parentheses/solutions/you-xiao-de-gua-hao-by-leetcode-solution/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
```

### 21. 合并两个有序链表（链表）

- **题意**：把两个按升序排列的链表合并成一个新的升序链表，返回合并后的头节点。
- **考点**：链表引用操作的基本功。引入一个「哑结点」避免对头节点的特判；每次比较两个链表的当前节点，把较小的接上去。这个 merge 过程与归并排序里合并两个有序子数组的步骤完全同构。
- **hello-algo**：[第 4 章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)；merge 思想见[第 11 章 归并排序](https://www.hello-algo.com/chapter_sorting/merge_sort/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/merge-two-sorted-lists/solutions/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/)

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
```

### 35. 搜索插入位置（二分查找）

- **题意**：给定一个升序且无重复的数组和一个目标值，找到目标值的下标；不存在时返回它按顺序插入后的位置。
- **考点**：这就是二分查找的「插入点」变体（lower_bound：第一个大于等于 target 的位置）。hello-algo 里对此有专门的模板推导，重点是循环不变量：`nums[left-1] < target <= nums[right+1]`。手写模板之外，工程上可以直接用 `bisect_left`（与你的「刷题原则」一致：手写最优解证明能力，调库作为补充说明）。
- **hello-algo**：[第 10 章 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/) 与 [二分查找插入点](https://www.hello-algo.com/chapter_searching/binary_search_insertion/)。
- **题解**：@[endlesscheng《二分查找总是写不对？看看 lower_bound 模板》](https://leetcode.cn/problems/search-insert-position/solutions/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-nq23/)（取手写模板块）

```python
# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)  # 选择其中一种写法即可

class Solution:/n    def searchInsert(self, nums: List[int], target: int) -> int:/n        return lower_bound(nums, target)
```

### 70. 爬楼梯（动态规划）

- **题意**：你每次可以爬 1 或 2 个台阶，问爬到第 n 阶共有多少种不同方法。
- **考点**：动态规划的入门题。定义 f(i) 为爬到第 i 阶的方案数，则 f(i) = f(i−1) + f(i−2)（最后一步爬 1 阶或 2 阶），初始 f(1)=f(2)=1。这正是斐波那契数列——hello-algo 引入动态规划用的就是这道题，从暴力递归 → 记忆化搜索 → 递推，一步步推导。
- **hello-algo**：[第 14 章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)。
- **题解**：@[jyd（画解算法）](https://leetcode.cn/problems/climbing-stairs/solutions/hua-jie-suan-fa-70-pa-lou-tie-fu-bo-na-qi-shu-by-jy/)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
```

### 94. 二叉树的中序遍历（二叉树）

- **题意**：返回二叉树的中序遍历序列（左子树 → 根 → 右子树）。
- **考点**：递归写法三行；但这里选了社区高赞的「白灰标记法」迭代写法——用一个栈显式模拟递归，白色表示「还没访问、要继续展开」，灰色表示「可以输出」。理解这个写法，后续所有需要「迭代遍历」的中档题（比如用栈做前中后序）都是同一套路。
- **hello-algo**：[第 7 章 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)（书内有递归与栈迭代两种实现）；栈基础见[第 5 章](https://www.hello-algo.com/chapter_stack_and_queue/stack/)。
- **题解**：@[hzhu212](https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/25220/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/)

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
```

### 101. 对称二叉树（二叉树）

- **题意**：判断一棵二叉树是否关于自己的镜像对称。
- **考点**：不是比较「同一棵树的左右孩子」，而是递归比较两棵子树是否互为镜像：左的左对右的右、左的右对右的左。这个「双参数同步递归」的形态在树的题里非常常见。
- **hello-algo**：[第 7 章 树 · 二叉树](https://www.hello-algo.com/chapter_tree/binary_tree/)。
- **题解**：@[jyd（画解算法）](https://leetcode.cn/problems/symmetric-tree/solutions/hua-jie-suan-fa-101-dui-cheng-er-cha-shu-by-guanpe/)

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)
```

### 104. 二叉树的最大深度（二叉树）

- **题意**：求二叉树从根到最深叶子节点的节点数（最大深度）。
- **考点**：后序递归聚合的模板题——子问题（左右子树的深度）算出来后，当前层答案 = max(左, 右) + 1。543 直径是它的直接进阶。
- **hello-algo**：[第 7 章 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/maximum-depth-of-binary-tree/solutions/349250/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/)

```python
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1
```

### 108. 将有序数组转换为二叉搜索树（二叉树）

- **题意**：把一个升序数组转换成一棵高度平衡的二叉搜索树（左右子树高度差不超过 1）。
- **考点**：分治。要平衡，就要让左右两边的节点数尽量相等——取中点做根，左半段递归建左子树、右半段递归建右子树。数组有序保证了「左 < 根 < 右」的 BST 性质自动满足。
- **hello-algo**：[第 7 章 二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree/)；分治思想见[第 12 章](https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/)。
- **题解**：官方题解（方法一：取中点左边为根）@[LeetCode-Solution](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solutions/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/)

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)
```

### 118. 杨辉三角（动态规划）

- **题意**：生成杨辉三角的前 numRows 行。
- **考点**：二维数组的按行递推：f[i][j] = f[i−1][j−1] + f[i−1][j]，边界是每行首尾为 1。它是「用上一行推下一行」这种 DP 递推关系的最直观形态，没有状态压缩等干扰项。
- **hello-algo**：[第 4 章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)；递推思想衔接[第 14 章 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/pascals-triangle/solutions/5308/yang-hui-san-jiao-by-leetcode-solution-lew9/)

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
```

### 121. 买卖股票的最佳时机（贪心算法）

- **题意**：给定每天股价，只能完成一次买入和一次卖出（先买后卖），求最大利润；无法获利则返回 0。
- **考点**：一次遍历，维护「到今天为止的历史最低价」，用当天价格减去它更新答案。本质上是一种贪心：每一天都尝试在历史最低点买入、当天卖出。
- **hello-algo**：[第 15 章 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/136684/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
```

### 136. 只出现一次的数字（技巧）

- **题意**：数组里除一个元素出现一次外，其余元素都出现两次，找出那个只出现一次的元素（要求 O(n) 时间、O(1) 空间）。
- **考点**：异或（XOR）的三条性质：a⊕a=0、a⊕0=a、交换结合律。把所有数异或在一起，成对出现的互相抵消，剩下的就是答案。这与你在 389 题笔记里记的「异或是一种消除重复的运算」是同一个技巧。
- **hello-algo**：书外考点。位的基础表示可看[第 3 章 数据结构 · 数字编码](https://www.hello-algo.com/chapter_data_structure/number_encoding/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/single-number/solutions/5725/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
```

### 141. 环形链表（链表）

- **题意**：判断一个链表中是否存在环（某个节点的 next 指回了链表中前面的节点）。
- **考点**：快慢指针（Floyd 判圈）：慢指针每次走 1 步，快指针每次走 2 步；如果有环，快指针一定会从后面追上慢指针。hello-algo 讲了链表本身，但判圈技巧需要书外补充（见第 6 节）。
- **hello-algo**：[第 4 章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/linked-list-cycle/solutions/351104/huan-xing-lian-biao-by-leetcode-solution/)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
```

### 160. 相交链表（链表）

- **题意**：找出两个单链表相交的起始节点；不相交返回 null。
- **考点**：换轨双指针：指针 A 从 headA 出发，走到底后转去 headB；指针 B 反过来。若链表 A 独有 a 个节点、B 独有 b 个、公共 c 个，则两者都会走过 a+b+c 步，在交点相遇；不相交则同时到达 null。
- **hello-algo**：[第 4 章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)；换轨技巧书外补充（见第 6 节）。
- **题解**：@[jyd（画解算法）](https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/10774/tu-jie-xiang-jiao-lian-biao-shuang-zhi-zhen-wei-/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
```

### 169. 多数元素（技巧）

- **题意**：找出数组中出现次数超过 ⌊n/2⌋ 的元素（题目保证该元素一定存在）。
- **考点**：一题多解的典型。最直观是哈希计数（O(n) 时间 O(n) 空间）或排序取中位（多数元素必然占据中位）；最优雅是摩尔投票：维护一个候选人和计数，遇到不同的数就互相抵消，计数归零换候选人——由于多数元素超过一半，最终活下来的必然是它。
- **hello-algo**：哈希解法对应[第 6 章 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)，排序解法对应[第 11 章 排序](https://www.hello-algo.com/chapter_sorting/sorting_algorithm/)；摩尔投票是书外技巧（见第 6 节）。
- **题解**：官方题解（取最后一个 Python 块：摩尔投票）@[LeetCode-Solution](https://leetcode.cn/problems/majority-element/solutions/17430/duo-shu-yuan-su-by-leetcode-solution/)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```

### 206. 反转链表（链表）

- **题意**：把单链表反转，返回新的头节点（原尾节点）。
- **考点**：链表操作的「核心基本功」。迭代法用 prev/cur 双引用逐个掉头；递归法先递归到尾部，回溯时把每个节点的 next 指回自己。234 回文链表会直接用到它。
- **hello-algo**：[第 4 章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)。
- **题解**：@[jyd（画解算法，递归版）](https://leetcode.cn/problems/reverse-linked-list/solutions/36710/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/)

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回
```

### 226. 翻转二叉树（二叉树）

- **题意**：把每个节点的左右子树交换，得到镜像树（著名的「Homebrew 作者被 Google 拒」梗题）。
- **考点**：最基础的树递归：先递归翻转左右子树，再交换 root 的左右引用。与 104 同为「递归处理整棵树」的第一课。
- **hello-algo**：[第 7 章 树 · 二叉树](https://www.hello-algo.com/chapter_tree/binary_tree/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/invert-binary-tree/solutions/43478/fan-zhuan-er-cha-shu-by-leetcode-solution/)

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
```

### 234. 回文链表（链表）

- **题意**：判断链表里的值序列是否正读反读都一样（回文）。
- **考点**：进阶要求 O(n) 时间 + O(1) 空间，于是综合前面两题的技巧：快慢指针找到中点，反转后半段链表，再逐个比对。如果想省事，把值压入栈再弹出比对也可以（栈解法）。
- **hello-algo**：[第 4 章 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/) + [第 5 章 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)。
- **题解**：官方题解（快慢指针 + 反转后半段）@[LeetCode-Solution](https://leetcode.cn/problems/palindrome-linked-list/solutions/4566/hui-wen-lian-biao-by-leetcode-solution/)

```python
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
```

### 283. 移动零（双指针）

- **题意**：把数组里所有的 0 移到末尾，同时保持非零元素的相对顺序，要求原地操作。
- **考点**：快慢双指针：慢指针指向「下一个非零元素应该放的位置」，快指针扫到非零就交换过去。一趟完成。这与快速排序里 partition（哨兵划分）的指针配合是同一种思想。
- **hello-algo**：[第 4 章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)；partition 思想见[第 11 章 快速排序](https://www.hello-algo.com/chapter_sorting/quick_sort/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/move-zeroes/solutions/486634/yi-dong-ling-by-leetcode-solution/)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
```

### 543. 二叉树的直径（二叉树）

- **题意**：求二叉树中任意两节点之间路径的最大边数（可以不经过根）。
- **考点**：在 104「最大深度」上加一层聚合：对每个节点，经过它的路径长度 = 左深度 + 右深度；在递归过程中维护全局最大值。这个「递归返回一个值、同时维护一个全局答案」的模式是大量树题的通用骨架。
- **hello-algo**：[第 7 章 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)。
- **题解**：官方题解 @[LeetCode-Solution](https://leetcode.cn/problems/diameter-of-binary-tree/solutions/5379/er-cha-shu-de-zhi-jing-by-leetcode-solution/)

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
```

## 6. 四个书外考点速讲

这四个考点在 hello-algo 里没有专章，但都在简单题里出现了，补在这里：

1. **异或消除重复（136，也用于 389）**：异或 `^` 的规则是「相同为 0，不同为 1」，并满足交换律。所以把所有数字异或在一起，出现两次的会互相抵消成 0，最后剩下出现一次的那个数。时间 O(n)、空间 O(1)。
2. **摩尔投票（169）**：想象所有元素两两「打架」，不同的就同归于尽。因为多数元素超过一半，它一定能活到最后。代码里就是一个候选人变量加一个计数器。
3. **Floyd 判圈（141）**：快指针每次走两步、慢指针走一步。进入环之后，快指针相对慢指针每轮多走一步，距离不断缩小，必然相遇——就像操场跑步套圈。
4. **换轨双指针（160）**：让两个指针分别从两条链表头出发，走到头就换到另一条链表继续。这样两个指针走过的总长度相同（a+b+c），要么在交点相遇，要么同时走到空。

## 7. 文件与数据说明

- **题解文件**：`leetcode_0-1/codes/hot100_easy/` 下 20 个 `.py` 文件，命名沿用你现有的 `题号_题目slug.py` 风格。每个文件头部有完整标注（题意、考点、hello-algo 章节、题解来源链接）；引用了 `ListNode`/`TreeNode` 的文件内置了最小节点定义以便本地直接运行（LeetCode 提交时用不到，可忽略）。全部文件已通过 Python 语法检查。
- **CSV**：`leetcode_0-1/notes/hot100-easy-map.csv`（UTF-8 BOM，Excel 直接打开不乱码），含 20 行映射，字段与本文一致。
- **抓取方式**：2026-10-09 用浏览器自动化在 leetcode.cn 上读取学习计划页的完整题单（100 题、16 个官方分组），并通过站内 GraphQL 逐题验证题号、中文标题、难度与标签；题解正文优先取「官方题解」（作者 `LeetCode-Solution`），官方文章没有 Python 代码块的题目改用高赞社区题解，最终 20/20 全部取到可用的 Python 代码。
- **取块规则**：官方题解通常含多个 Python 解法（从暴力到最优），本地文件与本文统一取该文章的**最后一个** Python 代码块（通常是最优解法）；35 特意取了 endlesscheng 的手写二分模板而不是 `bisect` 调库版，108 取了确定性中点版而不是随机中点版，均与手写优先的刷题原则一致。
- **已知局限**：94 的代码是社区作者 hzhu212 的栈迭代写法（官方文章另有递归写法，hello-algo 7.2 两种都讲）；160 的官方文章没有 Python 代码块，用的是 jyd 的高赞解。题解版权归原作者，本文件仅作个人学习用途。
