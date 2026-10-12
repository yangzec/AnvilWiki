# 开发指导(给 AnvilWiki 本身写代码)

> 面向模板贡献者和维护者。fork 用户改配置/写内容请看 [apply-template.md](apply-template.md) 和 [content-format.md](content-format.md)。
> 硬约束(Agent 自动加载)在仓库根 [AGENTS.md](../AGENTS.md),本文解释**为什么**以及**怎么扩展**。

## 0. 开始前

先读根目录 [AGENTS.md](../AGENTS.md) 和 [ROADMAP.md](../ROADMAP.md)，再按任务读取 README 和 PRD 相关章节。目录职责、三层分离和工程边界由 AGENTS.md 统一维护；本指南仅说明操作方法。

## 1. 验证清单(每次改动后,提交前)

```bash
pnpm lint
pnpm typecheck
pnpm test
pnpm check-config
pnpm build
pnpm check-content
pnpm check-links
pnpm check-i18n --strict-ui
```

以上对应 `.github/actions/gates/action.yml` 的质量门禁，`check-links` 必须在 build 后运行。文档调整也需要检查相对链接、引用入口和受影响的文档契约。

初始化与 fork 清理变更还需真实模式 E2E：`pnpm test:e2e` 使用 `git archive HEAD`，只覆盖已提交内容。未提交改动不能据此宣称已验证；需要在项目 `.tmp/<task-slug>/` 创建隔离副本、把待验证文件带入副本后再验证，不为了运行测试擅自提交。

改了 `.astro` 路由文件 → 必跑 build(getStaticPaths 的错误只在构建时暴露)。
改了 workflow YAML → `python3 -c "import yaml; yaml.safe_load(open('<file>'))"`(v1.6 曾因 YAML 缩进断裂翻车)。

## 2. 常见扩展模式

### 2.1 加一个 frontmatter 字段

1. `src/content.config.ts` 加 Zod 字段(**必须 optional 或带 default**——旧文章永远要能构建,这是版本策略承诺)
2. 消费端:
   - 页面渲染 → `ArticlePage.astro`
   - 单独组件 → 新建 `src/components/article/XxxCard.astro`,在 ArticlePage 里 `return null` 门控
   - 结构化数据 → `src/lib/seo.ts` 加 builder(纯函数 + 测试)
3. UI 文案 → `src/locales/en.json` + `ja.json` 同步加 key(**禁止组件里硬编码文字**;Zod 默认值里的英文 fallback 除外)
4. 文档:`docs/content-format.md` 字段表加一行
5. 若 AI 要能产这类内容:`.agent/skills/anvil-new-article` 的 Step 2 硬规则同步更新

### 2.2 加一个 MDX 组件

- 放 `src/components/mdx/`,零 JS 优先(原生 `<details>`/`<dialog>`),颜色只走 `var(--brand)` token
- 语义色 warn/danger 用 amber/red Tailwind(先例:过期横幅、Callout)
- demo 文章里至少用一个(否则没人知道它存在)
- `docs/content-format.md` 组件清单同步；只有工程边界变化才更新 AGENTS.md

### 2.3 加一个页面类型(如 /tags、/recent)

- 英文无前缀:`src/pages/<name>.astro`;其他语言:`src/pages/[locale]/<name>.astro`
- **必须**双语两份(路由结构见 AGENTS.md 的 Astro Content Layer 易踩坑)
- hreflang:`languageAlternates((loc) => pathFor(loc), locales)`
- **不回退英文的列表页**(tags):hreflang 和语言切换器只列该内容真实存在的语言(先例:TagListPage 的 `availableLocales` 三层透传)
- URL 帮助函数一律放 `src/lib/url.ts`(纯函数可测,别在组件里拼)

### 2.4 加一个脚本(scripts/)

- 只用 node 内置依赖 + tsx,不引第三方(先例:全部运维脚本)
- 只读审计类(check-*)→ exit 1 可 gate CI;改写类(apply-template)→ 交互确认 + `--dry-run`
- 在 package.json scripts 注册；仅影响工作流或质量门禁时更新 AGENTS.md 验证入口与本指南，不复制完整脚本清单

### 2.5 加一个 CI 步骤 / workflow

- 只读审计 → 可直接进 ci.yml;**会写仓库的** → 单独 workflow + `permissions` 最小化 + 产出走 PR 或 issue,**永不直推 main**(先例:setup.yml 开 PR、content-pipeline.yml 开 issue)

## 3. 设计依据入口

规则由 AGENTS.md 维护；具体理由见 PRD 的相关模块章节与 ADR，以及 `docs/superpowers/specs/` 的特性设计记录。当前需要重评的决策和触发条件在 ROADMAP 中维护，避免在操作指南复制一份状态表。

## 4. 发版流程（SemVer）

仅在用户明确授权提交、推送和发版后执行对应操作，完成代码修改不等于获得发布授权。

1. 完成本节相关质量门禁；涉及初始化时完成真实模式 E2E。
2. 更新 package.json 版本、`src/config/landing-shared.ts` 的 PROJECT_VERSION 和 landing-en/zh 的发版横幅。
3. 在 CHANGELOG 将已验证的 Unreleased 内容整理为版本与日期；保留新的 Unreleased 段落，补版本链接并更新 `[Unreleased]` compare 指针。
4. 更新根目录 ROADMAP 的当前版本、完成与验证摘要；AGENTS 不追加发版摘要，PRD 不追加版本流水表。
5. 只有能力或操作方式变化时更新 README、专题文档和相关技能；规则变化写 AGENTS，设计变化写 PRD，其他入口通过链接引用。
6. 若随批发布运维包，独立更新该包版本和文档，完成包内验证。
7. 在已授权范围内提交、推送和创建 Release；检查实际 CI 与部署结果后，再在 ROADMAP 记录对应验证，不提前写全绿。

Minor 用于向后兼容的新功能，Patch 用于修复，Major 涉及 breaking 时必须在 CHANGELOG 写迁移说明。配置兼容承诺见 [staying-up-to-date.md](staying-up-to-date.md)。

## 5. 测试策略

- **优先测试纯函数**:`lib/url`、`lib/seo`、`lib/content-utils`(parseEntryId/isPossiblyOutdated 已从 i18n/content 下沉,tests/ 现状以 `pnpm test` 输出为准;依赖 astro:content 的加载器不进 vitest,新纯逻辑请下沉到 lib)
- 不测 .astro 组件(构建 + check-* 已覆盖)
- 为新增逻辑、修复失败路径和跨通道契约选择必要测试，不为低风险文案改动添加实现镜像测试；修 bug 时先稳定复现再修复。

## 6. 复杂度治理

工程约束见 AGENTS.md，剩余拆分计划见 [ROADMAP.md](../ROADMAP.md#待办与触发条件)。扩展核心文件前先检查职责是否独立；拆分按小批进行，通过本指南的质量门禁与必要 E2E 后记录完成。

## 7. 踩坑入口

Astro Content Layer 的项目规则见 [AGENTS.md](../AGENTS.md#astro-content-layer-易踩坑)。workflow 的 shell 续行必须保持 YAML 块缩进；主题 token 以 `tailwind.config.mjs` 的实际配置为准。
