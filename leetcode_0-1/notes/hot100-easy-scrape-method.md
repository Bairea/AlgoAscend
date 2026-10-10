# Hot 100 简单题抓取与映射：方法总结

> 本文记录 2026-10-09 抓取 LeetCode 热题 100 简单题并映射到 hello-algo 章节的完整做法，目的是把过程沉淀成可复用的流程：以后要抓中等题、困难题，或者换一本书做映射，照着走即可。学习地图本体见 `hot100-easy-study-map.md`。

## 1. 整体流程

整条链路分为六步，每步的产物都落盘，中间数据保存在 `.workbuddy/scratch/`：

1. **启动浏览器自动化环境**（bsk 守护进程 + 会话）。
2. **抓题单**：打开力扣学习计划页，从页面文本提取 100 题的分组、标题、难度。
3. **验证与补全元数据**：用页面内 GraphQL 逐题验证英文 slug、题号、标签。
4. **抓题解**：对每道简单题，取题解文章列表（官方优先），抓文章内容并正则提取 Python 代码块。
5. **生成文件**：从合并后的 JSON 程序化生成 `.py` 题解文件和 CSV 映射表，再用占位符回填方式生成 Markdown 学习地图。
6. **校验收尾**：语法检查、结构检查、关闭会话。

选择「浏览器页面内发 GraphQL 请求」而不是纯页面爬取或站外脚本，原因有三：请求自动带上登录态（credentials: include）；返回 JSON 比解析虚拟化渲染的 DOM 可靠得多；抓取行为发生在用户自己的已登录会话里，与手动浏览无异。

## 2. 关键步骤与命令

### 2.1 bsk 环境启动

宿主环境禁止守护进程自动启动（Job Object breakaway 被禁），自动启动会报 `拒绝访问 (os error 5)`。正确做法是两步：

```bash
# 第一步：起一个常驻前台守护进程（作为持久后台任务运行）
bsk daemon start --foreground

# 第二步：另开命令验证就绪，并禁用自动启动逻辑
BSK_AUTO_START=0 bsk status --json
```

`status` 返回的 `browsers` 列表非空说明浏览器扩展已连接（本机连接的是 Edge）。之后 `bsk session start --json` 拿到 `session_id`，所有命令带 `--session <id>`；结束时 `bsk session stop <id>` 归还借用的标签页。

### 2.2 抓题单：直接读页面文本

学习计划页（`https://leetcode.cn/studyplan/top-100-liked/`）是客户端渲染，但整份题单（100 题、16 个官方知识分组）一次性渲染在 DOM 里，无分页。所以最省事的做法是导航后直接取 `document.body.innerText`，再按「分组名 → 标题 → 简单/中等/困难」的文本模式解析。这一步拿到了简单题的 20 个中文标题和各自的官方分组。

### 2.3 GraphQL 探测：用报错信息驱动

力扣中国站的 GraphQL（`https://leetcode.cn/graphql/`）禁用了内省（`__schema` 查询返回空错误），所以字段名靠「试探 + 读报错」确定。在页面上下文里执行请求：

```js
// evaluate 中执行的通用请求模式
const res = await fetch("https://leetcode.cn/graphql/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  credentials: "include",
  body: JSON.stringify({ query: q, variables: v })
});
return await res.json();
```

探测结论（对本任务有用的最小集合）：

| 需求 | 可用字段 | 备注 |
| --- | --- | --- |
| 单题元数据验证 | `question(titleSlug:)` → `questionFrontendId / title / translatedTitle / difficulty / topicTags` | cn 站没有 `titleCn` 字段，中文标题在 `translatedTitle` |
| 题解文章列表 | `questionSolutionArticles(questionSlug:, first:)` → `edges { node { title slug } }` | 官方题解的文章 slug 以 `by-leetcode-solution` 结尾 |
| 题解文章正文 | `solutionArticle(slug:)` → `title / content / author { username }` | content 是 markdown，代码块含 Python |

明确不可用的（在 com 站文档里常见，但 cn 站没有）：`studyPlanDetail`、`problemsetQuestionList` 的 `searchKeyword` 参数、`questionSolutions`、`solutionDetailArticle`、`solutionArticles`（需要 `userSlug`，是查用户文章用的）。另外 `problemsetQuestionList` 的 `filters.searchKeywords` 虽然合法，但搜中文标题返回空——所以中文标题 → slug 的映射不能靠站内搜索。

### 2.4 slug 验证：不凭记忆写 slug

20 道简单题的英文 slug 先按常见命名写好候选，再逐题调用 `question(titleSlug:)` 查询，用返回的 `translatedTitle` 与题单页抓到的中文标题做严格相等比对、同时校验难度为 Easy。20/20 全部通过，slug 才算数。这一步的意义是：后面拼题目链接和题解链接时不会拼错。

### 2.5 抓题解：官方优先 + 兜底 + 重试

每道题的处理逻辑：

1. 调 `questionSolutionArticles` 拿最多 5 篇题解文章；
2. 排序候选：官方文章（slug 以 `by-leetcode-solution` 结尾）在前，社区文章在后；
3. 依次抓文章正文，用正则提取全部 Python 代码块，取到即停；
4. 一篇文章内取**最后一个** Python 块作为主解法——官方题解通常按「暴力 → 最优」排列，最后一个通常是最优解。

提取正则是本次最大的坑。官方题解的代码块标签不是裸的 ` ```Python `，而是带方括号标注：

````
```Python [sol1-Python3]
````

所以正则必须容忍标注：`/```[^\n]*[Pp]ython[^\n]*\r?\n([\s\S]*?)```/g`。第一版正则只认裸标签，20 题全部 0 命中，就是这个问题。

稳定性措施：所有 GraphQL 调用包一层重试（最多 3 次、失败退避 700ms），文章正文偶发返回 null（疑似限流），靠重试解决；题与题之间加 300–500ms 延迟。两处特判修正：35 搜索插入位置改用 endlesscheng 文章里的**手写 lower_bound 模板块**（而不是 `bisect_left` 一行调库），108 改用官方方法一的**确定性中点块**（而不是 `randint` 随机中点版），两者都更符合「手写最优解优先」的刷题原则。

### 2.6 hello-algo 章节核实：不信任记忆里的编号

hello-algo 新版在复杂度分析之后新增了独立的「第 3 章 数据结构」，之后所有章节编号整体后移（哈希表是第 6 章不是第 5 章，动态规划是第 14 章不是第 13 章）。映射里每一章的编号都用浏览器打开 hello-algo.com 对应页面、读左侧目录原文核实，章节文件夹名用 GitHub API 列 `docs/` 目录确认。教训：这类「版本会变」的外部事实必须现场验证。

### 2.7 文件生成：程序化产出，不做手工搬运

- **20 个 `.py` 文件**：脚本从合并 JSON 读取代码，统一生成文件头（题号、题意、考点、标签、hello-algo 链接、题解来源），自动补 `typing` import 和 `ListNode`/`TreeNode` 最小 stub（按代码里实际出现的标识符判断），生成后用 `ast.parse` 做语法检查。手抄 20 段代码必然出错，程序化生成保证 `.py` 文件与抓取内容逐字一致。
- **CSV**：同一份映射数据用 `csv` 模块生成，编码 `utf-8-sig`（带 BOM），Excel 直接打开不乱码。
- **Markdown**：正文手工撰写，但 20 个代码块的位置只写 `{{CODE_题号}}` 占位符，最后用脚本从同一份 JSON 回填——文档里的代码与 `.py` 文件、与抓取内容三处一致。

### 2.8 校验

收尾做了三类检查：`.py` 全部过 `ast.parse`；Markdown 代码围栏数量 = 代码块数 × 2（40 个，配对完整）、无残留占位符；CSV 行数 = 题数 + 表头。

## 3. 踩坑清单

| 坑 | 现象 | 解法 |
| --- | --- | --- |
| bsk 守护进程起不来 | `cannot start an independent Windows daemon … os error 5` | `bsk daemon start --foreground` 作为持久后台任务，另开命令用 `BSK_AUTO_START=0 bsk status` 验证 |
| bash 的 /tmp 与原生 Python 不互通 | 重定向到 `/tmp` 后 Python 报 FileNotFoundError | 中间数据一律放工作区路径（如 `.workbuddy/scratch/`） |
| cn 站 GraphQL 与 com 站不同 | `studyPlanDetail`、`questionSolutions` 等字段不存在，内省被禁 | 用报错信息驱动逐个试探，最终锁定 `questionSolutionArticles` + `solutionArticle` |
| 站内搜索不支持中文关键词 | `filters.searchKeywords` 搜「爬楼梯」返回空 | 不走搜索：slug 候选 + `question(titleSlug:)` 返回的 `translatedTitle` 反向验证 |
| 官方代码块标签带标注 | 正则 `/```(?:[Pp]ython3?)\n/` 全部 0 命中 | 放宽为「标签行含 python 即命中」 |
| 文章正文偶发为 null | 同一篇文章时有时无 | 请求层加重试与退避，题间加延迟 |
| hello-algo 新旧版章号不同 | 记忆里的「第 5 章哈希表」实为第 6 章 | 打开线上页面读侧栏原文核实每一章 |
| 官方题解老版代码在 iframe 里 | 正文只见 playground iframe 不见代码 | 改抓「文章形式」的官方题解（`by-leetcode-solution` 结尾），其为 markdown 代码块 |

## 4. 产出文件清单

| 文件 | 说明 |
| --- | --- |
| `notes/hot100-easy-study-map.md` | 学习地图主文档（分组全景、映射、阅读顺序、20 题详解含代码） |
| `notes/hot100-easy-map.csv` | 映射表（UTF-8 BOM，Excel 友好） |
| `notes/hot100-easy-scrape-method.md` | 本文 |
| `codes/hot100_easy/NN_slug.py` × 20 | 可独立运行的题解文件，头部含完整标注 |
| `.workbuddy/scratch/hot100_studyplan.json` 等 | 抓取中间数据（题单、验证结果、题解合并 JSON） |
| `.workbuddy/scratch/gen_deliverables.py` | 生成 `.py` 与 CSV 的脚本（可复跑，同路径覆盖、零删除） |

## 5. 复用指南

- **抓中等题/困难题**：流程不变，把题单解析时的难度过滤从「简单」换成目标难度即可；注意中等题数量大（69 道），抓取时间约按题数线性增长，建议分批（每批 10 题）落盘。
- **换映射目标书**：只需替换 2.6 节的章节核实与映射字典，抓取侧完全复用。
- **重跑生成**：`gen_deliverables.py` 与占位符回填脚本均为幂等覆盖写，改映射文案后重跑即可同步 `.py`、CSV、Markdown 三处内容。

## 6. 中等题实测补充（2026-10-09，68 题）

按本文流程跑完 68 道中等题后，新增以下经验，抓大批量题目时直接套用：

### 6.1 限流的真实表现与绕过

限流不是均匀的：连续大量请求后，`questionSolutionArticles`（列表接口）会**单独**返回空数据或 null，而 `solutionArticle`（按 slug 直抓正文）往往还能用。应对优先级：

1. **冷却**：批间隔 3–5 分钟，冷却后先试小批量。
2. **跳过列表接口**：若已知文章 slug，直接调 `solutionArticle`，每题只需 1 次请求。slug 来源见 6.2。
3. **绕开 GraphQL**：`bsk navigate` 到题目页面 + `evaluate` 读 DOM 里的 `/solutions/<article-slug>` 链接，完全不经过被限流的接口（成功率不稳定，页面有时不渲染链接）。

### 6.2 拿到准确文章 slug 的三条路

- **首次抓取时存全量**：`merged` JSON 里的 `articleSlug` 是完整值；诊断输出里若做过 `slice(0, 45)` 截断，不能当完整 slug 用。
- **搜索引擎反查**：CSDN/博客园引用官方题解时按惯例附「作者: LeetCode-Solution 链接: 原文 URL」，搜 `题目拼音 site:leetcode.cn` 或「题号+官方题解」即可拿到完整 slug。这是最可靠的兜底。
- **cn 站 slug 截断规律**：拼音 + `by-leetcode-solution` 拼接超过约 40 字符时会截断再加 4 位哈希后缀，如 74 题官方题解实为 `sou-suo-er-wei-ju-zhen-by-leetcode-solut-vxui`（"solution" 被截成 "solut"）。所以「猜完整拼写」经常错，反查最稳。

### 6.3 「取最后一个 Python 块」策略的失效场景

简单题阶段「最后一个块 = 最优解」基本成立，但中等题官方题解常把**工程化/进阶解法**放在最后，不适合学习直接照搬。实测踩到的：

| 题 | 最后一块实为 | 应取 |
| --- | --- | --- |
| 62 | `math.comb` 一行调库 | 官方二维 DP 块 |
| 230 | 官方 AVL 平衡树 7637 字符工程实现（还带随机插入删除演示） | 官方中序遍历块（348 字符） |
| 34 | `bisect_left` 调库版 | endlesscheng 手写 lower_bound 模板 |
| 17 | `itertools.product` 调库版 | 官方回溯块 |
| 78 | 同一篇文章里**别的题**的代码（powcai 的回溯合集） | 该篇中的 subsets DFS 块 |

结论：中等题必须**逐块审查后选题**，抓取脚本要把每题的全部候选块（标签+内容）落盘，选择放在第二阶段做。这也是把「抓取」与「选择」拆成两步的原因。

### 6.4 中等题的产出

| 文件 | 说明 |
| --- | --- |
| `notes/hot100-medium-study-map.md` | 学习地图主文档（68 题逐题详解含代码） |
| `notes/hot100-medium-map.csv` | 映射表（UTF-8 BOM，Excel 友好） |
| `codes/hot100_medium/NN_slug.py` × 68 | 可独立运行的题解文件 |
| `.workbuddy/scratch/gen_deliverables_medium.py` | 生成脚本（M 映射字典 + .py/CSV 生成） |
| `.workbuddy/scratch/gen_map_medium.py` | 学习地图生成脚本（复用前者导出的 M） |
| `.workbuddy/scratch/merge_medium_fixes.py` | 重抓轮次的选块合并脚本 |

68 题的题解构成：官方 36 题、社区 32 题（其中 endlesscheng 4 题用其手写模板版，jyd/powcai 等高赞作者兜底）。389（简单阶段遗留）等历史文件未受影响，输出全部走独立路径。
