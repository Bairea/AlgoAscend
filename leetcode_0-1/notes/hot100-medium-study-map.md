# LeetCode 热题 100 · 中等题 × hello-algo 学习地图

> 抓取日期 2026-10-09，共 **68 道中等题**（Hot 100 = 简单 20 + 中等 68 + 困难 12）。
> 题解优先取官方（`@LeetCode-Solution`），官方无 Python 代码块或版本不适合学习时用高赞社区题解兜底，全部经语法校验。
> 简单题版地图见 `hot100-easy-study-map.md`；本文档的章节编号为 hello-algo 新版（已对照 hello-algo.com 侧栏核实）。

## 1. 全景：68 道中等题考什么

| 官方分组 | 题数 | 题目 |
| --- | --- | --- |
| 二叉树 | 8 | 98.验证二叉搜索树、102.二叉树的层序遍历、105.从前序与中序遍历序列构造二叉树、114.二叉树展开为链表、199.二叉树的右视图、230.二叉搜索树中第 K 小的元素、236.二叉树的最近公共祖先、437.路径总和 III |
| 链表 | 7 | 2.两数相加、19.删除链表的倒数第 N 个结点、24.两两交换链表中的节点、138.随机链表的复制、142.环形链表 II、146.LRU 缓存、148.排序链表 |
| 回溯 | 7 | 17.电话号码的字母组合、22.括号生成、39.组合总和、46.全排列、78.子集、79.单词搜索、131.分割回文串 |
| 动态规划 | 7 | 139.单词拆分、152.乘积最大子数组、198.打家劫舍、279.完全平方数、300.最长递增子序列、322.零钱兑换、416.分割等和子集 |
| 多维动态规划 | 5 | 5.最长回文子串、62.不同路径、64.最小路径和、72.编辑距离、1143.最长公共子序列 |
| 堆 | 5 | 45.跳跃游戏 II、55.跳跃游戏、215.数组中的第K个最大元素、347.前 K 个高频元素、763.划分字母区间 |
| 二分查找 | 4 | 33.搜索旋转排序数组、34.在排序数组中查找元素的第一个和最后一个位置、74.搜索二维矩阵、153.寻找旋转排序数组中的最小值 |
| 矩阵 | 4 | 48.旋转图像、54.螺旋矩阵、73.矩阵置零、240.搜索二维矩阵 II |
| 普通数组 | 4 | 53.最大子数组和、56.合并区间、189.轮转数组、238.除了自身以外数组的乘积 |
| 图论 | 4 | 200.岛屿数量、207.课程表、208.实现 Trie (前缀树)、994.腐烂的橘子 |
| 技巧 | 3 | 31.下一个排列、75.颜色分类、287.寻找重复数 |
| 栈 | 3 | 155.最小栈、394.字符串解码、739.每日温度 |
| 滑动窗口 | 2 | 3.无重复字符的最长子串、438.找到字符串中所有字母异位词 |
| 双指针 | 2 | 11.盛最多水的容器、15.三数之和 |
| 哈希 | 2 | 49.字母异位词分组、128.最长连续序列 |
| 子串 | 1 | 560.和为 K 的子数组 |

**分布结论**：与简单题「链表+二叉树占 55%」不同，中等题的重心明显后移——
**动态规划（12 题）+ 回溯（7 题）+ 链表（7 题）+ 二叉树（8 题）占了一半以上**，
其余散布在堆（5）、二分（4）、图（4）、矩阵（4）、普通数组（4）、栈（3）、技巧（3）、双指针（2）、滑动窗口（2）、哈希（2）、子串（1）。

## 2. hello-algo 阅读重点（按优先级）

| 优先级 | 章节 | 对应题目 | 为什么读 |
| --- | --- | --- | --- |
| P0 | 第 14 章 动态规划（14.1 初探 / 14.4 0-1 背包 / 14.5 完全背包 / 14.11 编辑距离） | 53、152、198、139、300、416、62、64、5、1143、72、322、279 | 中等题第一大考点（12 题）。书内把爬楼梯、背包、编辑距离各设专节，几乎每道 DP 题都能落到具体小节 |
| P0 | 第 13 章 回溯（13.1 回溯算法 / 13.2 全排列 / 13.3 子集和） | 46、78、17、39、22、79、131 | 7 题全部可用书内「尝试→撤销→剪枝」框架套解，全排列与子集和两节是直接模板 |
| P0 | 第 7 章 树（7.2 二叉树遍历 / 7.4 二叉搜索树） | 102、98、230、199、114、105、437、236 | 8 题。层序/中序遍历是 102/230/199 的直接工具；98、230 依赖 BST 性质 |
| P1 | 第 4 章 数组与链表 | 2、19、24、138、146、142 + 数组类若干 | 链表 7 题全是引用操作与快慢指针基本功，LRU 需要手写双向链表 |
| P1 | 第 8 章 堆（8.1 堆 / 8.3 Top-K） | 215、347、55、45、763 | Top-K 是专节；55/45/763 官方分组虽在「堆」，本质是贪心 |
| P1 | 第 9 章 图（9.3 图遍历） | 200、994、207、208 | 网格 DFS/BFS 与拓扑排序的基础；208 Trie 只借「树」的形态 |
| P1 | 第 10 章 搜索（10.2 二分查找插入点 / 10.3 二分查找边界） | 74、34、33、153、240 | 34 正是「二分查找边界」一节的例题；33/153 是旋转数组的两个二分变体 |
| P2 | 第 5 章 栈与队列 | 155、394、739 + 102/199 的 BFS | 最小栈=辅助栈、字符串解码=栈配对，BFS 依赖队列 |
| P2 | 第 6 章 哈希表 | 49、128 + 贯穿 560/138/139/347 | 计数分组、哈希集合判连续；多题把它当工具 |
| P2 | 第 11 章 排序 | 56、75、215、148 | 快排 partition（75 三色、215 快速选择）、归并（148） |
| P2 | 第 12 章 分治（12.3 分治构建二叉树） | 105、53、236、148 | 105 与书内 12.3 节是同一问题 |
| P2 | 第 15 章 贪心 | 55、45、763、11 | 11 就是书内 15.4「最大容量问题」的原题；跳跃游戏两题是贪心经典 |
| 参考 | 第 2 章 复杂度分析 / 第 3 章 数据结构 | 全部 | 每题写解法前先能估算复杂度 |

## 3. 建议阅读顺序（按依赖排序）

1. **第 2 章 复杂度分析** —— 之后每题都默认你会算 O(n)/O(log n)。
2. **第 4 章 数组与链表** → 做链表 7 题（2、19、24、142、138、146、148 中的引用操作部分）。
3. **第 5 章 栈与队列、第 6 章 哈希表** → 做 155、394、49、128；这两个数据结构后面到处用。
4. **第 7 章 树** → 做 102、98、230、199、114、236；**第 8 章 堆** → 做 215、347。
5. **第 9 章 图** → 做 200、994、207、79；**第 10 章 搜索** → 做 74、34、33、153、240。
6. **第 11 章 排序、第 12 章 分治** → 做 56、75、148、105、53（分治视角）。
7. **第 13 章 回溯**（集中一个周末）→ 做 46、78、17、39、22、79、131。
8. **第 14 章 动态规划**（体量最大，留整块时间）→ 做 53、152、198、139、300、416、322、279、62、64、1143、72、5。
9. **第 15 章 贪心** → 做 55、45、763、11。

## 4. 书外考点速讲（hello-algo 未覆盖）

以下考点 hello-algo 没有专章，都是「一页纸能说清」的模式，先在这里补齐：

- **滑动窗口**（3、438）：双指针的变种。右指针一直往右扫，左指针只在窗口「变坏」时收缩；窗口内容用哈希表/计数数组维护，每步 O(1) 更新。和快慢指针的区别：两个指针都只单向移动，均摊 O(n)。
- **前缀和 + 哈希**（560）：`prefix[j] - prefix[i] = k` 等价于「子数组和为 k」。边扫边把见过的前缀和放进哈希表计数，查 `prefix[j] - k` 出现过几次即答案。这也是 437 树上版本的底层思想。
- **单调栈**（739）：栈内下标对应的值保持单调（本题递减）。新元素更大时逐个弹栈结算——每个元素至多进出栈一次，均摊 O(n)。形如「下一个更大元素」的题都往这想。
- **Trie 前缀树**（208）：多叉树，节点含 26 叉 children 数组与 isEnd 标志；插入/查询都沿字符走边。hello-algo 的树章讲二叉，多叉只是「每层分支更多」，思想不新。
- **拓扑排序**（207）：Kahn 算法——统计每个点入度，入度 0 的先出队，出队时把后继入度减 1；能出队的总数等于节点数则无环。属于图遍历的排序应用。
- **中心扩展**（5）：回文必以某字符（奇长）或某间隙（偶长）为中心，枚举 2n-1 个中心向两侧扩展。比区间 DP 直观，O(n²) 时间 O(1) 空间。
- ** Floyd 判圈 applied to 数组**（287）：把数组看成链表 `i → nums[i]`，因有重复值必有环，重复元素即环入口——142 题的判圈代码原样可用。

## 5. 逐题详解（68 题）

### 2. 两数相加

- **分组**：链表｜**标签**：递归、链表、数学
- **题意**：两个非负整数按逆序存于链表，求和返回同格式链表（[题目](https://leetcode.cn/problems/add-two-numbers/)）
- **考点**：链表模拟加法：逐位相加 + 进位标志，注意最后残留进位
- **hello-algo**：[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/add-two-numbers/solutions/liang-shu-xiang-jia-by-leetcode-solution/)）

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val+l2.val >= 10:
            i = 1
        else:
            i = 0
        node1 = ListNode((l1.val+l2.val)%10)
        node = node1
        if l1.next!=None and l2.next!=None:
            while l1.next and l2.next:
                node.next = ListNode((l1.next.val+l2.next.val+i)%10)
                if l1.next.val+l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                l2 = l2.next
                node = node.next
        if l1.next != None:
            while l1.next:
                node.next = ListNode((l1.next.val+i)%10)
                if l1.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                node = node.next
        if l2.next != None:
            while l2.next:
                node.next = ListNode((l2.next.val+i)%10)
                if l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l2 = l2.next
                node = node.next
        if i == 1:
            node.next = ListNode(1)
        return node1
```

### 3. 无重复字符的最长子串

- **分组**：滑动窗口｜**标签**：哈希表、字符串、滑动窗口
- **题意**：求不含重复字符的最长子串长度（[题目](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)）
- **考点**：滑动窗口：右指针扩张、左指针收缩，哈希集合判断窗口内字符是否重复（hello-algo 无滑动窗口专章，属书外考点）
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/)）

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
```

### 5. 最长回文子串

- **分组**：多维动态规划｜**标签**：双指针、字符串、动态规划、Manacher 算法
- **题意**：求字符串中的最长回文子串（[题目](https://leetcode.cn/problems/longest-palindromic-substring/)）
- **考点**：中心扩展法：枚举 2n-1 个中心向两侧扩；或区间 DP f(i,j)=回文且内层回文
- **hello-algo**：[第14章 动态规划 · 动态规划问题特性](https://www.hello-algo.com/chapter_dynamic_programming/dp_problem_features/)；[第12章 分治 · 分治算法](https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/longest-palindromic-substring/solutions/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)）

```python
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
```

### 11. 盛最多水的容器

- **分组**：双指针｜**标签**：贪心、数组、双指针
- **题意**：选两条竖线与 x 轴围成容器，求能装最多的水量（[题目](https://leetcode.cn/problems/container-with-most-water/)）
- **考点**：贪心 + 双指针夹逼：每次移动较短的一侧（移长侧不可能变优），面积取最大
- **hello-algo**：[第15章 贪心算法 · 最大容量问题](https://www.hello-algo.com/chapter_greedy/max_capacity_problem/)；[第15章 贪心算法 · 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/container-with-most-water/solutions/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/)）

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

### 15. 三数之和

- **分组**：双指针｜**标签**：数组、双指针、排序
- **题意**：找出数组中所有和为 0 且不重复的三元组（[题目](https://leetcode.cn/problems/3sum/)）
- **考点**：排序后固定最小数，双指针夹逼找另两数；相邻跳过重复值去重
- **hello-algo**：[第11章 排序 · 快速排序](https://www.hello-algo.com/chapter_sorting/quick_sort/)；[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/3sum/solutions/san-shu-zhi-he-by-leetcode-solution/)）

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
```

### 17. 电话号码的字母组合

- **分组**：回溯｜**标签**：哈希表、字符串、回溯
- **题意**：电话按键数字串对应的所有字母组合（[题目](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)）
- **考点**：回溯模板：按数字逐位枚举字母，index 到尾收集结果
- **hello-algo**：[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)；[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/)）

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
```

### 19. 删除链表的倒数第 N 个结点

- **分组**：链表｜**标签**：链表、双指针
- **题意**：删除链表倒数第 n 个节点（一趟扫描）（[题目](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)）
- **考点**：哑结点 + 快慢指针：快指针先走 n 步，快慢同走到快指针到尾，慢指针下一个即待删
- **hello-algo**：[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/)）

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
```

### 22. 括号生成

- **分组**：回溯｜**标签**：字符串、动态规划、回溯、括号序列
- **题意**：生成所有合法的 n 对括号组合（[题目](https://leetcode.cn/problems/generate-parentheses/)）
- **考点**：回溯 + 约束剪枝：左括号剩余可填条件 left<n，右括号条件 right<left
- **hello-algo**：[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/generate-parentheses/solutions/gua-hao-sheng-cheng-by-leetcode-solution/)）

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
```

### 24. 两两交换链表中的节点

- **分组**：链表｜**标签**：递归、链表
- **题意**：两两交换相邻节点（如 1↔2、3↔4）（[题目](https://leetcode.cn/problems/swap-nodes-in-pairs/)）
- **考点**：迭代交换：哑结点 temp，每轮把 node1/node2 交换接回（注意指针顺序），或递归
- **hello-algo**：[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/swap-nodes-in-pairs/solutions/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/)）

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next
```

### 31. 下一个排列

- **分组**：技巧｜**标签**：数组、双指针
- **题意**：把数组原地重排为字典序的下一个排列（[题目](https://leetcode.cn/problems/next-permutation/)）
- **考点**：固定套路：从右找第一个升序对 i，再找右边最后一个大于 nums[i] 的 j，交换后反转后缀
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/next-permutation/solutions/xia-yi-ge-pai-lie-by-leetcode-solution/)）

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

### 33. 搜索旋转排序数组

- **分组**：二分查找｜**标签**：数组、二分查找
- **题意**：在旋转过的升序数组中 O(log n) 查找 target（[题目](https://leetcode.cn/problems/search-in-rotated-sorted-array/)）
- **考点**：旋转数组二分：mid 把数组切成一半有序一半无序，先判哪半有序再判 target 在不在其中
- **hello-algo**：[第10章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/)）

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```

### 34. 在排序数组中查找元素的第一个和最后一个位置

- **分组**：二分查找｜**标签**：数组、二分查找
- **题意**：升序数组中 target 的首尾下标，O(log n)（[题目](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)）
- **考点**：二分查找边界：手写 lower_bound 找起点，再对 target+1 找终点（或右边界变体）
- **hello-algo**：[第10章 搜索 · 二分查找边界](https://www.hello-algo.com/chapter_searching/binary_search_edge/)；[第10章 搜索 · 二分查找插入点](https://www.hello-algo.com/chapter_searching/binary_search_insertion/)
- **题解**：社区题解 @endlesscheng（[题解原文](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-t9l9/)）

```python
class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]
```

### 39. 组合总和

- **分组**：回溯｜**标签**：数组、回溯
- **题意**：找出所有使数字和为 target 的组合（数字可重复选用）（[题目](https://leetcode.cn/problems/combination-sum/)）
- **考点**：组合回溯：可重复选当前数（递归传 i 而非 i+1），排序后剪枝（超 target 即 break）
- **hello-algo**：[第13章 回溯 · 子集和问题](https://www.hello-algo.com/chapter_backtracking/subset_sum_problem/)；[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/combination-sum/solutions/39-zu-he-zong-he-hui-su-qing-xi-tu-jie-b-9zx7/)）

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(
            state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
        ):
            """回溯算法：子集和 I"""
            # 子集和等于 target 时，记录解
            if target == 0:
                res.append(list(state))
                return
            # 遍历所有选择
            # 剪枝二：从 start 开始遍历，避免生成重复子集
            for i in range(start, len(choices)):
                # 剪枝一：若子集和超过 target ，则直接结束循环
                # 这是因为数组已排序，后边元素更大，子集和一定超过 target
                if target - choices[i] < 0:
                    break
                # 尝试：做出选择，更新 target, start
                state.append(choices[i])
                # 进行下一轮选择
                backtrack(state, target - choices[i], choices, i, res)
                # 回退：撤销选择，恢复到之前的状态
                state.pop()

        state = []  # 状态（子集）
        candidates.sort()  # 对 candidates 进行排序
        start = 0  # 遍历起始点
        res = []  # 结果列表（子集列表）
        backtrack(state, target, candidates, start, res)
        return res
```

### 45. 跳跃游戏 II

- **分组**：堆｜**标签**：贪心、数组、动态规划
- **题意**：求跳到最后一个下标的最少跳跃次数（保证可达）（[题目](https://leetcode.cn/problems/jump-game-ii/)）
- **考点**：贪心分层：当前层末端 end 与可达最远 maxPos，越过 end 步数 +1 并更新
- **hello-algo**：[第15章 贪心算法 · 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/jump-game-ii/solutions/tiao-yue-you-xi-ii-by-leetcode-solution/)）

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
```

### 46. 全排列

- **分组**：回溯｜**标签**：数组、回溯
- **题意**：返回不含重复数字的数组的所有全排列（[题目](https://leetcode.cn/problems/permutations/)）
- **考点**：回溯模板：选一个未用的数填入→递归→撤销；或原地交换法省 visited
- **hello-algo**：[第13章 回溯 · 全排列问题](https://www.hello-algo.com/chapter_backtracking/permutations_problem/)；[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/permutations/solutions/quan-pai-lie-by-leetcode-solution-2/)）

```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
```

### 48. 旋转图像

- **分组**：矩阵｜**标签**：数组、数学、矩阵
- **题意**：原地顺时针旋转矩阵 90°（[题目](https://leetcode.cn/problems/rotate-image/)）
- **考点**：先水平翻转再主对角线转置 = 顺时针旋转 90°；数学关系 (i,j)→(j,n-1-i)
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/rotate-image/solutions/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/)）

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### 49. 字母异位词分组

- **分组**：哈希｜**标签**：数组、哈希表、字符串、排序
- **题意**：把字母异位词（字母相同顺序不同）分到同一组（[题目](https://leetcode.cn/problems/group-anagrams/)）
- **考点**：哈希表分组：对每个词做 26 字母计数，计数元组作 key 归组（异序词计数相同）
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；[第11章 排序 · 计数排序](https://www.hello-algo.com/chapter_sorting/counting_sort/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/group-anagrams/solutions/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/)）

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())
```

### 53. 最大子数组和

- **分组**：普通数组｜**标签**：数组、分治、动态规划
- **题意**：求连续子数组的最大和（[题目](https://leetcode.cn/problems/maximum-subarray/)）
- **考点**：DP：f(i)=max(nums[i], f(i-1)+nums[i])，「以 i 结尾的最大子数组和」；也可分治
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)；[第12章 分治 · 分治算法](https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/)
- **题解**：社区题解 @liweiwei1419（[题解原文](https://leetcode.cn/problems/maximum-subarray/solutions/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-jav/)）

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
```

### 54. 螺旋矩阵

- **分组**：矩阵｜**标签**：数组、矩阵、模拟
- **题意**：按顺时针螺旋顺序返回矩阵所有元素（[题目](https://leetcode.cn/problems/spiral-matrix/)）
- **考点**：边界收缩模拟：按 左→右/上→下/右→左/下→上 四边遍历，逐层向内收缩
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/spiral-matrix/solutions/luo-xuan-ju-zhen-by-leetcode-solution/)）

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
```

### 55. 跳跃游戏

- **分组**：堆｜**标签**：贪心、数组、动态规划
- **题意**：判断能否从第一个下标跳到最后一个下标（[题目](https://leetcode.cn/problems/jump-game/)）
- **考点**：贪心维护「当前能到达的最远下标」rightmost，扫一遍判定
- **hello-algo**：[第15章 贪心算法 · 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/jump-game/solutions/tiao-yue-you-xi-by-leetcode-solution/)）

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
```

### 56. 合并区间

- **分组**：普通数组｜**标签**：数组、排序、快速排序
- **题意**：合并所有重叠的区间（[题目](https://leetcode.cn/problems/merge-intervals/)）
- **考点**：按左端点排序后扫描：当前区间与上一结果重叠则合并（右端点取 max）
- **hello-algo**：[第11章 排序 · 排序算法](https://www.hello-algo.com/chapter_sorting/sorting_algorithm/)；[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/merge-intervals/solutions/he-bing-qu-jian-by-leetcode-solution/)）

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
```

### 62. 不同路径

- **分组**：多维动态规划｜**标签**：数学、动态规划、组合数学
- **题意**：m×n 网格从左上到右下的路径数（只能右/下）（[题目](https://leetcode.cn/problems/unique-paths/)）
- **考点**：网格计数 DP：f(i,j)=f(i-1,j)+f(i,j-1)，边界为 1
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/unique-paths/solutions/bu-tong-lu-jing-by-leetcode-solution-hzjf/)）

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
```

### 64. 最小路径和

- **分组**：多维动态规划｜**标签**：数组、动态规划、矩阵
- **题意**：网格从左上到右下的最小路径和（只能右/下）（[题目](https://leetcode.cn/problems/minimum-path-sum/)）
- **考点**：网格 DP：f(i,j)=grid(i,j)+min(上, 左)，首行首列单独初始化
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/minimum-path-sum/solutions/zui-xiao-lu-jing-he-by-leetcode-solution/)）

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]
```

### 72. 编辑距离

- **分组**：多维动态规划｜**标签**：字符串、动态规划
- **题意**：把 word1 变成 word2 的最少编辑次数（增删改）（[题目](https://leetcode.cn/problems/edit-distance/)）
- **考点**：编辑距离 DP：增/删/改三种转移 dp(i,j)=1+min(dp(i-1,j), dp(i,j-1), dp(i-1,j-1))
- **hello-algo**：[第14章 动态规划 · 编辑距离问题](https://www.hello-algo.com/chapter_dynamic_programming/edit_distance_problem/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/edit-distance/solutions/bian-ji-ju-chi-by-leetcode-solution/)）

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [ [0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]
```

### 73. 矩阵置零

- **分组**：矩阵｜**标签**：数组、哈希表、矩阵
- **题意**：把含 0 的行列全部置 0（原地）（[题目](https://leetcode.cn/problems/set-matrix-zeroes/)）
- **考点**：原地标记：用第一行/第一列充当标记数组，空间 O(1)
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/set-matrix-zeroes/solutions/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/)）

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0
```

### 74. 搜索二维矩阵

- **分组**：二分查找｜**标签**：数组、二分查找、矩阵
- **题意**：每行升序且行首大于上行行尾的矩阵中查找 target（[题目](https://leetcode.cn/problems/search-a-2d-matrix/)）
- **考点**：二维升序矩阵按行拼接为一维有序数组：mid 映射到 (row, col) 做标准二分
- **hello-algo**：[第10章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)
- **题解**：社区题解 @infallible-napieror1（[题解原文](https://leetcode.cn/problems/search-a-2d-matrix/solutions/bao-li-er-fen-cha-zhao-ju-zhen-by-infall-4zd6/)）

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        # 需要将一维数组的索引转换为二维矩阵的行和列索引。

        # 获取矩阵维度
        m = len(matrix)     # 行
        n = len(matrix[0])  # 列
        # 定义一维数组的左右指针
        left = 0
        right = m * n -1

        # 闭区间形式
        while left <= right:
            mid = (left + right) // 2
            # 将一维数组的索引转换为二维矩阵的行列
            mid_value = matrix[mid // n][mid % n]
            
            # 注意！！！
            # mid 是 一维索引
            # mid_value 是根据一维索引找到的二维数组对应的值！
            # 用mid_value 跟 target对比
            # 根据结果改边界应该是mid！！！


            if mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
            else:
                return True
        return False
```

### 75. 颜色分类

- **分组**：技巧｜**标签**：数组、双指针、冒泡排序、排序、快速排序
- **题意**：原地把 0/1/2 三色数组排序（单遍扫描）（[题目](https://leetcode.cn/problems/sort-colors/)）
- **考点**：三指针一次遍历（荷兰国旗）：p0/p2 分界，i 扫描交换，快排三向切分思想
- **hello-algo**：[第11章 排序 · 快速排序](https://www.hello-algo.com/chapter_sorting/quick_sort/)；[第11章 排序 · 排序算法](https://www.hello-algo.com/chapter_sorting/sorting_algorithm/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/sort-colors/solutions/yan-se-fen-lei-by-leetcode-solution/)）

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
```

### 78. 子集

- **分组**：回溯｜**标签**：位运算、数组、回溯
- **题意**：返回数组的所有子集（幂集）（[题目](https://leetcode.cn/problems/subsets/)）
- **考点**：子集回溯：每个元素「选/不选」二叉决策；或枚举起点按长度收集
- **hello-algo**：[第13章 回溯 · 子集和问题](https://www.hello-algo.com/chapter_backtracking/subset_sum_problem/)；[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
- **题解**：社区题解 @powcai（[题解原文](https://leetcode.cn/problems/subsets/solutions/hui-su-suan-fa-by-powcai-5/)）

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res
```

### 79. 单词搜索

- **分组**：回溯｜**标签**：深度优先搜索、数组、字符串、回溯、矩阵
- **题意**：判断二维网格中是否存在上下左右相邻拼接的单词路径（[题目](https://leetcode.cn/problems/word-search/)）
- **考点**：网格 DFS + 回溯：visited 标记进入/撤销，四方向探索匹配单词
- **hello-algo**：[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)；[第9章 图 · 图遍历](https://www.hello-algo.com/chapter_graph/graph_traversal/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/word-search/solutions/dan-ci-sou-suo-by-leetcode-solution/)）

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False
```

### 98. 验证二叉搜索树

- **分组**：二叉树｜**标签**：树、深度优先搜索、二叉搜索树、二叉树
- **题意**：判断二叉树是否为合法二叉搜索树（[题目](https://leetcode.cn/problems/validate-binary-search-tree/)）
- **考点**：BST 性质验证：中序遍历严格递增，或递归传递 (下界, 上界)
- **hello-algo**：[第7章 树 · 二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree/)；[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/validate-binary-search-tree/solutions/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/)）

```python
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
```

### 102. 二叉树的层序遍历

- **分组**：二叉树｜**标签**：树、广度优先搜索、二叉树
- **题意**：层序遍历（每层输出一个列表）（[题目](https://leetcode.cn/problems/binary-tree-level-order-traversal/)）
- **考点**：BFS 逐层：队列按层处理，每轮循环次数 = 当前层节点数
- **hello-algo**：[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)；[第5章 栈与队列 · 队列](https://www.hello-algo.com/chapter_stack_and_queue/queue/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/102-er-cha-shu-de-ceng-xu-bian-li-yan-du-dyf7/)）

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
```

### 105. 从前序与中序遍历序列构造二叉树

- **分组**：二叉树｜**标签**：树、数组、哈希表、分治、二叉树
- **题意**：由前序与中序遍历序列构造二叉树（[题目](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)）
- **考点**：分治建树：前序首元素为根，哈希定位根在中序的位置，切分左右递归
- **hello-algo**：[第12章 分治 · 分治构建二叉树问题](https://www.hello-algo.com/chapter_divide_and_conquer/build_binary_tree_problem/)；[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)
- **题解**：社区题解 @jalan（[题解原文](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/python-di-gui-xiang-jie-by-jalan/)）

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
```

### 114. 二叉树展开为链表

- **分组**：二叉树｜**标签**：栈、树、深度优先搜索、链表、二叉树
- **题意**：把二叉树原地展开为「右指针串联」的链表（前序顺序）（[题目](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)）
- **考点**：前序展开：对每个节点找左子树的最右节点（前序前驱），把右子树接到前驱上，类似 Morris 遍历
- **hello-algo**：[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)；[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/)）

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
```

### 128. 最长连续序列

- **分组**：哈希｜**标签**：并查集、数组、哈希表
- **题意**：求无序数组中最长连续数字序列的长度（[题目](https://leetcode.cn/problems/longest-consecutive-sequence/)）
- **考点**：哈希集合 O(n)：只从「无左邻居」的数起数连续段，每个数至多访问两次
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/longest-consecutive-sequence/solutions/zui-chang-lian-xu-xu-lie-by-leetcode-solution/)）

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

### 131. 分割回文串

- **分组**：回溯｜**标签**：字符串、动态规划、回溯
- **题意**：把字符串分割成若干回文子串，返回所有方案（[题目](https://leetcode.cn/problems/palindrome-partitioning/)）
- **考点**：回溯 + 预处理：枚举每个切割点，回文判断用记忆化（DP 预计算）避免重复比较
- **hello-algo**：[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)；[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/palindrome-partitioning/solutions/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/)）

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret
```

### 138. 随机链表的复制

- **分组**：链表｜**标签**：哈希表、链表
- **题意**：深拷贝带 random 指针的链表（[题目](https://leetcode.cn/problems/copy-list-with-random-pointer/)）
- **考点**：哈希表存「旧节点→新节点」两遍扫描建立 next/random；或拼接-拆分法 O(1) 空间
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/copy-list-with-random-pointer/solutions/138-fu-zhi-dai-sui-ji-zhi-zhen-de-lian-b-6jeo/)）

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点
```

### 139. 单词拆分

- **分组**：动态规划｜**标签**：字典树、记忆化、数组、哈希表、字符串、动态规划、Brute-Force Search
- **题意**：判断字符串能否被字典单词完全切分（[题目](https://leetcode.cn/problems/word-break/)）
- **考点**：DP：f(i)=存在 j<i 使 f(j) 且 s[j:i] 在字典；字典用哈希集合 O(1) 查
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)；[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：社区题解 @wu_yan_zu（[题解原文](https://leetcode.cn/problems/word-break/solutions/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/)）

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    res=back_track(s[i:]) or res
            return res
        return back_track(s)
```

### 142. 环形链表 II

- **分组**：链表｜**标签**：哈希表、链表、双指针、Floyd 判圈算法
- **题意**：返回链表入环的第一个节点（无环返回 null）（[题目](https://leetcode.cn/problems/linked-list-cycle-ii/)）
- **考点**：Floyd 判圈第二阶段：相遇后把一个指针放回头部，同速再走，再次相遇即入环口
- **hello-algo**：[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/linked-list-cycle-ii/solutions/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/)）

```python
class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
```

### 146. LRU 缓存

- **分组**：链表｜**标签**：设计、哈希表、链表、双向链表
- **题意**：实现 LRU 缓存：get/put 均 O(1)（[题目](https://leetcode.cn/problems/lru-cache/)）
- **考点**：设计题：哈希表 O(1) 定位 + 双向链表 O(1) 移动/淘汰，伪头尾简化边界
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/lru-cache/solutions/lruhuan-cun-ji-zhi-by-leetcode-solution/)）

```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```

### 148. 排序链表

- **分组**：链表｜**标签**：链表、双指针、分治、排序、归并排序
- **题意**：O(n log n) 时间排序链表（进阶：O(1) 空间）（[题目](https://leetcode.cn/problems/sort-list/)）
- **考点**：归并排序：快慢指针找中点断开，递归排序两段，再合并（链表排序的标准解）
- **hello-algo**：[第11章 排序 · 归并排序](https://www.hello-algo.com/chapter_sorting/merge_sort/)；[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/sort-list/solutions/pai-xu-lian-biao-by-leetcode-solution/)）

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        if not head:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1
        
        return dummyHead.next
```

### 152. 乘积最大子数组

- **分组**：动态规划｜**标签**：数组、动态规划
- **题意**：求乘积最大的非空连续子数组（[题目](https://leetcode.cn/problems/maximum-product-subarray/)）
- **考点**：DP 双状态：同时维护以 i 结尾的最大积与最小积（负数乘负数翻转），fmax=max(三种来源)
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)
- **题解**：社区题解 @powcai（[题解原文](https://leetcode.cn/problems/maximum-product-subarray/solutions/duo-chong-si-lu-qiu-jie-by-powcai-3/)）

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
```

### 153. 寻找旋转排序数组中的最小值

- **分组**：二分查找｜**标签**：数组、二分查找
- **题意**：找旋转升序数组中的最小值，O(log n)（[题目](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)）
- **考点**：二分找旋转点：mid 与右端比较，nums[mid]>右端 说明最小值在右半
- **hello-algo**：[第10章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/)）

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]
```

### 155. 最小栈

- **分组**：栈｜**标签**：栈、设计
- **题意**：设计支持 push/pop/top/getMin 均 O(1) 的栈（[题目](https://leetcode.cn/problems/min-stack/)）
- **考点**：辅助栈同步维护当前最小值（或存差值省空间）
- **hello-algo**：[第5章 栈与队列 · 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/min-stack/solutions/zui-xiao-zhan-by-leetcode-solution/)）

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### 189. 轮转数组

- **分组**：普通数组｜**标签**：数组、数学、双指针
- **题意**：数组向右轮转 k 个位置（原地）（[题目](https://leetcode.cn/problems/rotate-array/)）
- **考点**：三次反转技巧：整体反转→反转前 k 个→反转剩余，原地 O(1) 空间轮转
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：社区题解 @endlesscheng（[题解原文](https://leetcode.cn/problems/rotate-array/solutions/tu-jie-yuan-di-zuo-fa-yi-tu-miao-dong-py-ryfv/)）

```python
# 注：请勿使用切片，会产生额外空间
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等同于轮转 k % n 次
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

### 198. 打家劫舍

- **分组**：动态规划｜**标签**：数组、动态规划
- **题意**：不能偷相邻两家，求能偷到的最高金额（[题目](https://leetcode.cn/problems/house-robber/)）
- **考点**：线性 DP：f(i)=max(f(i-1), f(i-2)+nums[i])（不偷相邻），滚动变量省空间
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/house-robber/solutions/da-jia-jie-she-by-leetcode-solution/)）

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second
```

### 199. 二叉树的右视图

- **分组**：二叉树｜**标签**：树、深度优先搜索、广度优先搜索、二叉树
- **题意**：从右侧看二叉树，返回每层最右节点值（[题目](https://leetcode.cn/problems/binary-tree-right-side-view/)）
- **考点**：BFS 每层最后一个节点即右视图；或 DFS 根-右-左首个到达者
- **hello-algo**：[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)；[第5章 栈与队列 · 队列](https://www.hello-algo.com/chapter_stack_and_queue/queue/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/binary-tree-right-side-view/solutions/er-cha-shu-de-you-shi-tu-by-leetcode-solution/)）

```python
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
```

### 200. 岛屿数量

- **分组**：图论｜**标签**：深度优先搜索、广度优先搜索、并查集、数组、矩阵
- **题意**：统计矩阵中岛屿（相连的 '1'）的数量（[题目](https://leetcode.cn/problems/number-of-islands/)）
- **考点**：网格 DFS「沉岛」：遍历到 '1' 计数 +1 并把连通陆地全部改 '0'
- **hello-algo**：[第9章 图 · 图遍历](https://www.hello-algo.com/chapter_graph/graph_traversal/)；[第9章 图 · 图](https://www.hello-algo.com/chapter_graph/graph/)
- **题解**：官方题解 @LeetCode（[题解原文](https://leetcode.cn/problems/number-of-islands/solutions/dao-yu-shu-liang-by-leetcode/)）

```python
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands
```

### 207. 课程表

- **分组**：图论｜**标签**：深度优先搜索、广度优先搜索、图、拓扑排序、有向无环图
- **题意**：判断先修课依赖关系（有向图）是否存在环（[题目](https://leetcode.cn/problems/course-schedule/)）
- **考点**：拓扑排序（Kahn）：建邻接表 + 入度表，入度 0 者入队，能出队数 = 课程数则无环
- **hello-algo**：[第9章 图 · 图遍历](https://www.hello-algo.com/chapter_graph/graph_traversal/)；[第9章 图 · 图](https://www.hello-algo.com/chapter_graph/graph/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/course-schedule/solutions/ke-cheng-biao-by-leetcode-solution/)）

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
```

### 208. 实现 Trie (前缀树)

- **分组**：图论｜**标签**：设计、字典树、哈希表、字符串
- **题意**：实现前缀树（插入/查找/前缀查询）（[题目](https://leetcode.cn/problems/implement-trie-prefix-tree/)）
- **考点**：Trie 前缀树：节点含 26 叉 children 数组 + isEnd 标志，逐字符走边
- **hello-algo**：[第7章 树 · 二叉树](https://www.hello-algo.com/chapter_tree/binary_tree/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/)）

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
```

### 215. 数组中的第K个最大元素

- **分组**：堆｜**标签**：数组、分治、快速选择、排序、堆（优先队列）
- **题意**：找无序数组中第 k 大的元素（[题目](https://leetcode.cn/problems/kth-largest-element-in-an-array/)）
- **考点**：快速选择（partition 缩小范围，均摊 O(n)）或大小为 k 的堆 O(n log k)
- **hello-algo**：[第8章 堆 · Top-K 问题](https://www.hello-algo.com/chapter_heap/top_k/)；[第8章 堆 · 堆](https://www.hello-algo.com/chapter_heap/heap/)；[第11章 排序 · 快速排序](https://www.hello-algo.com/chapter_sorting/quick_sort/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/215-shu-zu-zhong-de-di-k-ge-zui-da-yuan-d786p/)）

```python
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)
```

### 230. 二叉搜索树中第 K 小的元素

- **分组**：二叉树｜**标签**：树、深度优先搜索、二叉搜索树、二叉树
- **题意**：求 BST 中第 k 小的元素（[题目](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)）
- **考点**：BST 中序遍历有序：第 k 个访问的节点即第 k 小
- **hello-algo**：[第7章 树 · 二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree/)；[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solutions/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07/)）

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```

### 236. 二叉树的最近公共祖先

- **分组**：二叉树｜**标签**：树、深度优先搜索、二叉树、最近公共祖先、Binary Lifting
- **题意**：求二叉树中两节点的最近公共祖先（[题目](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)）
- **考点**：后序分治：左右子树分别找 p/q，两边都命中则当前节点即 LCA，否则上交非空一侧
- **hello-algo**：[第7章 树 · 二叉树](https://www.hello-algo.com/chapter_tree/binary_tree/)；[第12章 分治 · 分治算法](https://www.hello-algo.com/chapter_divide_and_conquer/divide_and_conquer/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/)）

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right:
```

### 238. 除了自身以外数组的乘积

- **分组**：普通数组｜**标签**：数组、前缀和
- **题意**：返回除自身外其余元素乘积的数组（禁用除法）（[题目](https://leetcode.cn/problems/product-of-array-except-self/)）
- **考点**：前缀乘积分解：answer[i]=左缀积×右缀积，两次遍历，不用除法
- **hello-algo**：[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/product-of-array-except-self/solutions/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/)）

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]
        
        return answer
```

### 240. 搜索二维矩阵 II

- **分组**：矩阵｜**标签**：数组、二分查找、分治、矩阵
- **题意**：在每行每列均升序的矩阵中判断 target 是否存在（[题目](https://leetcode.cn/problems/search-a-2d-matrix-ii/)）
- **考点**：从右上角出发搜索：比目标小向下、比目标大向左，本质像在 BST 上走（每步排除一行或一列）
- **hello-algo**：[第10章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)；[第7章 树 · 二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/sou-suo-er-wei-ju-zhen-ii-by-leetcode-so-9hcx/)）

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
```

### 279. 完全平方数

- **分组**：动态规划｜**标签**：广度优先搜索、数学、动态规划、背包问题、完全背包
- **题意**：和为 n 的最少完全平方数个数（[题目](https://leetcode.cn/problems/perfect-squares/)）
- **考点**：完全背包：f[i]=min(f[i-平方数]+1)；也可 BFS 求最短步数
- **hello-algo**：[第14章 动态规划 · 完全背包问题](https://www.hello-algo.com/chapter_dynamic_programming/unbounded_knapsack_problem/)；[第9章 图 · 图遍历](https://www.hello-algo.com/chapter_graph/graph_traversal/)
- **题解**：社区题解 @zi-lai-huo（[题解原文](https://leetcode.cn/problems/perfect-squares/solutions/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/)）

```python
class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1
```

### 287. 寻找重复数

- **分组**：技巧｜**标签**：位运算、数组、双指针、二分查找、Floyd 判圈算法、抽屉原理
- **题意**：n+1 个数在 [1,n] 内找唯一重复数（不改数组 O(1) 空间）（[题目](https://leetcode.cn/problems/find-the-duplicate-number/)）
- **考点**：Floyd 判圈（快慢指针）把 nums 看作 i→nums[i] 的链表，重复值即环入口；或二分抽屉原理
- **hello-algo**：[第4章 数组与链表 · 链表](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/)；[第10章 搜索 · 二分查找](https://www.hello-algo.com/chapter_searching/binary_search/)
- **题解**：社区题解 @endlesscheng（[题解原文](https://leetcode.cn/problems/find-the-duplicate-number/solutions/yong-ji-huan-shu-li-jie-zuo-fa-tong-142-tkoc2/)）

```python
# 代码逻辑同 142. 环形链表 II
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0  # 0 一定不在环上，适合作为起点
        while True:
            slow = nums[slow]  # 等价于 slow = slow.next
            fast = nums[nums[fast]]  # 等价于 fast = fast.next.next
            if fast == slow:  # 快慢指针移动到同一个节点
                break

        head = 0  # 再用一个指针，从起点出发
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        return slow  # 入环口即重复元素
```

### 300. 最长递增子序列

- **分组**：动态规划｜**标签**：数组、二分查找、动态规划、最长上升子序列
- **题意**：求最长严格递增子序列的长度（[题目](https://leetcode.cn/problems/longest-increasing-subsequence/)）
- **考点**：LIS：f(i)=以 i 结尾的最长上升子序列，O(n²) DP；进阶 O(n log n) 贪心+二分
- **hello-algo**：[第14章 动态规划 · 初探动态规划](https://www.hello-algo.com/chapter_dynamic_programming/intro_to_dynamic_programming/)；[第10章 搜索 · 二分查找插入点](https://www.hello-algo.com/chapter_searching/binary_search_insertion/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/longest-increasing-subsequence/solutions/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)）

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

### 322. 零钱兑换

- **分组**：动态规划｜**标签**：广度优先搜索、数组、动态规划、背包问题、完全背包
- **题意**：凑出 amount 的最少硬币数（每种面额无限）（[题目](https://leetcode.cn/problems/coin-change/)）
- **考点**：完全背包：f[x]=min over coins(f[x-coin]+1)，f[0]=0
- **hello-algo**：[第14章 动态规划 · 完全背包问题](https://www.hello-algo.com/chapter_dynamic_programming/unbounded_knapsack_problem/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/coin-change/solutions/322-ling-qian-dui-huan-by-leetcode-solution/)）

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```

### 347. 前 K 个高频元素

- **分组**：堆｜**标签**：数组、哈希表、分治、桶排序、计数、快速选择、排序、堆（优先队列）
- **题意**：返回出现频率前 k 高的元素（[题目](https://leetcode.cn/problems/top-k-frequent-elements/)）
- **考点**：哈希计数 + Top-K：小顶堆维护前 k 高频，或桶排序按频次分桶
- **hello-algo**：[第8章 堆 · Top-K 问题](https://www.hello-algo.com/chapter_heap/top_k/)；[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；[第11章 排序 · 桶排序](https://www.hello-algo.com/chapter_sorting/bucket_sort/)
- **题解**：社区题解 @xxinjiee（[题解原文](https://leetcode.cn/problems/top-k-frequent-elements/solutions/python-dui-pai-xu-by-xxinjiee/)）

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1) 
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1) 
        return [item[0] for item in heap[1:]]
```

### 394. 字符串解码

- **分组**：栈｜**标签**：栈、递归、字符串
- **题意**：解码 k[encoded_string] 形式的字符串（嵌套）（[题目](https://leetcode.cn/problems/decode-string/)）
- **考点**：栈解码：遇 '[' 压入当前串与倍数，遇 ']' 弹出拼接；或递归处理嵌套
- **hello-algo**：[第5章 栈与队列 · 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)
- **题解**：社区题解 @jyd（[题解原文](https://leetcode.cn/problems/decode-string/solutions/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/)）

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res
```

### 416. 分割等和子集

- **分组**：动态规划｜**标签**：数组、动态规划、背包问题、0-1 背包
- **题意**：能否把数组分成两个元素和相等的子集（[题目](https://leetcode.cn/problems/partition-equal-subset-sum/)）
- **考点**：0-1 背包判定：总和一半为容量，dp[j] |= dp[j-num] 倒序遍历
- **hello-algo**：[第14章 动态规划 · 0-1 背包问题](https://www.hello-algo.com/chapter_dynamic_programming/knapsack_problem/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/partition-equal-subset-sum/solutions/fen-ge-deng-he-zi-ji-by-leetcode-solution/)）

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]
```

### 437. 路径总和 III

- **分组**：二叉树｜**标签**：树、深度优先搜索、二叉树
- **题意**：统计路径和等于 targetSum 的路径数（向下、不必到叶）（[题目](https://leetcode.cn/problems/path-sum-iii/)）
- **考点**：树上前缀和 + 回溯：prefix=根到当前路径和，查 prefix-target 计数；离开时撤销（回溯思想）
- **hello-algo**：[第7章 树 · 二叉树遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal/)；[第13章 回溯 · 回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/path-sum-iii/solutions/lu-jing-zong-he-iii-by-leetcode-solution-z9td/)）

```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)
```

### 438. 找到字符串中所有字母异位词

- **分组**：滑动窗口｜**标签**：哈希表、字符串、滑动窗口
- **题意**：找出 s 中所有 p 的异位词子串的起始下标（[题目](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)）
- **考点**：定长滑动窗口：维护 26 长度计数数组，每步 O(1) 更新与比对
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/)）

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            
            if differ == 0:
                ans.append(i + 1)

        return ans
```

### 560. 和为 K 的子数组

- **分组**：子串｜**标签**：数组、哈希表、前缀和
- **题意**：统计和恰好等于 k 的连续子数组的个数（[题目](https://leetcode.cn/problems/subarray-sum-equals-k/)）
- **考点**：前缀和 + 哈希计数：prefix[j]-prefix[i]=k 即子数组和为 k，边扫边查（前缀和属书外考点）
- **hello-algo**：[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)；[第4章 数组与链表 · 数组](https://www.hello-algo.com/chapter_array_and_linkedlist/array/)
- **题解**：社区题解 @endlesscheng（[题解原文](https://leetcode.cn/problems/subarray-sum-equals-k/solutions/qian-zhui-he-ha-xi-biao-cong-liang-ci-bi-4mwr/)）

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s - k]
        return ans
```

### 739. 每日温度

- **分组**：栈｜**标签**：栈、数组、单调栈
- **题意**：求每天等到一个更高温度所需的天数（[题目](https://leetcode.cn/problems/daily-temperatures/)）
- **考点**：单调栈（递减栈）：温度更高时弹栈结算天数差（hello-algo 无单调栈专章，属书外考点）
- **hello-algo**：[第5章 栈与队列 · 栈](https://www.hello-algo.com/chapter_stack_and_queue/stack/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/daily-temperatures/solutions/mei-ri-wen-du-by-leetcode-solution/)）

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
```

### 763. 划分字母区间

- **分组**：堆｜**标签**：贪心、哈希表、双指针、字符串
- **题意**：把字符串切成尽量多的段，使每段字母不跨段出现（[题目](https://leetcode.cn/problems/partition-labels/)）
- **考点**：贪心：记录每字符最后出现位置，当前段延伸到 end=max(end, last[c])，到达即切分
- **hello-algo**：[第15章 贪心算法 · 贪心算法](https://www.hello-algo.com/chapter_greedy/greedy_algorithm/)；[第6章 哈希表 · 哈希表](https://www.hello-algo.com/chapter_hashing/hash_map/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/partition-labels/solutions/hua-fen-zi-mu-qu-jian-by-leetcode-solution/)）

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition
```

### 994. 腐烂的橘子

- **分组**：图论｜**标签**：广度优先搜索、数组、矩阵
- **题意**：新鲜橘子每分钟被相邻烂橘子传染，求全部腐烂时间（[题目](https://leetcode.cn/problems/rotting-oranges/)）
- **考点**：多源 BFS：所有烂橘子同时入队作为第 0 层，扩散层数即分钟数
- **hello-algo**：[第9章 图 · 图遍历](https://www.hello-algo.com/chapter_graph/graph_traversal/)
- **题解**：官方题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/rotting-oranges/solutions/fu-lan-de-ju-zi-by-leetcode-solution/)）

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d
```

### 1143. 最长公共子序列

- **分组**：多维动态规划｜**标签**：字符串、动态规划、最长公共子序列
- **题意**：求两字符串的最长公共子序列长度（[题目](https://leetcode.cn/problems/longest-common-subsequence/)）
- **考点**：经典二维 DP：相等则 dp(i,j)=dp(i-1,j-1)+1，否则取两侧最大
- **hello-algo**：[第14章 动态规划 · 编辑距离问题](https://www.hello-algo.com/chapter_dynamic_programming/edit_distance_problem/)；[第14章 动态规划 · 动态规划问题特性](https://www.hello-algo.com/chapter_dynamic_programming/dp_problem_features/)
- **题解**：社区题解 @LeetCode-Solution（[题解原文](https://leetcode.cn/problems/longest-common-subsequence/solutions/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/)）

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
```

## 6. 与简单题地图的关系

简单题（20 道）练的是**数据结构的基本操作**：链表翻转/判圈、树的四种遍历、栈的配对、哈希计数。
中等题在这些操作之上加了两类东西：

1. **组合技巧**——快慢指针升级为 Floyd 判圈的第二阶段（142）、辅助栈（155）、前缀和（560/437）、双状态 DP（152）；
2. **系统化方法**——回溯的「尝试-撤销」框架、DP 的「状态定义→转移方程→初始值」流水线、图遍历的 BFS 分层。

建议的学习闭环：每道中等题先自己写 30 分钟，卡住再看本文题解的**考点行**（只看提示不看代码），再卡再展开代码；写完对照 hello-algo 对应小节把「为什么这样做」补全。
