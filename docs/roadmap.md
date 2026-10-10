> 中文版当前状态：10 篇真实中文源稿及五个中文站务页面已部署 6b47e5dc（源 b5ac36b）；本地／线上各 46 项与 400 项测试通过，专属分支已同步。工程门禁通过，自动上传凭据条件仍未满足。详见 [中文交付](clover-time/chinese-localization-20261010.md)。初始化旧记录保留为历史。

> 初始化最终交付：已部署 a306ff44（源提交40f4fd1），GitHub八项门禁通过，上传受仓库Secrets缺失阻塞；本地/线上各35项页面交互检查通过，主域15端点符合预期，备用域301两项仍失败。账号侧与正式事实验收继续待办。

> Clover Time 初始化优化（2026-10-10）：当前默认 `pnpm build` 读取仓库配置并输出受保护的 10 页预览至 `dist/`，不会再因直接使用标准命令丢失文章；`pnpm build:production` 仍按原稿草稿状态过滤。旧日期记录保留为历史。模板落地页和示例资产已移除，事实表已整理至 requirements，当前验收见 [交付记录](clover-time/initialization-optimization-20261010.md)。

# 路线图:走过什么方向,接下来去哪(Roadmap)

> 本页回答两个问题:**这套模板过去按什么方向演化**(帮你判断它的成熟度和侧重),以及**接下来会往哪走**(帮你决定现在入场合不合适)。逐版本的完整变更见 [CHANGELOG](../CHANGELOG.md);正在做什么见 [PRD](./PRD.md) 第 14 章。

> **当前版本:v2.37.0**(2026-10-03 发布)。发版历史与最新版本见 [Releases](https://github.com/PNGTRID/AnvilWiki/releases)。

## 当前项目施工计划

源码维护分支：`clover-time`（yangzec/AnvilWiki）。当前运行的构建源提交为 b5ac36b，网站部署为 6b47e5dc，中英文各 10 篇可阅读；源码及验收资料已正常推送，main 未改。新状态见 [中文交付](./clover-time/chinese-localization-20261010.md)，以下早期记录保留为历史。

- 2026-10-10 11:10：当前部署 a1074fde，10 篇按内置文章 Skill 和历史调研修订，39 个分节直答、50 FAQ、8 图库示意图；本地／线上各 30 项与中文搜索通过。49 相关测试通过，全量另有 2 个既有模板配置检查失败。源码 draft／noindex／正式 0/10 保留。[交付](./clover-time/skills-content-20261010.md)、[Goal](../goals/20261008-0047-clover-time-wiki.md)。

### 最近完成

- 2026-10-10 13:13：从干净源码 b5ac36b 构建并上传到既有 Pages 项目，6b47e5dc 中文版上线；同步专属分支，保留 draft／noindex，不修改 DNS、统计和仓库 Secrets。[交付](./clover-time/chinese-localization-20261010.md)。

- 2026-10-10 13:07：按加语言 SOP 完成 10 篇中文稿、50 个 FAQ、8 个图库说明及五个站务页面，预览构建逐语言使用真实源稿并修复语言切换；英文源稿哈希不变。[中文交付](./clover-time/chinese-localization-20261010.md)。

- 2026-10-10 11:53：按用户授权将 Clover Time 源码、配图、调研和验收资料提交并推送至游戏专属 clover-time 分支，主提交 2e1d30e；远程引用校验一致，main 保持原提交。[同步交付](./clover-time/git-sync-20261010.md)。

- 2026-10-10 11:10：执行 anvil-new-article／anvil-batch-articles，按搜索意图重写现有 10 篇并新增 FAQ／图库；保存 Skill 适用调整和来源准入记录，部署同一预览项目 a1074fde。[交付](./clover-time/skills-content-20261010.md)。

- 2026-10-10 10:51：重写 10 篇标题／摘要／正文和中英文首页／栏目／FAQ，移除公开资料审校措辞及旧说明图引用；导出不再插入研究横幅，内部全文与引用档案保留，更新同一 Pages 项目。[交付](./clover-time/player-copy-20261010.md)。

- 2026-10-10 10:28：配置公开 GA4 衡量 ID，复用既有同意控制重新构建部署；访客拒绝不加载、同意才加载，Cloudflare 原有边缘 beacon 保留。[交付](./clover-time/ga4-binding-20261010.md)。

- 2026-10-10 10:20：完成 Pages 自定义域名关联、两处网站地址配置及研究预览部署 ebc625e5；用户补齐 DNS 权限后，备份并将两条旧 A 替换为 Pages CNAME，5 条邮件／TXT 保留，域名和 HTTPS 激活通过。[交付](./clover-time/domain-binding-20261010.md)。

- 2026-10-10 07:45：10 组插画封面／正文 WebP、首页／分享图、四叶草 favicon／移动图标、导航／栏目／卡片图标更新。资源批次认证服务拒绝后，优化封面、重建和重测，新会话上传成功；未改凭据／代理／TLS。[交付](./clover-time/visual-refresh-20261010.md)。
- 2026-10-10 07:21：补全部正文配图／相关入口，修正 P07 低清 HUD 名称与 P08 归属，通用首页卡片补封面渲染；修复隔离导出漏带 Tailwind 配置，最终更新 a9d83b4a。保存可复用 start_skill，无 Git／DNS 操作。[交付](./clover-time/content-preview-20261010.md)。
- 2026-10-09 21:03：独立 Pages 预览创建、直接上传与在线验收完成，部署 00762cd2。联系页 URL 换行和 /zh/ 真实首页修复，保留草稿隔离与 noindex；没有 Git 提交／推送／DNS 操作。[交付记录](./clover-time/cloudflare-deployment-20261009.md)。
- 2026-10-09 14:04：Cloudflare 预览部署准备完成：关闭上游广告／统计／评论／IndexNow，配置候选 Pages 域与预览 noindex，生成排除六个广告文件的上传包；凭据需求与实际启动说明保存云环境草稿，未创建或上传远端项目。[交付记录](./clover-time/cloudflare-deployment-20261009.md)。
- 2026-10-09 13:30：A1–A4 独立验收交付，主 Agent 复核原图／正文／日志／生产截图；P04/P08 核心公开资料通过，撤回实体交易／全觉醒附加门槛及 C 行名称确证，发布阻塞分类保存。[四份报告与总验收](./clover-time/subagent-acceptance-20261009.md)。
- 2026-10-09 09:50：新增 S28–S30 并读 Tower 原卡，核对 Dual／Rush／Bag 各 6 帧与三张外观图；四篇补十书分类／排名对照／属性方向／HUD 及能力表，原验收标准保留。[逐项矩阵](./clover-time/ranking-entity-review-20261009.md)。
- 2026-10-09 08:04：自主检索 S22–S27，查看祭坛／AFK／重抽截图及 Counter／Second Form 采样，补 8 篇正文；区分 Plus 保底条件、指出 Human 正文与图片矛盾。10 篇原创文字封面接入，未改生成器、schema、依赖或部署。[本轮研究](./clover-time/autonomous-research-20261009.md)。
- 2026-10-09 01:17：S19/S20 原始出版物与 S21 公开看板可读；实际查看两张兑换图，核对 Cut GIF 的 6 个时间帧，补全部 10 页。更正“兑换入口必然互斥”的判断，记录回蓝数值／码／技能名差异和资料空缺。[研究与画面](./clover-time/independent-source-research.md)。
- 2026-10-09 00:41：读取 S10–S18，补 P03/P04/P05/P06/P07/P08/P09；Sovereign 属 Social Class，Chosen One／Mana Sensitive 属 Trait。记录概率、资源、配方及来源内部冲突，保留全部 draft。[研究记录](./clover-time/character-magic-fishing-research.md)。
- 2026-10-08 23:49：官方 API 确认 BETA 0.1，补入 P05/P10 并验证开发显示；新文章入口仍 403，整体事实验收受阻。
- 2026-10-08 23:47：接入 10 个 Clover Time 草稿，完成中英文 UI、真实身份、首页、法律说明和必要测试适配；生成站点品牌图，修复模板格式页失效入口。
- 2026-10-08 12:43：完成 P05 下一轮路线与操作检索，整理 10 项操作的证据验收表，同步阶段验收与交接；没有新增独立画面，P05 继续保持草稿。[记录](./clover-time/beginner-flow-research.md)。
- 2026-10-08 12:38：独立读取工具及首次魔导书两篇具体教程，补充 P05 的第三方研究流程；记录同源限制、钥匙分支和缺失的装备／技能步骤。[流程研究](./clover-time/beginner-flow-research.md)，仍保持草稿。

### 最近验证

- 2026-10-10 13:13：主域完整浏览器 46 项与 8 个端点通过，源码 SHA 标记匹配；最新 GitHub 工程门禁通过，自动上传仍受凭据条件阻塞。[线上证据](./clover-time/evidence/chinese-localization-20261010/online-browser.json)。

- 2026-10-10 13:07：严格含草稿覆盖 10/10、UI 166/166；400 项测试、类型／lint／构建和 1,593 内链通过。本地 46 项、缺译稿回退与生产草稿排除通过。[证据](./clover-time/evidence/chinese-localization-20261010/local-browser.json)。

- 2026-10-10 11:53：230 变更路径纳入主提交，疑似密钥扫描无命中、无超限文件，check-config／check-content 通过；远程 clover-time SHA 与本地一致。原始验证日志尾部空格保留，代码及文档 diff 检查通过。[同步证据](./clover-time/evidence/git-sync-20261010.json)。

- 2026-10-10 11:10：39 个 H2 首答及 10 摘要词数、50 FAQ 唯一性、3–5 内链与素材检查通过；49 相关测试、两种构建、9,733／10,933 链接，本地／线上各 30 浏览器检查和中文新标题搜索通过。全量 395 通过／2 既有模板配置检查失败，没有宣称全绿。[证据](./clover-time/evidence/skills-content-20261010.json)。

- 2026-10-10 10:51：4 套件／41 项、202 文件类型检查、144/144 UI、两种构建和 9,733／10,921 内链通过；22 页文案扫描、本地／线上各 32 项、中文 Poison 搜索新标题及目标 URL 通过，域名 active、草稿哈希保留。[证据](./clover-time/evidence/player-copy-20261010.json)。

- 2026-10-10 10:28：2 套件／23 项同意与 SEO 测试、配置／内容／构建／10,771 内链通过；148 HTML 同意控制和草稿哈希检查通过，真实线上 9 项通过，正确 ID 的 gtag HTTP 200、首页 page_view HTTP 204。[证据](./clover-time/evidence/ga4-binding-20261010.json)。

- 2026-10-10 10:20：绑定版本配置／内容／构建／10,771 内链、20 个详情元信息及源码哈希通过；Pages 4 页和新域名 5 页 HTTP 200，配图、375px、资源及 HTTP→HTTPS 共 9 项通过，域名三状态 active。初始统计关闭断言失败，核对为 Cloudflare 边缘 beacon，保留实测日志与观察。[证据](./clover-time/evidence/domain-binding-20261010.json)。

- 2026-10-10 07:45：37 本轮相关测试、类型 0 错误／警告、UI 141 键、默认／隔离内容构建及 9,733／10,771 内链通过；最终本地 79／线上 80 项通过，375／768／1440 两首页与 10 详情无溢出，图标／图片／菜单／搜索可用，29 资源及页面响应哈希匹配。原稿隔离与 noindex 保留，无集成请求。[证据](./clover-time/evidence/visual-refresh-20261010.json)。
- 2026-10-10 07:21：本轮 37 相关测试、类型 0 错误／警告、默认构建／9,733 内链及隔离构建／10,771 内链通过；最终本地 26／线上 45 项通过，10 详情、13 新图、中文阅读入口和 Poison 搜索可用，计算样式／375–1440px 无溢出、响应及媒体哈希匹配，无集成请求。默认草稿隔离／研究 noindex 保留。[证据](./clover-time/evidence/content-preview-20261010.json)。
- 2026-10-09 21:03：9 个重定向测试、相关 lint、最终构建／9,733 内链通过；在线英文／中文／联系页 200、375px 无溢出且原始响应匹配上传哈希。10 草稿详情和广告 HTML 404，sitemap 排除草稿，安全与 noindex 响应头生效；手机菜单／搜索可用，无第三方集成请求。[证据](./clover-time/evidence/cloudflare-deployment-20261009.json)。
- 2026-10-09 16:57：Cloudflare Token verify HTTP 200／active，Wrangler 识别目标账户；Pages projects HTTP 403／10000，CLI 列表退出 1。284 个上传文件哈希与原清单一致，未执行远端创建／上传。[证据](./clover-time/evidence/cloudflare-deployment-20261009.json)。
- 2026-10-09 14:04：配置、37 个 SEO／URL 测试、构建／Pagefind、普通产物及上传包各 9,733 链接通过；上传包 123 HTML、10 草稿排除，手机首页 200／375px 无溢出／无广告统计评论请求。Wrangler whoami 未认证；线上未验证。[部署准备证据](./clover-time/evidence/cloudflare-deployment-20261009.json)。
- 2026-10-09 13:30：九项工程命令重跑退出 0，24 套件／397 passed、0 failed／skipped；9,733 内链通过。10 开发详情 200、6 代表页×2 视口无溢出，生产 10 详情 404／无 sitemap 泄漏；392 业务文件指纹未变。[当前证据](./clover-time/evidence/subagent-acceptance-20261009.json)。
- 2026-10-09 09:50：10/10 元数据与实际 MDX、check-content／build／9,733 内链通过；四篇 1440px／375px 共 8 次显示检查通过，宽表可滚动；10 开发详情 HTTP 200，生产详情／sitemap 排除草稿。[当前证据](./clover-time/evidence/ranking-entity-checks-20261009.json)。
- 2026-10-09 08:04：10/10 元数据／实际 MDX 编译及封面引用通过；check-content／build／9,733 内链通过。10 个开发详情和封面 HTTP 200、封面均 1200×675；生产详情／sitemap 排除草稿。P05/P06 在 375px 无横向溢出。[当前结果](./clover-time/evidence/autonomous-content-checks-20261009.json)。
- 2026-10-09 01:17：当前 10/10 元数据／MDX 编译，check-content／build／9,733 内链通过；10 个开发详情新增内容可见，生产详情／sitemap 排除全部草稿；保留 10 条内链数量警告。[当前正文检查](./clover-time/evidence/independent-content-checks-20261009.json)。
- 2026-10-09 00:41：当前 10/10 元数据与 MDX 编译通过；check-content、build、check-links 退出 0，9,733 内链有效；10 个开发详情 HTTP 200，7 页新增内容可见，生产详情／sitemap 全部排除草稿。保留 10 条低内链警告。[检查记录](./clover-time/evidence/content-continuation-20261009.json)。
- 2026-10-08 23:47：397/397 测试（24 套件）、类型检查 0 错误／警告、构建／Pagefind、9,733 内链检查通过；10 个开发草稿 HTTP 200，生产路径和 sitemap 排除草稿；375px 无横向溢出。
- 2026-10-08 05:38：S06/S07 原始页面 HTTP 200；YouTube CONNECT 403，X HTTP 页面壳可读但浏览器失败，两个 Discord 公开邀请接口 403；没有新增实机通过结果。
- 2026-10-08 01:14：10/10 暂存草稿通过 YAML 解析、元数据长度及当前 Astro MDX 编译；17 个备份文件校验一致。网页内容资料读取不等于实机验证，0/10 页面完成公开验收。

## 演化主线:从「建站模板」到「内容经营操作系统」

AnvilWiki 的版本历史不是功能大杂烩,而是一条主线:**不断把「个人做游戏 wiki 赚钱」这件事里机器能干的部分,搬进模板**。每个阶段的方向:

| 阶段 | 版本 | 方向 | 代表能力 |
| --- | --- | --- | --- |
| 地基 | v0.1 – v1.0 | 架构定型:纯静态、三层分离、开箱即绿 | Astro 5 + Cloudflare Pages 零适配器、代码/配置/内容三层分离、i18n、主题变量、Lighthouse 4×100 |
| 官网与内容体验 | v1.1 – v1.3 | 站点门面与栏目形态 | 官网 landing(中英)、displayType 栏目形态(卡片/时间线/视频网格)、demo 站上线 |
| 互动与信任 | v1.4 – v1.7 | 留住访客、攒信任信号 | giscus 评论、标签聚合页、gameVersion 徽章、画廊+灯箱、作者体系(Person JSON-LD)、AffiliateLink、check 工具链起步 |
| SEO 与质量收口 | v1.8 – v1.10 | 把技术 SEO 和质量门禁焊死 | og:image 绝对路径、404/FAQ/hreflang、check-i18n / check-links / check-content、五视角审计 65 文件修复 |
| 知识体系 | v1.11 – v1.13 | 把「怎么用」变成产品的一部分 | 站内文档中心(双手册,中英)、AI 内容技能(`.agent/skills/`)、一键套模板 CLI `apply-template` |
| 运营闭环 | v1.14 – v1.16 | 流量数据回流到内容决策 | `anvilwiki-ops` CLI+MCP(GSC/CF 数据,提交走 PR)、社区展示墙、专家团复审修复 |
| 媒体与规模化 | v1.17 – v1.18 | 补齐媒体示范、把一个站变多个站 | demo 全类型媒体示范、`template-audit` 模板健康检查、`bulk-new-posts` 批量产页、学习手册第 9/10 章 |
| SEO 进阶 | v1.19 | 对齐 2026 搜索新格局 | 学习手册「SEO 进阶」课(排名 + AI 引用;现拆为课 28 + 课 29)、`docs/seo.md` 收录 2026 Google 官方更新记录、封面图升级为图片搜索入口、本路线图 |
| **内容经营操作系统(当前)** | **v2.0** | **机器接管「产出与运营」环节** | PR 门控内容管道(auto-content.yml:确定性生成 → 八道门禁前置 → draft PR)、anvilwiki-ops 1.0 多站管理 + AI 引用追踪、`pnpm gen-covers` 封面产能(1200×675 + max-image-preview)、AffiliateSuggestion 建议位 |

一个可以观察到的规律:**每个阶段都在为下一个阶段铺路**——比如三层分离(v1.0)让模板化(v1.18)成为可能,check 工具链(v1.7)让 AI 技能(v1.13)有了验收标准,作者体系(v1.7)在 AI Overviews 时代(2026)变成了引用偏好里的信任信号。

## 接下来的方向

### 近期(v2.0+,候选池)

按「用户目标函数」排序——玩家做站要的是 选品 → 产能 → 流量 → 变现,v2.0 补强了「产能」(管道/封面)与「运营」(多站/AI 引用)两侧,接下来补两头:

- **邮件订阅**(v2.0 遗留):RSS 已就绪,差订阅表单的模板级支持——涉及第三方服务选型(Buttondown 等)与 double opt-in 合规,做就做干净。
- **preferred sources 适配**:Google 2026-08-20 刚发布「偏好来源」自定义按钮,等实现方式稳定后评估模板层支持。
- **选品决策支持**:「哪个游戏值得建站」目前靠学习手册课 7「打分拍板」的人工四关卡,可沉淀为数据脚本(搜索趋势/竞争度抓取)。
- **管道生成器扩展(继续)**:codes 同步已接入 auto-content.yml(v2.17.0);Trello 导入等更多确定性任务走同一套门禁契约。
- **可视化编辑层**(社区 issue #21):优先评估现成 git-based CMS 的模板级可选接入(Sveltia/Decap/Keystatic 本地模式——编辑对象就是仓库 Markdown,与纯静态架构天然兼容;注意 OAuth 配置门槛与 content.config.ts 的 schema 双源漂移风险);**不自研本地常驻后台**(CLI+setup.yml 已是两通道同步坑,第三通道是持续税,且偏离 AI 原生定位)——需求热度 n≥3 再启动。✅ 评估已完成(2026-09-08):Sveltia 因不支持 MDX 排除、Decap 平庸不推荐;推荐形态=**Keystatic 独立 admin 站**(不碰主站零 adapter 架构),先决解锁项=Zod schema→CMS 配置生成器(双源变单源)。详见 docs/superpowers/specs/2026-09-08-git-based-cms-evaluation.md。
- **依赖漏洞分层清理**(外部扫描 issue #37 + 官方 audit 实测 27 条:1 critical/13 high/10 moderate/3 low,2026-09-14 基线)✅ **已收官(2026-09-14:v2.22.0 A 层 + v2.23.0 B/C 层,`pnpm audit` 27→0)**:
  - **A 层(pnpm overrides)** ✅ v2.22.0:sharp/fast-uri/js-yaml/fflate/svgo 范围限定双条,audit 27→15;
  - **B 层(Astro 5→6→7 两跳)** ✅ v2.23.0:astro 系 10 条全清(critical AVIF RCE 修于 7.2.8;静态站实际可利用性低——无运行时图片端点,构建只处理仓库自有图片,但不背 critical 评级);fork 常规 merge 零迁移,视觉零漂移钉死三处(compressHTML/cssMinify/postbuild 区间语法降级);
  - **C 层(独立小项)** ✅ v2.23.0:vitest ^4.1.11(mocker path traversal ×2)、esbuild 随 Vite 8 达标、extract-zip ×2 随 astro 7 依赖树重排整体消失;overrides 回收六条留一条(fflate,@iconify/tools 仍钉旧线)。
- **Astro 6/7 升级** ✅ 已完成(v2.23.0,2026-09-14):5→6→7 两跳、每跳独立提交+八门禁全绿;回归重点 check-content/check-links/apply-template E2E/产物规则级对比全绿;零 fork 迁移。
- **核心文件复杂度治理**([誓言](https://github.com/lyglzhl) 外部代码审查报告 2026-09-15,P2):少数核心文件体积与职责持续膨胀——landing.ts 58KB / apply-template.ts 41KB / apply-rewrites.ts 30KB / CommunityHighlights.astro 29KB / SearchButton.astro 23KB / ArticlePage.astro 23KB / BaseLayout.astro 14KB——单个功能点看都合理,但一个小需求可能同时波及 SEO/广告/i18n/导航/构建。方案:拆 ArticlePage(结构化数据/文章辅助区/商业化插槽/导航组件化)、拆 BaseLayout(Head/SEO 与 Tracking/Consent 与 Theme Init 分离)、拆 apply-template(问答采集/计划生成/文件变更执行分层,CLI 只留 orchestration)。改动面大、回归风险高,按项目惯例拆成独立小批做,每批全门禁+E2E 伴随。
- **类型逃生口收敛 + 复杂度预算**(同一报告 P2/P3):src/ 下 17 处 `as unknown as Record<string, any>`(集中在 `shared` UI 对象,`lib/shared-ui.ts` 已有类型化 helper 未全面换用)继续贯通 UI JSON 类型;同时建立「复杂度预算」习惯——新能力先判断属于核心模板/可选插件/运维工具/文档 SOP,不全进主运行时;生产构建以「零 warning」为常态目标(fallback 构建日志两类警告已随 v2.27.0 清零,astro-icon 空目录 + getEntry 降噪)。
- **ja 落地面验证**(关键词依据:SimilarWeb Keyword Generator,2026-08,Japan:「ゲーム wiki」2,390/月 +「ゲーム攻略」2,050/月):ja wiki UI 已内建(`pnpm new-locale` 脚手架 + i18n 契约门禁),缺的是落地验证——日文市场对静态攻略站的接受度与广告变现(ja eCPM、广告位表现)。**触发条件**:出现日文 showcase 站或 ja 社群信号(日文用户的真实反馈/需求);**约束**:landing.ts 复杂度预算已告警(见上方复杂度治理条),ja 落地会再增 landing 文案面,不提前启动,排在拆分批之后。
- **「wiki page templates」模板展示页**(承接长尾:SimilarWeb Keyword Generator,2026-08,global:「wiki template」约 1,000/月,score 19;「wiki template character」约 1,490/月):单页展示模板能产出的各页型(boss/codes/tier list/画廊等),每型挂 demo 真实链接,页内导流 GitHub fork。**排序约束**:排在 landing.ts 拆分批之后做——新页面类型会先加重 landing.ts,拆分前不加新面。 ✅ **已交付(v2.32.0,2026-09-17)**:排序约束已满足(拆分批 v2.31.1 先行);/landing/templates + /zh/landing/templates 双语上线,文案独立新文件 src/config/landing-templates.ts(landing-en/zh.ts 零触碰),六页型卡(Boss 攻略/兑换码/Tier List/新手攻略/装备物品/文档中心)全挂 demo 真实链接(先 ls src/content/wiki/en/ 逐条核实),LandingLayout 导航+页脚三处加 Templates 入口,data-pagefind-body 进全站搜索,fork 三通道同步(apply-template LANDING_PATHS+setup.yml rm+e2e 纯净性断言),en+zh 375px 横向零溢出程序断言绿。
- **showcase 收录标准补「站点 README 回链 anvil.wiki」**(依据:SimilarWeb 反向链接实测,anvil.wiki 全站仅 28 个引荐域且均为自动收录型目录——外链是当前最短板):showcase 站是真实内容站,收录时要求对方站点 README 回链,是最自然的获外通道。**触发**:下一次 showcase 投稿受理时随收录流程落地,存量站不追溯。 09-18 首例触发:Warhounds/Sandustry 两投稿站仓库均私有,「README 回链」无法公开验证(站点本身核验为真实 AnvilWiki 构建,已在 PR 留言建议开源),标准自下次受理起执行。
- **Cloudflare Pages → Workers 迁移评估**(背景:2026-09 Cloudflare 官方将 Pages 列为历史产品线、静态与 git 部署能力并入 Workers,社区热议迁移;本项目 2026-09-19 完成评估,**定案暂不迁**):一票否决=Workers 的 `wrangler.toml` `[vars]` 只进 runtime 不进**构建期**,正中 apply-template「env 单源在构建期读取」设计与 GA/广告/评论全套 env 门控契约(PRD ADR-003 维持 Pages 默认);次因=Workers 自定义域要求域名 NS 托管在 Cloudflare(外部 NS 不支持)。**重开触发**:Cloudflare 公布 Pages 实际停服时间表,或 Workers 支持构建期 vars——届时按 ADR 流程重评;在此之前 fork 用户零动作,现役 Pages 部署不受影响。

### 中期(v2.0 方向)——✅ 已随 v2.0.0 交付

从「建站模板」升级为「内容经营操作系统」,三件全部落地:

- **PR 门控 CI 内容管道** ✅:`auto-content.yml`——确定性生成器 → 八道质量门禁前置(全绿才开 PR)→ draft PR;LLM 永不进 CI(ADR-004)。
- **多站管理** ✅:`anvilwiki-ops` 1.0.0——站点注册表 + `--site`/`--all` + 统一巡检,并附赠 AI 引用追踪(CF AI referrals + GSC AIO 探测 + CSV 导入)(ADR-005)。
- **变现层深化** ◐:AffiliateSuggestion 文末建议位已交付;**邮件订阅留 v2.1**(涉及第三方选型与 opt-in 合规文案,不污染本版)。

### 不做清单(同样重要)

- 不做课程/培训——模板和文档本身就是产品(README/手册免费公开)。
- 不做社区运营——展示墙收录真实站点,但不经营论坛/群。
- 不引入 React/Vue 运行时——纯 Astro 静态是 Lighthouse 4×100 和零带宽成本的地基(PRD ADR-002)。
- 不做 SaaS 托管——Cloudflare Pages 免费额度 + 你自己的仓库,数据主权在你。

## 给 fork 用户的含义

- **方向稳定性**:主线一年未偏——「让个人低成本经营游戏 wiki」没有 pivot 过,你的 fork 不用担心模板方向突变。
- **升级节奏**:语义化版本 + 三层分离,merge 上游通常只动代码层(见 [staying-up-to-date.md](./staying-up-to-date.md))。
- **参与**:路线优先级欢迎开 issue 讨论;做出成绩的站点欢迎提 PR 上展示墙。
