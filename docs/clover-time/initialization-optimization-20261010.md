# Clover Time 初始化优化交付

2026-10-10。按用户初始化清单优化当前游戏分支。当前为受保护的可读预览，正式事实验收不随工程检查自动通过。

## 本轮改动

- 清理 17 个模板路由文件与 24 个示例图片/广告/Google 验证文件；模板展示截图和维护者二维码也已清理。原始输入仅保留在 tests/fixtures，不发布到网站。
- 四叶草绿主题与 manifest 对齐，浅色文字/白字按钮派生色对比度为 4.62:1，保留当前 Hero、封面、正文插画、导航图标和 8 张图库示意图；修改 manifest 的旧研究措辞。
- requirements 中落盘 10 页事实表和 3 个对标站分析；原始证据仍使用 sources.md 单一台账。
- 官方 apply-template 已在隔离副本以当前身份、语言、栏目和绿色主题实际执行成功。它会额外生成脚手架并重写首页，因此不整包覆盖已完成的文章和专属素材；主站采用核对后的定向配置和清理。
- 标准 pnpm build 读取 wrangler vars，受保护预览输出到 dist；原稿 10 个 draft 不变，预览构建失败不会覆盖旧 dist。显式 build:production 保留普通 Astro 草稿过滤。
- 稳定公共 .indexnow-key 已初始化并随构建发布验证文件；当前预览不提交 IndexNow。
- 专属 deploy-clover-time.yml：clover-time push → Node22 / pnpm固定版本 / frozen install → 八项工程门禁 → 既有 Pages 项目上传；不部署 main，不使用未经验证的 dist。
- 修复两项原模板测试读取线上身份的错误前提，并保留 landing/redirect/广告迁移断言所需样本；没有删断言或将 Clover Time 域名加入 demo 白名单。测试素材不参与网站构建或应用类型检查。

## 验收清单

| 清单项目 | 当前结果 |
| --- | --- |
| Node / pnpm / fork / clone / install | Node22.23.3、pnpm11.1.1；自己的 fork 与 clover-time 分支；frozen install 通过 |
| dev 可用 | 上轮已实际启动并检查 200；本轮验证完整 dist 浏览器页面 |
| apply-template | 当前身份在隔离副本实际执行成功；主站定向落盘，保留专属素材 |
| 身份、语言、栏目、主题 | Clover Time / clovertime.world / 英文正文和中英文 UI / Codes Guides Items / 四叶草绿 |
| demo 文章与落地页 | 公开路由已清理，测试样本与内部上游手册保留 |
| Hero / favicon | 既有专属配图与四叶草图标保留 |
| template-audit | 13/14，唯一提示为 10 篇源稿的 draft，已无 demo 资产警告 |
| check-content / build | 成功；默认导出包含 10 篇英文及中文 UI 详情，51 HTML；正式导出排除草稿 |
| 事实来源 / 10 页计划 / FAQ | requirements 已填，既有 Goal 保留；每篇 5 条 FAQ，共50条；不凑无资料 Boss |
| 页面三关 | 工程与代表交互通过；正式事实验收尚未完成，draft 与 noindex 保留 |
| commit / push | 待本轮最终同步验证 |
| GitHub 自动部署 | 工作流就绪；当前 API 无权查看或管理 Actions，必须以仓库端实际运行补验收 |
| Pages build / dist / Node22 | 当前直接上传。工作流实际执行 pnpm build，上传 dist，Node 使用 .nvmrc=22；不是 Pages 原生 Git 构建 |
| SITE_URL / wrangler | https://clovertime.world；统一从 wrangler.toml 读取构建 vars，覆盖外部同名值 |
| 主域绑定 | 原绑定 active；本轮不更改 DNS / MX / TXT |
| pages.dev 301 | Bulk Redirects API 403；等待现有 Token 权限更新，不能用 _redirects 的域名匹配替代 |
| GSC | 未验证账号侧 property / sitemap 状态；既有 Google DNS TXT 不是提交成功证明 |
| IndexNow | key 与验证文件已就绪；预览模式禁止提交，正式放行后才能自动生效 |
| 首页 / sitemap / robots / 文章 200 | 待本轮线上部署后复核 |

## 账号侧操作

### Cloudflare 域名跳转

官方直接上传项目不能原地切换成 Git 集成。继续复用项目 clover-time-wiki-preview，使用仓库 Actions 构建后上传，不迁移域名。

当前 Token 调用 Account rules lists 返回 HTTP403。需要在现有 Token 增加 Account → Account Filter Lists → Edit 和 Account → Account Rulesets → Edit，并在云环境设置保存同一个 Token。也可自行设置 Bulk Redirect：源 https://clover-time-wiki-preview.pages.dev，目标 https://clovertime.world，301，开启子路径匹配、保留路径和 query string。不要设置覆盖所有 pages.dev 项目的全局匹配。分支别名若需要跳转，须逐个核对后添加。

验收：根路径、/items/poison/ 和带 query 参数都 301 到同一路径；主域返回200且不循环。官方说明：https://developers.cloudflare.com/pages/configuration/redirects/ 。当前 Wrangler 的来源 URL 解析也只接受相对路径。

### GitHub 自动上传

工作流文件：[deploy-clover-time.yml](../../.github/workflows/deploy-clover-time.yml)。仓库 https://github.com/yangzec/AnvilWiki 的 Settings → Secrets and variables → Actions 中增加 CLOUDFLARE_API_TOKEN 和 CLOUDFLARE_ACCOUNT_ID 两项 Secrets；Token 要覆盖现有账户的 Pages Edit。Actions 页面若提示 fork 工作流未启用，先启用。云环境凭据不会自动同步到 GitHub，本会话 Github API 管理 Actions 返回403。

启用后推送 clover-time，检查 Deploy Clover Time 的八项门禁与上传均成功；随后核对线上 /.well-known/anvilwiki-deploy.txt 与提交 SHA 一致。仅写入工作流不计作已经自动部署成功。

### Search Console 和正式发布

在拥有该域名的 Google 账号中添加 Domain property clovertime.world；保留既有 Google TXT 记录，使用 GSC 页面显示的实际验证要求，不猜验证值。提交 https://clovertime.world/sitemap-index.xml，并检查提交结果。

当前所有页面仍 noindex，sitemap 排除游戏详情；现在提交 sitemap 不意味着可以收录。先逐页完成原 Goal 的事实验收，再切换生产构建、移除全局收录保护，并验证 sitemap 包含真正发布的英文详情。中文正文仍是英文镜像，正式模式采用模板既有 fallback noindex，不当作独立译文收录。

## 维护与回滚

日常更新：激活工具链 → pnpm install --frozen-lockfile → 内容和工程检查 → pnpm build → pnpm check-links → 检查 dist → 上传。build:static 是隔离导出的内部步骤，不直接用来覆盖网站。预览模式不会修改源稿，也不会提交待验收页面到 IndexNow。

构建输出替换前保留上一份 dist 至本次 .tmp 构建目录，失败恢复旧产物。线上回滚使用 Pages 既有上一成功部署；不要恢复 DNS 邮件记录或将自定义域重新指向旧服务器。新增工作流在凭据齐备前不能依赖它更新线上内容。

本轮最终命令结果、页面截图、上线验证及 Git 身份写入 evidence/initialization-optimization-20261010.json；账户管理拒绝响应仅保存状态和错误，不保存任何凭据。
