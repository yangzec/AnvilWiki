# Clover Time：正文与配图预览交付

> 本页记录 07:21 的正文预览修复及通用导出流程。之后已更新插画和图标，当前部署与素材见 [视觉更新交付](./visual-refresh-20261010.md)；下列 374 文件、文字封面和 a9d83b4a 属于前一轮。

状态：2026-10-10 07:21（北京时间），更新同一 Cloudflare Pages 项目并完成线上检查。可阅读研究稿 **10/10**；正式内容验收 **0/10**。这两项分别记录。

- [主站](https://clover-time-wiki-preview.pages.dev/)、[中文界面](https://clover-time-wiki-preview.pages.dev/zh/)。
- [本次部署](https://a9d83b4a.clover-time-wiki-preview.pages.dev/)；部署 ID：`a9d83b4a-b99c-426e-a83a-f5f75ff29f93`。
- [验收证据与文件哈希](./evidence/content-preview-20261010.json)、[实际命令日志](./evidence/content-preview-20261010-validation.log)。

## 修复结果

此前上线的是基础站，默认构建排除了全部 draft，首页卡片也没有显示已有封面。用户指出“缺少配图、内容都缺”后，改为清楚标注研究状态的可阅读预览，保留原来的事实验收标准。

10 页现有来源研究正文已经上线，涵盖兑换码报告、兑换入口、魔导书榜、种族榜、新手流程、重抽、Anti Magic、Poison、钓鱼／碎片和更新资料。各页约 400–1,500 个英文词，均有 Research preview 说明、出处、未确认项和至少 3 条相关研究页入口。首页、栏目与实际 Pagefind 搜索可以找到文章。

修正 Anti Magic 低清 C 行名称被误称 HUD 确证的表述，并纠正 Poison 排名理由的来源归属。未新增本轮游戏亲测、有效兑换码或官方更新事实；原公开资料的读取日期仍按来源标注。

## 配图与语言

- 保留 10 张 1200×675 原创文字封面，补齐首页卡片的实际渲染。
- 新增 10 张 1200×675 原创说明图，每页一张，分别解释该页的系统或资料关系。
- 新增 3 张 1672×941 原创概念插画，用于新手、Anti Magic 和 Poison；生成原图完整复制，没有改尺寸或裁切。
- 图注明确说明示意／概念性质，**全部不是游戏实机截图**。没有公开复制第三方截图或冒充路线证据。[媒体记录](./evidence/content-preview-media-20261010.json)。

正文继续以英文为准。中文入口提供中文导航、栏目和明确标注的英文阅读视图；隔离导出复制同一英文正文，并说明“英文研究稿／不是中文翻译”。源码没有新增中文文章，不宣称完成中文翻译。

## 构建边界

10 篇源码仍全部 `draft: true`，默认 `pnpm build` 仍排除详情。本次部署使用 [独立研究预览构建脚本](../../scripts/build-research-preview.py)，在隔离副本内输出带 `noindex: true` 的阅读页面；这个渲染开关不表示事实验收通过。全站响应 `X-Robots-Tag: noindex, nofollow`，英文和中文研究详情均不进入 sitemap，广告／统计／评论／IndexNow 保持关闭。

唯一通用显示修复是 HomePage 复用既有 ArticleCover 显示已有 image；没有加入游戏专用框架文字、新路由、schema、业务依赖或 CI 变更。隔离构建使用明确输入清单，包括既有 Tailwind 配置。

第一次内容更新 fbb24f01 漏带 Tailwind 配置。实际截图发现布局没有正确样式，因此该版本未通过显示验收。补齐配置后重新构建、部署为 a9d83b4a；最终检查增加标题实际字号和网格布局，不能用旧版本的 HTTP 通过代替最终显示验收。

## 本轮实际检查

- 中文 UI 检查：check-i18n --strict-ui 退出 0，141/141 UI 键覆盖；源码中文文章仍为 0，不代表正文翻译完成。
- 原始构建：相关两组件 lint；3 套件／37 个首页、i18n、SEO 测试；类型检查 202 文件，0 错误／警告／提示；内容、构建、9,733 内链检查通过。未重跑历史 397 全套测试。
- 最终研究预览：配置、内容、Astro／Pagefind、10,771 内链／155 HTML 检查通过。最终上传包 374 文件、149 HTML、22,538,020 字节；包括既有手册，不当作 149 篇攻略。
- 本地最终样式验收 26 项通过：两视口（375／1440）、两首页和 10 详情；图片实际加载、计算样式、无文档溢出，真实 Poison 搜索命中目标实体。
- 最终线上 45 项通过：24 次页面检查、两次搜索、3 个中文入口／阅读视图、13 个新媒体、两 sitemap 和当前部署地址。全部页面／新媒体 HTTP 200；页面原始响应匹配上传哈希，媒体匹配原文件哈希，noindex 生效，无失败请求和广告／统计／评论请求。
- 源码 10 个 draft 及默认构建隔离再次核对；每个目标正文 3 条以上相关入口有效。

[桌面首页](./evidence/content-preview-20261010-home-desktop.png)、[中文手机首页](./evidence/content-preview-20261010-home-zh-mobile.png)、[新手手机页](./evidence/content-preview-20261010-beginner-mobile.png)、[Anti Magic 桌面页](./evidence/content-preview-20261010-anti-magic-desktop.png)、[手机搜索](./evidence/content-preview-20261010-search-mobile.png) 是本站真实截图，不是游戏画面。

## 可复用更新步骤

```bash
source /workspace/.anvil-toolchain/activate.sh
cd /workspace/AnvilWiki
# 必须选择不存在的新目录；依赖缺失时先按冻结锁文件安装。
python3 scripts/build-research-preview.py --output-dir .tmp/clover-time-content-preview-<date>/review-<new-id>
# 检查 manifest、源码哈希、图片／样式／搜索及 noindex 后上传该目录的 upload/：
.tmp/clover-time-deploy-20261009/cli/node_modules/.bin/wrangler pages deploy \
  .tmp/clover-time-content-preview-<date>/review-<new-id>/upload \
  --project-name clover-time-wiki-preview --branch main --commit-dirty=true
```

本次实际包为 `.tmp/clover-time-content-preview-20261010/review-5/upload/`。不要上传原项目 dist，否则预览会再次缺全部研究页。CLI 和临时包缺失时重建，不假设快照保留。后续使用既有 Pages 项目，普通 pages deploy，不重新创建。

Cloudflare 凭据只经环境注入使用。本轮没有 Git 提交／推送、DNS、Search Console 或变现操作。按 cloud-environment-onboarding:setup 保存了 start_skill，保留安装脚本及其他设置；保存草稿不执行脚本、不发布环境快照。未来新环境使用它前，用户需在环境设置检查、保存并发布；当前站点部署已实际完成。

## 正式发布仍缺什么

当前有效码与奖励、关键操作的完整实机结果、钓鱼／碎片关系和带日期的官方改动仍按原 Goal 记录缺口。研究预览保留原文归属、冲突和未确认步骤，不把空码表解释为“证实没有有效码”，不把 Beta 0.1 标签当作更新日志。P04/P08 已通过的核心公开资料层也不追加实体交易／全部觉醒硬门槛。完整正式验收保持 0/10。
