# Clover Time 视频与社交渠道调查

查阅时间：2026-10-08 05:34–05:38（北京时间）。
目的：为 10 页施工寻找公开实机画面及官方公告。未登录、未加入服务器、未发布消息、未进入 Roblox 游戏。

## 已找到的具体入口

### VID-01：新手攻略视频线索

- 视频地址：https://www.youtube.com/watch?v=brL0Crd9GYE
- 引用标题：BEST BEGINNER GUIDE in CLOVER TIME (BEST WEAPONS, GRIMOIRES, ITEMS, CODES) Roblox。
- 发现来源：https://clovertime.wiki/ ，HTTP 200；首页实际包含该视频的 YouTube iframe，并链接已确认的 Roblox 体验 ID 93934100402512。
- 标题来自该 Wiki 的 iframe，不是本次读取的 YouTube 元数据。作者、发布日期、时长及游戏版本未知。
- 状态：找到具体视频入口，未观看。YouTube 首页的 Chromium 请求失败；公开搜索页的普通 HTTP 请求返回代理 CONNECT 403。未取得播放画面、字幕或时间点。
- 待核对范围：P02 兑换入口、P05 开局、P06 重抽、P07/P08 实体。标题不证明视频实际覆盖全部主题。
- 准入限制：不能以 iframe 的存在宣称游戏操作已验证；不能编造视频时间点。旧视频即使展示过兑换成功，也不能单独证明查阅日仍有效。

### S06：Clover Time 玩家 Wiki 首页

- 原始 URL：https://clovertime.wiki/
- 发布／修改日期：本次首页未查得可靠文章日期。
- 实际读取：首页正文和公开 HTML，HTTP 200。自称 independent fan-made wiki，不能当作官方来源。
- 首页提供开局、Grimoire Tower、重抽、Anti Magic、Poison、钓鱼碎片等具体线索。有关配方、概率、属性和排名均为该站陈述，本次未读取其原始实机证据。
- `/progression/clover-time-beginner-guide`、`/activities/clover-time-fishing`、`/updates` 三个详情页均返回 HTTP 403，未读取。不能声称其完整教程或更新公告已核实。
- 首页把 NEWCODE、CLOVERTIMEONTOP 列为 2026-10-03 reported active；S05 列为过期。时间不同，保留冲突，不能选取首页作为当前有效证明。
- 作用：找到 VID-01 和主题入口；帮助定位后续核实对象，不复制整页文案或素材。

### S07：RoCodes 兑换文章

- 原始 URL：https://rocodes.gg/codes/clover-time
- HTTP 200，实际读取正文和 JSON-LD。
- JSON-LD 发布：2026-10-02T14:39:45.000Z；修改：2026-10-06T14:30:28.000Z。正文写 checked for new codes on October 07, 2026；两种时间分别记录。
- 原文路径：Launch Clover Time → Lobby → 左下角 Code box → 输入码 → Enter；另称须入群。
- 原文所谓 group 链接实际指向游戏体验 URL，不能用它确认群组加入条件。
- 截图原始地址：https://images.rocodes.gg/howto/2026/10/2/1038_Roblox%20Clover%20Time%20codes.png 。请求 HTTP 403，未看到截图。图片路径中的日期不等于经核实的拍摄日期。
- BETARELEASE 原文奖励为 Big Chest、50 Spins、5 Crystal Mana，与 S04/S06 的 1 个 Mana Crystal 说法冲突；1KLIKES 原文为 10 Normal Chests，与 S04 的 1 个 Normal Chest 冲突。
- 文章提供 Discord 邀请 `ZEySAMjRQs`，与 S05 同一个邀请，但不构成官方归属证明。
- 页面页脚的 X／YouTube 账号是 RoCodes 自身账号，不是 Clover Time 开发者账号。
- 该站自称人工测试所有码。本次没有取得对应兑换录像或逐码结果，因此记录为第三方报告，不升级为本站实机验证。

## 社交渠道实际访问结果

| 渠道／URL | 实际结果 | 能得出的结论 |
|---|---|---|
| https://www.youtube.com/ | Chromium：ERR_TUNNEL_CONNECTION_FAILED | 当前浏览器请求失败；没有看到视频。 |
| https://www.youtube.com/results?search_query=Clover+Time+Roblox | HTTP 客户端：Tunnel connection failed: 403 Forbidden | 代理拒绝该请求；不能据此判断视频不存在。 |
| https://x.com/search?q=%22Clover%20Time%22&src=typed_query | HTTP 200，只取得通用页面壳；Chromium：ERR_HTTP_RESPONSE_CODE_FAILURE | 未取得可核对的搜索帖子、账号归属或公告。 |
| https://discord.com/api/v10/invites/Y2axazN6JE?with_counts=false | HTTP 403 | 无法通过公开接口核对服务器身份；没有加入。 |
| https://discord.com/api/v10/invites/ZEySAMjRQs?with_counts=false | HTTP 403 | 同上；不能断言邀请失效。 |
| https://www.ign.com/wikis/clover-time-roblox/Clover_Time_Codes | 代理 CONNECT 403 | 未读正文。 |

环境接口显示 network mode 为 unrestricted、state 为 unknown；这不保证每个域名可访问。普通请求已验证部分域名可读、部分被拒绝。未修改代理、TLS 验证或网络策略来绕过失败。

Google 搜索本次只返回 JavaScript 跳转页。Bing 若干查询返回 Clover 收银系统等无关结果，不能作为本游戏证据；其中一次结果提供 S06/S07 的入口，随后已打开原始页面核对。

## 对施工的影响与下一步

1. 视频可以补充公开实机证据：实际观看后，记录作者、发布时间、原始 URL、明确时间点、画面中的前提及结果。来源状态写“视频画面支持”，与“本次亲测”分开。
2. 当前 VID-01 仍只是待观看线索。P02、P06、P09 的关键路径不能标记验收通过；本次没有新增亲测成功码。
3. 新手、实体与钓鱼主题已有更具体的研究入口，但概率、配方、奖励及强度结论须追溯画面或可信原始资料，不直接从 S06 首页入正式页。
4. 下一步优先读取 VID-01，并对照三种兑换路径；再找开发者身份可交叉确认的公告入口。若视频访问仍被代理拒绝，保留限制，不把要求用户提供截图作为已完成研究。

本次交付是公开渠道调查记录；10 页事实验收仍未完成，站点公开页仍为 0/10。
