# A1：入口与操作事实独立验收

验收时间：2026-10-09 13:22（北京时间）。验收对象为当前未提交工作区；HEAD：`ce64308f494df793f07c5b0b304737a65c61eba4`。范围：P01、P02、P05、P06、P09、P10。

**结论：六页的证据整理部分成立，六页均未通过原 Goal 的正式页面验收；正式发布候选为 0/6。** 未发现这些正文把已知矛盾数值或未执行交易直接写成已验证事实。阻塞主要是关键操作结果缺证据和补丁记录缺失，不能称作六页已经存在事实错误，也不能用免责声明替代可执行攻略。

## 验收方法与边界

- 独立逐行阅读六篇当前 `src/content/wiki/en/` 正文，对照 [Goal 第 2、3 节](/workspace/AnvilWiki/goals/20261008-0047-clover-time-wiki.md:39)；不使用历史验收结论代替本次判断。
- 读取 Beebom、Destructoid、Gamepur、Roonby、玩家 Wiki 的既有原文缓存，以及 331 张公开 Trello 卡片导出中的相关条目；复核官方游戏／群组 API 缓存。缓存抓取时间来自原证据记录，本轮没有重新请求网络，也不声称重新确认了当前游戏状态。
- 本轮实际查看五张原始来源图片：两张兑换入口、塔内祭坛、角色重抽界面、AFK 奖励。它们只能证明画面中存在的控件、标签和数值，不能证明点击、扣费、领取或装备结果。
- 没有进入游戏，没有兑换、重抽、捕鱼或联系作者。没有构建、运行工程测试、修改正文、配置、测试、封面、draft 或 Git。工程及显示验收由其他委派处理。
- 阅读、提取缓存、生成审核清单的 shell 命令均退出 0；首次综合读取输出被截断，已对关键正文和来源分别重读。未以截断输出作为最终依据。
- [审核输入及 SHA256 清单](/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A1/review-manifest.json) 保存六篇正文、来源缓存和实际查看图片的指纹。`.tmp/` 是核查缓存，不是正式发布素材。

## 逐页验收矩阵

“部分”指页面中若干事实或界面有证据，**不代表正式验收通过**。

| 页面 | 原标准 | 当前通过的部分 | 未通过的核心条件 | 页面结果 |
|---|---|---|---|---|
| P01 码表 | 码、奖励、状态、来源、整表核对日期；至少一个当前有效码或可靠证明当前没有有效码；复制原文 | 正文没有伪造 active／expired；仅 frontmatter 维护码名单；公开候选矛盾有原文依据 | `codes: []`；没有当前成功兑换，也没有当前无有效码的证据。无可验复制项目，不能把空表视作复制功能已通过；`lastModified` 不等同于码表有效性核对 | 不通过 |
| P02 兑换 | 一条实际验证路径、必要条件、截图、可确认失败提示 | 两张图确有大厅 Codes 和游戏内 Settings 两种上下文；没有拼接成唯一必经步骤 | 提交动作、资格条件、成功／失败提示和奖励结果未验证；截图未证明当前版本，也不是完整操作录像 | 部分，正式不通过 |
| P05 新手 | 首次进入至首轮成长的可执行顺序；资源用途／限制有证据；相关页面链接 | Lily／工具、箱子链有第三方原文；祭坛 E／Read／x1 和版本标签可直接看见；Finral 付费且已到访限制有看板陈述 | 工具领取及装备、出生到塔的适用路线／钥匙分支、箱子当前保证掉落、第一次书的获取／装备／施法未形成完整可执行且已验证顺序；无已上线相关内链 | 部分，正式不通过 |
| P06 重抽 | 实际入口、对象、消耗、覆盖／保留机制；未核实操作不公开 | 图片显示 Hage Priest、Race／Social Class／Trait、Roll／Get Special，普通及 Special 分列 | Spins (2) 是余额，不能说明每次成本；没有按钮点击、警告、余额变化、替换或保留结果。当前出生入口路线也未确认 | 部分，正式不通过 |
| P09 钓鱼碎片 | 入口、解锁、操作、奖励、碎片用途；不强行假定鱼换碎片成立 | V、鱼竿、鱼饵和小游戏可追溯到第三方文字；不同奖励说法被分开；AFK 图未误作捕鱼结果 | 鱼竿购买／制作／装备、实测捕鱼流程、Golden Marlin 实际产出、鱼到碎片的阶段和制作配方缺证据 | 部分，正式不通过 |
| P10 更新 | 至少一条可追溯官方日期、实际改动、影响页面 | 官方缓存确有 BETA 0.1；群组 shout 为 null；正文正确区分平台更新时间、创建日和补丁 | 没有一条官方日期＋实际改动的补丁条目；不存在可映射的受影响页面 | 不通过 |

共同情况：六篇均为 `draft: true`，正文内站内文章链接均为 0。保持草稿期间不应通过链接其他草稿来凑数量；转正前须依 Goal 补真实已上线相关链接。上表只判断本次负责的六页，不外推其余四页或工程自测结果。

## 按阻塞程度排列的发现

### B1：P01 没有可公布的码状态，阻塞兑换入口验收

正文定位：[all-codes.mdx:11](/workspace/AnvilWiki/src/content/wiki/en/codes/all-codes.mdx:11)、[all-codes.mdx:18](/workspace/AnvilWiki/src/content/wiki/en/codes/all-codes.mdx:18)、[all-codes.mdx:22](/workspace/AnvilWiki/src/content/wiki/en/codes/all-codes.mdx:22)。

独立核对：Beebom 缓存第 55–65 行给 `1KLIKES` 一只 Normal Chest、`BETARELEASE` 一只 Big Chest／一枚 Crystal Mana，且声称没有过期码。Destructoid 缓存第 128–143 行分别写十只 Normal Chests、十只 Big Chests／五枚 Crystal Mana，还列出过期码。公开 Codes 卡片 `Lyr4hnVN` 写 `10KLIKES!`、`25LFAVSTY`，并把 `30KLIKES` 写两个日期；月份／年份／时区不完整。正文不据此录入确定状态是正确处理。

证据类型：**未验证／来源冲突，未发现正文造假。** 最小转正证据为一个完整的当前成功兑换记录、原始公告和准确奖励；若主张当前无有效码，则另需支持该主张的可靠证据。不能把“本次没测出码”改成“当前没有有效码”。

### B2：P02 有入口图，没有经过验证的兑换过程

正文定位：[how-to-redeem-codes.mdx:17](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-redeem-codes.mdx:17)、[how-to-redeem-codes.mdx:26](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-redeem-codes.mdx:26)、[how-to-redeem-codes.mdx:30](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-redeem-codes.mdx:30)、[how-to-redeem-codes.mdx:34](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-redeem-codes.mdx:34)。

实际看图：Beebom 图为 Afk World／Play／Customize 大厅，左下 Codes／Enter code... 可见；Destructoid 拼图并列大厅、Menu、Settings、Codes 输入框，未显示成功、过期、已经使用或资格错误提示。两种上下文可以同时存在，因此不再强行认定入口冲突是合理的。但 Enter 提交和资格清单来自文字，不能说图片已经验证这些动作。

证据类型：**部分界面支持，关键动作未验证。** 可选其中一种上下文完成实际输入、提交、结果核对，并验证必要条件与至少一条明确失败提示；无需强制两条路径都完成后才能发布。

### B3：P05 未闭合首次成长链，缺口不是再写一份提纲能解决

正文定位：[beginner-guide.mdx:27](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:27)、[beginner-guide.mdx:29](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:29)、[beginner-guide.mdx:39](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:39)、[beginner-guide.mdx:46](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:46)、[beginner-guide.mdx:50](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:50)、[beginner-guide.mdx:68](/workspace/AnvilWiki/src/content/wiki/en/guides/beginner-guide.mdx:68)。

独立核对工具原文：`followup-0.html` 的 How to get the Rake 写 Lily 在教堂外，接四土豆任务免费给已装备耙子；How to get the Axe 只说 lumberjack，斧头入背包，没有准确名字或装备输入。Lily 看板有 level 3；Lucie 卡片葡语 level 4、英语 level 7，自相矛盾，也没有明确工具赠送字段。正文没有将 Lucie 猜作 lumberjack，是合理处理。

独立核对书路线：`followup-1.html` 有箱子链及塔旁 NPC 钥匙分支，但没有可独立查看的原始记录。塔图有 v0.10.41-T、level 2、E／Read、蓝水晶 x1、Epic 1/50／Legendary 1/100／Mythic 1/250 及 Roblox Plus 减 30%。正文正确称为画面读数，没有推断按钮按下和书已领取。Roonby 的 35／70／175 恰为读数的 70%，但不能因此断言作者订阅状态或当前保底计数规则。

Finral 卡片原文确写“place you have been”与“for a fee”。不能把文章建议的传送省略限制，直接用于从未到塔的新玩家开局。

证据类型：**第三方流程支持＋部分界面支持，首轮成长未验证。** 需要一段适用前提明确的开局至首次书装备和技能使用过程，并核对工具领取／装备。允许使用实际观看的公开录像，不要求老杨必须提供亲测资料。

### B4：P06 核心缺口为交易规则，不是三个选项是否存在

正文定位：[how-to-reroll.mdx:30](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-reroll.mdx:30)、[how-to-reroll.mdx:32](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-reroll.mdx:32)、[how-to-reroll.mdx:40](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-reroll.mdx:40)、[how-to-reroll.mdx:48](/workspace/AnvilWiki/src/content/wiki/en/guides/how-to-reroll.mdx:48)。

实际看图确认三个类别、Roll／Get Special、Hage Priest - Spins (2) - Special (0)，以及 Human／Commoner／Fast Learner。未显示警告或前后交易。玩家 Wiki 原文第 12–14、28、54 行确报告共享 Spins、每次一枚、立即替换；这些是书面来源，自称有录像也不能替代本轮实际看录像。

证据类型：**界面支持，成本和保留行为未验证。** 最小补证是一个明确类别的重抽记录，含按前余额、费用／警告及按后余额／旧新结果。若据此写所有类别共享相同规则，还应核对其适用范围，不能从一张 Race 结果推断 Special 或存储功能。

### B5：P09 尚不确定鱼到碎片处于哪个步骤

正文定位：[fishing-fragments.mdx:21](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:21)、[fishing-fragments.mdx:25](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:25)、[fishing-fragments.mdx:34](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:34)、[fishing-fragments.mdx:40](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:40)、[fishing-fragments.mdx:44](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:44)、[fishing-fragments.mdx:52](/workspace/AnvilWiki/src/content/wiki/en/guides/fishing-fragments.mdx:52)。

独立核对：玩家 Wiki fishing 原文第 16 行明确 6600 是一组商品的报价，正文没有把它当单竿价格。第 43–48 行说 Golden Marlin 提供碎片再制作水晶；Mana Crystals 原文同时记录土豆数量一／五冲突。Gamepur 写捕鱼可能得到整颗水晶，所配图却是 AFK Rewards。本轮看图确有 ONE TIME、168h、3x Crystal Mana，没有任何鱼或捕鱼结果。Fishing Rod／Golden Marlin／Crystal Mana Frags／Mana Crystal 卡片的 Acquirement 为空，名称列表不能验收产出链。

证据类型：**奖励阶段存在冲突，关键操作未验证。** 最小补证为鱼竿获取／装备与完整捕鱼、Golden Marlin 入袋后的实际物品或转换结果、碎片制作界面的原料及产物。未确认前既不能宣布主题成立，也不能宣布“钓鱼换碎片”已经被证伪。

### B6：P10 没有正式更新日志的最小内容

正文定位：[patch-notes.mdx:18](/workspace/AnvilWiki/src/content/wiki/en/guides/patch-notes.mdx:18)、[patch-notes.mdx:26](/workspace/AnvilWiki/src/content/wiki/en/guides/patch-notes.mdx:26)、[patch-notes.mdx:36](/workspace/AnvilWiki/src/content/wiki/en/guides/patch-notes.mdx:36)、[patch-notes.mdx:38](/workspace/AnvilWiki/src/content/wiki/en/guides/patch-notes.mdx:38)。

独立读取官方缓存确认 creator AnimeCore Studio、BETA 0.1 和 shout:null；`updated` 时间没有 change list。玩家 Wiki updates 原文明确“No detailed patch entries are confirmed yet”，March 16 标注的是体验记录创建，不是上线或补丁。界面 v0.10.41-T 和描述 BETA 0.1 的并列也没有发行日期。

证据类型：**必要文档缺失，未发现正文把错误事件当补丁。** 补至少一条来源归属可核对的开发者公告，附发布日期、具体改动与受影响页面，再据此写正式条目。当前没有公告不证明开发者从未发布过公告。

## 本轮发现的可复用线索

以下可以继续推进研究，但本轮没有修改正文或放行页面：

1. **Roonby 已有装备的书面线索。** S23 原文有“How to Equip a Grimoire”小节，写打开 inventory、找到物品、select to equip。P05 当前未收录这条线索。因此不宜再称“装备完全没有任何来源”；准确说法是缺装备控件原文、实际过程及结果。
2. **重抽图附带技能与快捷栏信息。** Gamepur 图片右下显示 Fire Ball—E、Fire Ground [Hold]—R、Click—M1、Block—F，底部 2 号栏有发亮书。能记录为这名 v0.10.41-T 角色的 HUD 控制提示；不能证明新账号已经解锁该书、2 是确定装备动作、E 已成功施法，或所有书共享输入。
3. **原文与看板可以缩短待验证列表。** 不必重新找游戏身份或反复证明三种角色配置类别存在；优先寻找缺失的动作与结果。地图、资格、费用和奖励转换仍须各自核对。

## 来源入口与可复核缓存

| 来源 | 原始入口 | 本轮复核对象 |
|---|---|---|
| 官方游戏／群组 | https://games.roblox.com/v1/games?universeIds=9891331827 ；https://groups.roblox.com/v1/groups/175661976 | `final-official-check.json` 中 2026-10-09 07:57 抓取的公开字段，不冒称本轮实时查询 |
| Beebom S04 | https://beebom.com/clover-time-codes/ | `independent-20261009-beebom-current.txt` 第 55–65、75–88 行及原图 |
| Destructoid S20 | https://www.destructoid.com/clover-time-codes/ | `independent-20261009-destructoid-codes.txt` 第 128–164 行及拼图 |
| 工具／首次书 S08／S09 | https://clovertime.wiki/gear/clover-time-how-to-get-tools ；https://clovertime.wiki/magic/clover-time-how-to-get-grimoire | `followup-0.html`、`followup-1.html`，已独立提取纯文字到 A1 缓存 |
| 重抽 S10 | https://clovertime.wiki/progression/clover-time-rerolls | `research-20261009-rerolls.txt` 第 12–14、28、45–58 行 |
| 制作／捕鱼 S13／S18 | https://clovertime.wiki/magic/clover-time-mana-crystals ；https://clovertime.wiki/activities/clover-time-fishing | `research-20261009-mana-crystals.txt`、`research-20261009-fishing.txt` 第 16、25–34、43–48 行 |
| 公开看板 S21 | https://trello.com/b/XHcUunD7.json | `trello-public-20261009.json`；具体 Codes／Lily／Lucie／Finral／Elsie／材料卡片按其 URL 查找；官方反向归属没有已确认记录 |
| Gamepur S22／S24／S25 | https://www.gamepur.com/guides/how-to-get-grimoire-clover-time ；https://www.gamepur.com/guides/how-to-get-crystal-mana-clover-time ；https://www.gamepur.com/guides/clover-time-races-tier-list | 三份原文和 tower／crystal／reroll 三张图；作者 Aleksa Stojković，文章日期 2026-10-05，截图采集日期未知 |
| Roonby S23 | https://roonby.com/2026/10/02/how-to-get-a-grimoire-in-clover-time-guide/ | `roonby-grimoire.txt` 原文，包括装备小节；作者 Jay，2026-10-02 |
| 玩家 Wiki 更新 S27 | https://clovertime.wiki/updates | `player-wiki-updates.html` 原文，已独立提取纯文字到 A1 缓存 |

所有相对缓存名称均位于 `/workspace/AnvilWiki/.tmp/clover-time-research/`。正式来源元数据记录可对照 [independent-sources-20261009.json](/workspace/AnvilWiki/docs/clover-time/evidence/independent-sources-20261009.json) 及 [autonomous-sources-20261009.json](/workspace/AnvilWiki/docs/clover-time/evidence/autonomous-sources-20261009.json)；这些文件只是历史抓取记录，不作为本轮新请求或新游戏测试。

## 发布判定与交付

这六页可以继续作为开发研究草稿，按原 Goal **不能转正发布**。正式转正需补 B1–B6 的各自核心证据，删去研究占位叙述、补真实相关内链，并由主 Agent 合并工程／页面验收判断。本次没有提出新的产品决策、要求用户提交资料或扩大施工范围。

交付：本报告及 A1 私有审核缓存。主 Agent 需读取实际图片／原文定位并独立核对结论；不能仅因为本子代理写了验收报告就将 Goal 标完成。
