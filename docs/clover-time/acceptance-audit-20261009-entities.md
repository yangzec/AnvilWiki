# A2 独立验收：排名与实体

验收记录完成时间：2026-10-09 13:24（北京时间）。范围为当前未提交工作区的 P03、P04、P07、P08；依据 Goal 第 2、3、5 节，而非此前“0/10”的汇报。仅写本报告及 A2 缓存，没有改正文、draft、配置、测试或资产，没有构建、Git 操作、游戏操作或外部写入。

**结论：四页整页均未通过发布验收，但不能据此说四页的公开事实都未核实。P04 的核心名单、属性方向和编辑依据可以通过；P08 的基本身份、获取类别与独特能力可在“公开来源支持”层级通过。P03 仍缺适用版本及明确的第二档理由；P07 有一处 HUD 名称转录需要复核。四页还缺共同要求中的真实相关内链及有依据的版本上下文。**

## 原标准的适用边界

- Goal 第 43 行允许“公开来源支持”这一事实状态。第 49 行对兑换、重抽、钓鱼等关键操作要求实际验证，不能推导为每个种族属性、编辑评价或实体简介均须本次亲测。
- 第 51 行允许编辑强度榜。没有受控 DPS 测试不自动否决排名，前提是依据、玩法、版本和归属明确。比较表不需要为每家出版物再建立一套本站实测体系。
- 第 69–70 行要求实体“游戏内准确名称、可确认的获取方式、能力与玩法；未知数值省略；与 P03 双向互链”。没有写“必须看到指定书抽取结果、完成装备交易、每个技能的按键输入和全觉醒解锁”。这些是可选补强证据，不能追加为四项硬门槛。
- 公开文档可支持名称、随机塔抽取类别、能力文字描述和编辑依据；普通塔提示不能证明某次抽中指定书或装备成功。本文只验收前一层事实，不把它升级为后一层操作记录。
- 未证明开发者归属的公开看板可以引用，必须说明归属未确认，不能冠以官方。没有官方反向链接也不等于看板所有定性文字均无效。
- 保留 draft 是正确的生产隔离状态，不是核心事实全部失败的证据。

## 三层逐页判定

“核心”指页面专属事实要求；“共同”指版本上下文、内容状态、真实内链等全页要求。下表不把历史测试当作本轮运行结果。

| 页面 | 核心事实 | 共同页面要求 | 整页发布结论 |
| --- | --- | --- | --- |
| P03 | 部分通过。十书名单、稀有度转录、三出版物档位与 PvE／混合玩法归属正确；第二档原因仍过于接近评级复述；适用版本未建立。 | 未通过。无 P07/P08 链接，正文无任何站内文章链接；元数据无 gameVersion。 | 不通过，保持草稿。 |
| P04 | 通过公开资料层级的核心验收。五族名单、定性属性方向、排名依据、冲突数字处理与可见 Human 数值均可追溯。不是全族当前服务器亲测。 | 未通过。没有正式相关内链；截图 v0.10.41-T 只适用于 Human 捕获，未建立整榜适用版本。 | 不通过，不能把核心通过等同整页可发布。 |
| P07 | 部分通过。Anti Magic 身份、Tower 随机获取类别、剑系能力／动作、编辑玩法归属有支持；C 行名称“Dual Slashes 已由 HUD 确证”的证据力度不足。 | 未通过。无 P03 反链，无其他站内文章链接，未知构建的 GIF 不能确定当前版本。 | 不通过。获取、装备和全觉醒录像不是额外必需条件。 |
| P08 | 通过公开资料层级的基本核心验收。Poison／Poison Grimoire 名称跨文档一致，Tower Epic 分类和一般抽取系统相互支持，四种能力与 Anti Magic 有实际区别，未填猜测数值。当前技能 HUD 原文仍未确认，但文章已区分各来源写法。 | 未通过。无 P03 反链，无其他站内文章链接；正文仍是研究状态且没有整页版本上下文。 | 不通过。不能以“没有 Poison GIF”单独判基本身份、获取类别和书面能力均失败。 |

### P03：名单、稀有度与排名

正文 [grimoire-tier-list.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/grimoire-tier-list.mdx:33) 的十书稀有度表与公开 Tower 原卡片相符：Earth／Fire／Snow／Water 为 Common，Ice 为 Uncommon，Chain 为 Rare，Explosive Flame／Poison 为 Epic，Battle Lightning 为 Legendary，Anti Magic 为 Mythic。没有把稀有度写成强度或单书概率。

第 54–65 行的三列排名与 Destructoid、Gamezebo、GAMES.GG 缓存原文一致。Poison 的 S／A／S，Battle Lightning 的 A／S／S 及 Earth／Fire 的 Trash／D／D 均保留差异。第 52、67、69、73–79 行的活动范围和编辑性质说明正确，没有伪称本站实测。

原“每档有理由”针对文章采用的排名，不要求对照表的每一家、每一书都追加理由。首表第 21 行有 damage／move variety 原因；第 23 行的 progression 用途及第 75 行的控制／召唤用途有解释。**第 22 行仅说“低于第一组的替代品”，不能解释为什么在第二档。** 可直接引用原 Destructoid 的“sub-meta PvE damage、great alternatives”并说明是来源判断，补齐这一小项；不需要新的受控测试。

真正发布阻塞：第 87 行承认当前构建未确定；文章未给整榜适用的有依据版本。第 83 行明确实体未验收所以暂不互链，做法没有制造死链，但第 65 行 Goal 的 P07/P08 链接条件仍未满足。

### P04：属性可用公开文档核实

正文 [race-tier-list.mdx](/workspace/AnvilWiki/src/content/wiki/en/guides/race-tier-list.mdx:25) 的五族定性属性表与各卡片文字相符。Dwarf 的 EXP 表述是“no EXP modifier listed”，比断言游戏绝无 EXP 更准确。Human-Dwarf 的卡片标题与 Half-Dwarf 描述差异在第 33 行公开说明，不是把两种拼法误当两个种族。

第 43 行截图转录正确：Human 为 +5% Health Regen、+5% Stamina Regen、+2.5% Mana Regen、+5% EXP；HUD 为 v0.10.41-T。第 45 行确实指出 Gamepur 正文的 5% 与其图的 2.5% 冲突。其他四族没有截图，不应因此否决有归属的定性属性表；其争议数字已省略，符合原标准。第 51–57 行各档的属性方向理由可追溯。Sovereign、Chosen One、Mana Sensitive 的分类纠正正确。

事实层通过仅限于这些有归属的内容，并不证明所有服务器当前数值。未确认的种族照片只有外观，没有属性或菜单标签，正文第 33 行没有过度使用它们。整体版本范围和正式相关页内链仍是共同层缺口，不能从单张 Human 图推导全榜 v0.10.41-T。

### P07：能力支持与一处转录疑点

正文 [anti-magic.mdx](/workspace/AnvilWiki/src/content/wiki/en/items/anti-magic.mdx:27) 的 Tower／Mythic 获取类别能由公开卡片、一般抽取教程及祭坛截图共同支持为公开资料事实。它没有证明作者抽中了 Anti Magic，但原实体条件不要求该作者必须抽到此书。官方描述与视频 HUD 支持基本名称。

Cut、Counter、Dual、Rush 采样支持剑姿、斩击效果、命中提示、靠近目标和目标位移；Second Form 采样支持变身和暗翼。正文没有从采样捏造减伤、无敌、冷却、伤害、输入窗口或完整觉醒。E／X、Z 的按键提示可以辨认，不能说播放器曾按这些键。

**转录疑点：第 56、62 行把 C 行写成 HUD 确认的 Dual Slashes。** 公开卡片文字确实写 Dual Slashes，但 430×240 GIF 的 C 行字形低清，我放大原帧后不能可靠排除另一写法，部分帧看起来近似 Dual Stance。这里不确认另一名称，也不把疑点写成已发现游戏机制错误。建议把“书面卡片名称”与“HUD 低清转录未确定”分开，取得清晰画面后再声称 HUD 已确证。对应证据 JSON 的“Same five HUD names”也需同样谨慎。原图和本轮最近邻放大图都保留在 A2 缓存，供主 Agent 再看。

获取结果、装备演示、其余招式输入与完整觉醒流程可继续研究，**不应作为当前实体简介必须齐全的新增验收项**。真正共同阻塞是与 P03 双向互链、适用版本和上述准确转录。

### P08：书面资料已形成有区别的实体简介

正文 [poison.mdx](/workspace/AnvilWiki/src/content/wiki/en/items/poison.mdx:25) 的 Tower Epic 类别转录准确，卡片直接链接 Poison Grimoire。独立出版物也使用 Poison Grimoire／Poison，未发现书籍身份冲突。公开资料支持一种可确认的获取类别，不证明具体抽奖概率、抽中画面或装备成功，文章也没有这样声称。

第 49–52 行的 Projectile／Mist／Explosion／Clone 表与葡萄牙语原卡片一致；Stop Clone／Order Clone 是文字命令名称，没有编造键位。第 41、54 行清楚区分 Toxic 与 Tox、Mist 与 Mister，未把未看视频写成已观察行为。无 Poison GIF 不等于这些有归属文字均不能引用，也不必强制拍到每招才能形成实体简介。

**文案问题：第 58 行先引 Gamezebo 的 A-tier，第 60 行紧接“It places Poison in its top PvE group”。** 意图应为回指最初玩家 Wiki，现有代词容易让读者误解为 Gamezebo 把 Poison 放 S。应明确写玩家 Wiki 的名称。这是来源归属不清，未发现具体数值造假。

正文第 64 行仍采用“publication needs independently supported ability behavior”的研究状态结论；不能把这句话自行扩张为 Goal 强制所有招式视频。精确技能 HUD 对照是进一步提高质量的路径，整页发布仍需版本归属、清晰来源段落及 P03 反链。

## 实际读取与查看

本轮没有发起新的网络请求。核查的是已保存的原 HTML／正文／公开卡片 JSON 和原 GIF；这是独立审阅既有证据，不能称为再次查询了实时游戏或当前服务器。缓存的原 URL 与原读取时间在 sources.md／证据 JSON；本轮新增查阅时间是本报告时间。

| 原来源 | 本轮核查对象 |
| --- | --- |
| https://trello.com/c/KhpwU5Vn | 原 Tower JSON 的十书分组，不仅看汇总表。 |
| https://trello.com/b/XHcUunD7 | 原公开导出中的五族与 Anti Magic 原卡片正文。 |
| https://trello.com/c/ishInW3U/118-poison-grimoire | 原 Poison JSON 的技能、命令及空附件列表。 |
| https://www.destructoid.com/clover-time-tier-list/ | 原正文排名、PvE 语境、属性方向与各档文字。 |
| https://www.gamezebo.com/walkthroughs/clover-time-grimoire-tier-list/ | 原十书档位、每组说明、Sho Roberts 及可见日期。 |
| https://games.gg/roblox/guides/clover-time-grimoire-tier-list/ | 原十书档位、混合活动范围、内部 D 档矛盾。 |
| https://www.gamepur.com/guides/clover-time-races-tier-list | 原种族表和 Human 截图，不把正文数字压过画面。 |
| https://www.gamepur.com/guides/how-to-get-grimoire-clover-time | 原一般获取教程与祭坛截图。 |

实际通过 view_image 查看：Dual／Rush 六帧接触表及 HUD 放大；Human 和祭坛原图；本轮从原 GIF 重制的 Cut／Counter／Second Form／Bag 各六帧接触表；Dwarf／Elf／Human-Dwarf 外观合集。采样时间与时长和前次记录一致。没有完整播放 GIF、观看 YouTube 或登录 Roblox。低清 HUD 的完整字词不因放大就自动变得可确认。

## 本轮命令及交付边界

- 读取 Goal、规则、四篇带行号正文、原来源缓存、现有证据 JSON：命令退出 0。
- Pillow 原 GIF 帧数／时长／采样复核并输出 A2 接触表：退出 0；Cut 36 帧／3.6 秒，Counter 41／4.1，Second Form 75／7.5，Bag 152／5.06。
- 四篇元数据／摘要／内链只读扫描：退出 0；摘要分别 50／47／49／50 词，345／323／373／349 字符；四篇均 draft true、无 gameVersion、无正文站内文章链接。未执行工程完整校验或构建。
- S28／S29／S30 原 HTML SHA-256 与交付记录复核：退出 0，3/3 一致。本轮没有把摘要或旧 Agent 结论当作原文。
- 本轮无命令失败；**未验证**当前服务器版本、实际交易和所有技能输入，不算失败。版本、真实相关链接及文稿准确性是本范围发布阻塞。

任务缓存与复核记录：`/workspace/AnvilWiki/.tmp/clover-time-acceptance-20261009/A2/read-only-checks.json`。A2 缓存被忽略，不是站点运行依赖。本报告是唯一项目交付修改；正文等业务文件保持原样。报告完成后请主 Agent 复核疑点、汇总三层结论，不因核心公开资料通过而直接切换 draft，也不沿用此前附加的实机门槛。
