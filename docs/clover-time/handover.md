# Clover Time 草稿站交接

源码维护：2026-10-10 11:53 已按用户授权同步到 yangzec/AnvilWiki 的 `clover-time` 专属分支，主提交 2e1d30e 与实际远程 SHA 一致。源码、配置、配图、调研和验收文档已提交；.tmp／凭据不纳入。网站部署与 Git 同步独立，源码草稿状态保持。[同步交付](./git-sync-20261010.md)。

当前交付：2026-10-10 11:10（北京时间），部署 a1074fde 已结合历史调研执行两个内置文章 Skill，修订 10 篇，补 39 个分节直答、50 条专属 FAQ 和 8 张图库示意图。49 个相关测试、两种构建及链接、本地／线上各 30 项和中文新标题搜索通过；全量另有 2 项既有模板配置检查失败，记录未隐藏。源码 draft、noindex 与正式事实 0/10 保留。[本轮交付](./skills-content-20261010.md)。下面各轮状态按历史时间阅读。

当前公开文案：2026-10-10 10:51（北京时间），部署 8622d67e 已将首页与 10 篇正文改为直接玩法介绍，移除公开研究标签、来源备注和缺口说明；旧全文与引用留内部。域名、配图、GA4 保留，41 项测试／类型／构建／链接及本地／线上各 32 项和中文搜索通过。源码 draft、noindex 与正式 0/10 保留。[当前交付](./player-copy-20261010.md)。以下为前轮历史状态。

当前统计：2026-10-10 10:28（北京时间），部署 cdb83016 已接入 GA4 G-XH7GWVG8ZK，访客同意后加载，Google 接受首页 page_view（204）。中英文拒绝后刷新不加载，线上 9 项与本轮 23 测试通过；域名 active，研究 noindex／正式 0/10 保留。[GA4 交付](./ga4-binding-20261010.md)。下方域名记录中的“GA4 未配置”属于 10:20 历史状态。

当前线上：2026-10-10 10:20（北京时间），主站 https://clovertime.world/、中文入口 https://clovertime.world/zh/；部署 ebc625e5，域名／DNS／HTTPS 均 active，实际访问检查通过。两条旧 A 已按授权换为 Pages CNAME，5 条 MX／TXT 保留。源码 draft、研究 noindex 和正式 0/10 保持；域名观察到 Cloudflare 边缘 beacon，GA4 未配置。[当前域名交付](./domain-binding-20261010.md)。下方为配图轮次记录。

状态：2026-10-10 07:45（北京时间），当前预览 e3d1cc23 已完成网站插画、四叶草标识与图标更新；最终 79 本地／80 线上检查通过。可阅读 10/10、正式 0/10，源码 draft／默认正式隔离／noindex 保留。[当前配图与图标交付](./visual-refresh-20261010.md)。没有 Git／DNS 操作。

## 文件入口

- 当前视觉素材与图标：[媒体及更新记录](./visual-refresh-20261010.md)。当前封面为 WebP，原 PNG 文字封面已不引用；恢复或生成前核对素材，勿用通用生成器覆盖自有图。
- 上一轮预览修复：[正文、配图与部署](./content-preview-20261010.md)，含 37 本轮测试、最终本地 26／线上 45 检查及独立导出方法。
- 2026-10-09 13:30 历史独立验收：[子代理总验收](./subagent-acceptance-20261009.md)，含四份子代理报告。工程重新通过九命令及 397 测试；P04/P08 通过核心公开资料层，但全页验收仍 0/10。P07 名称证据与 P08 代词归属已在 10 月 10 日修正；其余正式事实缺口仍按 Goal，不能追加实体交易／全觉醒硬门槛。
- 身份：src/config/site.ts；栏目：src/config/navigation.ts；作者注册：src/config/authors.ts。
- UI：src/locales/en.json、zh.json；语言与加载：src/i18n/routing.ts、ui.ts。
- 正文以 src/content/wiki/en/ 为当前编辑源。历史研究底稿保留于 docs/clover-time/drafts/，不要求双向同步。
- 来源、流程与版本限制：[sources.md](./sources.md)、[P05 研究](./beginner-flow-research.md)。
- 2026-10-09 新资料：[角色／魔导书／钓鱼研究](./character-magic-fishing-research.md)。9 篇同站原文支持补入 7 页；分类及来源冲突已记录，未独立实机核验。
- 2026-10-09 01:15 续查：[独立出版物／截图／Trello](./independent-source-research.md)。所有 10 页已补该轮资料，2 张兑换图与 Cut GIF 的 6 帧实际核对；公开看板有 331 卡片但未全量验证，官方归属待核对。原图／GIF 未复制进公开资产。
- 2026-10-09 自主检索：[本轮研究](./autonomous-research-20261009.md)。又读 6 篇原文，查看 3 张界面图及 Counter／Second Form 的各 6 帧，补 8 篇正文。祭坛 E／Read／x1、Human 2.5% 回蓝和 Hage Priest 类别有截图支持；保底数值区分 Plus 条件，交易与公告仍未核实。
- 2026-10-09 09:50 强度榜与实体页收口：[逐项收口与验收矩阵](./ranking-entity-review-20261009.md)。新增 S28–S30，四篇资料表／比较表／技能表已补；卡片、文章与实际观看帧分别归属，原验收条件保留。
- 实际命令、页面及搜索验证：[acceptance.md](./acceptance.md)、[工程证据](./evidence/README.md)。

## 10 个研究预览页面

| 路径 | 正文文件（src/content/wiki/en/ 下） |
|---|---|
| /codes/all-codes/ | codes/all-codes.mdx |
| /guides/how-to-redeem-codes/ | guides/how-to-redeem-codes.mdx |
| /guides/grimoire-tier-list/ | guides/grimoire-tier-list.mdx |
| /guides/race-tier-list/ | guides/race-tier-list.mdx |
| /guides/beginner-guide/ | guides/beginner-guide.mdx |
| /guides/how-to-reroll/ | guides/how-to-reroll.mdx |
| /items/anti-magic/ | items/anti-magic.mdx |
| /items/poison/ | items/poison.mdx |
| /guides/fishing-fragments/ | guides/fishing-fragments.mdx |
| /guides/patch-notes/ | guides/patch-notes.mdx |

上述详情已在研究预览上线，全部有显著说明和 noindex；中文导航下提供同一英文正文的阅读视图。源码仍只有英文 draft；默认正式构建排除详情，更新预览必须使用独立导出脚本，不能上传原项目 dist。

## 运行与检查

当前研究预览的复用构建、实际包与 26 本地／45 线上检查见当前交付；下列带日期结果为历史轮次，不能冒充本轮新跑。

2026-10-09 13:30 当前验收轮：九项命令全部重跑退出 0，24 套件、397 通过、0 失败／跳过；10 开发详情 HTTP 200，6 篇代表页电脑／手机共 12 次无溢出，生产 10 详情／sitemap 排除。生产搜索机制可用但仅见模板结果，当前不能发布。[实际验收证据](./evidence/subagent-acceptance-20261009.json)。

2026-10-09 09:50 上一轮：10/10 元数据与实际 MDX、内容检查、构建／Pagefind、9,733 内链通过；P03/P04/P07/P08 的 1440px／375px 显示通过，宽表可滚动，10 篇开发访问和生产隔离通过。[当前检查](./evidence/ranking-entity-checks-20261009.json)。10 条低内链警告保留，397 个单元测试仍是历史工程轮结果。

2026-10-09 08:04 上一轮：10/10 元数据及正文编译、内容检查、构建／Pagefind、9,733 内链通过。10 个开发详情及封面 HTTP 200；封面尺寸和哈希正确；P05/P06 在 375px 无溢出。详情／sitemap 继续排除草稿，正文有 10 条低内链警告，没有为凑数链接未发布页。[检查证据](./evidence/autonomous-content-checks-20261009.json)。

工作目录 /workspace/AnvilWiki，先 source /workspace/.anvil-toolchain/activate.sh，再执行 pnpm dev --host 0.0.0.0。Astro 7 的开发服务在本次环境内运行于 4321，可用 pnpm exec astro dev status 检查；连接恢复后的进程不能假设自动保留。端口只代表云工作区服务，不能称为已在用户电脑打开。

pnpm build 包含 Pagefind 后处理；pnpm check-links 检查最终产物。完整检查命令见 Goal。当前 build 为 122 路由页、Pagefind 为 90 页，包含上游模板及手册，不能当作游戏攻略数量。

## 媒体与模板保留

站点图标和分享图由 pnpm gen-assets 根据身份生成，属于文字品牌图。10 篇攻略当前各引用一张 1200×675 原创插画 WebP 封面，目录 src/assets/covers/，当前引用 clover-time-en-*.webp；尺寸、来源及当前哈希见 [媒体记录](./evidence/visual-refresh-media-20261010.json)。旧文字封面的历史记录与备份仍保留。正文现有 10 张原创说明图和 10 张概念插画，见当前交付。没有取得公开实机素材使用权，不以生成图冒充实机。保留的模板介绍和手册不属于游戏攻略，Wiki 导航入口已关闭，失效示例链接已清理；旧未引用的模板素材未扩大清理范围。

## 维护与转正

先补来源证据，再更新正文、lastModified 和正式互链。独立文章与录像分别标注；不得把同站多篇文章当作独立验证，也不把用户转述写成作者亲测。满足页面条件后才取消 draft，并运行受影响检查和生产隔离／搜索验证。

有效码仍未核实。码数据只放正式码页 frontmatter；不要用假 active 码填空。首页码高亮与正式码状态必须一致，draft 码不出现在首页。日期、奖励和状态分别核实；guides 排名的 90 天保鲜与 gameVersion 落后须人工检查。

## 备份和发布边界

独立验收发现的上游部署残留已在用户授权部署后清理：wrangler.toml 中评论、六个广告槽、统计及 IndexNow 关闭。直接上传构建已明确注入这些空值，上传包排除上游广告 HTML；Cloudflare 线上浏览器检查无相关请求，广告 HTML 404。

原文备份共 17 个文件，位于 /workspace/shared/clover-time-baseline/ce64308f494df793f07c5b0b304737a65c61eba4/，哈希已复核。恢复前先比较当前更改，不直接覆盖用户后续内容。

正式域名及真实 Wiki 联系渠道尚未确定；当前 Pages 域 clover-time-wiki-preview.pages.dev 已部署验证，SITE_URL／domain 一致，预览 noindex 保留。Discord 归属未确认，未填社交配置。依赖、锁文件、CI 未改；没有 Git 提交或推送。预览部署与正式内容发布分别验收，10 篇 draft 状态保留。首次创建用 Wrangler 的 Pages 兼容选项避免转交 Workers，后续直接 pages deploy；联系页溢出及 /zh/ 冲突重定向已修复。

用户已确认两项施工决策，普通后续施工无需重新授权。完整事实与发布验收仍见 [Goal](../../goals/20261008-0047-clover-time-wiki.md)。

23:49 资料续作：官方 API 的 BETA 0.1 标签已补入 P05/P10；该标签不代表第三方教程适用于同版本，也不能替代日期与改动记录。见 [复查证据](./evidence/source-check-20261008.md)。

2026-10-09 00:41 续作：S10–S18 返回正文，P03/P04/P05/P06/P07/P08/P09 已补具体归属资料，所有 draft 保留。编译、内容检查、构建、内链与 10 页开发检查通过；没有重跑旧单元测试，也没有新增已验证码、实际重抽或官方变更公告。后续优先独立操作画面和当前奖励证据。
