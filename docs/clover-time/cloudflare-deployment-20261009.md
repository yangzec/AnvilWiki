# Clover Time：Cloudflare Pages 部署记录

> 历史记录：本页保存 2026-10-09 的基础站部署。当前线上已在 2026-10-10 更新为可阅读研究预览；见 [当前正文、配图与部署交付](./content-preview-20261010.md)。下列旧详情 404／模板搜索等结果仅属于旧轮次，正式事实标准仍保留。

状态：2026-10-09 21:03（北京时间），Cloudflare Pages 预览部署及在线验收完成。用户已授权“你先部署到cf”，本次没有 Git 提交／推送或 DNS 变更。10 篇文章仍是草稿，正式内容验收 0/10。

- 主地址：[Clover Time Wiki](https://clover-time-wiki-preview.pages.dev/)。
- 中文入口：[中文首页](https://clover-time-wiki-preview.pages.dev/zh/)。
- 当前部署：[00762cd2](https://00762cd2.clover-time-wiki-preview.pages.dev/)。
- 项目：`clover-time-wiki-preview`；部署 ID：`00762cd2-e829-49e4-a998-dd7e0fb8c6a5`。
- Cloudflare API 确认 main 分支、production 环境、deploy 阶段 success。本项目用于预览，production 是 Pages 分支标签，不能据此宣称攻略正式发布。
- [完整部署及验收证据](./evidence/cloudflare-deployment-20261009.json)。

## 实际交付范围

独立项目直接上传首页、栏目、关于／联系／政策页，以及保留的模板手册。没有覆盖账户中其他项目，没有购买域名、修改 DNS、提交 Search Console 或启用变现。

10 篇游戏文章继续 `draft: true`；线上详情均 404，sitemap 不包含它们。栏目暂为空，搜索仍主要返回模板手册，不能用基础站部署代替 10 篇内容发布验收。

全站响应 `X-Robots-Tag: noindex, nofollow`；这是预览索引控制，页面仍公开可访问。正式开放索引须完成内容与模板清理验收。

## 部署与修复

`wrangler.toml`／site.domain／canonical／sitemap 已统一到实际 Pages 主地址。Giscus、六个 Adsterra 槽、GA、其他广告／统计和 IndexNow 关闭。本地 Astro 构建明确注入 TOML 的 [vars]；直接上传不会重新构建。

最终包：284 个文件、12,776,430 字节、123 个 HTML；282 个普通资产及独立上传的 _headers／_redirects。六个上游广告 HTML 排除上传，源码 public/ads/ 保留。最终本地包为 `.tmp/clover-time-deploy-20261009/upload-final/`，正式证据保存完整文件哈希。

用户更新凭据后，账户 Pages API 返回 200。Wrangler 4.149.0 首次创建默认转交 Workers，因缺 Worker 入口失败，没有部署。依据已安装官方 CLI 的 Pages 兼容选项，首次创建使用 `--force`，保持既有 Pages 架构；项目创建后，后续部署使用普通 `pages deploy`。

初次在线验收发现两项问题，修复并更新了部署：

- 联系页长 Roblox URL 在 375px 撑宽至 536px；链接增加 break-all，最终 375px 无溢出。
- 上游 _redirects 将真实 /zh/ Wiki 首页重定向到模板首页；移除冲突的两条规则，保留 /en 别名及手册旧路径。增强现有测试，检查重定向不能覆盖动态语言首页。

## 验证结果

准备阶段配置检查、37 个 SEO／URL 测试通过。修复后 9 个重定向测试、相关两文件 lint、Astro／Pagefind 构建、9,733 内链检查通过。最终修复没有重跑全套 397 个测试；全套结果属于 13:30 的独立验收。

通过普通 Chromium、既有云环境代理进行在线检查，TLS 验证保持开启。Python HTTP 客户端曾收到 Cloudflare 1010；浏览器正常访问，无 CAPTCHA／认证绕过或安全规则修改。

- 英文首页、三栏目、关于／联系／三政策页、robots、sitemap 与 Pagefind 资源实际 HTTP 200。
- 主域与当前部署 URL 首页均 HTTP 200；首页、联系页、/zh/ 和 /zh 的最终页面均 375px 无溢出。
- /zh 与 /zh/ 正确打开中文 Clover Time Wiki；canonical 指向本站对应路径。
- 最终首页／联系页／中文首页及 sitemap 原始响应哈希与上传包一致。
- 10 篇草稿详情及广告 HTML 实际 HTTP 404；sitemap 排除草稿。
- noindex、nosniff、SAMEORIGIN 响应头生效；未见广告／统计／评论请求，最终检查无网络失败。
- 手机菜单打开、栏目链接及 Pagefind 搜索／关闭实测通过；搜索内容限制见上文。

[英文手机首页](./evidence/cloudflare-20261009-home-mobile.png)、[中文手机首页](./evidence/cloudflare-20261009-home-zh-mobile.png)、[联系页](./evidence/cloudflare-20261009-contact-mobile.png) 为本次真实站点截图，不是游戏实机证据。

## 后续部署与恢复

Cloudflare 账号 ID 和 API Token 通过云环境设置注入，仅通过正常 API 使用，未写入源码或交付日志。无需再次索取当前已验证凭据；将来失败时检查具体接口权限，不额外要求无关 User Details／Memberships 权限。

先构建并验证新包，再更新本站既有项目：

```bash
source /workspace/.anvil-toolchain/activate.sh
cd /workspace/AnvilWiki
# [vars] 必须在本地 Astro 构建时明确注入。
# 验证新包后，使用其实际路径代替下列本次路径：
.tmp/clover-time-deploy-20261009/cli/node_modules/.bin/wrangler pages deploy \
  .tmp/clover-time-deploy-20261009/upload-final \
  --project-name clover-time-wiki-preview --branch main --commit-dirty=true
```

每次记录真实 deployment ID／URL／包指纹，并重新检查相关页面及草稿隔离。临时工具与包不能假定跨环境快照保留，缺失时按钉住版本安装到隔离工具目录并重建；不向业务依赖添加 CLI。

恢复采用本站已验证部署回滚；首次部署 19eb6c7e 与联系页修复部署 a0b053d0 保留作历史，当前版本为 00762cd2。工作区改动恢复前先比较用户后续内容，不覆盖其他站点或清空整个 .tmp。
