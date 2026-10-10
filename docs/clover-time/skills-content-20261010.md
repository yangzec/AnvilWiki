# Clover Time 内置文章 Skill 执行交付

交付时间：2026-10-10 11:10（北京时间）。同一 Pages 项目部署 a1074fde-a54f-4086-b1ad-657cfefdf207 已成功，主站 [clovertime.world](https://clovertime.world/) 与中文 UI 入口 [clovertime.world/zh/](https://clovertime.world/zh/) 已显示本轮文章。本地／线上各 30 项实际浏览器检查通过，中文 Poison 搜索命中新标题与 /zh/items/poison/。中文入口仍使用英文正文，没有新增翻译。

本轮按用户要求，结合已保存的调研资料执行 [anvil-new-article](../../.agent/skills/anvil-new-article/SKILL.md) 与 [anvil-batch-articles](../../.agent/skills/anvil-batch-articles/SKILL.md)，修订现有 10 篇英文 MDX。公开正文继续遵守用户要求：不展示来源备注、研究标签或未确认清单。没有依据的内容省略，内部证据保留；没有声称进入 Roblox 实机或重新观看 YouTube。

## 实际执行

写作前读取两个 SKILL.md、docs/content-format.md、src/content.config.ts、src/config/navigation.ts、批量文章手册与现有同类稿件，核对历史来源档案及独立验收更正。编辑前备份 10 篇全文并记录 SHA-256。CSV dry-run 结果为新建 0、跳过 10：本轮修订既有文章，不用脚手架覆盖文件。

- 39 个正文 H2 均为问题，首段均为 40–60 个英文词；10 个 summary 同样满足词数与字符限制。
- 新增 50 条页面专属 FAQ，使用既有 frontmatter 自动显示并生成 FAQPage JSON-LD。
- 重写两份 PvE 排名表，说明每组理由、属性方向以及排名与获取稀有度的区别；不使用测量伤害或 PvP 结论。
- 移除重复的文末推荐章节，将每篇 3–5 条相关链接放到对应语境中。没有重复 H2、首答段或 FAQ 问题。
- 兑换、重抽、新手和钓鱼各新增两张自有导航／操作图，接入现成 gallery／灯箱。保留 10 封面与 10 主题插画，魔导书排行另复用两张实体插画。

## 逐篇素材与处理

| 页面 | 本轮重点 | 调研依据入口 |
| --- | --- | --- |
| P01 Codes | 兑换入口、输入与三类资源，codes 数组保持空 | independent-source-research、editorial-source-records |
| P02 Redeem | Lobby 和 Settings 两条入口分开叙述，输入检查与资源去向 | 已查看的兑换界面、independent-source-research |
| P03 Grimoires | 十书 PvE 分组、逐行理由、稀有度、Anti Magic／Poison 对比 | Tower 原卡、ranking-entity-review、S16 原文 |
| P04 Races | 五族定性属性、编辑优先级、三个配置类别 | 五张种族卡、character-magic-fishing-research、独立验收 |
| P05 Beginner | 角色／UI／基础战斗／采集／塔／飞行的学习顺序 | 用户观察记录、任务卡、已查看的塔界面 |
| P06 Reroll | 三列菜单、按钮所属类别、Spins／Special 和水晶区别 | 已查看的 Hage Priest 界面、autonomous-research |
| P07 Anti Magic | 四个清晰 PC 标签与剑系练习，基础和变身分开 | GIF 采样记录、独立验收更正 |
| P08 Poison | 投射物、雾、近身爆炸与克隆命令的差异 | Poison 原卡、Tower Epic 分类 |
| P09 Fishing | 鱼竿／饵／PC V／点击捕鱼顺序，材料分类和出售 | S18、character-magic-fishing-research |
| P10 Beta | 官方功能、平台与更新渠道概览 | editorial-official-game-20261010.json |

历史出处与全文：[内部来源档案](./evidence/editorial-source-records-20261010.json)、[独立研究](./independent-source-research.md)、[角色／魔法／钓鱼研究](./character-magic-fishing-research.md)、[后续公开原文与界面](./autonomous-research-20261009.md)、[排名／实体核对](./ranking-entity-review-20261009.md)、[独立验收更正](./subagent-acceptance-20261009.md)。新增写作没有把互相转抄、书面描述或历史截图升级为本轮实机验证。

## Skill 的适用调整

1. 当前文章均已存在，保存批量 CSV 并执行 dry-run，跳过创建步骤。
2. 现有有意义标签只有 codes、guide、items；保留每篇相关的 1–2 个标签，不为凑 Skill 的 3–5 个数目添加无关标签。
3. 用户明确要求不在公开页面标来源或未确认内容，因此内部记录保留这些信息，公开省略缺乏依据的陈述。
4. 8 张流程素材为原创示意图，不是游戏截图。Astro 7 的图库固定转换 WebP，直接 SVG 输入构建失败；使用已安装 Sharp 将自有 SVG 渲染为 PNG 后，原图库正常完成优化。没有修改框架组件或启用危险 SVG 处理选项。
5. 缺少当前有效码和有日期的正式补丁内容。P01 不冒充有效码表，P10 标题保持 Beta 功能概览；这两个原始搜索需求没有被编造资料补齐。

## 检查与交付边界

内容校验、默认构建、隔离预览构建及链接检查通过。49 个相关测试通过；一次命令意外执行了全量测试，结果为 395 通过、2 失败。失败分别是 apply-template 的上游演示值白名单不接受现有 clovertime.world，以及 workflows 要求已移除的 FORKER 模板头。它们读取的 wrangler.toml 与本轮修改前的导出文件 SHA-256 相同。本轮不修改配置或削弱这些测试，也不宣称全量测试全绿。

10 篇源码继续 draft:true，默认构建排除；独立预览副本保持 noindex，与原有发布方式一致。没有新增有效码、精准费用、掉率、制作数量、觉醒条件或正式补丁日期。完整事实 Goal 不因写作结构修订自动通过。

浏览器／部署最终状态与日志见 [本轮验收证据](./evidence/skills-content-20261010.json)。正文及图片位于 src/content/wiki/en/ 和 src/assets/covers/clover-time-flow-*；临时备份、CSV、编辑及自检脚本在 .tmp/clover-time-skills-20261010/。原 SVG 与 PNG 均保留，正式内容不依赖临时目录运行。

浏览器验收检查了 10 个英文详情的手机／电脑显示和 10 个中文 UI 详情：标题准确、HTTP 200、无页面横向溢出、图片实际加载、5 条 FAQ 与 JSON-LD 一致、canonical 正确；四个图库页面可打开、切换到第二张图并用 Escape 关闭。线上全局 noindex 继续生效。图库中的示意图不是实机截图；没有 Git 提交／推送、DNS 或框架修改。
