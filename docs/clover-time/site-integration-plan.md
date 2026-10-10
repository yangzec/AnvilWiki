# Clover Time 站点接入方案（已获授权并执行）

目标：先交付可运行的 Clover Time 开发站和 10 个草稿页面；事实核实与工程接入分别记账。没有足够证据的页面不进入生产构建，不宣称 10 页已验收。

## 已完成的预检

- 11 个现有 MDX 均与 Git HEAD 及已存备份逐字节一致，确认为未改动的模板示例。
- 备份位置：/workspace/shared/clover-time-baseline/ce64308f494df793f07c5b0b304737a65c61eba4/ 。
- 已准备并执行官方 apply-template 的 dry-run，不执行实际改写；不能直接采用完整命令，因为它还会改 wrangler.toml、生成 IndexNow key 等任务外配置。
- 已准备 7 个受限配置候选文件，放于忽略目录 .tmp/clover-time-research/config-candidate/；候选 JSON 能解析，demo 码泄漏检查通过，尚未应用或通过全站验收。首页细节和法律文案需在接入阶段完成。

## 计划替换的示例内容

用户已确认“都同意”。以下 11 篇示例已从内容集合移除或替换；全部原文保留于上述备份。

- src/content/wiki/en/bosses/emberfang.mdx
- src/content/wiki/en/bosses/frostbound-monarch.mdx
- src/content/wiki/en/bosses/stormcaller.mdx
- src/content/wiki/en/codes/all-codes.mdx
- src/content/wiki/en/guides/beginner-guide.mdx
- src/content/wiki/en/guides/forging-guide.mdx
- src/content/wiki/en/guides/weapon-tier-list.mdx
- src/content/wiki/en/items/emberforged-armor-set.mdx
- src/content/wiki/en/items/forging-materials-guide.mdx
- src/content/wiki/ja/bosses/emberfang.mdx
- src/content/wiki/ja/codes/all-codes.mdx

## 受限手工接入范围

- src/config/site.ts、navigation.ts、authors.ts：真实游戏身份、三个栏目、去除虚构作者和社交链接。
- src/locales/en.json、新建 zh.json、src/i18n/routing.ts：英文主站、中文 UI、缺失内容回退英文；首页不展示假码或不存在的公开详情。
- src/i18n/ui.ts：将静态导入的 ja 改为 zh，匹配配置。它是现有框架文件中的必要接入改动，不引入新架构。
- src/components/layout/LegalContent.astro：移除“每日更新有效码”“加入我们的 Discord”等不实默认文案，保留明确非官方声明。
- src/content/wiki/en/：接入现有 10 个 draft，原有模板文章按清单备份后清理；中文不新增文章。
- public/manifest.json 和直接相关的站点图标／封面：仅在确认 demo 身份需要消除时更新；素材不能冒充游戏截图。
- 必要的现有测试适配：把写死 en/ja 与示例有码的前提改为配置驱动，同时维持草稿隔离、码表与首页一致性等行为断言。不得跳过套件或删断言制造通过。
- Goal、roadmap、验收和交接文档同步实际进度；README 只报告实际运行状态。

不改依赖、锁文件、CI、wrangler.toml、域名／DNS，不提交、推送或部署。正式域名没有确定，不作上线验收。

## 已确认的两项决策

1. 先完成可运行的 10 页草稿开发站，并持续补证据；还是等 10 页事实全部核实后才改造站点？推荐前者，草稿不公开。
2. 是否按上述 11 个文件清单备份后替换模板文章，并允许列出的 UI、关于页和必要测试适配？推荐允许，保留可恢复原文。

原 Goal 的清理要求：“模板 demo 清理先列清单并建立可恢复备份，仅在删除对象获明确授权后执行。”因此先提交具体清单；确认后才清理。该要求来自本项目 Goal，不是网络代理要求。

工程结果：10 个草稿已接入，中英文 UI 已配置。必要适配还包括移除不再使用的 ja.json、隐藏模板介绍导航及去除模板介绍页的失效示例链接；原模板迁移测试输入保留为 tests/fixtures/anvil-template。没有修改锁文件、部署配置、提交或部署。
