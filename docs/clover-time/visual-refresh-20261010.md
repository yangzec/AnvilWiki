# Clover Time：网站配图与图标更新

后续地址更新：2026-10-10 10:20，当前域名为 https://clovertime.world/，部署 ebc625e5；域名与 HTTPS 已通过，配图沿用本轮资产。[域名交付](./domain-binding-20261010.md)。以下是 07:45 配图轮次记录。

状态：2026-10-10 07:45（北京时间），配图与图标更新已部署并通过真实线上检查。[主站](https://clover-time-wiki-preview.pages.dev/)、[中文入口](https://clover-time-wiki-preview.pages.dev/zh/)，当前部署 [e3d1cc23](https://e3d1cc23.clover-time-wiki-preview.pages.dev/)，完整 ID：`e3d1cc23-0bfd-436c-9697-16a32329d8be`。

## 本次交付

10 页原文字封面已换成 10 张各有主题的原创插画封面，均为 1200×675 WebP，保留标题在卡片正文中呈现。各页正文也接入对应 WebP 插画；已有 10 张说明图保留。实际为 7 张本轮新生成的插画加 3 张已有原创概念图，覆盖兑换码、兑换、魔导书、种族、新手、重抽、Anti Magic、Poison、钓鱼、公告资料。

首页新增 1200×675 大图，电脑图文并排、手机上下排列；原分享图也更新为 1200×630，匹配站点配置。首页图注和文章图注明确是原创概念插画，不是游戏截图、实机路线或确认的角色／物品外观。

品牌标识统一为原创四叶草：页眉、页脚与 favicon 共用 SVG；同时生成 16／32px PNG、180px Apple、192／512px Android 图标，以及含 16／32／48px 的 ICO。导航、移动菜单、快捷入口、栏目标题及文章卡片复用已有图标配置：Codes 使用 ticket，Guides 使用 compass，Items 使用 book-open。

图片经过标准网页尺寸导出和压缩，未更改原始生成 PNG。10 张正文 WebP 共 1,903,136 字节，每张约 122–241 KB；10 张封面合计同为约 1.9 MB，卡片由 Astro 继续生成响应式 WebP。完整原图保存在 /workspace/shared/clover-time-art-originals-20261010/，生成位置也保留不删除。[媒体路径、原图哈希、尺寸和图标映射](./evidence/visual-refresh-media-20261010.json)。

## 实现与边界

首页配图路径、alt 和图注放在中英文 locale JSON；品牌使用已有 favicon 路径，导航读取既有 item.icon。仅修改 HomePage、SiteHeader、SiteFooter 的通用显示，不在框架中写游戏专用字符串；没有新增路由、内容字段、依赖或 CI 变更。

10 篇源码仍 `draft: true`，默认构建排除。可阅读研究预览使用现有隔离导出脚本，保持 noindex 和明确研究说明；中文仍是标注的英文阅读视图。本轮没有新增游戏亲测或事实认证，正式内容验收保持 0/10。广告、统计、评论、IndexNow 状态保持关闭；没有 Git 提交／推送或 DNS 变更。

## 实际验收

- 相关三组件 lint、3 套件／37 个首页／i18n／SEO 测试通过；类型检查 202 文件、0 错误／警告／提示；中文 UI 141/141 键检查通过。没有重跑历史 397 全套测试。
- 最终默认构建：内容、Astro／Pagefind、9,733 内链检查通过，10 篇草稿继续排除。
- 最终研究预览：配置、内容、构建、10,771 内链检查通过；实际上传 385 文件、149 HTML、26,314,406 字节，包含既有手册，不作为 149 篇游戏攻略。
- 最终本地 79 项、线上 80 项全部通过：375／768／1440 三视口、两首页和 10 详情，图标、品牌图片、图片自然尺寸／实际加载、标题计算样式、无文档横向溢出；三次真实 Poison 搜索、两语言手机菜单、六栏目、深色模式显示、29 个媒体／图标资源、sitemap 和当前部署地址。
- 在线页面原始响应和 29 个资源哈希匹配实际上传包；全部目标 HTTP 200，noindex 生效，无失败请求或广告／统计／评论请求。源码哈希与隔离导出清单一致。

[桌面首页](./evidence/visual-refresh-20261010-home-1440.png)、[手机首页](./evidence/visual-refresh-20261010-home-375.png)、[中文完整手机页](./evidence/visual-refresh-20261010-home-zh-mobile.png)、[兑换码手机页](./evidence/visual-refresh-20261010-codes-mobile.png)、[Poison 桌面页](./evidence/visual-refresh-20261010-poison-desktop.png)、[深色手机首页](./evidence/visual-refresh-20261010-home-dark-mobile.png) 为本站实际线上截图，非游戏实机。[完整证据](./evidence/visual-refresh-20261010.json)、[实际命令日志](./evidence/visual-refresh-20261010-validation.log)。

## 上传故障及恢复

第一包为 46,243,332 字节，上传资源批次收到托管凭据服务 401；同一凭据读取项目 HTTP 200。将引用封面从 PNG 换成 WebP、重建为 26,314,406 字节并重做本地检查后，新普通 Wrangler 会话上传成功。没有更换凭据、关闭代理／TLS、绕过权限或要求额外账户权限。不能据此认定第一次认证服务错误的唯一根因；完整日志与重试结果分别记录。

## 后续维护

当前正式媒体是 src/assets/covers/ 下 clover-time-en-*.webp、public/images/articles/clover-time/*-concept.webp、public/images/clover-time-hero.webp、public/images/hero.webp 和 favicon／移动图标系列；不要将仍保留的旧文字 PNG 封面误作当前引用。

先更新素材和 MDX 引用，再按 [研究预览更新流程](./content-preview-20261010.md) 导出全新目录、检查图片／图标／搜索、上传该目录的 upload/。本次包为 `.tmp/clover-time-visual-refresh-20261010/review-3/upload/`，使用既有 Pages 项目与普通 pages deploy。默认 dist 不含研究详情，不能用它覆盖可阅读预览。通用 gen-assets／gen-covers 会生成模板式文字图，不用于维护这批原创插画及标识；有意重新生成时先保留现有素材和引用。

旧状态备份位于 `.tmp/clover-time-visual-refresh-20261010/before/`；回退先核对后续用户更改，不能覆盖其他项目或清空整个 .tmp。原生成 PNG 的保存位置、哈希和本次提示词都在媒体记录，不依赖临时处理脚本作为上线资产。
