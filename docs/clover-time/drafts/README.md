# 10 页暂存草稿

状态：10 份 MDX 研究草稿已创建，全部 draft: true。此目录保留研究底稿，已复制接入 src/content/wiki/en/。开发模式生成草稿详情，生产构建排除草稿；不是 10 篇已完成攻略。

迁移结果：原有同名示例已备份并按用户授权替换，站点身份已切换。后续应用正文修改以 src/content/wiki/en/ 为当前版本；本目录保留研究阶段的历史底稿。

草稿保留了独立页面结构、元数据、已核实的有限信息以及待补事实。没有虚构有效码、排名、数值或操作路径。官方来源和第三方冲突见 [来源记录](../sources.md)。

| 编号 | 暂存文件 | 最终目标 |
|---|---|---|
| P01 | [码表](./codes/all-codes.mdx) | src/content/wiki/en/codes/all-codes.mdx |
| P02 | [兑换](./guides/how-to-redeem-codes.mdx) | src/content/wiki/en/guides/how-to-redeem-codes.mdx |
| P03 | [魔导书榜](./guides/grimoire-tier-list.mdx) | src/content/wiki/en/guides/grimoire-tier-list.mdx |
| P04 | [种族榜](./guides/race-tier-list.mdx) | src/content/wiki/en/guides/race-tier-list.mdx |
| P05 | [新手](./guides/beginner-guide.mdx) | src/content/wiki/en/guides/beginner-guide.mdx |
| P06 | [重抽](./guides/how-to-reroll.mdx) | src/content/wiki/en/guides/how-to-reroll.mdx |
| P07 | [Anti Magic](./items/anti-magic.mdx) | src/content/wiki/en/items/anti-magic.mdx |
| P08 | [Poison](./items/poison.mdx) | src/content/wiki/en/items/poison.mdx |
| P09 | [钓鱼](./guides/fishing-fragments.mdx) | src/content/wiki/en/guides/fishing-fragments.mdx |
| P10 | [更新](./guides/patch-notes.mdx) | src/content/wiki/en/guides/patch-notes.mdx |

## 已完成检查

- 10 份 frontmatter 均能被项目现有 yaml 依赖解析；全部明确标记草稿。
- title、description、summary 长度检查通过；summary 均为 40–60 个英文词且不超过 400 字符。
- 正文使用当前 @astrojs/mdx 所依赖的 @astrojs/markdown-satteri 编译器直接编译，10/10 通过。初次发现的 HTML 注释语法错误已改为 MDX 注释并复测。

## 尚未通过的验收

- 已通过 Astro 内容集合 schema、全站构建和开发详情检查；事实与公开内容验收仍未通过。
- 本目录历史底稿缺封面；当前 src 正文已接入 10 张原创文字封面，见 [交接](../handover.md)。实机截图、完整事实资料、公开互链与交互自测仍缺。
- 所有草稿都必须补齐证据后逐页审核；不能因为语法通过就去掉 draft: true。
