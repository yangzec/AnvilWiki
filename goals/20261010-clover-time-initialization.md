# Goal：Clover Time 初始化逐项优化

- 来源：用户初始化清单及“逐项进行优化”的指令。
- 目标：补齐可独立完成的初始化、构建、模板清理和部署工程项；受限账号项与事实验收分别记录。
- 边界：保持既有 10 页范围、专属分支和 Pages 项目；不编造码、数值、Boss 或补丁；不把预览当正式验收，不移除未验收内容的 noindex，不覆盖现有 DNS 邮件记录。

## 施工与验收

- [x] Node / pnpm 可用；frozen-lockfile 安装完成。
- [x] 清理公开模板落地页、示例图片、原模板 Google 验证文件和广告 HTML；原始测试输入保留在 fixtures。
- [x] 将身份、栏目、主题色和 manifest 对齐；保留当前原创图片与图标。
- [x] requirements 中提供逐页事实表、来源日期、验收缺口和竞品结构分析。
- [x] 默认 pnpm build 输出当前受保护的 10 页网站，源稿 draft 标志不变；失败构建不覆盖旧 dist。
- [x] 初始化稳定 IndexNow 公共 key；预览模式禁止自动提交。
- [x] 提供 clover-time 分支专属验证与 Pages 上传工作流。
- [x] 工程验收：测试、类型、lint、配置、内容、构建、内链和 UI 语言检查通过。
- [x] 浏览器验收：首页、10 详情、图片、表格、复制、图库与搜索正常；375/1440px 无溢出。
- [x] 部署到既有项目并检查页面、SEO 保护、key 文件与部署 SHA；源码同步 clover-time，main 不变。
- [ ] Bulk Redirects：pages.dev 根域、文章路径及 query string 301 到主域，主域不循环。
- [ ] GitHub Actions：仓库端凭据和权限具备后，以实际远端运行验证，不能用本地通过代替。
- [ ] 正式内容与 SEO：逐页补足原 Goal 要求后移除对应草稿；正式站 sitemap、IndexNow、GSC 提交均实测。

## 自测与交付

执行 pnpm install --frozen-lockfile、pnpm test、pnpm lint、pnpm typecheck、pnpm check-config、pnpm check-content、pnpm build、pnpm check-links、pnpm check-i18n --strict-ui、pnpm template-audit；核对普通生产导出仍排除草稿，默认导出完整且 noindex。模板健康度剩余草稿警告必须说明，不删草稿来追求满分。

交付文档：[初始化优化与账号侧操作](../docs/clover-time/initialization-optimization-20261010.md)，包含最终清单、命令结果、部署身份、回滚与剩余边界；原始证据存 docs/clover-time/evidence/。


## 当前交付状态（2026-10-10）

工程项已实现并部署 a306ff44，源提交40f4fd1，源码同步clover-time，main未改。GitHub八项门禁已通过，上传仅因两项仓库Secrets缺失而停止；Actions已经启用。Bulk Redirects权限和GSC账号状态待用户补齐。模板健康度13/14唯一草稿提示保留，正式事实验收仍0/10；本Goal的账号/收录项继续待办，不宣称全部初始化完成。
