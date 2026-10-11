# Goal：Sims-Life.com 首批上线施工清单

> 用途：给 goal 模式执行的施工单。§1 是可直接粘进 goal 的目标描述，§2–§8 是执行时逐项对照的细则。
> 需求依据：落地方案「★ 当前有效需求」与架构说明（项目存储 `docs/lagos-life-wiki-plan.md`、`docs/sims-life-architecture.md`）。两者与本清单冲突时，以本清单为准，并回头修正那两份文档。
> 日期：2026-10-11。

---

## 1. Goal 目标（粘进 goal 模式）

```text
在分支 cursor/sims-life-site-dc82（从 AnvilWiki main 切出）上，把 AnvilWiki 模板改造成 Sims-Life.com：
一个非官方的 Lagos Life 入口与速查站（英文、栏目 games + guides、品牌色 #F5B800、SITE_URL=https://sims-life.com），
上线首批 6 页（总览入口、下载 iPhone/Android、登录注册、是不是真钱、仿冒 App 警示、新手入门），
每个事实都有可点击的出处，代码层零改动，八道门禁 + template-audit 全绿，
并产出 README、出处清单、交付报告三份文档。不部署、不合并进 AnvilWiki main、不开 PR。
严格按 goals/sims-life-build.md 的边界、验收标准和自测执行。
```

---

## 2. 固定输入

| 项 | 值 |
|---|---|
| 站名 / 短名 | `Sims-Life.com` / `Sims-Life` |
| 域名 / `SITE_URL` | `sims-life.com` / `https://sims-life.com`（域名已在 Cloudflare） |
| 语言 | 只有 `en` |
| 栏目 | `games`（`lucide:gamepad-2`）、`guides`（`lucide:book-open`） |
| 品牌色 | `#F5B800` |
| 游戏 | `Lagos Life`；platform `Browser`；genre `Life simulation`；developer 以官方站标注为准，查不到写公开报道口径并在出处清单标"待官方确认" |
| 官方站 | `https://lagoslife.app`（`social.official` 与 `sameAs` 唯一值） |
| 作者 | `Sims-Life.com Editors` |
| 联系邮箱 | `contactEmail` 留空（Email Routing 开通后再填 `hello@sims-life.com`） |
| 社群 | 全部留空 |
| tagline | `Unofficial guides to life-sim games: official links, how to play, safety and FAQs` |
| description | `Unofficial guides to Lagos Life and other life-sim games: official links, how to play on phone, login help, fake-app warnings and FAQs, with sources on every page.` |
| legalNotice | `Sims-Life.com is an unofficial fan guide. Not affiliated with or endorsed by the Lagos Life team, Electronic Arts, or The Sims™. Lagos Life is the property of its respective owners; The Sims is a trademark of Electronic Arts Inc.` |

---

## 3. 边界

**必须做：**

- 只在分支 `cursor/sims-life-site-dc82` 上工作，一个逻辑改动一个 commit，阶段完成就 push 该分支。
- 只改配置层和内容层（见 §5 文件清单）。
- 所有事实先查证再写，出处写进页面正文和 `docs/sources.md`。

**禁止做（任一触发即停下汇报）：**

- 改代码层：`src/pages/`、`src/components/`、`src/layouts/`、`src/lib/`、`scripts/`、`tests/`、`.github/`（含 `LegalContent.astro`）。
- 合并进 AnvilWiki `main`、向 AnvilWiki 开 PR、force push、改历史。
- 部署到 Cloudflare、改 Cloudflare / DNS / GitHub 设置、公开发帖或评论。
- 写入任何密钥或 token；动 `.env`。
- 编造数据：薪资、房租、兑换码、玩家数、开发者名等任何查不到出处的数字或事实。
- 写 The Sims 内容、用 The Sims 视觉元素、把站点叫成 "Lagos Life Wiki" 或任何以 Lagos Life 为主体的品牌。
- 断言某个第三方 App / 网站是诈骗（只能写"官方渠道未列出"）。
- 开 `jobs` / `housing` / `locations` / `systems` / `news` 栏目，加广告、评论、统计、导流卡。

**停下来问老杨的情况：**

- 官方站 `lagoslife.app` 打不开或内容与已知信息矛盾。
- 某一页凑不出两个以上可靠出处。
- 门禁失败且修复需要改代码层。
- `yangzec/sims-life` 仓库权限开通（届时把分支推为该仓库 `main`，需确认）。

---

## 4. 里程碑、验收标准与自测

### M1 初始化模板

任务：

1. 从最新 `main` 切 `cursor/sims-life-site-dc82`。
2. 用 `pnpm apply-template --answers <json>` 非交互初始化（答案顺序参考 `scripts/e2e-apply-template.mjs`）：游戏名 `Lagos Life`、§2 的身份值、品牌色、`en`、`games,guides`、清除 demo 内容、移除落地页。
3. apply-template 会把站名写成 `Lagos Life Wiki`：在 `src/config/site.ts`、`public/manifest.json`、`src/locales/en.json`（页脚版权、首页标题等）手工改为 `Sims-Life.com`。
4. `src/config/authors.ts` 只留 `Sims-Life.com Editors`；`src/config/affiliates.ts` 保持空；`wrangler.toml` `[vars]` 除 `SITE_URL` 外全空。
5. `pnpm gen-assets` 重生成 favicon / hero。

验收标准：

- `site.ts` 各字段等于 §2；`routing.ts` 只有 `en`；`navigation.ts` 只有 `games`、`guides`。
- 仓库里不存在 demo 文章、`ja.json`、落地页文件，`.indexnow-key` 已生成。

自测：

```bash
pnpm template-audit                         # 无 demo 残留
pnpm check-config                           # 0 项错误
rg -n "Anvil Quest|anvil\.wiki|Lagos Life Wiki" src public wrangler.toml   # 0 命中
```

### M2 首页与 UI 文案

任务：按 §2 改 `src/locales/en.json` 的首页 hero、quick links、explore、FAQ、closingCta、`nav.*`、`overview.*`、页脚。

验收标准：

- hero 标题 `Life-sim games, explained fast`，徽章 `Unofficial fan guide`；FAQ 第一条回答"不是官方站"。
- closingCta 的 Play 按钮指向 `https://lagoslife.app`。
- 所有文案不出现 "verified by players"、"checked in-game"、"updated daily" 一类做不到的承诺。

自测：

```bash
pnpm check-i18n --strict-ui
rg -ni "verified by players|checked in-game|updated daily|the sims" src/locales   # 只允许 legalNotice/FAQ 里的免责声明命中
```

### M3 首批 6 页内容

| 文件 | 目标关键词 | 要点 |
|---|---|---|
| `src/content/wiki/en/games/lagos-life.mdx` | lagos life game / website / link | 是什么、官方入口、平台、Abuja / PH 扩展、相关页链接 |
| `src/content/wiki/en/guides/lagos-life-download-iphone-android.mdx` | how to download / for iphone / app store / android | 浏览器游戏无需下载、Safari / Chrome 打开、添加到主屏幕步骤 |
| `src/content/wiki/en/guides/lagos-life-login-sign-up.mdx` | login / sign in / sign up | 只走官方站登录、注册步骤、找回密码（以官方说明为准） |
| `src/content/wiki/en/guides/is-lagos-life-real-money.mdx` | is lagos life real money / legit | 虚拟货币、能否提现（引官方条款或权威报道），frontmatter `faq` |
| `src/content/wiki/en/guides/lagos-life-fake-apps-scam-warning.mdx` | lagos life app / app store | 官方渠道清单；非官方 App / 域名列表标"官方未列出" |
| `src/content/wiki/en/guides/how-to-play-lagos-life-beginner.mdx` | how to play | 开局与基础循环；视频嵌入 + 重写；交叉确认前 `draft: true` |

验收标准（每页）：

- frontmatter：`title` ≤ 80 字符，`description` 40–165 字符，`summary` 40–60 词，`category` 等于目录名，`date` 与 `lastModified` 为当天，`image` 指向 1200×675 封面。
- 正文：无 H1，首个标题是问句 H2；站内链接以 `/` 结尾且 ≥3 条；每个事实句后有出处链接，或在文末 "Sources" 段列出。
- 只用模板现有组件；引用视频走 `<Video>` 并在 frontmatter `videos` 登记。
- 找不到两个以上可靠出处的页：`draft: true`，并写进交付报告。

自测：

```bash
pnpm gen-covers
pnpm check-content            # 0 error；内链不足的 warning 也要清零
pnpm build                    # schema 校验通过
```

### M4 全量门禁

验收标准：下面每条退出码 0。

```bash
pnpm lint
pnpm typecheck
pnpm test
pnpm check-config
pnpm check-content
pnpm check-i18n --strict-ui
pnpm build
pnpm check-links
pnpm template-audit
```

产物抽查（自测）：

```bash
rg -l "https://sims-life.com" dist/index.html                       # canonical / og 用正式域名
rg -c "<loc>" dist/sitemap-0.xml                                    # 只含已发布页 + 栏目页 + 首页 + 法律页
rg -n "adsterra|adsbygoogle|giscus|googletagmanager" dist -g "*.html"   # 0 命中
rg -n "Anvil Quest|Lagos Life Wiki" dist -g "*.html"                 # 0 命中
```

另用 `pnpm dev` 打开首页和 6 页，在 375px 宽度下确认无横向滚动、标题和按钮完整。

### M5 交付文档

见 §6。验收标准：三份文档齐全，内容与实际产物一致（页数、draft 页、未确认事项）。

### M6 收尾

- 所有 commit 已 push 到 `cursor/sims-life-site-dc82`。
- 交付报告路径和分支地址发给老杨。
- **不部署、不合并、不开 PR**，等老杨确认后再做部署（见 §7）。

---

## 5. 允许改动的文件

| 层 | 文件 |
|---|---|
| 配置 | `src/config/site.ts`、`src/config/navigation.ts`、`src/config/authors.ts`、`src/config/affiliates.ts`、`src/config/project.ts`（仅 apply-template 自动改动）、`src/i18n/routing.ts`、`src/styles/globals.css`、`wrangler.toml`、`public/**`、`.indexnow-key` |
| 内容 | `src/content/wiki/en/**`、`src/locales/en.json`、`src/assets/covers/**`、`public/images/articles/**` |
| 文档 | `README.md`、`docs/sources.md`、`docs/launch-report.md`、`goals/**` |
| 由 apply-template 自动删除 | demo 文章、`src/locales/ja.json`、`src/content/wiki/ja/`、落地页相关文件 |

其他文件出现在 `git diff --stat main` 里即为越界，要回退或停下汇报。

自测：

```bash
git diff --stat main -- src/pages src/components src/layouts src/lib scripts tests .github   # 必须为空
```

---

## 6. 完成后的交付文档

| 文档 | 位置 | 内容 |
|---|---|---|
| README | `README.md`（替换模板 README） | 站点是什么、本地运行（`pnpm install` / `pnpm dev` / `pnpm build`）、目录说明、如何加新页、如何同步 AnvilWiki 上游、部署步骤、免责声明 |
| 出处清单 | `docs/sources.md` | 按页列出每条事实与出处 URL、访问日期、出处类型（官方 / 报道 / 视频）、是否交叉确认；"待官方确认"事项单列 |
| 交付报告 | `docs/launch-report.md` | 完成了什么（页面清单 + URL 路径 + draft 状态）、九条门禁结果、产物抽查结果、越界自查结果、未确认事项、已知风险、下一步（部署、Email Routing、GSC、第二批页面与 Accra Life 评估） |

交付报告同时在项目存储 `docs/` 下放一份副本，供老杨查看。

---

## 7. 后续（不在本 goal 内，需老杨确认后另开）

1. `yangzec/sims-life` 权限开通后，把分支推为该仓库 `main`。
2. Cloudflare Pages 连接仓库，构建 `pnpm build`、输出 `dist/`，先绑 `sims-life.com` 再部署。
3. 开 Email Routing，回填 `contactEmail`。
4. GSC 验证并提交 sitemap；确认 IndexNow 自动推送。
5. 第 2–4 周：看 GSC 数据补页，评估 Accra Life。

---

## 8. 完成定义（全部满足才算 goal 完成）

- [ ] M1–M6 每条验收标准满足，自测命令全部通过并把输出摘要写进交付报告。
- [ ] 代码层零改动（§5 自测为空）。
- [ ] 6 页全部有出处；未达标的页为 `draft: true` 且在报告中说明。
- [ ] 三份交付文档齐全且与产物一致。
- [ ] 分支已 push；未部署、未合并、未开 PR。
