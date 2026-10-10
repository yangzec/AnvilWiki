# Clover Time：自定义域名绑定

后续统计更新：2026-10-10 10:28，当前部署 cdb83016 已接入 GA4 G-XH7GWVG8ZK，同意控制和 page_view 上报通过。[GA4 交付](./ga4-binding-20261010.md)。以下保留 10:20 域名轮次记录。

状态：2026-10-10 10:20（北京时间），绑定及验收完成。主站 https://clovertime.world/，中文入口 https://clovertime.world/zh/。Cloudflare 的域名、DNS 验证及 HTTPS 验证状态均为 active；实际浏览器正常访问。

## 本次更改

用户授权绑定至现有 clover-time-wiki-preview Pages 项目。添加自定义域名关联，将 wrangler.toml 的 SITE_URL 与 src/config/site.ts 的 domain 更新到 clovertime.world；通过隔离研究导出脚本构建并上传，部署 ebc625e5-7a34-4bff-b03e-44ad47369c85，部署地址 https://ebc625e5.clover-time-wiki-preview.pages.dev/。原 Pages 地址仍可访问，没有新增项目或绑定 www。

开始时现有 DNS 权限返回 403；用户更新同一个 Token 后读取成功。实际根域存在 A 记录 54.149.79.189、34.216.117.25，已完整保存原记录。删除其中一条冲突 A，将另一条改为代理 CNAME：clovertime.world → clover-time-wiki-preview.pages.dev、TTL 自动。五条 Zoho MX／TXT 和 Google 验证记录逐字段核对一致，未修改其他子域或注册商。调用官方 Pages 域名重试验证接口后，最终 status、verification_data.status、validation_data.status 均 active。

## 验证结果

- 配置、内容、Astro／Pagefind 构建和 10,771 内链检查退出 0，上传包 385 文件；20 个中英文详情的 canonical、研究标签、noindex 及源码哈希检查通过。
- 原 Pages 入口的两个首页和两个代表详情均 HTTP 200，canonical 使用新域名。
- 新域名两个首页、Codes、新手、Poison 共五页 HTTP 200；375px 无横向溢出，可见图片加载成功，canonical 和 noindex 正确。favicon、首页图片、sitemap HTTP 200；HTTP 访问自动转到 HTTPS。九项域名／页面／资源检查通过；没有关闭 TLS 证书验证。[手机首页截图](./evidence/domain-home-mobile-20261010.png)。
- 初始浏览器验收里“所有统计关闭”的附加断言失败：新域名实际加载 Cloudflare beacon。进一步核对发现上传 HTML 没有统计脚本，源码两个统计变量仍为空，脚本出现在 Cloudflare 返回的域名页面。记录为 Cloudflare 边缘注入观察，未擅自关闭域名原有设置，也未声称已核实后台统计入库；GA4 未配置。不能继续将线上统计一概描述为关闭。

10 篇源码仍 draft:true，全部可阅读预览保留研究标签和 noindex，正式事实验收仍 0/10。配图沿用已验收版本，没有 Git 提交／推送，没有开启广告、评论或 IndexNow。绑定到正式域名不代表已允许搜索引擎收录。

## 后续维护和恢复

保留 CNAME 指向现有 Pages 项目，不要将根域重新指向旧服务器。更新内容时沿用独立研究预览构建，不直接上传排除草稿的默认 dist。网站地址的源码配置与构建时 SITE_URL 均已更新。

完整 DNS 修改前后记录、响应和检查见 [验收证据](./evidence/domain-binding-20261010.json)，真实构建、部署与验收退出状态见 [命令日志](./evidence/domain-binding-20261010-validation.log)。原配图交付见 [视觉更新](./visual-refresh-20261010.md)。若用户要求恢复旧域名入口，先核对后续变更，恢复两个网站地址配置并重新构建部署；若恢复旧服务器，应核对备份中的两条原 A 记录并保留现有 MX／TXT，不盲目删除当前记录。

参考 Cloudflare [自定义域名文档](https://developers.cloudflare.com/pages/configuration/custom-domains/) 与 [官方 SDK 的域名重试验证接口](https://raw.githubusercontent.com/cloudflare/cloudflare-python/main/src/cloudflare/resources/pages/projects/domains.py)。
