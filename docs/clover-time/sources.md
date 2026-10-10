# Clover Time 事实来源与核实记录

更新时间：2026-10-09 13:30（北京时间）
状态：官方游戏身份已核实；10 页资料底稿已建立，草稿站工程已接入并自测。关键操作、兑换码有效性及部分实体资料仍缺证据；工程通过不改变这些事实状态。

## 当前证据边界

2026-10-09 13:30 独立验收更正：[子代理总验收](./subagent-acceptance-20261009.md)。P04/P08 核心公开资料可通过，不额外要求指定实体抽取／装备／所有输入／全觉醒录像；整页仍缺文稿与互链等原条件。Anti Magic GIF 的 C 行字词不能可靠转录，撤回原“五名均由 HUD 确证”；仅有 C 键及书面 Dual Slashes 名称的各自证据，不武断换为另一名称。旧研究矩阵以本次更正为准。

用户上传的架构文档是选题和检索线索，不是事实证明。现已通过 Roblox 官方页面与 API 核实游戏名、开发商、beta 状态、体验及群组 ID；排名、码有效性、奖励和操作步骤不能因此视为已验证。

当前可用工具只有本地命令和环境配置接口，没有专用网页搜索或浏览器工具。2026-10-08 00:54，通过环境代理请求 https://www.roblox.com/ 和 https://www.destructoid.com/，均返回 CONNECT 403（curl 退出码 56）。这是资料网站访问受限，不是游戏不存在或来源内容错误的证据。未读取上述网站正文，未进行实机验证。

历史上已保存网络配置草稿。2026-10-08 01:02 新环境复查报告网络模式为 unrestricted、状态 enforced；Roblox 官方页面、games.roblox.com 和 groups.roblox.com API 请求成功。此前环境代理限制已解除，但部分第三方文章仍返回站点 403，不能声称已读到这些文章。

## 来源等级与记录规则

2026-10-08 05:38 补查：当前已确认可用 Python Playwright 和 Chromium，浏览器访问 YouTube／X 仍失败。新增 S06/S07 原始页面及 VID-01 视频入口，详见 [视频与社交调查](./video-social-research.md)。未观看视频、未取得官方社交公告、未进入游戏。

- 一级：Roblox 官方体验页面、已确认归属的开发者公告、游戏内实际结果。
- 二级：独立攻略站的原始文章或作者的实际测试。只支持其具体陈述，不把编辑排名当成官方结论。
- 线索：用户提供的架构、检索摘要、转载和聚合列表。须追到原始页面。
- 状态：待查／公开来源支持／实机已验证／存在冲突／无法验证。
- 不写无法读取的文章发布日期、作者或内容；不把拟检索 URL 写成已查阅来源。
- 证据时间按北京时间记录；截图应遮蔽账号、聊天、个人信息，核实资料不包含凭据。
- 第三方实机视频须实际观看并记录作者、日期、时间点及画面；可标记“视频画面支持”，不得称为本次亲测。仅有标题或嵌入链接仍是线索。

2026-10-09 续查已实际查看 S04/S20 的兑换截图、抽帧核对 S21 的 Anti Magic Cut GIF。画面支持限于具体界面／动作，不等于完整路线或本次游戏操作；详细时间点和出处见 [独立来源与看板记录](./independent-source-research.md)。

2026-10-09 自主检索又读 S22–S27，实际查看祭坛、AFK、重抽三个界面及 Counter／Second Form 的各六帧，补 8 篇正文并完成全部 10 篇原创文字封面。来源与边界见 [本轮研究](./autonomous-research-20261009.md)；仍未进入游戏。Brave 一次检索有效，后续返回 429，已停止继续检索；没有绕过访问拒绝。

## 游戏身份

| 事实编号 | 陈述 | 当前来源 | 查阅时间 | 状态 | 需要补齐 |
|---|---|---|---|---|---|
| ID-01 | Clover Time [BETA RELEASE]；体验 ID 93934100402512；universe ID 9891331827 | S01、S02 | 2026-10-08 01:08 | 公开来源支持 | 已确认，未进入游戏。 |
| ID-02 | 创建者为 AnimeCore Studio，群组 ID 175661976 | S01、S02、S03 | 2026-10-08 01:08 | 公开来源支持 | 官方体验创建者与群组匹配。 |
| ID-03 | Roblox 上的 Black Clover 风格动作 RPG，当前标题标为 beta release | S01、S02 | 2026-10-08 01:08 | 公开来源支持 | 不把 API updated 时间当版本更新公告。 |
| ID-04 | Discord／X 官方公告入口 | 未提供链接 | — | 待查 | 由官方体验页面或开发者群组交叉确认归属。 |

site.social.official、sameAs、developer 可使用已核实的 Roblox 资料。2026-10-08 23:49 复查 S02，官方描述明确标注 BETA 0.1；这是已核实的描述标签，不证明发布日期或具体改动，也不把第三方未注明版本的玩法自动归入该版本。Discord 官方归属仍未确认。

## 实际读取的原始来源

| 编号 | 原始 URL | 发布／更新日期 | 查阅时间（北京时间） | 支持的事实与限制 |
|---|---|---|---|---|
| S01 | https://www.roblox.com/games/93934100402512/Clover-Time | 页面未标明文章日期 | 2026-10-08 01:04 | 200；标题、创建者、官方介绍支持 ID-01–03，以及 Grimoires、Anti-Magic、Magic Brooms、Magic Squads、AFK World 等功能提及。不是实机证据。 |
| S02 | https://games.roblox.com/v1/games?universeIds=9891331827 | API 元数据；不是文章 | 2026-10-08 01:08 | 200；返回 creator.id 175661976、creator.name AnimeCore Studio、rootPlaceId 93934100402512、genre_l2 Action RPG。updated 只作平台更新时间，不能生成 patch notes。 |
| S03 | https://groups.roblox.com/v1/groups/175661976 | API 元数据；不是文章 | 2026-10-08 01:05 | 200；群组名称 AnimeCore Studio，与 S02 创建者匹配。shout 为 null，没有可用更新公告。 |
| S04 | https://beebom.com/clover-time-codes/ | JSON-LD：发布 2026-10-05T22:05:18+05:30；修改 2026-10-06T17:05:38+05:30 | 2026-10-08 01:04；元数据复核 01:10 | 200；提供候选码、奖励和底部 Codes 路径。全部为第三方陈述，未实机验证。 |
| S05 | https://gamerant.com/clover-time-codes-roblox/ | JSON-LD：发布 2026-10-02T10:28:11Z；修改 2026-10-06T15:29:48Z | 2026-10-08 01:05；元数据复核 01:10 | 200；提供另一份候选码、过期码和 Menu→Settings 路径。与 S04 存在冲突。 |
| S06 | https://clovertime.wiki/ | 首页未查得可靠文章日期 | 2026-10-08 05:36 | 200；玩家 Wiki 首页嵌入 VID-01，提供开局、实体和钓鱼研究线索；详情页 403，未读取原始实机证据。 |
| S07 | https://rocodes.gg/codes/clover-time | JSON-LD：发布 2026-10-02T14:39:45.000Z；修改 2026-10-06T14:30:28.000Z | 2026-10-08 05:36 | 200；Lobby→左下角 Code box→Enter 路径。截图 403；BETARELEASE、1KLIKES 奖励及部分码状态与既有来源冲突，未亲测。 |
| S08 | https://clovertime.wiki/gear/clover-time-how-to-get-tools | Article 元数据未提供发布日期／修改日期 | 2026-10-08 12:38 | 200；已读 Lily 任务领耙子、伐木任务领斧头等具体陈述；没有原始录像入口或操作截图，第三方支持，未亲测。 |
| S09 | https://clovertime.wiki/magic/clover-time-how-to-get-grimoire | 同上 | 2026-10-08 12:38 | 200；已读初始箱子、Mana Crystal 和塔内抽取流程；钥匙分支与制作配方存在差异，装备及技能输入缺失。与 S08 为同一站点，不算独立佐证。 |
| S10 | https://clovertime.wiki/progression/clover-time-rerolls | Article 元数据无发布日期／修改日期 | 2026-10-09 00:34 | 200；报告三类角色重抽、共享 Spins、菜单和立即替换。无独立画面。 |
| S11 | https://clovertime.wiki/progression/clover-time-races | 同上 | 2026-10-09 00:34 | 200；报告五种族，Devil 概率读数不一致；当前属性和版本未核对。 |
| S12 | https://clovertime.wiki/tier-list/clover-time-races-tier-list | 同上 | 2026-10-09 00:34 | 200；属性包编辑排名，明确不是 DPS／升级速度测试。 |
| S13 | https://clovertime.wiki/magic/clover-time-mana-crystals | 同上 | 2026-10-09 00:34 | 200；角色 Spins／水晶区分、首次箱子、制作和碎片；土豆数量冲突。 |
| S14 | https://clovertime.wiki/progression/clover-time-social-classes | 同上 | 2026-10-09 00:34 | 200；Sovereign 列入 Social Class，而非种族。 |
| S15 | https://clovertime.wiki/progression/clover-time-traits | 同上 | 2026-10-09 00:34 | 200；Chosen One／Mana Sensitive 列入 Trait；一项最高回复率评价与表格矛盾。 |
| S16 | https://clovertime.wiki/tier-list/clover-time-grimoires-tier-list | 同上 | 2026-10-09 00:34 | 200；十书 PvE 分级和 Poison 行为；Elf 类别及部分技能条件有问题。 |
| S17 | https://clovertime.wiki/magic/clover-time-anti-magic-guide | 同上 | 2026-10-09 00:34 | 200；剑系、Power 和 Devil 觉醒报告；获取段混用资源名。 |
| S18 | https://clovertime.wiki/activities/clover-time-fishing | 同上 | 2026-10-09 00:34 | 200；鱼竿、鱼饵、V 和小游戏、Golden Marlin 碎片；产出与装备未验证。 |
| S19 | https://www.destructoid.com/clover-time-tier-list/ | 发布 2026-10-01T13:47:24+00:00；修改 2026-10-06T09:01:10+00:00；Gordan Perisic | 2026-10-09 01:05 | 200；原始榜单、类别、重抽及塔路线；不同出版物，底层数值独立性未确定。Earth／Fire 评价与 S16 不同。 |
| S20 | https://www.destructoid.com/clover-time-codes/ | 发布 2026-10-08T07:05:21+00:00；修改 2026-10-08T07:05:25+00:00；Ana Mitic | 2026-10-09 01:06 | 200；码表、双入口与截图；奖励／过期仍有差异，新增候选未验证。 |
| S21 | https://trello.com/b/XHcUunD7；https://trello.com/b/XHcUunD7.json | 卡片有活动时间，不是文章日期或版本公告 | 2026-10-09 01:08 | 200；331 卡片公开导出，检查相关条目和 Cut GIF。游戏／群组匹配，官方反向归属未确认；数值、配方和步骤仍有冲突／空缺。 |
| S22 | https://www.gamepur.com/guides/how-to-get-grimoire-clover-time | Aleksa Stojković；发布 2026-10-05T05:01:54+00:00，修改 05:01:58 | 2026-10-09；落盘时间见证据 JSON | 200；已读祭坛、资源、书容量与 Drop 报告；实际看祭坛截图 E／Read／x1、保底分母与 Plus 条件。没有领取／装备结果。 |
| S23 | https://roonby.com/2026/10/02/how-to-get-a-grimoire-in-clover-time-guide/ | Jay；发布 2026-10-02T17:59:29+00:00，无修改日期 | 同上 | 200；35/70/175 缺条件；Golden Marlin 与碎片报告，没有转换步骤。 |
| S24 | https://www.gamepur.com/guides/how-to-get-crystal-mana-clover-time | Aleksa Stojković；发布 2026-10-05T05:23:40+00:00，修改 05:23:45 | 同上 | 200；文字说钓鱼可能得整水晶；实际图是 AFK Rewards，ONE TIME 168h 里程碑，不是捕鱼结果。 |
| S25 | https://www.gamepur.com/guides/clover-time-races-tier-list | Aleksa Stojković；发布 2026-10-05T04:32:32+00:00，修改 04:36:22 | 同上 | 200；Human-Dwarf／Dwarf 同为 B；Hage Priest 三类界面、普通／Special 余额可见。Human 图片回蓝 2.5%，与其正文 5% 矛盾。 |
| S26 | https://games.gg/roblox/guides/clover-time-grimoire-tier-list/ | Larc；发布 2026-10-07T22:05:03.466Z，修改 22:05:03.371Z，按原值保留 | 同上 | 200；十书排名与既有来源不同；声称测试却无方法／结果，Fire 与 Earth 的 D 档陈述内部不一致。 |
| S27 | https://clovertime.wiki/updates | 仅页面最后核对日期 2026-10-04；无可靠 Article 日期 | 同上 | 200；只有 Roblox 创建记录，明确没有详细补丁，不能用作 P10 官方变更。 |
| S28 | https://www.gamezebo.com/walkthroughs/clover-time-grimoire-tier-list/ | Sho Roberts；可见日期 2026-10-05，无解析到的 Article 时间 | 2026-10-09 09:36 | 200；十书混合 PvE/PvP 排名，Poison A／Battle Lightning S；没有公开受控测量，Fire Strength 投资说法不直接采纳。 |
| S29 | https://robolibrary.org/wikis/clover-time/grimoires | RoboLibrary Editorial；可见最后编辑 2026-10-04 | 2026-10-09 09:36–09:46 | 200；十书名单及原看板／官方体验链接；“未发布稀有度”与实际 Tower 卡片不同，未来更新说法无开发者公告佐证。 |
| S30 | https://clovertime.wiki/magic/clover-time-grimoires | 未建立可靠 Article 发布／修改日期 | 同上 | 200；十书图鉴、Power 和 Poison 书面技能；同 S08–S18 站点，不算独立验证。Water／Poison 稀有度及技能名与卡片不同。 |

P05 逐条流程、用户视频观察记录及本次访问限制见 [新手流程研究](./beginner-flow-research.md)。P05 暂存草稿已补入归属明确的第三方陈述，仍未满足完整操作验收。

日期以来源 JSON-LD 原样记录，并保留时区。查阅时间使用北京时间；网站正文描述的“更新日期”不替代结构化修改时间。

## 冲突及处理决定

| 编号 | 具体冲突 | 来源 | 处理决定 |
|---|---|---|---|
| C01 | S04：左下角 Codes；S05：Menu→Settings | S04、S05、S20 | S04/S20 截图显示大厅与游戏内两种上下文，不再当作必然互斥；当前资格、提交与成功结果仍待验证。 |
| C02 | S04 表示尚无过期码；S05 将 NEWCODE、CLOVERTIMEONTOP 列为过期 | S04、S05 | 不自行判定过期，不录入正式 expired。 |
| C03 | S04 给出具体数量；S05 多条仅写 Spins／Chests 等泛称；名单也不同 | S04、S05 | 数字奖励和有效性分别核实，不能用两源出现同一码代替实机成功。 |
| C04 | S04 Discord：Y2axazN6JE；S05 Discord：ZEySAMjRQs | S04、S05 | 不选择其中一个冒充官方。官方 social-links API 返回 401，不请求用户凭据来绕过。 |
| C05 | Mana Regen：S21 五种族值均为 S11/S19 的一半；S25 正文 Human 5%，其图 2.5% | S11、S19、S21、S25 | 图片支持 v0.10.41-T 的 Human 2.5%，但其他四族和当前版本仍未知；不生成平衡补丁。 |
| C06 | S19 强烈否定 Earth／Fire 后期；S16 称可用 | S16、S19 | 各自编辑判断保留归属，不改成本网站已验证排行。 |
| C07 | S20 的 BETARELEASE／1KLIKES 奖励及过期状态与 S04 有差异 | S04、S20 | 较新文章不是兑换证明；候选和奖励均不进入 active／expired。 |
| C08 | Trello 码名／标点、重复日期，与文章列表不同 | S20、S21 | 不纠正码文本、不猜到期年份／时区，不填 expiryDate。 |
| C09 | 35/70/175 与图片 50/100/250 保底分母 | S09、S22、S23 | 图片明确 Plus 减 30%；两组数数学匹配，但作者状态未知。正文分开基础读数与条件，不作为当前保证结果。 |
| C10 | Golden Marlin 碎片、鱼制作碎片／水晶、捕鱼直接得水晶 | S18、S19、S23、S24 | 没有结果／转换界面，不选一种作为确定流程；AFK 图不能证明钓鱼。 |
| C11 | S26 Battle Lightning S／Ice B，且两书 D 与仅 Earth D 自相矛盾 | S16、S19、S26 | 按来源与玩法保留分级差异，不以自述测试建立本站测评。 |
| C12 | S28 Poison A／Battle Lightning S，S19 Poison S／Battle Lightning A | S19、S26、S28 | P03 按作者与 PvE／混合玩法逐行呈现，不求均值或冒充本站测试。 |
| C13 | S29 称无稀有度，S30 称 Water／Poison 未记录；S21 Tower 有十书完整分类 | S21、S29、S30 | 已读原卡片，写为看板报告的分类，仍不把看板归属或当前实机可得性视为已确认。 |
| C14 | Human-Dwarf 卡片标题与英文 Half-Dwarf；书面 Dual Slashes 与 Double Cut 文章，C 行 HUD 名称未确认 | S21、S17 | 分别保留原标签；不无依据合并成当前同名同技能。 |

S04 提及 15KLIKES、600KVISITS、25KFAVSTY、10KLIKES 等码；S05 提及 MEGADROP、80KFAVSWOW!、40KLIKES 等。所有候选只留作核实线索，不进入 active 数组。官方页面提到“社区奖励”并不验证这些具体码。

## 逐页资料清单

| 页面 | 资料状态 | 需要核实的事实 | 所需证据 | 发布阻塞 |
|---|---|---|---|---|
| P01 兑换码 | 存在冲突 | 当前有效及过期名单、准确奖励、必要条件。 | 官方发布记录＋当前成功兑换结果；过期需明确失效结果。 | 没有任何实机已验证码，S04/S05 的过期与奖励陈述冲突。 |
| P02 兑换教程 | 公开来源支持（部分） | 当前 UI、资格、提交与提示。 | 已看 S04/S20 画面＋当前提交结果。 | 大厅／Settings 两入口有画面支持；条件和成功／失败仍缺实机结果。 |
| P03 魔导书榜 | 公开来源支持（部分） | 当前名单、能力、分级依据、玩法、版本。 | S16/S19/S21/S26/S28＋当前能力证据。 | 十书及卡片分类已溯源，三出版物逐行对照；当前版本及正式实体互链仍缺。 |
| P04 种族榜 | 核心公开资料通过，Human 界面支持 | 五族名单、定性属性、排名依据有支持；不称全族当前亲测。 | S11/S12/S19/S21/S25。 | 正式文稿、排名适用范围及真实相关内链；不以其他四族无截图作为额外否决项。 |
| P05 新手攻略 | 公开来源支持（部分），祭坛界面支持 | 首次进入顺序与完整工具／书获取。 | S01/S02/S22/S23＋实际开局记录。 | E／Read／x1 可见；领取工具、装备书和首技能步骤仍缺。 |
| P06 重抽 | 公开来源支持（部分），角色界面支持 | 当前入口、对象、消耗、覆盖或保留。 | S10/S19/S21/S25＋警告和前后结果。 | Hage Priest、三类别和余额可见；余额不能代替成本和消费结果。 |
| P07 Anti Magic | 公开来源支持（部分），五个演示采样支持 | 身份、Tower 获取类别和能力支持；C 行 HUD 名称待可靠转录。 | S17/S19/S21；原帧与卡片分别归属。 | C 行名称断言修订、正式文稿与 P03 互链；指定抽取／装备交易／全觉醒不是实体附加硬门槛。 |
| P08 Poison | 核心公开资料通过 | 名称、Tower Epic 获取类别、能力差异与编辑玩法可追溯。 | S16/S19/S21/S26/S28/S30。 | 代词来源明确、正式文稿及 P03 互链；不以没有 Poison GIF 单独否决有归属的书面能力。 |
| P09 钓鱼碎片 | 公开来源支持（部分） | 当前入口、解锁、奖励、碎片用途。 | S13/S18/S19/S21＋实际结果。 | 看板获取栏空，鱼→碎片转换说法不同；完整过程未验证。 |
| P10 更新日志 | 待查 | 正式公告日期、实际更新项目、受影响页面。 | 至少一条可追溯官方更新公告。 | beta 状态不能代替更新日志。 |

## 兑换码线索（禁止直接入 active）

| 线索编号 | 原文码 | 原文说法 | 当前状态 | 奖励 | 官方出处／实机结果 |
|---|---|---|---|---|---|
| CODE-01 | MEGADROP | 原文称 2026-10-07 被多站列为有效 | 待查 | 未确认 | 未提供 |
| CODE-02 | 40KLIKESGG | 同上 | 待查 | 未确认 | 未提供 |
| CODE-03 | 90KFAVS | 同上 | 待查 | 未确认 | 未提供 |

上述表是研究线索，不是正式码表。没有进行兑换操作，不声称有效或过期，不推断奖励。

## 排名线索（禁止直接写为本站结论）

原文提到 Destructoid 2026-10-01 榜单，以及 Anti Magic、Poison、Ice、Explosive Flame、Battle Lightning、Devil、Sovereign、Chosen One、Mana Sensitive。未提供具体文章 URL，本文未读取原文，名称、日期、类别和档位全部待核实。

2026-10-09 已读 S11–S16，部分名称获得玩家 Wiki 原文支持：Sovereign 在 Social Class，Chosen One／Mana Sensitive 在 Trait，不应都放入种族榜。分级只能带来源归属写进草稿；仍未读取 Destructoid 原文，不当作它的结论或独立验证。

2026-10-09 01:05 已读取 S19 的 Destructoid 原文，上述历史访问限制已变化。来源有作者与日期，分类和名单支持增加；这次才核对其具体分级，未称为本站实测。

## 单条事实记录模板

- 事实编号／关联页面：
- 原始 URL／来源名称／作者：
- 来源发布或更新日期（查不到写未知）：
- 查阅时间（北京时间）：
- 适用版本／测试时间：
- 具体陈述及支持它的最短证据摘录：
- 实机记录或截图路径（如有）：
- 是否独立于其他来源：
- 冲突、限制与处理结论：
- 状态／允许公开的表述：

## 2026-10-08 23:49 自动续作

S02 和 S03 返回 HTTP 200；官方描述明确出现 `BETA 0.1 — STILL IN EARLY PHASE!`，群组 shout 为 null。P05/P10 已补入官方版本标签与适用范围，P10 继续保持草稿，不把版本标签冒充更新公告。

Anti-Magic 详情、魔导书榜、钓鱼详情及 Destructoid 榜单候选入口均返回 403，未取得新正文或独立画面。[本轮访问及证据记录](./evidence/source-check-20261008.md)。当前仍无成功兑换、角色重抽、钓鱼操作或带日期的官方变更公告，0/10 正式验收不变。

## 2026-10-09 00:34 资料读取恢复

新具体页面返回 200，随后 Anti-Magic、魔导书榜与钓鱼详情也正常返回正文；这次才记录为已读取，而非沿用上轮 403 的猜测。新增 S10–S18 均同一站点、无 Article 发布／修改日期，没有原始视频链接。P03/P04/P05/P06/P07/P08/P09 已补有归属的资料，仍全部草稿。逐项摘录、分类修正、资源／配方／数值冲突与剩余验收见 [本轮研究](./character-magic-fishing-research.md)。

## 2026-10-09 01:15 独立出版物与画面续作

新增 S19/S20/S21，实际查看两张兑换图和 Anti Magic Cut GIF 的 6 个时间帧，补全部 10 页研究内容。新码候选 2MVISITS／100KFAVS／50KLIKES 及奖励只记为 S20 陈述；没有已验证码。官方 S02/S03 仍 BETA 0.1、shout:null，没有可追溯变更公告。正式验收仍 0/10；详见 [来源、帧与冲突](./independent-source-research.md)。


## 2026-10-09 强度榜与实体页收口

新增 S28–S30，并读取 Tower 原卡片，实际查看 Dual／Rush／Grimoire Bag 各 6 帧及三张种族图片。P03/P04/P07/P08 已补名单／比较／属性方向／HUD 与能力表。种族图片仅外观，Bag 演示没有装备操作；当前交易及版本对应仍缺。逐项结论见 [收口与验收矩阵](./ranking-entity-review-20261009.md)，正式验收仍 0/10。
