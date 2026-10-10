# A3 独立工程验收

验收时间：2026-10-09 13:23（北京时间）。对象：`/workspace/AnvilWiki` 当前未提交工作区；标准：Goal 第 5 节九条命令和第 8 节 A3 委派。

**结论：本轮九条工程命令全部退出 0，397 个测试全部通过，草稿生产隔离有效；当前仍不能作为 10 页 Wiki 正式发布。** 10 篇均 `draft: true`，生产没有这 10 个详情页；工程通过不验收攻略事实。

## 范围与工作区保护

- HEAD：`ce64308f494df793f07c5b0b304737a65c61eba4`；运行前 Git 状态有 63 条，已有修改及未跟踪文件，本轮未提交。
- 读取全局 `/workspace/shared/global-agent-config/AGENTS.md`、项目 `AGENTS.md`、Goal、README 和 roadmap；实际执行检查，未沿用历史测试结果。
- 工具链实际版本：Node v22.23.3、pnpm 11.1.1；`git diff --check` 本轮退出 0。
- 使用现有 `/workspace/.anvil-toolchain/activate.sh`；独立读取确认它只导出 PATH、缓存及遥测环境变量，没有安装命令。本轮未调用安装／升级命令；各命令日志保留 pnpm 的 `Already up to date` 输出。
- 运行前后对 src、public、scripts、tests 和现有主要依赖／构建配置共 297 个文件做 SHA-256 对比：没有业务文件变化，包括 package.json、pnpm-lock.yaml 和 wrangler.toml。
- A3 独占本次 build，仅构建一次，完成后立即通知主 Agent；未切换 draft，未改正文、源码、测试、依赖及配置；未运行 test:e2e，未提交、部署或执行外部写操作。
- 原始日志、命令时间和业务文件快照在 [.tmp 任务证据](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/) 。该目录是核验缓存，正式结论在本报告。

## 本轮九条命令

| 命令 | 退出码 | 北京时间区间 | 结果与证据 |
|---|---:|---|---|
| `pnpm check-config` | 0 | 13:20:08–13:20:13 | 配置一致；其中域名一致不表示正式域名正确。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/01-check-config.log) |
| `pnpm check-content` | 0 | 13:20:13–13:20:16 | 10 篇通过基础内容校验；保留 10 条低内链警告。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/02-check-content.log) |
| `pnpm check-i18n --strict-ui` | 0 | 13:20:16–13:20:18 | zh UI 141/141；文章 0/0 是无正式文章，不能视作 10 篇已翻译。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/03-check-i18n.log) |
| `pnpm lint` | 0 | 13:20:18–13:20:32 | 通过。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/04-lint.log) |
| `pnpm typecheck` | 0 | 13:20:32–13:21:13 | 202 个文件，0 errors、0 warnings、0 hints。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/05-typecheck.log) |
| `pnpm test` | 0 | 13:21:13–13:21:22 | 24 个套件，397 passed、0 failed、0 skipped；397/397 全量实际执行。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/06-test.log) |
| `pnpm build` | 0 | 13:21:22–13:21:40 | 122 个 Astro 页面；129 个 HTML；Pagefind 90 页、2 种语言、12,582 词；6/6 包转换到 ES2018。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/07-build.log) |
| `pnpm check-links` | 0 | 13:21:40–13:21:43 | 当前 dist 的 9,733 个内链／129 个 HTML 全部可解析。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/08-check-links.log) |
| `pnpm refresh-audit` | 0 | 13:21:43–13:21:47 | 报告 Nothing stale、扫描文件数 10；所有草稿被实际新鲜度规则跳过，不能证明 10 篇新鲜。 [日志](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/09-refresh-audit.log) |

构建与 Pagefind 后处理完成时间：13:21:40；九命令全部结束时间：13:21:47。构建日志中的中国时间由本报告统一转换，日志内 Astro/Vitest 自带时间为主机 UTC。

Pagefind 明确忽略没有 `<html>` 外壳的 `google8362d9398114b66b.html`（既有验证文件），并提示 zh 无词干匹配支持。IndexNow 没有配置 key，跳过 key 文件输出。本轮没有因此失败；这些提示不能当成游戏页面完成证明。

## 10 篇元数据与生产隔离

独立解析当前 YAML 并用 sharp 读取每一个真实图像。10 篇的 title、description、summary 均满足 Goal 长度；date、lastModified 和 category 与路径一致；10 个相对封面引用均存在且尺寸 1200×675。这里验收文件和尺寸，不判断图片是否游戏截图或素材许可。

| 页面 | summary 词／字符 | draft 行 | 实际封面 | 英文／中文详情产物 | sitemap |
|---|---:|---:|---|---|---|
| `/codes/all-codes/` | 46／302 | [all-codes.mdx](/workspace/AnvilWiki/src/content/wiki/en/codes/all-codes.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/beginner-guide/` | 49／337 | [beginner-guide.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/fishing-fragments/` | 51／324 | [fishing-fragments.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/grimoire-tier-list/` | 50／345 | [grimoire-tier-list.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/grimoire-tier-list.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/how-to-redeem-codes/` | 48／331 | [how-to-redeem-codes.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-redeem-codes.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/how-to-reroll/` | 51／326 | [how-to-reroll.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-reroll.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/patch-notes/` | 49／295 | [patch-notes.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/patch-notes.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/guides/race-tier-list/` | 47／323 | [race-tier-list.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/race-tier-list.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/items/anti-magic/` | 49／373 | [anti-magic.mdx](/workspace/AnvilWiki/src/content/wiki/en/items/anti-magic.mdx:8) | 1200×675 | 均排除 | 排除 |
| `/items/poison/` | 50／349 | [poison.mdx](/workspace/AnvilWiki/src/content/wiki/en/items/poison.mdx:8) | 1200×675 | 均排除 | 排除 |

生产产物实际统计：122 个 Astro 生成页面、129 个 HTML 文件；sitemap-0.xml 内 115 个页面 URL，sitemap-index.xml 另有 1 个子 sitemap URL。10 个英文详情及 10 个中文回退详情均没有 HTML 文件，也没有 sitemap 条目。90 个 Pagefind 索引页面属于当前其他页面，不是 10 篇 Clover Time 攻略。具体矩阵见 [产物检查 JSON](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/artifacts.json) 。

P01 的 `codes: []` 见 [all-codes.mdx:11](/workspace/AnvilWiki/src/content/wiki/en/codes/all-codes.mdx:11) 。它仅表示本站尚无验证记录，不能证明游戏当前没有有效码；没有有效码按钮可用于复制验收。

## 发现与发布判定

| 严重程度 | 发现及定位 | 影响／转正条件 |
|---|---|---|
| 发布阻塞 | 10 篇 frontmatter 第 8 行仍是 draft；当前生产详情均缺失。 | 满足各页事实标准后按授权逐页转正，并重新构建与验收。当前不能把 122 路由或 90 搜索页作为 10 页完成数量。 |
| 发布阻塞 | [site.ts:68](/workspace/AnvilWiki/src/config/site.ts:68) 和 [wrangler.toml:38](/workspace/AnvilWiki/wrangler.toml:38) 均使用 anvil.wiki。 | 仍是模板正式域名；配置一致检查没有验证域名属于本项目。正式域名、canonical 和部署验收待完成。 |
| 发布验收未满足 | check-content 每篇正文实际 0 内链，10 条警告；Goal 要求真实相关内链及 P03 与实体页双向链接。 | 相关页面通过后增加实际可达链接；不能用草稿死链抹去警告。 |
| 验证限制 | [refresh-audit.ts:60](/workspace/AnvilWiki/scripts/refresh-audit.ts:60) 跳过 draft；脚本只报告且不自动判断版本，guides 强度榜也不属于 90 天自动规则。 | P0=0 不代表 10 篇事实、码时效或游戏版本已通过；仍需人工事实验收。 |

本报告不独立判定兑换码有效性、首轮获取、重抽、钓鱼或技能事实；这些由 A1/A2 对照实际来源审查。开发／生产 HTTP、导航、搜索和手机交互由 A4 检查，本报告只核对工程与产物，不能据此声称浏览器操作全部通过。没有发现本轮命令失败，不做未经授权的修复。

## 证据入口

- [逐命令退出码与时间](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/commands.json) 。
- [10 篇当前元数据与实际图像尺寸](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/articles.json) 。
- [产物、sitemap 和业务文件保护矩阵](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/artifacts.json) 。
- [运行前 HEAD、Git 状态和文件哈希](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/baseline.json) 。
- [日志 SHA-256](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A3/log-sha256.json) 。
