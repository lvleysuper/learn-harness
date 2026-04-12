# AI编程工具 Harness/配置框架生态调研报告

> 调研日期：2026年4月12日
> 调研方法：GitHub搜索 + Web搜索 + Exa搜索

---

## 一、框架全景对比表

| # | 框架名称 | GitHub仓库 | Stars | 核心问题 | 核心功能 | 适用工具范围 |
|---|---------|-----------|-------|---------|---------|------------|
| 1 | **Everything Claude Code (ECC)** | `affaan-m/everything-claude-code` | ~149.4K | AI编程Agent缺乏系统化的技能、本能、记忆和安全机制 | 156+ Skills、27 Agents、33 Commands、交互式安装器、记忆系统、安全审查 | Claude Code / Codex / OpenCode / Cursor（多工具） |
| 2 | **Superpowers** | `obra/superpowers` | ~147.6K | AI编程Agent缺乏结构化的开发工作流和可组合的技能体系 | TDD、异步测试、反模式检测、计划-执行工作流、brainstorm、code review | Claude Code / Cursor / Codex / OpenCode / Gemini（14+ Agent） |
| 3 | **Spec Kit** | `github/spec-kit` | ~71K | "氛围编程"(vibe coding)不可靠，需要结构化规范驱动开发 | Plan-Specify-Implement工作流、富Markdown查看器、CLI、模板、版本控制规范 | GitHub Copilot / Claude Code / Gemini CLI（多工具） |
| 4 | **gstack** | `garrytan/gstack` | ~66.9K | Claude Code作为通用助手缺乏专业化角色分工 | 23个专业化工具（CEO、设计师、工程经理、发布经理、文档工程师、QA等） | 仅 Claude Code |
| 5 | **Get Shit Done (GSD)** | `gsd-build/get-shit-done` | ~49.2K | AI编程过程中"上下文腐化"(context rot)导致质量下降 | 元提示(meta-prompting)、上下文工程、规范驱动开发、防上下文腐化 | Claude Code / OpenCode / Copilot / Codex（多工具） |
| 6 | **OpenSpec** | `Fission-AI/OpenSpec` | ~38.7K | AI编程助手在需求仅存在于聊天历史时行为不可预测 | 轻量级规范层、artifact-guided工作流、proposal-spec-design-tasks分层 | 20+ AI编程工具（Claude Code、Cursor、Windsurf等） |
| 7 | **Awesome Claude Code** | `hesreallyhim/awesome-claude-code` | ~38K | 社区缺乏统一的高质量Claude Code资源索引 | 精选列表：Skills、Hooks、Slash Commands、Agent Orchestrators、Plugins | 仅 Claude Code 生态 |
| 8 | **oh-my-claudecode (OMC)** | `Yeachan-Heo/oh-my-claudecode` | ~26.5K | Claude Code缺乏团队级多Agent编排和零配置体验 | 19个专业Agent、Team模式（staged pipeline）、tmux CLI workers、Autopilot/Ralph/Ultrawork模式、技能学习、HUD监控、通知系统 | Claude Code / Codex / Gemini CLI / OpenCode（多工具） |
| 9 | **Claude Plugins Official** | `anthropics/claude-plugins-official` | ~16.7K | 缺乏官方管理的插件质量标准和分发渠道 | Anthropic官方管理的插件目录、30+官方插件（LSP、code review、security等） | 仅 Claude Code |
| 9 | **Claude Code Templates** | `davila7/claude-code-templates` | ~20K | 配置Claude Code需要从零开始，缺乏即用型模板 | CLI工具：AI Agent、Custom Commands、Settings、Hooks、MCP集成模板 | 仅 Claude Code |
| 10 | **Trail of Bits Config** | `trailofbits/claude-code-config` | ~1.8K | 安全场景下Claude Code缺乏沙箱化、权限管理和最佳实践 | 沙箱配置、权限管理、安全审计Skills、MCP Server配置、开发容器 | 仅 Claude Code |
| 11 | **Jarrod Watts Config** | `jarrodwatts/claude-code-config` | ~1K | 缺乏个人配置的最佳实践参考 | Rules（路径范围指令）、Skills、Agents、Commands、Hooks完整示例 | 仅 Claude Code |
| 12 | **feiskyer/claude-code-settings** | `feiskyer/claude-code-settings` | N/A | 多模型后端接入Claude Code的配置复杂 | LiteLLM/OpenRouter/SiliconFlow/GitHub Copilot模型网关配置、Spec-Kit Skill | 仅 Claude Code（但支持多模型后端） |
| 13 | **ChrisWiles Showcase** | `ChrisWiles/claude-code-showcase` | ~1.2K+ | 缺乏完整的项目级Claude Code配置范例 | 完整项目配置示例：Hooks、Skills、Agents、Commands、GitHub Actions | 仅 Claude Code |
| 14 | **Claude Code官方配置系统** | 内置于 `anthropics/claude-code` (~84.6K) | N/A（内置） | AI编程工具需要可配置的指令、行为控制和扩展机制 | CLAUDE.md、settings.json、Hooks、Skills(SKILL.md)、Agents、Commands、Plugins、MCP | 仅 Claude Code |

---

## 二、按功能域的分层分类

### 第1层：基础设施层（Infrastructure）

这些框架提供AI编程工具的**基础配置机制和标准**，是其他所有框架运行的根基。

| 框架 | 定位 |
|------|------|
| **Claude Code官方配置系统** | 定义了CLAUDE.md、settings.json、Hooks、Skills、Agents、Commands、Plugins、MCP等核心机制 |
| **Claude Plugins Official** | Anthropic官方管理的插件分发和质量标准，定义了插件结构规范 |
| **Claude Code Templates** | CLI工具，提供即用型配置模板，降低配置门槛 |

### 第2层：规范与上下文管理层（Specification & Context）

这些框架解决**"AI应该做什么"**的问题，通过结构化规范确保AI行为可预测。

| 框架 | 定位 |
|------|------|
| **Spec Kit**（GitHub官方） | 规范驱动开发(SDD)工具包，Plan-Specify-Implement工作流 |
| **OpenSpec**（Fission-AI） | 轻量级规范框架，artifact-guided工作流，支持20+工具 |
| **Get Shit Done (GSD)** | 元提示+上下文工程，解决"上下文腐化"问题 |

### 第3层：技能与工作流层（Skills & Workflows）

这些框架提供**"AI如何做得更好"**的具体技能包和工作流模板。

| 框架 | 定位 |
|------|------|
| **oh-my-claudecode (OMC)** | Teams-first多Agent编排平台（19专业Agent、Team staged pipeline、tmux CLI workers、技能学习、HUD监控） |
| **Superpowers** | 完整的软件工程工作流技能库（TDD、调试、协作、计划执行） |
| **Everything Claude Code (ECC)** | 最大的技能生态（156+ Skills、27 Agents），含记忆和安全系统 |
| **gstack** | YC总裁Garry Tan的工作流，23个专业化角色技能 |

### 第4层：参考与索引层（Reference & Curation）

这些框架不直接提供功能，而是**索引和指引**整个生态。

| 框架 | 定位 |
|------|------|
| **Awesome Claude Code** | 社区精选资源列表，索引Skills、Hooks、Plugins |
| **feiskyer/claude-code-settings** | 多模型后端配置参考 |
| **Trail of Bits Config** | 安全领域最佳实践参考 |
| **ChrisWiles Showcase** | 完整项目配置范例 |
| **Jarrod Watts Config** | 个人配置最佳实践参考 |

---

## 三、框架之间的配合关系图

```
┌─────────────────────────────────────────────────────────────┐
│                    官方基础设施层                              │
│  ┌──────────────────┐    ┌────────────────────────────┐     │
│  │ Claude Code       │    │ Claude Plugins Official     │     │
│  │ 官方配置系统       │    │ (anthropics)                │     │
│  │ CLAUDE.md/Hooks/  │    │ 官方插件分发目录              │     │
│  │ Skills/Commands   │    │                             │     │
│  └────────┬─────────┘    └──────────┬─────────────────┘     │
│           │                          │                       │
└───────────┼──────────────────────────┼───────────────────────┘
            │                          │
            ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    规范与上下文管理层                          │
│                                                              │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ Spec Kit     │  │ OpenSpec      │  │ Get Shit Done     │  │
│  │ (GitHub官方) │◄─┤ (Fission-AI)  │  │ (GSD)             │  │
│  │ SDD工具包    │  │ 轻量SDD框架   │  │ 元提示+上下文工程  │  │
│  └──────┬──────┘  └──────┬───────┘  └────────┬──────────┘  │
│         │ 互为替代         │ 互为替代           │              │
└─────────┼─────────────────┼───────────────────┼──────────────┘
          │                 │                   │
          ▼                 ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│                    技能与工作流层                              │
│                                                              │
│  ┌───────────────────┐  ┌────────────────┐  ┌──────────────────────┐
│  │ Superpowers        │  │ ECC             │  │ oh-my-claudecode     │
│  │ (obra)             │  │ (affaan-m)      │  │ (Yeachan-Heo)        │
│  │ 软件工程工作流      │  │ 最大技能生态     │  │ 多Agent编排平台       │
│  │ TDD/计划执行        │  │ 156+ Skills     │  │ Team/Autopilot/Ralph │
│  └─────────┬─────────┘  └────────┬────────┘  └──────────┬───────────┘
│            │ 可共存/互补          │ 可共存/互补               │
│            │                      │                          │
│  ┌─────────┴──────────────────────┴────────┐                │
│  │ gstack (garrytan)                       │                │
│  │ 角色化工作流（CEO/设计师/工程经理/QA等）  │                │
│  └─────────────────────────────────────────┘                │
│                                                              │
└──────────────────────────────────────────────────────────────┘
          ▲
          │ 参考引用
┌─────────┴──────────────────────────────────────────────────┐
│                    参考与索引层                               │
│                                                              │
│  ┌──────────────────────┐  ┌──────────────────────────┐    │
│  │ Awesome Claude Code  │  │ Trail of Bits Config     │    │
│  │ (hesreallyhim)       │  │ 安全最佳实践参考           │    │
│  │ 社区精选资源列表       │  └──────────────────────────┘    │
│  └──────────────────────┘  ┌──────────────────────────┐    │
│  ┌──────────────────────┐  │ ChrisWiles Showcase      │    │
│  │ davila7 Templates    │  │ 完整项目配置范例           │    │
│  │ CLI配置模板工具       │  └──────────────────────────┘    │
│  └──────────────────────┘  ┌──────────────────────────┐    │
│  ┌──────────────────────┐  │ Jarrod Watts Config      │    │
│  │ feiskyer Settings    │  │ 个人配置参考              │    │
│  │ 多模型后端配置        │  └──────────────────────────┘    │
│  └──────────────────────┘                                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 关键关系说明

1. **互补关系**：
   - **Superpowers + ECC**：Superpowers侧重软件工程工作流（TDD、计划执行），ECC侧重广泛技能覆盖（156+ Skills）+ 安全/记忆系统。两者可同时安装。
   - **GSD + Superpowers/ECC**：GSD解决上下文管理层的问题（防腐化），Superpowers/ECC提供具体执行技能，天然互补。
   - **OpenSpec/Spec Kit + 任意技能包**：规范层定义"做什么"，技能层决定"怎么做"，完全互补。
   - **gstack + 任意框架**：gstack的角色化视角是独特维度，可以与其他技能框架叠加使用。

2. **替代关系**：
   - **OpenSpec vs Spec Kit**：同为规范驱动开发工具，但OpenSpec更轻量（"fluid not rigid"），Spec Kit更结构化（GitHub官方出品）。根据团队偏好二选一。
   - **ECC vs Superpowers**：在"全功能技能包"定位上有部分重叠，但理念不同——ECC追求广度（156+技能），Superpowers追求深度（完整工程方法论）。

3. **依赖关系**：
   - 所有技能框架都依赖 **Claude Code官方配置系统** 提供的 CLAUDE.md、Skills、Hooks 等基础机制。
   - **Claude Plugins Official** 是 Superpowers 等插件的官方分发渠道。
   - **Awesome Claude Code** 索引了所有其他框架的信息。

---

## 四、推荐的组合方案

### 方案A：个人开发者极速方案（推荐新手）

> 目标：快速上手，获得最大生产力提升

| 组件 | 选择 | 理由 |
|------|------|------|
| 技能包 | **Superpowers** (官方插件市场一键安装) | 安装最简单，20+核心技能，覆盖日常开发 |
| 配置参考 | **Jarrod Watts Config** | fork后修改即可，完整的个人配置模板 |
| 工具范围 | 仅 Claude Code | 降低复杂度 |

**安装步骤**：
```bash
/plugin install superpowers@claude-plugins-official
```

### 方案B：专业开发者全栈方案（推荐进阶用户）

> 目标：系统化工作流 + 规范驱动 + 多工具支持

| 组件 | 选择 | 理由 |
|------|------|------|
| 编排层 | **oh-my-claudecode (OMC)** | Teams-first多Agent编排，19专业Agent，零配置上手 |
| 规范层 | **OpenSpec** | 轻量灵活，支持20+工具，MIT开源 |
| 上下文管理 | **Get Shit Done (GSD)** | 解决长会话中的上下文腐化问题 |
| 技能包 | **ECC** | 156+技能覆盖各种场景，含记忆和安全系统 |
| 角色化 | **gstack**（可选） | 需要多角色协作时使用 |
| 工具范围 | Claude Code + OpenCode + Codex + Gemini CLI | 跨工具保持一致工作流 |

### 方案C：团队/企业方案（推荐组织）

> 目标：标准化、可审计、安全可控

| 组件 | 选择 | 理由 |
|------|------|------|
| 编排层 | **oh-my-claudecode (OMC)** | Team模式天然适合团队协作，tmux workers支持多Agent并行 |
| 规范层 | **Spec Kit**（GitHub官方） | 与GitHub生态深度集成，企业级支持 |
| 安全基线 | **Trail of Bits Config** | 安全审计沙箱化配置，权限管理最佳实践 |
| 插件管理 | **Claude Plugins Official** | 官方质量保证，可审计的插件来源 |
| 模板分发 | **Claude Code Templates** | CLI工具，团队统一配置分发 |
| 工具范围 | Claude Code + GitHub Copilot | 企业主流工具链 |

### 方案D：安全敏感场景方案（推荐安全团队）

> 目标：安全第一、沙箱化、可审计

| 组件 | 选择 | 理由 |
|------|------|------|
| 安全配置 | **Trail of Bits Config** | 专业安全团队出品，沙箱化+权限管理 |
| 规范层 | **OpenSpec** 或 **Spec Kit** | 结构化需求减少安全漏洞 |
| 技能包 | **ECC**（仅选用安全相关Skills） | 精选安全审计相关技能 |
| 工具范围 | 仅 Claude Code（沙箱模式） | 最小攻击面 |

---

## 五、关键发现与趋势分析

### 5.1 生态热度排行（按GitHub Stars）

| 排名 | 项目 | Stars | 增长速度 |
|------|------|-------|---------|
| 1 | Everything Claude Code | ~149.4K | 极快（Anthropic Hackathon获奖项目） |
| 2 | Superpowers | ~147.6K | 极快（2天+3.1K stars） |
| 3 | Spec Kit (GitHub官方) | ~71K | 极快（首周16K+ stars） |
| 4 | gstack | ~66.9K | 极快（48小时9.7K stars，YC总裁背书） |
| 5 | Get Shit Done | ~49.2K | 快速 |
| 6 | OpenSpec | ~38.7K | 快速（"most loved spec framework"） |
| 7 | Awesome Claude Code | ~38K | 稳定增长 |
| 8 | oh-my-claudecode | ~26.5K | 极快（90+贡献者，212个release） |

### 5.2 核心趋势

1. **规范驱动开发(SDD)成为共识**：Spec Kit、OpenSpec、GSD三个独立项目都聚焦于"先定义规范再写代码"，标志着AI编程从"氛围编程"走向工程化。

2. **技能生态系统化**：ECC（156+ Skills）和Superpowers代表了技能的两条路线——广度优先 vs 深度优先，说明市场在探索最优的技能组织方式。

3. **多工具支持成为标配**：Superpowers支持14+工具、OpenSpec支持20+工具、GSD支持多CLI，说明AI编程工具的配置正在走向跨工具标准化。

4. **角色化/团队化**：gstack的"CEO+设计师+工程经理"模式和ECC的"Agent"概念代表了AI编程从单人助手向虚拟团队演进的趋势。

5. **安全性意识提升**：Trail of Bits Config的出现（安全审计公司出品）表明AI编程工具的安全配置需求正在被严肃对待。

6. **Anthropic官方生态成型**：Claude Code官方配置系统 + Claude Plugins Official + 内置30+插件，形成了完整的官方基础设施。

### 5.3 oh-my-claudecode 补充说明

**oh-my-claudecode (OMC)** 是一个重要的编排框架，由 Yeachan-Heo 开发（~26.5K Stars）：

- **定位**：Teams-first Multi-agent orchestration，类似 oh-my-zsh 对 zsh 的角色
- **核心能力**：19个专业Agent、Team模式（staged pipeline: plan→prd→exec→verify→fix）、tmux CLI workers（支持Claude/Codex/Gemini并行）
- **编排模式**：Autopilot（自主执行）、Ralph（持久验证循环）、Ultrawork（最大并行）、Deep Interview（苏格拉底式需求澄清）
- **特色功能**：HUD状态栏实时监控、技能自动学习与注入、通知集成（Telegram/Discord/Slack）、OpenClaw网关集成
- **工具范围**：Claude Code / OpenCode / Codex / Gemini CLI，真正跨工具
- **npm包名**：`oh-my-claude-sisyphus`（注意：包名与项目名不同）

**与其他框架的关系**：
- OMC vs Superpowers：OMC侧重**多Agent编排和团队协作**，Superpowers侧重**软件工程方法论**（TDD、计划执行）。可共存互补。
- OMC vs ECC：OMC侧重**编排调度**，ECC侧重**技能广度**（156+ Skills）。可共存互补。
- OMC vs gstack：OMC提供更完整的**技术实现**（tmux workers、staged pipeline），gstack提供更轻量的**角色化视角**。

---

## 六、参考来源

- [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [obra/superpowers](https://github.com/obra/superpowers)
- [github/spec-kit](https://github.com/github/spec-kit)
- [garrytan/gstack](https://github.com/garrytan/gstack)
- [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)
- [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
- [trailofbits/claude-code-config](https://github.com/trailofbits/claude-code-config)
- [jarrodwatts/claude-code-config](https://github.com/jarrodwatts/claude-code-config)
- [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings)
- [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase)
- [Claude Code官方文档](https://code.claude.com/docs/en/overview)
- [Anthropic - The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
