# Clover Time：面向玩家的正文与首页

状态：2026-10-10 10:51（北京时间），用户要求的公开文案调整已完成并部署至 https://clovertime.world/、https://clovertime.world/zh/。当前部署 8622d67e-54c2-49fd-8537-724a63f2d5f1，域名 active。

## 本次交付

首页中英文文案改为玩家 Wiki 和攻略入口，去除研究预览、来源备注、待核实说明；栏目介绍、空状态、FAQ 与站点摘要同步更新。10 篇文章的标题、description、summary 和正文改为直接介绍玩法、角色、魔导书、菜单、资源与成长建议。正文只保留主题插画，旧说明图含研究提示的引用撤下，素材文件保留。插画仍标识为原创概念插画，没有包装成实机截图。

公开文章没有来源列表、作者观察日志、冲突比较或未确认清单。旧全文与引用地址保存到 [内部资料档案](./evidence/editorial-source-records-20261010.json)，保留可追溯性，不属于公开页面渲染。官方 Roblox API 本轮再次读取，Beta 0.1 和功能说明保存于 [内部官方记录](./evidence/editorial-official-game-20261010.json)。

没有把缺证据的数据改写成确定结论。兑换码结构仍为空，Codes 页提供输入入口、兑换方法和资源区分；没有编造有效码、过期码或奖励。版本页改为 Beta 0.1 功能介绍，没有虚构补丁日期或平衡改动。概率、抽取消耗、配方数量、冲突的技能名称和解锁条件从正文删除。PvE 选择顺序是编辑建议，不声称实测 DPS 或亲自进入游戏。

## 构建和展示方式

源码 10 篇 draft:true、默认导出排除、隔离副本 noindex 和全站响应 noindex 保留。导出脚本不再强制或插入 Research preview 横幅，中文入口使用同一英文正文，不声明已翻译；首页和栏目显示正常攻略标题。用户本轮授权改变公开说明方式，不改变游戏事实验收状态，正式 Goal 仍 0/10。没有修改框架组件、依赖、CI、DNS 或 Git 提交／推送；GA4 G-XH7GWVG8ZK 及既有同意控制保留。

## 实际验证

- 4 套件／41 项相关测试通过；类型检查 202 文件、0 错误／警告／提示；144/144 UI 键通过，源码中文文章仍为 0。
- 默认内容／构建／9,733 内链通过，10 草稿详情排除；隔离配置／内容／构建／10,921 内链通过，上传包 385 文件。
- 22 个首页与详情静态扫描：旧研究／核实文案及出版社引用不出现，文章保留配图、GA4 和 noindex，源码导出前后哈希一致。
- 最终本地 32／线上 32 项全部通过：两个首页 × 375／768／1440，20 个中英文入口详情及 6 栏目页 HTTP 200；检查图片实际加载、手机无横向溢出、canonical 和线上 noindex。
- 中文入口实际逐字输入 Poison，搜索返回 Clover Time Poison Guide: Projectiles, Mist & Clone 和 /zh/items/poison/，没有旧 Draft 标题。

最初浏览器脚本对首页大小写和搜索 input 类型的假设有误；核对实际 CSS／DOM 后修正验收脚本，未修改网站来迁就断言。初始失败和最终结果在日志／证据中分别保留。

[完整证据](./evidence/player-copy-20261010.json)、[实际命令日志](./evidence/player-copy-20261010-validation.log)、[中文手机首页](./evidence/player-copy-20261010-home-375-zh.png)、[英文电脑首页](./evidence/player-copy-20261010-home-1440-en.png)、[Codes 正文](./evidence/player-copy-20261010-codes-all-codes.png)、[Poison 正文](./evidence/player-copy-20261010-items-poison.png)。

## 维护

文案继续在 src/locales/ 与 src/content/wiki/en/ 修改，不改组件或直接修改构建产物。更新时使用 scripts/build-research-preview.py 新目录导出，检查后上传 upload/，不拿默认 dist 覆盖在线详情。内部来源和验证缺口写入 docs/clover-time/，不重新插入玩家正文。需要回退本次文案时先核对后续更改，内部档案保留旧全文；本次开始前的 14 个文件另有 .tmp/clover-time-editorial-20261010/before/ 快照，不覆盖其他任务改动。
