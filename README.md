# Clover Time Wiki

Clover Time 玩家 Wiki，基于 [AnvilWiki](https://github.com/PNGTRID/AnvilWiki)（MIT）。主站 https://clovertime.world，中文 UI 入口 /zh/，正文目前为英文。源码维护在 [yangzec/AnvilWiki 的 clover-time 分支](https://github.com/yangzec/AnvilWiki/tree/clover-time)。

## 开发与构建

需要 Node.js 22.13+、pnpm 11.1.1、Python 3.11+。本云环境先激活 `/workspace/.anvil-toolchain/activate.sh`。

```bash
pnpm install --frozen-lockfile
pnpm dev
pnpm build
pnpm check-content
pnpm check-links
```

`pnpm build` 读取 `wrangler.toml`，输出可直接上传的 `dist/`。当前 `ANVIL_BUILD_MODE="preview"`：隔离构建 10 篇可读文章及中文 UI 阅读入口，原稿 `draft: true` 不变，保留全站 noindex。`pnpm build:production` 使用普通 Astro 草稿过滤；它不代表内容验收通过，也不会自行移除配置中的收录保护。不要直接运行内部 `build:static` 覆盖当前网站。

## 内容与发布

- 事实表：[requirements/00事实来源.md](requirements/00事实来源.md)；竞品：[requirements/00对标参考.md](requirements/00对标参考.md)。
- 10 页施工 Goal：[首版规划](goals/20261008-0047-clover-time-wiki.md)。
- 初始化优化：[Goal](goals/20261010-clover-time-initialization.md) / [验收与发布说明](docs/clover-time/initialization-optimization-20261010.md)。
- 配图、图标和 GA4 保留；广告与评论关闭；公开正文不展示内部来源备注或缺口列表。
- 默认构建和线上部署一致，但 10 页正式事实验收尚未完成。未验证的兑换码不进入 active / expired。
- GitHub Actions 工作流 `.github/workflows/deploy-clover-time.yml` 会验证后上传到既有 Cloudflare Pages 项目。运行需要仓库端的 Cloudflare 凭据；云环境 Token 不会自动同步到 GitHub。
- IndexNow 使用已提交的公共 `.indexnow-key`，预览模式不提交收录请求。正式发布前按交付文档验收内容和 SEO。

上游使用手册保留在 `docs/`；模板示例仅用于测试，不作为网站页面发布。AnvilWiki 原始介绍与教程：https://anvil.wiki/zh/landing/docs/dev/。
