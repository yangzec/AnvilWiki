# A4 页面与发布配置独立验收

验收时间：2026-10-09 13:20–13:25，北京时间。依据：Goal 第 8 节 A4，当前未提交工作区。独立访问当前页面；历史报告不作为本轮执行证明。

**结论：开发显示和生产草稿隔离通过；10 页正式站发布不通过。** 生产详情全部不可访问，搜索无法找到目标文章，正式域名仍指向模板域。部署配置还保留上游评论、广告和分析标识，不能将本地关闭状态直接当作未来部署状态。

## 实际检查结果

| 对象 | 结果 | 实际证据 |
| --- | --- | --- |
| 10 个英文开发详情 | 通过 | 逐个 HTTP 200，匹配文章 H1，并读取真实正文；正文提取含页面辅助区为 2,926–8,689 字符，每页 5–10 个 H2。 |
| 桌面及手机显示 | 通过，本次代表范围 | P01/P03/P04/P05/P07/P08 共 6 页，分别在 1440px 和 375px 截图；12 次 document.scrollWidth 均等于视口宽度。未声称其他页面完整视觉验收。 |
| 手机排名表 | 通过 | P03 第三张表 clientWidth=343、scrollWidth=417；table 自身 overflow-x=auto，实际 scrollLeft 从 0 改为 50，并另截两端 0/74。首列与末列可通过滚动查看，页面没有整体横向溢出。 |
| 桌面／手机导航 | 通过，栏目入口 | 生产 Codes／Guides／Items 实际点击到对应栏目，HTTP 200；375px 展开菜单并点击 Guides 成功。栏目均显示无公开攻略空态。 |
| 生产 10 详情 | 隔离通过；正式可达性不通过 | 全部 HTTP 404，目标 dist/index.html 均不存在，sitemap 无匹配。不能把排除草稿的成功记成已交付 10 个公开页面。 |
| 生产搜索 | 机制通过；目标内容验收不通过 | Pagefind 弹窗可加载、逐字输入并返回结果，Esc 可关闭。Poison 返回模板分类手册，Clover Time 返回 3 篇模板手册，redeem 返回 8 个模板结果；没有目标码表、攻略或实体详情。 |
| 开发搜索 | 未通过本轮检查 | 弹窗显示加载失败，搜索输入等待 12 秒超时。源码从 /pagefind/pagefind-ui.js 加载索引；生产可用，不能用开发失败推断生产搜索不可用。 |
| 中文回退 | 通过本次样例 | /zh/items/poison/ 开发详情显示英文文章，robots=noindex,nofollow，未伪造中文正文。生产仍排除该草稿。 |
| 首页／关于／政策 | 内容身份通过 | 生产英文首页、中文首页、关于、联系、隐私、条款、版权页均 HTTP 200，显示 Clover Time 身份；非官方说明清晰。 |
| 有效码复制／失败反馈 | 未验证 | src/content/wiki/en/codes/all-codes.mdx:11 为 codes: []，没有有效码按钮可用于该验收。码表为空不能记作复制交互通过。 |
| 正式域、canonical、hreflang | 发布不通过 | 本地生产首页 canonical=https://anvil.wiki/，en／zh／x-default alternate 同样使用 anvil.wiki；10 个检查生产页面均为该域的 canonical。 |

开发文章明细、显示尺寸、H1、HTTP 和 meta 原始记录：
[dev-results.json](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/dev-results.json) 。
实际点击、表格滚动及开发搜索记录：
[dev-interactions.json](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/dev-interactions.json) 。
生产 HTTP、导航、搜索、meta、隔离记录：
[production-results.json](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/production-results.json) 。
中文回退及第三方加载复核：
[supplement-results.json](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/supplement-results.json) 。

## 发布阻塞与配置差异

1. **P0：10 页目标没有生产详情。** 10 篇 MDX 第 8 行均为 draft: true。当前首页／栏目无公开攻略，两次点击内无法抵达 P01/P02/P03，目标文章也不在生产搜索中。应先通过各自事实验收再转正；本报告没有修改 draft。
2. **P1：正式域名未配置。** src/config/site.ts:68 为 anvil.wiki，:91 使用 SITE_URL 或该默认域；astro.config.ts:197、:280 使用 process.env.SITE_URL 或模板默认域。wrangler.toml:38 同样保留模板域。需正式域配置及新产物的 canonical、hreflang、sitemap 联合验收。
3. **P1：上游模板页面仍混入生产检索。** 实际 Poison 搜索返回 /landing/docs/categories-and-locales/，访问结果 HTTP 200、H1 为 Add Categories and Add Languages，内容是模板建站手册。src/pages/landing/docs/[slug].astro:20 仍生成这些路由，src/components/landing/HandbookChapter.astro:58 将手册加入 Pagefind 正文。机制能搜索不等于玩家可搜索到游戏资料；正式玩家站需处理模板页面公开与索引边界。此项不应靠放行未核实草稿解决。
4. **P1：部署配置残留须在发布前处理。** wrangler.toml:43–46 有上游 Giscus 四个必填值，:69–74 有 6 个非空 Adsterra 槽，:76 有上游 GA ID。Comments.astro:31–40 在 import.meta.env 四字段齐全时启用，:58 加载 Giscus；BaseLayout.astro:126、:247 根据 GA 值生成同意后加载器；AdsterraSlot.astro:55–61 根据槽位值决定渲染及同意门控。**若这些值进入未来 Pages 构建环境且页面挂载相应组件，就会启用对应上游配置；GA／广告加载仍受现有同意逻辑及挂载条件约束。** 本轮未部署、未读 Cloudflare 线上环境，不将这个条件性判断写成线上已经加载。仓库 docs/deployment.md:74–79 说明保留 wrangler.toml 时由其配置环境，本轮只核对仓库规则和代码，未独立验证云端实际注入行为。

当前本地生产产物的结果不同：10 个检查页面均没有 Giscus script／iframe；另检查首页、关于页、模板搜索目标的 DOM，无广告 iframe、无 GA 加载器，实际浏览请求也无第三方请求。当前本地构建未见这些功能启用。Astro 配置和页面组件没有直接解析 wrangler.toml；本地环境状态不能保证 Pages 下次构建状态。

联系页和版权页诚实显示“公共联系渠道尚不可用”，site.ts:73 地址为空，不能记作纠错／版权联系渠道可用。About／Contact 还显示 Last updated: 2026-08-11（src/pages/about.astro:7、contact.astro:7），这是残留页面日期，建议在正式交付时同步，未将它误认为实际本轮审校日期。

## 截图与复核入口

- [375px 生产首页](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/production-home-375.png) ：无公开攻略空态与非官方页脚。
- [375px 生产菜单](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/production-mobile-nav.png) ：展开后的导航和语言入口。
- [Poison 生产搜索](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/production-search-poison.png) ：模板手册结果，未出现实体详情。
- [搜索目标页面](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/production-template-search-target.png) ：实际 HTTP 200 的模板手册。
- [手机表格左端](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/dev-grimoire-table-375-0.png) 与 [手机表格右端](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/dev-grimoire-table-375-74.png) ：实际可滚动范围。
- [全部 26 张截图路径、大小和 SHA256](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A4/screenshot-manifest.json) 。桌面、种族、实体及新手截图包含在内；开发截图可出现 Astro 工具条，生产截图没有该工具条。

## 执行边界和复现

使用已存在的 Python Playwright 和 /usr/bin/chromium；开发检查访问 127.0.0.1:4321。收到 A3 构建完成通知后，使用本人创建的 Python 静态服务在空闲 4322 端口只读 dist，未构建或安装依赖。当地静态服务的 404 状态结合 dist 和 sitemap 判定隔离，不声称已验收 Cloudflare 的自定义 404、重定向或线上网络。

执行脚本 check-dev.py、check-interactions.py、check-production.py、check-supplement.py 最终均退出 0；保存在同一 A4 临时目录。首次后台服务退出导致连接失败，首次手机菜单定位同时命中语言开关和菜单；已改为保留本人的前台服务 session 和限定菜单选择器，重跑真实检查成功，均不是产品缺陷。开发搜索的加载失败按实际结果保留，没有改代码使检查“通过”。

本次只写本报告及 A4 临时证据，未修改正文、配置、测试、依赖、图片、部署文件，未操作游戏、外部账号或发布。完整工程测试由 A3 独立报告承担，事实验收由 A1/A2 报告承担；本报告不代替它们。
