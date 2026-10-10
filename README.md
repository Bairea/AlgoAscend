# AlgoAscend

算法与数据结构学习仓库：跟随 [hello-algo](https://www.hello-algo.com/) 系统学习，用 LeetCode 热题 100 实战巩固，题解、学习地图与笔记按知识点整理入库。

## 目录结构

| 路径 | 内容 |
| --- | --- |
| `hello-algo/` | hello-algo 配套代码练习（`ch7/` 第 7 章树已完成，`ch7-re/` 为复习重写） |
| `leetcode_0-1/` | LeetCode 练习与题解：热题 100（`codes/hot100_easy`、`codes/hot100_medium`）与早期题目（`codes/`） |
| `notes/` | 通用刷题原则 |
| `.workbuddy/` | 本地学习工作区（未入库）：工作日志与抓取、生成脚本 |
| `main.py` | uv 项目入口 |

## LeetCode 热题 100 进度

热题 100 = 简单 20 + 中等 68 + 困难 12。

| 难度 | 进度 | 题解目录 | 学习地图 |
| --- | --- | --- | --- |
| 简单 | 20 / 20 | `leetcode_0-1/codes/hot100_easy/` | [hot100-easy-study-map.md](leetcode_0-1/notes/hot100-easy-study-map.md) |
| 中等 | 68 / 68 | `leetcode_0-1/codes/hot100_medium/` | [hot100-medium-study-map.md](leetcode_0-1/notes/hot100-medium-study-map.md) |
| 困难 | 待开始 | - | - |

- 题解 `.py` 文件头部含题号、题意、考点、标签、hello-algo 章节链接与题解来源；自带 `ListNode` / `TreeNode` stub，无第三方依赖，可独立运行。
- 学习地图含官方知识分组全景、hello-algo 章节阅读优先级、建议阅读顺序与逐题详解（代码与 `.py` 文件一致）。
- 映射表（UTF-8 BOM，Excel 可直接打开）：[hot100-easy-map.csv](leetcode_0-1/notes/hot100-easy-map.csv)、[hot100-medium-map.csv](leetcode_0-1/notes/hot100-medium-map.csv)。
- 抓取与生成流程沉淀于 [hot100-easy-scrape-method.md](leetcode_0-1/notes/hot100-easy-scrape-method.md)（含中等题实测补充，换书、换难度可复用）。

## hello-algo 学习进度

| 章节 | 内容 | 状态 |
| --- | --- | --- |
| 第 7 章 树 | 二叉树（链表、数组存储与 BFS/DFS 遍历）、二叉搜索树、AVL 树 | 已完成 |
| 第 8 章 堆 | 堆与 Top-K 问题 | 待开始 |

## 刷题原则

见 [notes/刷题原则.md](notes/刷题原则.md)：面试中先用最优手写解法证明算法能力，再用内置工具展示工程素养，最后点明各方案 trade-off。

## 环境与运行

使用 [uv](https://docs.astral.sh/uv/) 管理，Python 3.13，无第三方依赖：

```bash
uv sync
uv run main.py                                        # 项目入口
uv run leetcode_0-1/codes/hot100_easy/1_two_sum.py    # 单独运行某份题解
```
