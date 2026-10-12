# AnvilWiki 项目协作规范

## 项目定位

AnvilWiki 是 MIT 开源游戏 Wiki 模板，使用纯静态 Astro 和 Cloudflare Pages，让新手通过配置和内容替换建立自己的游戏站。主站不引入 React、Vue、Svelte 运行时或部署 adapter。

## 阅读入口与文档职责

进入项目先读本文件和 [ROADMAP.md](ROADMAP.md)。涉及功能、架构、安装或使用方式时，再读 [README.md](README.md)；改代码前读 [产品设计](docs/PRD.md) 的相关章节。

| 文件                  | 唯一职责                                       |
| --------------------- | ---------------------------------------------- |
| `AGENTS.md`           | 长期稳定的项目规则、工程边界、工作流和验证入口 |
| `README.md`           | 当前已实现能力、安装和使用说明                 |
| `ROADMAP.md`          | 当前进度、待办、阻塞、最近完成和最近验证       |
| `CHANGELOG.md`        | 长期版本变化和发版历史                         |
| `docs/PRD.md`         | 产品设计、数据模型、模块说明和架构决策         |
| `docs/development.md` | 扩展方式、验证流程和发版操作说明               |
| `docs/README.md`      | 专题文档索引和按任务组织的阅读路径             |

本文件不维护版本摘要、测试数量或审计历史。其他文档引用上述内容源，不复制规则或进度。`CLAUDE.md` 如需创建，只作为本文件的兼容入口。

全局沟通、授权、临时文件和进度维护要求遵循当前 Agent 已加载的全局规范；本文件只补充项目规则，不降低全局要求。

## 核心目录与职责

| 目录                                                     | 职责                                                  |
| -------------------------------------------------------- | ----------------------------------------------------- |
| `src/pages/`、`src/components/`、`src/lib/`、`src/i18n/` | 路由、原生组件、共享逻辑和多语言内容加载              |
| `src/config/`、`src/styles/`、`src/i18n/routing.ts`      | 站点身份、导航、主题和语言配置                        |
| `src/content/wiki/`、`src/locales/`                      | 游戏文章和多语言 UI、首页内容                         |
| `src/assets/`、`public/`                                 | 构建处理的图片与直接发布的静态资源                    |
| `scripts/`、`tests/`                                     | 内容与配置工具、质量检查和契约测试                    |
| `tools/anvil-ops/`                                       | 独立运维 CLI、MCP 包，使用自己的 workspace 和验证流程 |
| `docs/`、`.agent/skills/`、`requirements/`               | 专题说明、AI 内容工作流和产页素材模板                 |

代码、配置、内容三层分离：换游戏只改配置和内容，不改框架；框架代码不得含游戏专用字符串。新增能力先确定归属核心模板、可选插件、运维工具或文档 SOP。

## 工程边界

1. UI 文案走 `src/locales/<locale>.json`，组件不得硬编码文字；UI 图标使用 lucide，不使用 emoji。动态键用结构化类型，不使用 `as unknown as` 双跳断言。
2. 主题只配置 `--brand`、`--brand-light`、`--brand-h`、`--brand-s`，明暗模式各一组；`--brand-text` 自动派生，组件使用主题 token。
3. sitemap 根据真实文章和索引资格生成，不根据可能为空的配置列表造 URL；`og:image`、`twitter:image` 使用绝对 URL。
4. 分类必须在 `navigation.ts` 的 key、locale JSON 的 `nav.<key>` 和 `src/content/wiki/<locale>/<key>/` 目录一致；先有文章再进入导航，frontmatter category 必须等于目录。
5. 语言列表必须在 `routing.ts`、`src/locales/*.json` 和内容语言目录一致。默认语言无前缀，其他语言带前缀。
6. 详情页缺翻译时回退英文，回退页使用 `noindex, nofollow` 并退出 sitemap；列表页不回退。详情级 hreflang 只列真实可索引的翻译。
7. 广告、评论、统计等可选集成默认关闭，空 env 不渲染，不注入 demo 默认值；跟踪与广告遵守现有同意门控。接入细节见 [广告](docs/ads.md)、[评论](docs/comments.md) 和 [部署](docs/deployment.md)。
8. 域名通过带 `https://` 的 `SITE_URL` 配置。有 `wrangler.toml` 时，Cloudflare Pages 的构建 env 由其 `[vars]` 管理，不能假定 dashboard 覆盖有效。
9. 初始化与重跑必须保留用户配置和自有内容；改初始化通道时核对 CLI、setup workflow 和真实模式 E2E 的一致性，避免只在 demo 构建验证。
10. CI 内容生成只使用确定性任务，LLM 不进入 CI；自动写仓库经门禁后产出 PR 或 issue，不直接推 main。
11. 核心文件新增职责优先拆分，避免继续膨胀；新 frontmatter 字段应 optional 或带 default，以保旧内容兼容。具体扩展方法见 [开发指南](docs/development.md)。

## 工作流与执行纪律

- 内容创建：先读 [内容格式](docs/content-format.md)、`src/content.config.ts`、导航配置及同类型示例，再产页；正文从 H2 开始，内部页链接以 `/` 结尾，非默认语言链接带语言前缀。游戏事实、兑换码和数值必须有来源，未核实内容设为草稿。
- 配置与部署：按 [套模板](docs/apply-template.md) 和 [部署指南](docs/deployment.md) 执行；IndexNow 初始化和轮换也使用这两份说明。
- 工程变更：按 [开发指南](docs/development.md) 选择验证；同步受影响的真实内容源及其入口，扫描旧文案和引用，不为了同步制造无关改动。
- 运维包：先读 [tools/anvil-ops/README.md](tools/anvil-ops/README.md)，在该目录独立安装和验证；根项目检查不覆盖这个包。写入流程经验证后走分支和 PR，不直接推 main。
- 保持纯静态、Cloudflare Pages 默认、MIT 协议和虚构 demo 游戏 Anvil Quest；改变这些边界必须有用户明确授权。发布、提交、推送等操作遵守已加载的全局授权规则，修改任务不自动包含发布。

## 验证入口

质量检查与顺序见 [开发指南](docs/development.md) 第 1 节，CI 的实际门禁定义在 `.github/actions/gates/action.yml`。测试数量和完整脚本列表以运行结果及 `package.json` 为准。

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

修改初始化或 fork 清理路径还需 `pnpm test:e2e`；该命令使用已提交树，验证未提交改动的方法见开发指南，不可把旧树通过写成本次通过。内容产页至少运行 `pnpm check-content` 和 `pnpm build`。

## Astro Content Layer 易踩坑

- `getCollection()` 的 `entry.id` 带 `.mdx`，`getEntry()` 的查询 ID 不带；通过 `parseEntryId` 归一化。
- 使用 `render(entry)`，不是 `entry.render()`。
- `getStaticPaths()` 看不到文件顶层 const，其依赖数据须放入函数体或从模块导入。
- rest 参数从 `Astro.params.slug` 读取，不是 `Astro.props.slug`。
- 文章放在 `src/content/wiki/<locale>/`，避免 `src/content/<locale>/` 触发旧式自动 collection。
- 默认语言首页在 `/`，不可重定向到 `/en/`；其他语言路由使用 `[locale]`。
