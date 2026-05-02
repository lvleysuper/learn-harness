# AI编程工具对比与选型指南

> 调研日期：2026年4月12日
> 数据来源：arena.ai Code Leaderboard、SWE-bench Verified/Pro、LiveCodeBench、Terminal-Bench、多源专业评测、GitHub、官方文档
> 覆盖范围：15+ 主流AI编程工具（含开源/闭源、国际/国内）、60+ 编码模型

---

## 一、工具与模型能力评估方式

### 1.1 核心概念：工具 vs 模型

AI编程能力由两个独立维度共同决定：

- **工具（Agent/Scaffold）**：完整的AI编程工具——包含模型接入、工具集成、工作流编排、配置系统。例如 Cursor、Claude Code、Aider。
- **模型（LLM）**：底层大语言模型的编码能力——在标准化基准测试中的客观表现。例如 Claude Opus 4.6、GPT-5.4、GLM-5。

> **关键洞察：Harness比模型更重要。** SWE-bench数据显示，同一模型（Claude Sonnet 4.5）在不同scaffold下差距达 **22分**，而不同模型在相同scaffold下差距仅 **1-3分**。工具的选择远比模型的选择影响更大。

### 1.2 评估基准体系

| 基准名称 | 类型 | 评估对象 | 方法论 | 权威性 |
|----------|------|----------|--------|--------|
| **Arena.ai Code Elo** | 人类偏好 | 模型 | 盲测对决 + Elo评分，231K+ votes | 最高（真人实测） |
| **SWE-bench Verified** | 客观基准 | Agent+Scaffold | 真实GitHub issue自动生成patch并验证 | 行业金标准 |
| **SWE-bench Pro** | 客观基准 | Agent+Scaffold | 更难更干净的测试集，避免数据污染 | 进阶金标准 |
| **LiveCodeBench** | 客观基准 | 模型 | 竞赛编程题目，持续更新防污染 | 高 |
| **Terminal-Bench** | 客观基准 | Agent | 终端环境中的多步骤任务 | 高 |
| **多源专业评测** | 综合评估 | 工具 | NxCode/YBuild/ProPicked等独立评测平台 | 中高 |

### 1.3 评估维度说明

- **Arena.ai Code Elo**：衡量模型的编码偏好度——用户在盲测中更偏好哪个模型的代码输出。数据量最大、最贴近真实体验。
- **SWE-bench**：衡量Agent的端到端问题解决能力——不仅看模型，还看工具的编排、上下文管理、测试验证等综合能力。
- **专业评测排名**：综合考量IDE体验、补全质量、Agent能力、价格等多维度。

---

## 二、工具排行榜

### 2.1 综合 TOP 10

| 排名 | 工具 | 类型 | 开源/商业 | 底层模型 | GitHub Stars | 起步价 | 综合评分 |
|------|------|------|-----------|----------|-------------|--------|----------|
| 1 | **Claude Code** | CLI Agent | 商业 | Claude Opus/Sonnet 4.5/4.6 | N/A | $20/月 (Pro) | 9.2/10 |
| 1 | **Cursor** | AI原生IDE | 商业 | 多模型 (Claude/GPT/Gemini) | N/A | $20/月 | 9.2/10 |
| 3 | **Aider** | CLI | 开源 (Apache 2.0) | 75+ 模型 (BYOK) | 43K+ | 免费 (BYOK) | 8.9/10 |
| 4 | **OpenCode** | CLI/Desktop/IDE | 开源 (MIT) | 75+ 模型 (BYOK) | 112K+ | 免费 (BYOK) | 8.8/10 |
| 5 | **GitHub Copilot** | IDE插件 | 商业 | GPT-5.2/Claude/Gemini | N/A | $10/月 | 8.7/10 |
| 6 | **Windsurf** | AI原生IDE | 商业 | Claude/GPT/SWE自有 | N/A | 免费/$15/月 | 8.5/10 |
| 7 | **Cline** | VS Code插件 | 开源 | 多模型 (BYOK) | 58K+ | 免费 (BYOK) | 8.4/10 |
| 8 | **Augment Code** | IDE+CLI+平台 | 商业 | 多模型智能路由 | N/A | $20/月 | 8.3/10 |
| 9 | **Amazon Q Developer** | IDE插件 | 商业 | 自有模型 | N/A | 免费/$19/用户/月 | 8.1/10 |
| 10 | **Kiro** (AWS) | AI原生IDE | 商业 | Claude Sonnet 4.5 | 1.8K+ | $20/月 | 7.5/10 |

> **排名说明**：Claude Code 和 Cursor 并列第一，分别在终端和IDE领域各具绝对优势。Claude Code 拥有 SWE-bench 80.9% 行业最高分、NxCode #1、Pragmatic Engineer 2026调查"最常用AI编码工具"；Cursor 拥有最佳IDE体验、Tab补全72%接受率、多数IDE评测排名第一。

### 2.2 多源评测交叉验证

| 评测来源 | #1 | #2 | #3 | #4 |
|----------|----|----|-----|-----|
| NxCode (2026) | **Claude Code** | Cursor | Copilot | - |
| AIMadeTools (2026) | Cursor | **Claude Code** | Copilot | - |
| AI Tool Clash (2026实测) | **Claude Code** (9.0质量) | Cursor (8.5) | Windsurf (8.0) | Copilot (7.0) |
| AIToolChaser (2026) | Cursor (4.8) | **Claude Code** (4.7) | Copilot (4.6) | Windsurf (4.4) |
| AIToolVs (2026) | Cursor (4.7) | **Claude Code** (4.7) | Windsurf (4.5) | Copilot (4.4) |
| YBuild (2026) | Cursor (9.2) | **Claude Code** (9.0) | Windsurf (8.5) | Copilot (8.3) |
| OpenAIToolsHub (2026) | **Claude Code** (~80%) | Augment (~80%) | Aider (~72%) | Cursor (~65%) |
| MightyBot (2026) | - | - | **OpenCode** (#3) | - |
| Pragmatic Engineer (2026调查) | **Claude Code** (最常用) | - | - | - |

> **共识**：Claude Code 和 Cursor 在所有权威评测中均为 TOP 2，差距极小。Claude Code 在客观基准（SWE-bench）和终端场景中胜出；Cursor 在IDE体验和日常开发中胜出。OpenCode 在开源领域增长最快（112K+ Stars，2.5M月活开发者）。

### 2.3 核心工具详细能力对比

| 维度 | Claude Code | Cursor | GitHub Copilot | OpenCode | Aider | Windsurf | Cline | Augment Code | Kiro |
|------|-------------|--------|----------------|----------|-------|----------|-------|--------------|------|
| **代码补全** | N/A | 极佳 (72%接受率) | 极佳 | N/A | N/A | 良好 | 良好 | 良好 (<100ms) | 良好 |
| **多文件编辑** | 极佳 | 极佳 (Composer) | 良好 | 良好 | 良好 | 极佳 (Cascade) | 良好 | 极佳 | 良好 |
| **Agent自主性** | 最佳 (80.9%) | 极佳 | 良好 | 良好 | 良好 | 极佳 | 良好 | 良好 | 良好 |
| **模型灵活性** | 仅Claude | 多模型 | 多模型 | 75+提供商 | 75+提供商 | 有限 | 多模型 | 智能路由 | 仅Claude Sonnet |
| **上下文窗口** | 200K-1M | 最高1M | 128K-1M | 依模型 | 依模型 | 最高128K | 依模型 | 全代码库 | 200K |
| **Git集成** | 基础 | 良好 | GitHub深度 | 基础 | 最佳(自动commit) | 良好 | 基础 | GitHub深度 | 良好 |

### 2.4 核心工具简介

**Cursor** — 最佳全能型 AI IDE。VS Code无缝迁移，Tab补全72%接受率领先，Composer多文件编辑+Agent模式，多模型自由切换。100万+用户。劣势：需切换IDE，$20/月起。

**Claude Code** — 最强自主编码工具（CLI）。SWE-bench 80.9%行业最高，NxCode 2026 #1，Pragmatic Engineer调查"最常用AI编码工具"，AI Tool Clash实测评分最高（9.0/10质量，23分钟完成 vs Cursor 47分钟）。1M上下文，四层配置系统（CLAUDE.md/Rules/Skills/Subagents），15+事件Hooks。劣势：仅限Claude模型，无GUI。

**Aider** — 最成熟的Git原生CLI。43K+ Stars，每次AI编辑自动commit可回溯，Architect/Editor双模式，支持DeepSeek等廉价模型（低至$0.07/百万token）。劣势：无GUI，无实时代码补全。

**GitHub Copilot** — 行业标准。68%开发者使用率，最广IDE支持（VS Code/JetBrains/Neovim/Xcode），$10/月最低入门价，GitHub生态深度集成。劣势：Agent能力不如Claude Code/Cursor深。

**OpenCode** — 最大开源AI编程工具生态。112K+ Stars（开源工具最高），2.5M月活开发者，增长速度4.5倍于Claude Code。MIT协议，75+ LLM提供商，终端+桌面+VS Code三种形态，MightyBot 2026排名#3。完全免费零锁定。劣势：Agent自主性略逊Claude Code/Aider。

**Windsurf** — 最佳性价比Agentic IDE。Cascade引擎最流畅工作流，免费层含无限补全，被Cognition AI收购。劣势：不支持VS Code Remote Dev。

**Augment Code** — 企业级大规模代码库平台。Context Engine实时索引400K+文件，ISO 42001认证（首家），智能模型路由。劣势：初始索引耗时。

**Kiro** — 规格驱动AI IDE（AWS）。三阶段工作流（Requirements→Design→Implementation），Agent Hooks事件驱动自动化，AWS深度集成。劣势：公开预览阶段，AWS绑定较深。

---

## 三、模型排行榜

### 3.1 Code Arena TOP 10（人类偏好Elo）

> 数据来源：[arena.ai Code Leaderboard](https://arena.ai/leaderboard/code)
> 投票量：231,158 votes（截至2026年4月9日）
> 方法论：盲测对决 + Elo评分，基于真实agentic编码任务（多步推理+工具使用）
> 注意：Arena Elo 是人类偏好指标，与 SWE-bench 等客观基准可能存在偏差。投票量少的模型置信区间较宽。

| 排名 | 模型 | 开发者 | Code Elo | 投票数 | SWE-bench | 许可协议 | 价格 (输入/输出 per 1M) |
|------|------|--------|----------|--------|-----------|----------|------|
| 1 | **Claude Opus 4.6 (Thinking)** | Anthropic | ~1560 | 2,766 | - | 闭源 | $5 / $25 |
| 2 | **Claude Opus 4.6** | Anthropic | ~1553 | 2,115 | - | 闭源 | $5 / $25 |
| 3 | **Claude Sonnet 4.6** | Anthropic | ~1533 | 1,675 | - | 闭源 | $3 / $15 |
| 4 | **Claude Opus 4.5 (Thinking 32K)** | Anthropic | ~1499 | 11,032 | - | 闭源 | $5 / $25 |
| 5 | **GPT-5.4 High** | OpenAI | ~1471 | 1,696 | - | 闭源 | - |
| 6 | **Claude Opus 4.5** | Anthropic | ~1470 | 11,113 | - | 闭源 | $5 / $25 |
| 7 | **Gemini 3.1 Pro Preview** | Google | ~1461 | 1,826 | - | 闭源 | - |
| 8 | **MiniMax M2.7** | MiniMax | ~1452 | 2,520 | - | 闭源 | $0.30 / $1.20 |
| 9 | **GLM-5** | 智谱AI | ~1444 | 16,948 | **72.80%** | **MIT (开源)** | $1 / $3.20 |
| 10 | **GLM-4.7** | 智谱AI | ~1440 | 12,778 | - | **MIT (开源)** | $0.39 / $1.75 |

**关键发现**：
- Anthropic **包揽前4名**，编码领域具有压倒性优势
- **GLM-5 的 Arena Elo 与 MiniMax M2.7 仅差 8 分**（1444 vs 1452），但 GLM-5 投票量是 M2.7 的 6.7 倍（16,948 vs 2,520），统计置信度更高。两者置信区间高度重叠
- GLM-5 在 SWE-bench Verified 上得分 **72.80%**，与 GPT-5-2 并列，**高于 Claude Sonnet 4.5 (71.4%)**，是开源模型中的客观编码能力最强者
- GLM-5 和 GLM-4.7 是 TOP 10 中**仅有的开源模型**（MIT协议）

### 3.2 SWE-bench Verified TOP 10（Agent + 模型客观基准）

> 数据来源：[SWE-bench Verified Leaderboard](https://www.swebench.com/)
> 方法论：在真实GitHub issue上自动生成patch并验证，行业金标准
> 注意：Agent排名测量的是scaffold+模型的综合能力；模型排名测量纯模型能力（无scaffold辅助）

**Agent/Scaffold 排名**：

| 排名 | Agent/Scaffold | 底层模型 | SWE-bench Verified |
|------|---------------|----------|-------------------|
| 1 | **Claude Code** | Claude Opus 4.5/4.6 | **80.9%** |
| 2 | **Augment Code (SWE Pro)** | 多模型路由 | ~78-82% |
| 3 | **Amazon Q Developer Agent** | Amazon Q | 70.6% |
| 4 | **OpenAI Codex** | GPT-5.4 | 68.5% |
| 5 | **Aider** | Claude Sonnet 4.5 | ~72% |

**纯模型排名**（独立于工具）：

| 排名 | 模型 | 开发者 | SWE-bench Verified | 许可协议 |
|------|------|--------|-------------------|----------|
| 1 | Claude Opus 4.6 (Thinking) | Anthropic | ~80%+ | 闭源 |
| 2 | GPT-5-2 | OpenAI | 72.80% | 闭源 |
| 2 | **GLM-5 (high reasoning)** | 智谱AI | **72.80%** | **MIT (开源)** |
| 4 | GPT 5.2 Codex | OpenAI | 72.80% | 闭源 |
| 5 | Claude Sonnet 4.5 | Anthropic | 71.4% | 闭源 |
| 6 | Kimi K2.5 | 月之暗面 | 70.8% | - |

> GLM-5 在纯模型 SWE-bench 排名中与 GPT-5-2 并列第二，远超 Arena Elo 排名（#9）所暗示的位置。这说明 Arena 的人类偏好投票与客观编码能力存在差异——GLM-5 的代码生成质量很高，但在盲测偏好中可能因输出风格等因素被低估。

### 3.3 开源模型 Code Arena TOP 10

> 数据来源：[arena.ai Code Leaderboard (Open Source)](https://arena.ai/leaderboard/code?license=open-source)

| 排名 | 模型 | 开发者 | Code Elo | 许可协议 | 价格 (per 1M) |
|------|------|--------|----------|----------|------|
| 1 | **GLM-5** | 智谱AI | 1441 | MIT | $1 / $3.20 |
| 2 | **GLM-4.7** | 智谱AI | 1439 | MIT | $0.39 / $1.75 |
| 3 | **Kimi-K2.5-Thinking** | 月之暗面 | 1391 | - | - |
| 4 | **Qwen3.5-397B-A17B** | 阿里巴巴 | 1386 | Apache 2.0 | $0.12 / $0.99 |
| 5 | **Qwen3.5-235B-A35B** | 阿里巴巴 | ~1362 | Apache 2.0 | - |
| 6 | **GLM-4.6** | 智谱AI | 1354 | MIT | $0.39 / $2.34 |
| 7 | **DeepSeek-R1** | DeepSeek | 1327 | MIT | $0.26 / $0.38 |
| 8 | **MiniMax-M2** | MiniMax | 1303 | Apache 2.0 | - |
| 9 | **Qwen3-Coder-480B** | 阿里巴巴 | 1280 | Apache 2.0 | - |
| 10 | **Devstral** | Mistral | ~1221 | Apache 2.0 | - |

**关键发现**：中国模型在开源编码领域占主导——TOP 8中6席为中国团队出品（智谱、月之暗面、阿里、DeepSeek、MiniMax）。

### 3.4 TOP 5 模型综合能力对比

| 模型 | Code Elo | SWE-bench (纯模型) | 性价比 | 中文能力 | 综合推荐 |
|------|----------|-------------------|--------|----------|----------|
| **Claude Opus 4.6** | ★★★★★ (1560) | ★★★★★ (~80%+) | ★★★ | ★★★★ | **编码首选** |
| **Claude Sonnet 4.6** | ★★★★★ (1533) | ★★★★ | ★★★★ | ★★★★ | **性价比首选** |
| **GLM-5** (开源) | ★★★★ (1444) | ★★★★★ (**72.80%**) | ★★★★★ | ★★★★★ | **开源首选 / SWE-bench并列第二 / 中文最佳** |
| **GPT-5.4 High** | ★★★★ (1471) | ★★★★ (68.5% w/ Codex) | ★★★ | ★★★★ | **GPT生态首选** |
| **Gemini 3.1 Pro** | ★★★★ (1461) | ★★★ | ★★★★ | ★★★ | **Google生态首选** |

> **GLM-5 说明**：Arena Elo 排名 #9（1444），但 SWE-bench Verified **72.80%** 与 GPT-5-2 并列第二，高于 Claude Sonnet 4.5（71.4%）。Arena 偏好投票与客观编码能力存在差异，建议综合两个维度评估。GLM-5 是目前开源模型中编码客观能力最强者，且 MIT 协议 + $1/$3.20 价格具有极高性价比。

---

## 四、按场景选择建议

### 4.1 场景决策矩阵

| 场景 | 首选 | 备选 | 理由 |
|------|------|------|------|
| **日常IDE开发** | Cursor Pro | GitHub Copilot | 最佳IDE体验 + Tab补全 |
| **终端/CLI** | Claude Code | Aider | 最强自主能力 / 最佳Git集成 |
| **预算有限** | Aider + DeepSeek | OpenCode | 月成本$1，完全开源 |
| **企业团队** | Copilot Enterprise | Augment Code | 最广IDE支持+合规 / 大型代码库 |
| **大型代码库(100K+文件)** | Augment Code | Claude Code | 400K+文件索引 / 1M上下文 |
| **全自主任务** | Devin | OpenAI Codex | 端到端自主 / 后台并行 |
| **前端/可视化** | Windsurf | Cursor | Cascade实时预览 / 最佳补全 |
| **AWS/云原生** | Kiro + Amazon Q | - | 规格驱动+AWS深度集成 |
| **开源/零锁定** | OpenCode / Aider | Continue.dev | MIT/Apache 2.0 协议 |
| **安全合规** | Tabnine Enterprise | Amazon Q | 本地部署/离线 / AWS安全 |
| **JetBrains用户** | GitHub Copilot | Augment Code | 最完整JetBrains支持 |

### 4.2 黄金组合推荐

**方案A：能力最大化 ($40/月)**
- **Cursor Pro** ($20/月) — 日常编辑、补全、多文件工作
- **Claude Code** ($20/月 Claude Pro) — 复杂重构、架构决策、多步骤代理任务

**方案B：性价比最优 (~$1-5/月)**
- **Aider** (免费) + GLM-5/DeepSeek-R1 API (~$1/月) — 终端编程
- **Windsurf Free** ($0) — IDE编程

**方案C：开源全栈 ($1-3/月)**
- **OpenCode** + GLM-5 (MIT) — CLI
- **Continue.dev** + Qwen3.5 (Apache 2.0) — IDE
- **Cline** + GLM-5 (MIT) — VS Code Agent

**方案D：企业全覆盖**
- **Copilot Enterprise** ($39/用户/月) — 全员基础
- **Augment Code** — 大型代码库核心团队
- **Devin** ($500/月) — 特定自主任务

---

## 五、Harness 可配置性对比

> Harness可配置性是本项目的核心关注维度——决定了一个工具能被定制到什么程度。

### 5.1 配置系统总览

| 配置维度 | Claude Code | Cursor | GitHub Copilot | Aider | OpenCode | Windsurf | Cline | Kiro | Augment Code |
|----------|-------------|--------|----------------|-------|----------|----------|-------|------|--------------|
| **自定义指令文件** | CLAUDE.md (三层) | .cursor/rules/*.mdc | copilot-instructions.md | .aider.conf.yml | opencode.json | .windsurfrules | .clinerules | .kiro/steering/ | Instructions |
| **分层配置** | 全局/项目/子目录 | 全局/项目/文件类型 | 全局/项目 | 单文件 | 单文件 | 单文件 | 单文件 | .kiro/ 目录 | 项目级 |
| **Rules/规则系统** | 路径过滤Rules | glob+条件触发 | 有限 | 命令行参数 | 配置文件 | Memories | 有限 | Steering Files | Instructions |
| **Hooks 系统** | 15+ 事件类型 | 兼容Claude Hooks | 有限 | Git hooks | 无 | 无 | 无 | Agent Hooks | 无 |
| **自定义Commands** | Skills | Agent Skills | 无 | 无 | 无 | Workflows | Custom Prompts | 无 | Instructions |
| **MCP 支持** | 原生 | 原生 | 原生 (2025+) | 无 | 原生 | 原生 | 原生 | 原生 | Easy MCP |
| **子代理** | 自定义(配置化) | 无 | Coding Agent | Architect/Editor | 并行Agent | 无 | 无 | Subagents | Intent编排 |
| **权限控制** | 精细allow/deny/ask | 基础 | 企业策略 | 基础 | 基础 | Turbo Mode | 审批制 | Review/Auto | Auto Mode |
| **企业托管** | managed-settings | Enterprise Dashboard | Enterprise Policy | 无 | 无 | 企业RBAC | 无 | 无 | Enterprise |

### 5.2 配置能力评分

| 工具 | 自定义指令 | Rules规则 | Hooks/自动化 | MCP/工具集成 | 子代理 | 企业管控 | **综合配置分** |
|------|-----------|----------|-------------|-------------|--------|---------|--------------|
| **Claude Code** | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 | **10/10** |
| **Kiro** | 9/10 | 8/10 | 9/10 | 9/10 | 8/10 | 7/10 | **8.5/10** |
| **Cursor** | 9/10 | 9/10 | 7/10 | 8/10 | 6/10 | 8/10 | **8.0/10** |
| **Augment Code** | 8/10 | 7/10 | 6/10 | 9/10 | 9/10 | 9/10 | **8.0/10** |
| **GitHub Copilot** | 7/10 | 6/10 | 5/10 | 7/10 | 7/10 | 10/10 | **7.0/10** |
| **Windsurf** | 7/10 | 6/10 | 5/10 | 8/10 | 5/10 | 7/10 | **6.5/10** |
| **Devin** | 5/10 | 4/10 | 5/10 | 7/10 | 8/10 | 9/10 | **6.5/10** |
| **Aider** | 6/10 | 5/10 | 7/10 | 3/10 | 7/10 | 3/10 | **5.5/10** |
| **OpenCode** | 6/10 | 5/10 | 4/10 | 8/10 | 7/10 | 3/10 | **5.5/10** |
| **Cline** | 6/10 | 5/10 | 4/10 | 8/10 | 5/10 | 5/10 | **5.5/10** |

### 5.3 配置能力亮点

#### Claude Code — 配置能力之王

```
~/.claude/CLAUDE.md        # 全局：适用于所有项目
./CLAUDE.md                # 项目级：项目约定和架构
./src/CLAUDE.md            # 子目录级：模块级指令
```

- **CLAUDE.md**：三层层级（全局/项目/子目录），Markdown格式
- **Rules** (`.claude/rules/*.md`)：路径过滤，仅在处理匹配文件时激活
- **Skills** (`.claude/skills/`)：将可复用工作流封装为Slash命令
- **Hooks**（15+ 生命周期事件）：PreToolUse / PostToolUse / Stop / SessionStart 等，支持 Shell/HTTP/LLM Prompt 三种类型
- **Subagents**：内置 Explore/Plan/Code + 自定义子代理（专属提示、工具限制、模型选择）
- **MCP**：原生协议支持，企业级管控 `allowManagedMcpServersOnly`
- **权限**：精细 allow/deny/ask 规则

#### Kiro — 规格驱动的典范

- **Spec 三阶段**：Requirements (EARS) → Design → Tasks
- **Agent Hooks**：onSave / onCommit 事件触发自动化
- **Steering Files**：`.kiro/steering/` 持久化项目知识
- **Powers**：动态工具加载（AWS IaC、CDK 等）

---

## 六、市场格局总结

### 6.1 市场规模

- AI编程工具市场 2025 年年收入超过 **50亿美元**
- **85-92%** 的开发者定期使用 AI 编程工具
- GitHub Copilot 占据 **68%** 市场份额，采用最广泛
- 开源工具迅速崛起：OpenCode (112K+ Stars, 2.5M月活)、Cline (58K Stars)、Aider (43K Stars)

### 6.2 关键趋势

1. **Agentic转型完成**：所有主流工具已从"补全"转向"代理"，自主执行任务成为标配
2. **多模型成为趋势**：除Claude Code和Devin外，大部分工具支持多模型切换
3. **开源与商业分化**：OpenCode/Aider/Cline/Continue代表开源力量，Cursor/Copilot/Devin代表商业产品
4. **MCP协议标准化**：Model Context Protocol成为连接外部工具的行业标准
5. **Harness能力差异化**：Claude Code的Hooks+Skills+Subagents体系领先，Kiro的Spec+Hooks独特
6. **中国模型崛起**：GLM-5（智谱AI）SWE-bench 72.80%与GPT-5-2并列第二，是开源编码客观能力最强者；Qwen/DeepSeek/MiniMax紧随其后

---

## 七、选型建议

### 7.1 按关注维度选择

| 你的核心关注 | 推荐工具 | 理由 |
|-------------|---------|------|
| **最强编码能力** | Claude Code + Claude Opus 4.6 | SWE-bench 80.9%，Arena Elo 1560 |
| **最佳IDE体验** | Cursor | Tab补全72%，Composer多文件编辑 |
| **最低成本** | Aider/OpenCode + GLM-5 | 月费$1，MIT开源模型 |
| **最大自由度** | OpenCode | 75+模型提供商，零供应商锁定 |
| **最强Harness/配置** | Claude Code | 配置分10/10，6维满分 |
| **企业合规** | GitHub Copilot / Augment Code | 68%市场份额 / ISO 42001认证 |
| **规格驱动开发** | Kiro | EARS三阶段，Agent Hooks |
| **中文场景** | GLM-5 (模型) + Aider/OpenCode (工具) | 中文能力★★★★★，MIT开源 |

### 7.2 最终建议

> 2026年不存在"单一最佳工具"，正确选择取决于工作流、预算和团队规模。两个被广泛验证的组合：
>
> - **能力最大化**：Cursor（日常IDE）+ Claude Code（深度代理），月费 $40
> - **性价比最优**：Aider/OpenCode + GLM-5（开源MIT），月费 ~$1

---

## 附录：数据来源索引

| 数据源 | 类型 | 用途 |
|--------|------|------|
| [arena.ai Code Leaderboard](https://arena.ai/leaderboard/code) | 人类偏好Elo | 模型编码偏好排名 (231K+ votes) |
| [arena.ai Open Source](https://arena.ai/leaderboard/code?license=open-source) | 开源模型Elo | 开源模型编码排名 |
| [SWE-bench Verified](https://www.swebench.com/) | 客观基准 | Agent+模型自动修复能力 |
| [BenchLM.ai](https://benchlm.ai/models/glm-5) | 聚合基准 | GLM-5综合评分 |
| [FreeAcademy Arena Rankings](https://freeacademy.ai/blog/best-ai-tools-for-developers-lmarena) | 聚合排名 | arena.ai数据验证 |
| [Arena.ai March 2026 Blog](https://arena.ai/blog/march-2026-arena-updates/) | 官方更新 | 排名变化趋势 |
| [NxCode](https://www.nxcode.io/resources/news/best-ai-for-coding-2026-complete-ranking) | 专业评测 | 工具排名 (#1 Claude Code) |
| [AI Tool Clash](https://aitoolclash.com/posts/ai-coding-assistants-compared-2026/) | 实测对比 | Claude Code 9.0 vs Cursor 8.5 |
| [AIToolChaser](https://aitoolchaser.com/best-ai-coding-tools-2026/) | 专业评测 | 工具排名 |
| [OpenAIToolsHub](https://www.openaitoolshub.org/en/blog/ai-pair-programming-tools-compared) | 专业评测 | SWE-bench对比 |
| [AIMadeTools](https://aimadetools.com/blog/best-ai-coding-tools-2026/) | 专业评测 | 工具排名 |
| [MightyBot](https://www.mightybot.ai/blog/coding-ai-agents-for-accelerating-engineering-workflows) | 专业评测 | OpenCode #3 |
| [FailingFast](https://failingfast.io/ai-coding-guide/benchmarks/) | 基准分析 | SWE-bench模型排名 |
| [LLM Stats](https://llm-stats.com/models/glm-5) | 模型数据 | GLM-5参数 |

---

*数据截止至2026年4月。AI编程工具市场变化迅速，建议定期更新评估。*
