# Clover Time 当前进度

本文件是本站当前进度源。依据 2026-10-12 的代码、配置与目录核对；不把旧记录或上游模板版本视为本轮验证结果。[历史路线图](/Users/yangzechuan/Documents/GitHub/clovertime/docs/roadmap.md) 保留历史，[首版 Goal](/Users/yangzechuan/Documents/GitHub/clovertime/goals/20261008-0047-clover-time-wiki.md) 保留原施工过程。

## 当前阶段

关键词页面已上线：维护 3 个已有主题，新增 6 个主题的 12 篇双语页面，9 个规划主题均可访问。当前 19 个双语文章主题、38 篇非草稿 MDX；工程、产物、浏览器与线上版本核对通过。游戏实测与搜索引擎收录缺口保留，完整事实 Goal 尚未验收。见 [上线交付](/Users/yangzechuan/Documents/GitHub/clovertime/docs/clover-time/keyword-pages/release.md) 与 [施工清单](/Users/yangzechuan/Documents/GitHub/clovertime/goals/20261013-0032-clover-keyword-pages.md) 。

| 事项 | 当前证据与状态 |
| --- | --- |
| 内容与语言 | en／zh 各 19 篇，共 38 篇非草稿；严格双语覆盖通过，事实限制明确 |
| 工程与产物 | 全部门禁通过，24 套件／400 测试、69 HTML、38 个搜索详情、sitemap 68/68 通过 |
| 交互 | 36 次双语手机／桌面页面检查无横向溢出；菜单、FAQ、语言切换和搜索通过，线上手机操作通过 |
| 生产部署 | clovertime.world 对应 85ffcc69-149f-41cb-a789-6c27a5e6e013；固定地址 173 项文件哈希匹配，域名 HTML 的 Cloudflare 注入差异已单独核对 |
| 源码追溯 | 未提交／推送；生产部署 dirty=true，产物哈希与工作区记录保存，Source 01454bf 不代表新稿已提交 |
| 事实验收 | 兑换、重抽结果、Shadow 能力、Discord／Trello 开发者反向归属仍待补证；不影响来源边界如实呈现 |
| 受保护预览 | build:preview 仍限制英文恰好 10 篇，当前英文 19 篇；本轮未修复，不使用该入口 |
| 统计与服务 | GA4 配置保留；新增自托管 Plausible（analytics.clipcanva.com，无 cookie、不走同意门控），变量 PUBLIC_PLAUSIBLE_SRC 写入 wrangler.toml 与 .env.example，未部署 |
| 搜索引擎 | sitemap 可访问；本轮未提交 IndexNow、未读取 GSC，不声称已收录 |
| 例行与自动部署 | 工作流存在；远端源码同步、CI Secrets 与保鲜排程实际执行未核对 |

## 下一步与验收标准

| 优先级 | 工作 | 验收标准 |
| --- | --- | --- |
| P1 | 补游戏实测事实 | 兑换、重抽、Shadow 与入群权限有对应实际结果；来源说法与本站测试分开 |
| P1 | 搜索引擎提交与收录跟踪 | 明确授权提交后保存回执；GSC 有账号证据，不以提交成功推断收录 |
| P1 | 同步发布源码 | 明确授权 Git 提交／推送后，保留既有改动归属，发布产物可与源码追溯 |
| P2 | 恢复受保护预览 | 消除固定 10 篇限制，原稿哈希不变，预览 noindex 且不进 sitemap，失败不替换原 dist |
| P2 | 核对 CI、备用域与保鲜 | 记录工作流和排程实际结果；不把脚本退出 0 当作保鲜通过 |

## 待确认与保留边界

- 原事实 Goal 的未验收检查点继续保留；上线不证明游戏内兑换与机制已实测。
- public/robots.txt 与 src/pages/robots.txt.ts 双入口仍保留，本轮正式输出符合预期，没有重构。
- package.json 的上游元信息与模板文档用途未变，不据此判断本站产品状态。

## 最近完成

- 2026-10-14 13:18：接入自托管 Plausible 统计，脚本地址 https://analytics.clipcanva.com/js/script.js ，`data-domain` 自动取站点域名 clovertime.world；新增环境变量 `PUBLIC_PLAUSIBLE_SRC`（`wrangler.toml` 与 `.env.example` 同步），注入位置 `src/components/layout/BaseLayout.astro` ，无 cookie、不走同意门控。未部署，生效待下次 Cloudflare Pages 构建。

- 2026-10-13 07:44：9 个关键词主题的双语页面已发布到现有 clovertime.world；转正 12 篇新稿并纠正 Discord 入口，保存部署回执、产物哈希与恢复版本。游戏事实缺口和收录未知保留，未提交／推送。

- 2026-10-13 01:19：开发优先完成 3 个已有主题维护及 6 个新增主题的双语草稿，保持既有状态，新稿 draft／noindex。更新主词源码入口、事实边界与交付记录；手机、搜索交互和部分事实验收未完成，未提交或部署。

- 2026-10-13 00:44：关键词页面施工 Goal 0 验收，记录工作区基线、27 个词与 9 个主题归属、26 篇源稿及 8 项工程检查结果；业务内容尚未修改。Goal 1 保存搜索和平台原始证据，未验收。

- 2026-10-13 00:36：形成 [关键词页面 Goal 施工清单](/Users/yangzechuan/Documents/GitHub/clovertime/goals/20261013-0032-clover-keyword-pages.md) ，拆为 Goal 0–5 六个阶段，明确基线、补证、已有页维护、社区草稿、待补证页面及本地验收的范围、失败处理和交付要求；README 添加入口。只编制清单，运行中的 Goal、业务实施与发布均未启动。

- 2026-10-13 00:29：按老杨确认的“每页一个主关键词”方案，整理 [关键词与页面布局](/Users/yangzechuan/Documents/GitHub/clovertime/docs/clover-time/keyword-page-map-20261013.md) 与两份分配表；27 个相关词分配至 9 个主题，3 个已有页面、6 个新增规划，记录辅助词、内容边界、补证条件与执行顺序。仅文档，未创建或发布页面。

- 2026-10-13 00:15：清洗第一轮 71 个词，保留 20、排除 48、watch 3；用 ego-browser 完成 20 个词的第二轮 Trends，19 个返回查询、1 个相关查询数据不足。整理 480 条有效记录、110 个词面、26 个相关词和 19 个研究候选，实际新增相关词 6 个。见 [第二轮报告](/Users/yangzechuan/Documents/GitHub/clovertime/docs/clover-time/research-20261013-round2/report.md) 。止于第二轮，未改文章、发布或索引状态。

- 2026-10-12 23:54：用 ego-browser 查询 Wiki／Codes 竞品并分别采集 clover time、clover time wiki、clover codes 的全球过去 30 天 TOP／RISING；保存 112 条记录、71 个去重词面、原始证据与相关性判断，见 [研究报告](/Users/yangzechuan/Documents/GitHub/clovertime/docs/clover-time/research-20261012/report.md) 。未查绝对搜索量，未改文章或发布状态。

- 2026-10-12 15:22：按实际目录、代码与运行脚本重写 [AGENTS.md](/Users/yangzechuan/Documents/GitHub/clovertime/AGENTS.md) 、[README.md](/Users/yangzechuan/Documents/GitHub/clovertime/README.md) ，建立根目录 ROADMAP.md；CLAUDE.md 仅保留 `@AGENTS.md`，历史路线图加入口说明。仅修改文档，验证结果见下方。

## 最近验证

- 2026-10-14 13:18：Plausible 接入验证。正式构建通过，69 个 HTML 全部含 `<script defer src="https://analytics.clipcanva.com/js/script.js" data-domain="clovertime.world">`；脚本地址 curl 返回 200（content-type application/javascript）；`pnpm lint`、`astro check`（0 errors／0 warnings）通过。未做线上页面实测与部署。

- 2026-10-13 07:44：全工程门禁通过，400 测试、69 HTML、38 个搜索详情、sitemap 68/68；本地 36 次页面检查与交互通过。固定部署地址 173 项哈希匹配，主域全部返回 200，69 HTML 移除已定位 Cloudflare 注入脚本后匹配；线上手机菜单、FAQ、语言切换与搜索通过。见 release.md。

- 2026-10-13 01:19：配置、内容、正式／含草稿严格 i18n、lint、类型、24 套件／400 测试、正式构建、内链和 sitemap 全部通过。12 个草稿 HTTP 200 且 noindex、生产 404；6 个维护入口元信息与资源通过，sitemap 56/56 返回 200。具体失败、更正和日志覆盖说明见 acceptance.md。

- 2026-10-13 00:46：Goal 1 的 G1.1 完成。逐一核对 9 份 SERP 的查询词、时间、URL 与非空结果；同步来源台账 S31–S35 和事实表，保留官方公布／第三方说法／未知的边界。原执行 manifest 全部哈希匹配，`git diff --check` 通过。G1.2–G1.4 及后续内容阶段未验收；恢复浏览器确认待回复。

- 2026-10-13 00:44：当前工作区配置、内容、严格 i18n、lint、类型检查、24 套件／400 项测试、正式构建与 1991 条内链检查通过；日志见 keyword-pages/checks/，本地 UI、事实、sitemap HTTP 与线上部署未验收。

- 2026-10-13 00:36：施工清单六个阶段及未启动状态检查通过，文档本地链接存在，验证命令与 package.json 一致，`git diff --check` 通过。没有执行所列工程命令、事实补证、浏览器或部署验收。

- 2026-10-13 00:29：页面规划检查通过，27 个词覆盖完整且唯一归属，9 个 URL 不重复且各有一个主关键词，3 个现有源码入口及文档本地链接存在；两轮 Raw 的 manifest 哈希匹配，`git diff --check` 通过。未执行构建或线上验证。

- 2026-10-13 00:15：第二轮参数、单词比较集合、分页、连续名次、声明数量及数据不足文本核对通过；原始 481 行含 1 条完全相同的 Trello TOP 重复，清洗后 480 行（TOP 253／RISING 227）。原始重复、数据不足检测标志差异及菜单失败证据保留；第一轮词表 SHA-256 不变，`git diff --check` 通过。未查绝对搜索量，未执行工程验收。

- 2026-10-12 23:54：研究数据检查通过，6 个词根／模式分组数量分别为 25／25、8／6、25／23，共 112 条、71 个词面；逐行来源文件存在。Wiki 三个候选首页已打开，Codes 六个候选仅确认 SERP 链接；原生 CSV 仅 clover time 下载成功，其他两词根使用页面分页提取。未执行工程验收。

- 2026-10-12 15:22：执行 `pnpm exec vitest run tests/agents-consistency.test.ts`，1 个套件、2 项测试通过；文档本地链接、package.json 命令名称、CLAUDE 单行入口及 `git diff --check` 通过。738 个非本次文档文件的合并 SHA-256 与修改前一致，确认未改业务代码及其他已有文件。未执行全量工程验收。

- 2026-10-12 15:13：静态核对 package.json 命令、构建与预览脚本、路由／schema／配置及部署工作流；确认 26 篇非草稿源稿、预览固定篇数冲突、模板 E2E 的 fork 跳过条件与 refresh-audit 非门禁行为。未运行全量测试、构建、浏览器或外部发布检查。
