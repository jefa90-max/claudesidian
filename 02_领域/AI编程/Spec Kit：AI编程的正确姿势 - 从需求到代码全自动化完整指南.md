## **什么是****Spec** **Kit**

  

Spec Kit 是由 GitHub 官方开源的一个革命性工具包，它实现了**规格驱动开发（Spec-Driven Development,** **SDD****）**的理念。这是一种颠覆传统软件开发流程的方法论。

  

### **传统开发 vs 规格驱动开发**

  

**传统开发模式：**

```Plain
需求 → 编写代码 → 测试 → 调试 → 部署
（规格文档往往被丢弃，代码才是王道）
```

  

**规格驱动开发：**

```Plain
规格文档 → 可执行的规格 → 自动生成代码 → 内置测试 → 部署
（规格即代码，代码即规格）
```

  

### **Spec Kit 的突破性创新**

  

Spec Kit 将**规格文档**从传统的"脚手架"角色转变为**可执行的第一公民**。规格不再只是指导编码的参考文档，而是直接驱动代码生成的核心资产。

  

---

  

## **核心理念**

  

### **1. 规格驱动开发（****SDD****）**

  

**核心思想：** 规范即代码，代码即规范

  

- **意图优先：** 先定义"要做什么"（What），再考虑"怎么做"（How）

- **规格为王：** 规格文档成为项目的核心资产，直接生成工作代码

- **多步骤精炼：** 不是一次性从提示词生成代码，而是通过结构化流程逐步完善

  

### **2. 测试驱动开发（TDD）**

  

**强制测试先行，防止AI产生幻觉**

  

Spec Kit 内置了严格的 TDD 流程：

- ✅ 测试用例优先于实现代码
    
- ✅ 每个功能都必须有对应的测试
    
- ✅ AI 生成的代码自动包含测试覆盖
    
- ✅ 减少AI"幻觉"带来的代码质量问题
    

### **3. 结构化模板约束**

  

通过预定义的模板和检查点，确保：

- 代码质量一致性
    
- 架构设计规范性
    
- 开发流程标准化
    
- 团队协作高效性
    

---

  

## **为什么选择Spec Kit**

  

### **🚀 核心优势**

  

#### **1. 多AI支持，自由选择**

支持 10+ 主流 AI 编程助手：

- Claude Code
    
- GitHub Copilot
    
- Cursor
    
- Windsurf
    
- Gemini CLI
    
- Qwen Code
    
- opencode
    
- Codex CLI
    
- Kilo Code
    
- Auggie CLI
    
- Roo Code
    

#### **2. 效率提升数倍**

相比传统的 "Vibe Coding"（随意编码）方式：

- ⚡ 零基础小白 5 分钟开发完整应用
    
- ⚡ 企业级应用快速原型搭建
    
- ⚡ 从需求到上线全自动化流程
    

#### **3. 质量保障机制**

- 🔒 结构化模板约束AI输出
    
- 🔒 强制 TDD 确保代码质量
    
- 🔒 一致性检查防止架构偏差
    
- 🔒 自动生成测试用例
    

#### **4. 企业级支持**

- 🏢 支持组织约束（云服务商、技术栈、工程实践）
    
- 🏢 支持企业设计系统
    
- 🏢 支持合规性要求
    
- 🏢 支持不同开发方法（从 vibe-coding 到 AI-native 开发）
    

### **📊 适用场景**

  

|   |   |   |
|---|---|---|
|开发阶段|使用场景|关键活动|

| **0-to-1 开发**<br>（绿地项目） | 从零开始创建新应用 | • 生成初始代码库<br>• 建立项目结构<br>• 设定开发规范 |

| **创意探索** | 并行实现多个方案 | • 快速原型验证<br>• A/B 技术方案对比<br>• 探索最优架构 |

| **迭代增强**<br>（棕地项目） | 现有项目现代化改造 | • 功能扩展<br>• 技术栈升级<br>• 代码重构 |

  

---

  

## **环境准备与安装**

  

### **系统要求**

  

**操作系统：**

- Linux / macOS
    
- Windows（需要 WSL2）
    

**必需工具：**

```Bash
# Python 3.11+
python --version

# Git
git --version

# uv（Python 包管理工具）
curl -LsSf https://astral.sh/uv/install.sh | sh
```

  

### **安装 Spec Kit**

  

#### **方式一：全局安装（推荐）**

  

```Bash
# 安装 specify-cli 工具
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 验证安装
specify check
```

  

**优势：**

- ✅ 工具持久化安装，随处可用
    
- ✅ 自动添加到系统 PATH
    
- ✅ 更好的工具管理（`uv tool list` / `uv tool upgrade` / `uv tool uninstall`）
    
- ✅ Shell 配置更简洁
    

#### **方式二：直接运行（无需安装）**

  

```Bash
# 直接运行命令
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

  

### **检查环境**

  

```Bash
# 检查所有已安装的 AI 工具
specify check

# 输出示例：
# ✓ git found
# ✓ claude found
# ✓ cursor-agent found
# ✗ gemini not found
```

  

---

  

## **七大核心命令详解**

  

Spec Kit 的开发流程由 7 个核心命令驱动，形成一个完整的开发链条：

  

```Plain
Constitution → Specify → Clarify → Plan → Tasks → Analyze → Implement
   (铁律)      (需求)     (澄清)    (计划)  (任务)   (分析)    (实现)
```

  

### **命令 1:`/constitution` - 建立项目铁律**

  

**作用：** 创建项目的治理原则和开发指南

  

**时机：** 项目初始化的第一步

  

**示例：**

```Plain
/constitution 创建以下开发原则：
1. 代码质量：遵循 SOLID 原则，保持代码简洁可读
2. 测试标准：测试覆盖率不低于 80%，关键路径 100% 覆盖
3. 用户体验：响应式设计，支持移动端和桌面端
4. 性能要求：首屏加载时间不超过 2 秒
5. 技术债务：每个 Sprint 预留 20% 时间处理技术债务
```

  

**生成文件：** `.specify/memory/constitution.md`

  

**重要性：**

- 🎯 作为所有后续决策的"宪法"
    
- 🎯 AI 在规划和实现时会参考这些原则
    
- 🎯 确保整个开发过程的一致性
    

---

  

### **命令 2:`/specify` - 定义功能需求**

  

**作用：** 描述要构建什么（What）和为什么（Why），不涉及技术栈

  

**时机：** 建立 constitution 后

  

**关键原则：**

- ✅ **越详细越好** - 提供具体的功能描述

- ✅ **聚焦用户价值** - 说明为什么需要这个功能

- ✅ **避免技术细节** - 不要在这个阶段指定技术栈

  

**示例（来自视频 - iOS 番茄专注 APP）：**

```Plain
/specify 构建一个原生 iOS 番茄专注应用，具备以下功能：

**核心功能：**
1. 番茄钟计时器
   - 默认工作时长 25 分钟，可自定义（5-60 分钟）
   - 短休息 5 分钟，长休息 15 分钟
   - 完成 4 个番茄钟后触发长休息

2. 任务管理
   - 创建、编辑、删除任务
   - 为任务分配预期番茄钟数量
   - 任务完成状态标记
   - 任务列表支持拖拽排序

3. 统计数据
   - 每日完成的番茄钟数量
   - 每周趋势图表
   - 任务完成率统计
   - 历史记录查看

4. 用户体验
   - 简洁优雅的界面设计
   - 深色模式支持
   - 计时器完成时的通知提醒
   - 背景音效（可选）

**数据持久化：**
- 所有数据本地存储
- 无需账户登录
- 支持数据导出
```

  

**示例（来自官方文档 - Taskify 项目管理）：**

```Plain
/specify 开发 Taskify，一个团队生产力平台：

**功能范围：**
- 用户可以创建项目、添加团队成员、分配任务
- 看板风格的任务拖拽移动
- 任务评论功能

**初始阶段限制：**
- 预定义 5 个用户（1 产品经理 + 4 工程师）
- 创建 3 个示例项目
- 标准看板列：待办、进行中、审核中、完成

**任务卡片功能：**
- 在不同看板列之间更改任务状态
- 为任务添加无限条评论
- 从预定义用户中分配任务负责人

**UI 流程：**
1. 启动时选择用户（无需密码）
2. 进入项目列表视图
3. 点击项目打开该项目的看板
4. 拖拽任务卡片在不同列之间移动
5. 当前用户的任务用不同颜色高亮显示

**评论权限：**
- 可以编辑/删除自己的评论
- 不能编辑/删除他人的评论
```

  

**生成文件：** `.specify/specs/001-feature-name/spec.md`

  

**包含内容：**

- 用户故事（User Stories）
    
- 功能需求（Functional Requirements）
    
- 验收标准（Acceptance Criteria）
    
- 审查清单（Review Checklist）
    

---

  

### **命令 3:`/clarify` - 澄清模糊需求**

  

**作用：** 通过结构化问答澄清规格中未明确的部分

  

**时机：** 在 `/specify` 之后、`/plan` 之前（强烈推荐）

  

**为什么重要：**

- 🎯 减少后续返工
    
- 🎯 覆盖遗漏的需求细节
    
- 🎯 确保所有利益相关者的理解一致
    

**工作流程：**

```Plain
用户 → /clarify
  ↓
AI 逐个提出澄清问题
  ↓
用户回答问题
  ↓
AI 将答案记录到 Clarifications 部分
  ↓
重复直到所有关键问题都得到解答
```

  

**示例对话：**

```Plain
AI: "关于任务优先级，我需要澄清几个问题：
     1. 是否支持任务优先级设置（高/中/低）？
     2. 是否需要根据优先级自动排序？
     3. 紧急任务是否需要特殊的视觉标识？"

用户: "是的，支持三级优先级。高优先级任务在列表顶部显示，
      用红色标记。不需要自动排序，用户可以手动拖拽。"

AI: [将答案记录到 spec.md 的 Clarifications 部分]
```

  

**跳过 clarify 的情况：**

- 探索性原型（spike）
    
- 快速概念验证
    
- 需求已经非常明确
    

**明确表示跳过：**

```Plain
"我想跳过 clarify 步骤，直接进入技术规划。"
```

  

---

  

### **命令 4:`/plan` - 制定技术方案**

  

**作用：** 指定技术栈和架构选择

  

**时机：** 在 `/specify` 和 `/clarify` 完成后

  

**示例（视频中的 iOS 应用）：**

```Plain
/plan 使用以下技术栈开发：

**前端框架：**
- SwiftUI（原生 iOS）
- 最新 iOS SDK 特性

**数据持久化：**
- Swift Data（Apple 的现代数据框架）
- 替代 Core Data，更简洁的 API

**架构模式：**
- MVVM 架构
- Combine 框架处理响应式数据流

**依赖管理：**
- Swift Package Manager
- 最小化第三方依赖

**测试：**
- XCTest 框架
- SwiftUI 预览测试
```

  

**示例（官方文档的 .NET 应用）：**

```Plain
/plan 技术栈如下：

**后端：**
- .NET Aspire（微服务编排）
- PostgreSQL 数据库

**前端：**
- Blazor Server
- 拖拽任务看板
- 实时更新（SignalR）

**API 设计：**
- REST API
  • Projects API
  • Tasks API
  • Notifications API

**部署：**
- Docker 容器化
- Azure 云部署
```

  

**生成文件：**

```Plain
.specify/specs/001-feature-name/
├── plan.md              # 技术实现计划
├── data-model.md        # 数据模型设计
├── research.md          # 技术调研文档
├── quickstart.md        # 快速开始指南
└── contracts/           # API 契约
    ├── api-spec.json    # REST API 规格
    └── signalr-spec.md  # SignalR 规格
```

  

**关键检查点：**

  

1. **验证技术栈版本：**

```Plain
"检查 plan.md 和 research.md，确保使用了最新稳定版本的框架。
如果是快速变化的库（如 .NET Aspire），请从网上获取最新文档。"
```

  

2. **避免过度工程化：**

```Plain
"审查实现计划，检查是否有过度工程化的组件。
根据 constitution 中的原则，简化不必要的复杂度。"
```

  

3. **针对性研究：**

```Plain
"识别实现过程中不确定的技术点，为每个疑问创建独立的研究任务，
并行进行针对性调研。不要进行泛泛的技术调研。"
```

  

---

  

### **命令 5:`/tasks` - 生成任务清单**

  

**作用：** 将技术计划分解为可执行的任务列表

  

**时机：** 在 `/plan` 完成后

  

**示例：**

```Plain
/tasks
```

  

**生成文件：** `.specify/specs/001-feature-name/tasks.md`

  

**任务结构示例（46 个任务）：**

  

## **Phase 1: 项目基础设施 (Tasks 1-8)**

  

### **Task 1: 创建 Xcode 项目**

- 使用 SwiftUI App 模板创建新项目
    
- 配置项目设置（Bundle ID、版本号）
    
- 设置最低 iOS 版本（iOS 17.0）
    

  

### **Task 2: 设置 Swift Data 数据模型**

- 创建 Task 模型
    
- 创建 Session 模型
    
- 配置 ModelContainer
    
- 编写模型单元测试
    

  

## **Phase 2: 核心功能 (Tasks 9-25)**

  

### **Task 9: 实现番茄钟计时器**

- 创建 TimerViewModel
    
- 实现倒计时逻辑
    
- 添加开始/暂停/重置功能
    
- 编写计时器单元测试
    

  

### **Task 10: 构建计时器 UI**

- 设计圆形进度条组件
    
- 显示剩余时间
    
- 添加控制按钮
    
- 实现 SwiftUI 预览
    

  

## **Phase 3: 任务管理 (Tasks 26-35)**

...

  

## **Phase 4: 统计功能 (Tasks 36-42)**

...

  

## **Phase 5: 优化与测试 (Tasks 43-46)**

...

**任务特性：**

- ✅ **依赖关系：** 任务之间的先后顺序

- ✅ **并行标记：** 可以同时执行的任务

- ✅ **TDD 要求：** 每个任务都包含测试编写

- ✅ **验收条件：** 明确的完成标准

  

---

  

### **命令 6:`/analyze` - 一致性检查**

  

**作用：** 跨文档验证一致性和覆盖率

  

**时机：** 在 `/tasks` 之后、`/implement` 之前（必须运行）

  

**示例：**

```Plain
/analyze
```

  

**检查内容：**

  

1. **规格 ↔ 计划一致性**

- spec.md 中的所有功能是否在 plan.md 中都有技术方案？
    
- 是否有在计划中但规格中没有的功能？
    

2. **计划 ↔ 任务一致性**

- plan.md 中的所有模块是否都分解为任务？
    
- tasks.md 是否覆盖了所有技术细节？
    

3. **Constitution 合规性**

- 计划和任务是否遵循 constitution.md 中的原则？
    
- 是否违反了既定的技术约束？
    

4. **完整性检查**

- 是否有遗漏的功能点？
    
- 是否有未考虑的边界情况？
    

**输出报告：**

```Plain
✅ Specification Coverage: 100%
✅ Plan-to-Tasks Mapping: Complete
⚠️  Warning: Task 23 缺少单元测试计划
⚠️  Warning: Data migration 策略未在 plan.md 中说明
❌ Error: Constitution 要求 80% 测试覆盖率，但当前任务只涵盖 65%
```

  

**修复问题后再运行：**

```Plain
/analyze
```

  

---

  

### **命令 7:`/implement` - 自动化实现**

  

**作用：** 执行所有任务，生成完整的应用代码

  

**时机：** 在 `/analyze` 通过后

  

**示例：**

```Plain
/implement
```

  

**执行流程：**

  

```Plain
1. 前置验证
   ↓
   检查 constitution.md ✓
   检查 spec.md ✓
   检查 plan.md ✓
   检查 tasks.md ✓

2. 任务解析
   ↓
   读取 tasks.md
   识别依赖关系
   确定执行顺序

3. 逐任务实现（TDD 模式）
   ↓
   For each task:
   ├─ 步骤 1: 编写测试用例
   ├─ 步骤 2: 实现最小可工作代码
   ├─ 步骤 3: 运行测试（必须通过）
   ├─ 步骤 4: 重构优化
   └─ 步骤 5: 最终验证

4. 进度报告
   ↓
   Task 1/46: ✓ 创建 Xcode 项目
   Task 2/46: ✓ 设置 Swift Data 数据模型
   Task 3/46: ✓ 实现番茄钟计时器
   ...

5. 完成
   ↓
   生成代码统计报告
   运行集成测试
   生成文档
```

  

**重要提示：**

  

⚠️ **本地工具需求：**

AI 会执行本地 CLI 命令（如 `dotnet`、`npm`、`xcodebuild` 等），请确保已安装所需工具。

  

**示例（视频中的结果）：**

- ✅ 46 个任务全部完成
    
- ✅ 生成完整的 SwiftUI 代码
    
- ✅ 所有单元测试通过
    
- ✅ 应用可以在 Xcode 中直接运行
    

**测试与调试：**

  

实现完成后：

1. 在对应的 IDE 中打开项目（Xcode / VS Code / Visual Studio）
    
2. 运行应用，测试功能
    
3. 检查浏览器控制台/设备日志中的错误
    
4. 将错误信息复制回 AI，让它修复
    

**示例调试：**

```Plain
"应用启动时崩溃，Xcode 控制台显示：
'Thread 1: Fatal error: No exact matches in call to initializer'
在 TimerView.swift 第 23 行。请修复这个问题。"
```

  

---

  

## **完整实战演示**

  

以下是视频中展示的完整开发流程（iOS 番茄专注 APP）：

  

### **步骤 0: 环境准备（2:39 - 3:40）**

  

```Bash
# 安装 specify-cli
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 验证安装
specify check

# 确保已安装：
# - Python 3.11+
# - Git
# - Claude Code（或其他支持的 AI 工具）
# - Xcode（iOS 开发）
```

  

---

  

### **步骤 1: 初始化项目（3:40 - 4:03）**

  

```Bash
# 创建新项目
specify init pomodoro-focus-app --ai claude

# 或在当前目录初始化
specify init . --ai claude

# 进入项目目录
cd pomodoro-focus-app

# 启动 Claude Code
claude
```

  

**生成的项目结构：**

```Plain
pomodoro-focus-app/
├── .specify/
│   ├── memory/
│   │   └── constitution.md      # 待创建
│   ├── scripts/
│   │   ├── create-new-feature.sh
│   │   ├── setup-plan.sh
│   │   └── ...
│   ├── specs/                   # 功能规格目录
│   └── templates/
│       ├── spec-template.md
│       ├── plan-template.md
│       └── tasks-template.md
├── CLAUDE.md                    # Claude Code 配置
└── README.md
```

  

---

  

### **步骤 2: 建立项目铁律（4:03 - 6:02）**

  

在 Claude Code 中输入：

  

```Plain
/constitution 创建以下开发原则：

**代码质量：**
1. 遵循 Swift 官方编码规范
2. 使用有意义的变量和函数命名
3. 每个函数职责单一，不超过 50 行
4. 避免魔法数字，使用常量或枚举

**测试标准：**
1. 测试覆盖率目标：80%+
2. 关键业务逻辑 100% 测试覆盖
3. 所有 ViewModel 必须有单元测试
4. UI 组件使用 SwiftUI 预览测试

**用户体验：**
1. 响应式设计，适配所有 iOS 设备尺寸
2. 支持浅色和深色模式
3. 动画流畅自然（60 FPS）
4. 无障碍支持（VoiceOver、动态字体）

**性能要求：**
1. 应用启动时间 < 1 秒
2. 所有用户操作响应时间 < 100ms
3. 内存占用 < 50MB
4. 电池消耗优化（后台最小化活动）

**架构原则：**
1. MVVM 架构，清晰的层次分离
2. 使用 Combine 处理异步和数据流
3. 依赖注入，方便测试
4. 单向数据流

**依赖管理：**
1. 优先使用系统框架
2. 第三方库必须经过评估（License、维护状态、Star 数）
3. 使用 Swift Package Manager

**数据安全：**
1. 敏感数据本地加密存储
2. 用户隐私第一，不收集个人信息
3. 遵循 Apple 的隐私准则
```

  

**结果：**

- 生成 `.specify/memory/constitution.md`
    
- 后续所有决策都将参考这些原则
    

---

  

### **步骤 3: 创建功能规范（6:02 - 7:29）**

  

```Plain
/specify 构建一个原生 iOS 番茄专注应用：

**应用名称：** Focus Flow

**核心功能：**

1. **番茄钟计时器**
   - 工作时长：默认 25 分钟，可自定义（1-60 分钟）
   - 短休息：默认 5 分钟，可自定义（1-30 分钟）
   - 长休息：默认 15 分钟，可自定义（5-60 分钟）
   - 完成 4 个番茄钟后自动触发长休息
   - 计时器状态：未开始、运行中、暂停、休息中
   - 显示当前番茄钟进度（如 2/4）

2. **任务管理**
   - 创建任务：输入任务名称和描述
   - 编辑任务：修改名称、描述、预估番茄钟数
   - 删除任务：支持滑动删除
   - 任务状态：待办、进行中、已完成
   - 为任务分配预期番茄钟数量（1-10 个）
   - 实际完成番茄钟数自动记录
   - 任务列表支持拖拽重新排序
   - 今日任务快捷视图

3. **统计与洞察**
   - 今日完成的番茄钟数量
   - 本周每日趋势折线图
   - 本月总番茄钟数和任务完成数
   - 最高连续完成天数（连击记录）
   - 按任务类别的时间分布（饼图）
   - 生产力热力图（日历视图）
   - 历史记录列表（可按日期筛选）

4. **用户体验**
   - **主题：** 浅色模式 + 深色模式自动切换
   - **界面：** 简洁优雅，符合 Apple Human Interface Guidelines
   - **通知：**
     * 番茄钟完成时推送通知
     * 休息结束时提醒通知
     * 可自定义通知声音（系统音效）
   - **音效：**
     * 计时器滴答声（可选，默认关闭）
     * 完成时的庆祝音效
     * 支持静音模式
   - **专注模式集成：**
     * 番茄钟运行时自动开启"请勿打扰"
     * 结束后恢复原有设置
   - **Widget 支持：**
     * 主屏幕小组件显示当前任务和剩余时间
     * 锁屏小组件快速启动计时器

5. **设置与个性化**
   - 自定义番茄钟时长
   - 自定义休息时长
   - 每日目标番茄钟数设置
   - 通知开关
   - 音效开关
   - 主题选择（跟随系统 / 始终浅色 / 始终深色）
   - 数据导出（CSV 格式）
   - 数据清除（带二次确认）

**数据持久化：**
- 使用 Swift Data（iOS 17+）
- 所有数据本地存储，不上传云端
- 支持 iCloud 同步（可选）
- 无需账户登录

**非功能性需求：**
- 最低支持 iOS 17.0
- 支持 iPhone 和 iPad（自适应布局）
- 无广告
- 完全离线使用
- 首次启动时的简短引导
```

  

**AI 响应：**

- 创建新分支：`001-focus-flow-core-features`
    
- 生成 `.specify/specs/001-focus-flow-core-features/spec.md`
    
- 包含详细的用户故事和验收标准
    

---

  

### **步骤 4: 澄清需求（可选但推荐）**

  

```Plain
/clarify
```

  

**AI 可能提出的问题：**

```Plain
Q1: 关于任务类别，是否需要预定义类别（工作、学习、运动等），
    还是由用户自定义？

Q2: 番茄钟进行中如果用户切换到其他应用，计时器是否继续运行？

Q3: 统计数据保留多长时间？是否需要设置自动清理旧数据的策略？

Q4: Widget 更新频率如何控制？（考虑电池消耗）

Q5: 是否支持多任务同时进行？还是一次只能专注一个任务？
```

  

**回答示例：**

```Plain
A1: 支持用户自定义任务类别，同时提供 5 个预设类别作为模板
    （工作、学习、健身、阅读、其他）

A2: 是的，切换应用后计时器继续在后台运行。但如果设备锁屏超过 5 分钟，
    计时器自动暂停（防止误计时）

A3: 统计数据永久保留，但在设置中提供"清除 X 天前数据"的选项

A4: Widget 每 30 秒更新一次（在计时器运行时），停止时不更新

A5: 一次只能专注一个任务，这符合番茄工作法的核心理念
```

  

---

  

### **步骤 5: 技术栈规划（7:29 - 8:02）**

  

```Plain
/plan 使用以下技术栈：

**平台：**
- iOS 17.0+（利用最新特性）
- Swift 5.9+
- Xcode 15+

**UI 框架：**
- SwiftUI（100% SwiftUI，不使用 UIKit）
- SF Symbols 5.0（图标）
- Charts 框架（统计图表）

**数据层：**
- Swift Data（替代 Core Data）
- @Model 宏简化模型定义
- @Query 属性包装器实现响应式查询
- ModelContainer 管理数据栈

**架构：**
- MVVM（Model-View-ViewModel）
- 使用 @Observable 宏（替代 ObservableObject）
- 单向数据流
- 依赖注入模式

**状态管理：**
- @State、@Binding、@Environment
- Combine 框架（处理异步事件）
- Timer.publish 实现倒计时

**通知：**
- UNUserNotificationCenter（本地通知）
- 请求授权，处理用户交互

**Widget：**
- WidgetKit 框架
- TimelineProvider 定时更新
- AppIntents 快捷操作

**测试：**
- XCTest 框架
- @Testable import 白盒测试
- SwiftUI Previews（快速 UI 测试）
- Mock 对象模拟数据层

**依赖管理：**
- Swift Package Manager
- 无第三方依赖（纯系统框架）

**项目结构：**
```

FocusFlow/

├── Models/

│ ├── Task.swift

│ ├── Session.swift

│ └── Settings.swift

├── ViewModels/

│ ├── TimerViewModel.swift

│ ├── TaskListViewModel.swift

│ └── StatisticsViewModel.swift

├── Views/

│ ├── TimerView.swift

│ ├── TaskListView.swift

│ ├── StatisticsView.swift

│ ├── SettingsView.swift

│ └── Components/

│ ├── CircularProgressView.swift

│ ├── TaskRowView.swift

│ └── ChartView.swift

├── Services/

│ ├── DataService.swift

│ ├── NotificationService.swift

│ └── TimerService.swift

├── Utilities/

│ ├── Extensions.swift

│ └── Constants.swift

├── FocusFlowWidget/

│ ├── FocusFlowWidget.swift

│ └── TimelineProvider.swift

└── Tests/

├── ViewModelTests/

└── ServiceTests/

  

**AI 响应：**

- 生成 `plan.md`（技术实现计划）
    
- 生成 `data-model.md`（数据模型设计）
    
- 生成 `research.md`（技术调研文档）
    

**验证计划：**

```Plain
"请审查 plan.md，确保：
1. 所有选择的框架都是 iOS 17 支持的
2. 没有引入不必要的第三方库
3. 架构设计符合 constitution 中的原则"
```

  

---

  

### **步骤 6: 任务分解（8:02 - 8:40）**

  

```Plain
/tasks
```

  

**AI 响应：**

生成 46 个可执行任务，分为 5 个阶段：

  

## **Phase 1: 项目基础设施（Tasks 1-8）**

- Task 1: 创建 Xcode 项目和基础配置
    
- Task 2: 设置 Swift Data 模型和 ModelContainer
    
- Task 3: 创建项目文件夹结构
    
- Task 4: 配置 Info.plist 权限（通知、后台模式）
    
- Task 5: 设置主 App 和 AppDelegate
    
- Task 6: 实现基础导航结构（TabView）
    
- Task 7: 创建 Theme 和 Color 配置
    
- Task 8: 编写项目 README 和文档
    

## **Phase 2: 核心计时器功能（Tasks 9-18）**

- Task 9: 实现 TimerService 核心逻辑
    
- Task 10: 编写 TimerViewModel
    
- Task 11: 创建 CircularProgressView 组件
    
- Task 12: 构建 TimerView 主界面
    
- Task 13: 实现开始/暂停/重置功能
    
- Task 14: 添加番茄钟周期管理（工作/休息切换）
    
- Task 15: 集成 Combine 实现响应式计时
    
- Task 16: 后台计时逻辑处理
    
- Task 17: 编写计时器单元测试
    
- Task 18: SwiftUI Preview 和 UI 调试
    

## **Phase 3: 任务管理（Tasks 19-28）**

- Task 19: 创建 Task 数据模型
    
- Task 20: 实现 DataService 增删改查
    
- Task 21: 编写 TaskListViewModel
    
- Task 22: 构建 TaskListView
    
- Task 23: 实现 TaskRowView 组件
    
- Task 24: 添加任务创建表单
    
- Task 25: 实现任务编辑功能
    
- Task 26: 滑动删除和拖拽排序
    
- Task 27: 任务与计时器关联逻辑
    
- Task 28: 任务管理单元测试
    

## **Phase 4: 统计与数据分析（Tasks 29-37）**

- Task 29: 创建 Session 数据模型
    
- Task 30: 实现统计数据查询逻辑
    
- Task 31: 编写 StatisticsViewModel
    
- Task 32: 使用 Charts 框架创建折线图
    
- Task 33: 创建饼图显示任务分布
    
- Task 34: 实现生产力热力图（日历视图）
    
- Task 35: 构建 StatisticsView 主界面
    
- Task 36: 历史记录列表和筛选
    
- Task 37: 统计功能单元测试
    

## **Phase 5: 高级功能与优化（Tasks 38-46）**

- Task 38: 集成 UNUserNotificationCenter
    
- Task 39: 实现本地通知（完成/休息提醒）
    
- Task 40: 创建 WidgetKit Extension
    
- Task 41: 实现 Widget TimelineProvider
    
- Task 42: Widget UI 设计和数据同步
    
- Task 43: 设置界面（SettingsView）
    
- Task 44: iCloud 同步配置（可选）
    
- Task 45: 无障碍功能适配（VoiceOver）
    
- Task 46: 性能优化、内存泄漏检测、最终测试
    

**每个任务包含：**

- ✅ 详细的实现步骤
    
- ✅ 测试要求
    
- ✅ 验收标准
    
- ✅ 预估时间
    

---

  

### **步骤 7: 一致性检查（8:40 - 9:33）**

  

```Plain
/analyze
```

  

**AI 分析输出：**

```Plain
🔍 Spec-Driven Development Consistency Analysis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Specification Coverage Analysis
✅ All user stories in spec.md are covered in plan.md
✅ All features have corresponding technical designs
⚠️  Warning: "iCloud 同步" 在 spec 中标记为"可选"，
    但在 plan.md 中未提供技术细节

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 Plan-to-Tasks Mapping
✅ All components in plan.md are decomposed into tasks
✅ Task dependencies are properly sequenced
⚠️  Warning: Task 44 (iCloud 同步) 标记为"可选"，
    建议在 constitution 中明确是否必须实现

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📏 Constitution Compliance
✅ MVVM 架构符合 constitution 要求
✅ 测试覆盖率目标已在任务中体现（每个 ViewModel 都有测试任务）
⚠️  Warning: constitution 要求 80% 测试覆盖率，
    当前 tasks.md 中测试任务占比 19.6%（9/46）
    建议增加集成测试和 UI 测试任务

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Completeness Check
✅ All phases have clear deliverables
✅ No missing functional areas detected
❌ Error: Widget 功能在 spec 中要求支持"锁屏小组件"，
    但 tasks.md 中只有"主屏幕小组件"任务
    需要添加 Task 42.1: 实现锁屏 Widget

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary:
- Total Issues: 4
  • Errors: 1 ❌
  • Warnings: 3 ⚠️
  • Info: 0 ℹ️

❌ Analysis Failed - Please address errors before implementing
```

  

**修复问题：**

```Plain
"请解决 /analyze 发现的问题：
1. 添加 Task 42.1，实现锁屏小组件
2. 在 plan.md 中补充 iCloud 同步的技术方案（或在 constitution 中明确标记为 V2 功能）
3. 增加 3 个任务以提升测试覆盖率：
   - Task 46.1: SwiftUI View 快照测试
   - Task 46.2: 集成测试（完整番茄钟流程）
   - Task 46.3: 性能基准测试"
```

  

**再次检查：**

```Plain
/analyze
```

  

**通过后的输出：**

```Plain
✅ All checks passed!
📊 Summary:
- Specification Coverage: 100%
- Plan-to-Tasks Mapping: Complete
- Constitution Compliance: Verified
- Test Coverage Target: 82.3% (meets 80% requirement)

✨ Ready for implementation!
```

  

---

  

### **步骤 8: 自动化实现（9:33 - 10:30）**

  

```Plain
/implement
```

  

**AI 执行流程（视频演示）：**

  

```Plain
⏳ Starting implementation...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 1: 项目基础设施
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1/49] 🏗️  Task 1: 创建 Xcode 项目
$ xcodebuild -project FocusFlow.xcodeproj -scheme FocusFlow build
✅ 项目创建成功

[2/49] 💾 Task 2: 设置 Swift Data 模型
📝 创建 Task.swift
📝 创建 Session.swift
📝 创建 ModelContainer.swift
🧪 编写单元测试...
$ swift test --filter TaskModelTests
✅ 测试通过 (3/3)

[3/49] 📁 Task 3: 创建文件夹结构
✅ 项目结构创建完成

[4/49] ⚙️  Task 4: 配置 Info.plist
✅ 通知权限配置完成
✅ 后台模式配置完成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 2: 核心计时器功能
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[9/49] ⏱️  Task 9: 实现 TimerService
📝 创建 TimerService.swift
✅ 倒计时逻辑实现完成
✅ 状态机实现完成

[10/49] 🎨 Task 10: TimerViewModel
🧪 TDD 模式：先写测试
📝 创建 TimerViewModelTests.swift
📝 创建 TimerViewModel.swift
$ swift test --filter TimerViewModelTests
✅ 测试通过 (8/8)

[11/49] 🔵 Task 11: CircularProgressView
📝 创建自定义 Shape 和动画
✅ 进度圆环渲染完成

[12/49] 📱 Task 12: TimerView 主界面
✅ UI 布局完成
✅ SwiftUI Preview 验证通过

[进度：26%] ⏳ 预计剩余时间：18 分钟

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 3: 任务管理
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[19/49] 📋 Task 19: Task 数据模型
✅ @Model 宏配置完成
✅ 数据关系定义完成

[20/49] 🔄 Task 20: DataService CRUD
🧪 TDD: 先实现 Mock 和测试
$ swift test --filter DataServiceTests
✅ 测试通过 (12/12)

...（中间任务省略）...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 5: 高级功能与优化
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[46/49] ✅ Task 46: 最终测试和优化
$ swift test --enable-code-coverage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Test Coverage Report:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ViewModels:          91.3% ✅
Services:            87.5% ✅
Models:              100%  ✅
Views:               68.4% ⚠️  (SwiftUI views, acceptable)
Overall:             82.8% ✅ (exceeds 80% target)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 内存泄漏检测...
$ xcrun leaks --atExit -- FocusFlow
✅ No leaks detected

⚡ 性能基准测试...
- 启动时间: 0.68s ✅ (< 1s target)
- 内存占用: 32MB ✅ (< 50MB target)
- CPU 占用: 4.3% ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Implementation Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Statistics:
- Tasks Completed: 49/49 (100%)
- Tests Written: 67
- Tests Passed: 67/67 (100%)
- Code Coverage: 82.8%
- Lines of Code: 3,247
- Files Created: 38
- Warnings: 0
- Errors: 0

📦 Deliverables:
✅ Xcode 项目：FocusFlow.xcodeproj
✅ Widget Extension
✅ 单元测试套件
✅ SwiftUI Previews
✅ README 文档

🚀 Next Steps:
1. 在 Xcode 中打开项目
2. 运行模拟器测试
3. 提交代码到 Git
```

  

---

  

### **步骤 9: 测试与验证（10:30 - 视频结束）**

  

**在 Xcode 中运行：**

  

```Bash
# 方式 1: 使用 Xcode GUI
# 打开 FocusFlow.xcodeproj
# 选择目标设备（iPhone 15 Pro 模拟器）
# 点击 Run (⌘R)

# 方式 2: 使用命令行
xcodebuild -project FocusFlow.xcodeproj \
           -scheme FocusFlow \
           -destination 'platform=iOS Simulator,name=iPhone 15 Pro' \
           build
           
xcrun simctl boot "iPhone 15 Pro"
xcrun simctl install booted build/Release-iphonesimulator/FocusFlow.app
xcrun simctl launch booted com.yourdomain.FocusFlow
```

  

**视频中的测试结果：**

- ✅ 应用成功启动
    
- ✅ 计时器正常工作
    
- ✅ 任务创建和管理功能正常
    
- ✅ 通知推送正常
    
- ✅ 统计图表正确显示
    
- ✅ 深色模式切换流畅
    
- ✅ 所有交互响应灵敏
    

**完成的应用特性：**

5. 精美的圆形进度条计时器
    
6. 流畅的任务拖拽排序
    
7. 实时更新的统计图表
    
8. 系统级通知集成
    
9. 主屏幕和锁屏 Widget
    
10. 完整的浅色/深色主题
    

---

  

## **支持的AI工具**

  

Spec Kit 支持 10+ 主流 AI 编程助手，选择你喜欢的工具：

  

|   |   |   |   |
|---|---|---|---|
|AI 工具|命令行|支持状态|备注|

| **Claude Code** | `claude` | ✅ 完全支持 | 推荐，视频演示使用 |

| **GitHub Copilot** | `code` / `code-insiders` | ✅ 完全支持 | VS Code 集成 |

| **Cursor** | `cursor-agent` | ✅ 完全支持 | AI-first IDE |

| **Windsurf** | `windsurf` | ✅ 完全支持 | Codeium 出品 |

| **Gemini CLI** | `gemini` | ✅ 完全支持 | Google AI |

| **Qwen Code** | `qwen` | ✅ 完全支持 | 阿里云通义千问 |

| **opencode** | `opencode` | ✅ 完全支持 | 开源 AI 助手 |

| **Codex CLI** | `codex` | ⚠️ 部分支持 | 不支持自定义参数 |

| **Kilo Code** | `kilo` | ✅ 完全支持 | 轻量级选择 |

| **Auggie CLI** | `auggie` | ✅ 完全支持 | Augment Code |

| **Roo Code** | `roo` | ✅ 完全支持 | 新兴工具 |

  

### **初始化时选择 AI 工具**

  

```Bash
# 使用 Claude Code（推荐）
specify init my-project --ai claude

# 使用 GitHub Copilot
specify init my-project --ai copilot

# 使用 Cursor
specify init my-project --ai cursor

# 使用 Windsurf
specify init my-project --ai windsurf

# 使用通义千问
specify init my-project --ai qwen
```

  

### **特殊说明**

  

**Codex CLI 限制：**

- ⚠️ 不支持为斜杠命令传递自定义参数
    
- 可以使用，但功能受限
    
- 参考：[GitHub Issue #2890](https://github.com/openai/codex/issues/2890)
    

---

  

## **最佳实践与技巧**

  

### **1. Constitution 编写技巧**

  

**不好的示例：**

```Plain
/constitution 代码要写得好，测试要全面
```

  

**好的示例：**

```Plain
/constitution 建立以下开发原则：

**代码质量标准：**
1. 每个函数不超过 50 行，职责单一
2. 圈复杂度不超过 10
3. 代码审查必须通过才能合并
4. 禁止魔法数字，使用命名常量

**测试策略：**
1. 单元测试覆盖率 > 80%
2. 关键路径 100% 覆盖
3. 每个 public 方法都有测试
4. 使用 AAA 模式（Arrange-Act-Assert）

**性能基准：**
1. API 响应时间 < 200ms (P95)
2. 数据库查询 < 100ms
3. 前端首屏渲染 < 1.5s

**安全要求：**
1. 所有输入必须验证和清理
2. 使用参数化查询防止 SQL 注入
3. 敏感数据加密存储
4. 遵循 OWASP Top 10 准则
```

  

### **2. Specify 描述技巧**

  

**❌ 避免技术术语（在 /specify 阶段）：**

```Plain
/specify 使用 React + Redux 构建一个 SPA，
后端用 Node.js + Express + MongoDB...
```

  

**✅ 聚焦功能和价值：**

```Plain
/specify 构建一个在线协作白板应用：

**核心价值：**
远程团队可以实时协作绘图、头脑风暴和设计

**用户可以：**
- 创建无限大小的画布
- 绘制形状、线条、文字、便签
- 实时看到其他人的鼠标和编辑
- 导出为 PNG / SVG / PDF
- 通过链接邀请他人协作（无需注册）

**关键体验：**
- 所有操作延迟 < 50ms
- 支持触控笔和手指操作（iPad）
- 支持离线编辑，上线后自动同步
```

  

### **3. Clarify 最佳实践**

  

**主动触发 clarify：**

```Plain
/clarify

# AI 会提出 5-10 个结构化问题
# 回答完后，AI 会将答案整合到 spec.md

# 如果还有疑问，继续自由形式补充：
"关于文件上传，用户可以上传哪些格式？
大小限制是多少？是否需要病毒扫描？"
```

  

**跳过 clarify（明确表示）：**

```Plain
"这是一个探索性原型，需求还在变化中，
我想先快速实现一个 MVP，跳过 /clarify。"
```

  

### **4. Plan 精炼技巧**

  

**验证技术栈版本：**

```Plain
"检查 plan.md，确认所有框架版本：
- Next.js 使用哪个版本？
- 是否使用了 App Router（Next.js 13+）？
- Tailwind CSS 版本是否支持我们需要的特性？

对于快速演进的框架，请从官网获取最新最佳实践。"
```

  

**避免过度工程化：**

```Plain
"审查 plan.md，标记出所有'可能过度设计'的地方：
- 是否引入了不必要的微服务？
- 是否过早优化了性能？
- 是否添加了当前不需要的功能？

根据 constitution 的'简单优先'原则简化设计。"
```

  

**针对性研究（重要！）：**

```Plain
"不要进行泛泛的技术调研。识别实现中的具体不确定点，
为每个疑问创建独立的并行研究任务。

例如：
❌ 不好：'研究 Next.js'
✅ 好：'Next.js App Router 中如何实现服务端认证中间件？'
✅ 好：'Next.js 14 的 Server Actions 是否支持文件上传？'
```

  

### **5. Analyze 修复流程**

  

**系统化修复：**

```Plain
1. 运行 /analyze
2. 记录所有 Error 和 Warning
3. 从 Error 开始修复（按优先级）
4. 再次运行 /analyze
5. 重复直到通过
```

  

**示例对话：**

```Plain
用户: "/analyze"
AI: "❌ Error: 缺少任务 - Widget 锁屏小组件
     ⚠️  Warning: 测试覆盖率只有 65%，未达到 80% 目标"

用户: "添加 Task 42.1 实现锁屏小组件，
      添加 3 个测试任务提升覆盖率到 82%"
AI: [修改 tasks.md]

用户: "/analyze"
AI: "✅ 所有检查通过！"
```

  

### **6. Implement 执行优化**

  

**监控实现过程：**

- 不要在实现开始后立即离开
    
- 观察前 5-10 个任务的执行情况
    
- 如果发现方向错误，及时暂停并纠正
    

**处理错误：**

```Plain
# 编译错误
"编译失败，错误信息：
[复制完整的错误输出]
请修复这个问题。"

# 测试失败
"单元测试 TaskViewModelTests.testCreateTask 失败：
Expected: 3 tasks
Actual: 2 tasks
请调试并修复。"

# 运行时错误
"应用启动时崩溃，控制台显示：
[复制 stack trace]
请修复。"
```

  

### **7. 团队协作技巧**

  

**分支策略：**

```Plain
main
├── 001-user-authentication (feature branch)
├── 002-payment-integration (feature branch)
└── 003-notification-system (feature branch)

# Spec Kit 自动为每个 feature 创建分支
```

  

**PR 管理：**

```Plain
# 让 AI 创建 PR
"使用 GitHub CLI 创建 PR，从当前分支到 main，
包含详细的变更说明、测试结果和截图。"

# AI 会执行：
# $ gh pr create --title "..." --body "..."
```

  

**Code Review Checklist：**

```Plain
在合并前，请人工审查：
□ Constitution 原则是否被遵守
□ 测试覆盖率是否达标
□ 是否有明显的性能问题
□ 是否引入了不必要的复杂度
□ 文档是否完整
```

  

### **8. 高级技巧**

  

**并行实现探索：**

```Plain
# 创建多个分支，探索不同技术方案
git checkout -b 001-react-implementation
specify init . --ai claude --force

git checkout -b 001-vue-implementation  
specify init . --ai claude --force

# 比较两种实现，选择最优方案
```

  

**增量式开发：**

```Plain
# V1: MVP（最小可行产品）
/specify 只实现核心功能：用户登录、创建文档、基本编辑

# V2: 迭代增强
/specify 在 V1 基础上添加：实时协作、评论、版本历史
```

  

**技术债务管理：**

```Plain
# 在 constitution 中设定技术债务策略
/constitution 每个 Sprint 预留 20% 时间重构技术债务，
不允许连续 3 个 Sprint 不处理技术债务
```

  

---

  

## **常见问题解答**

  

### **Q1: Spec Kit 适合什么规模的项目？**

  

**A:** 从小型原型到企业级应用都适用：

  

- ✅ **小型原型**（1-3 天）：快速验证想法

- ✅ **中型应用**（1-4 周）：完整功能的产品

- ✅ **大型项目**（数月）：通过多个 feature 分支迭代开发

- ✅ **企业级应用**：利用 constitution 统一团队规范

  

### **Q2: 我需要会编程吗？**

  

**A:** 取决于你的目标：

  

- **零基础小白：** 可以生成可运行的应用，但调试错误可能需要帮助

- **有编程基础：** 可以完全掌控流程，修复 AI 的错误

- **专业开发者：** 可以用 Spec Kit 加速开发，聚焦架构设计

  

**建议：**

- 至少了解基本的命令行操作
    
- 能看懂错误信息并搜索解决方案
    
- 理解项目中使用的编程语言基础语法
    

### **Q3: 生成的代码质量如何？**

  

**A:** 质量取决于你的规格质量：

  

**高质量输入 → 高质量输出：**

- 详细的 constitution（质量标准）
    
- 清晰的 specify（功能描述）
    
- 完善的 plan（技术选型）
    
- 严格的 TDD（测试驱动）
    

**视频中的案例质量：**

- 测试覆盖率 82.8%
    
- 零编译警告和错误
    
- 符合 Swift 官方规范
    
- 架构清晰，易于维护
    

**常见问题：**

- AI 可能过度工程化 → 在 constitution 中强调简单性
    
- AI 可能遗漏边界情况 → 在 /clarify 阶段补充
    
- AI 可能使用过时的 API → 要求从官网研究最新版本
    

### **Q4: Spec Kit vs 传统 Vibe Coding 有什么区别？**

  

|   |   |   |
|---|---|---|
|维度|传统 Vibe Coding|Spec Kit (SDD)|

| **方法** | 随意编码，边写边改 | 规格驱动，结构化流程 |

| **规划** | 最少或没有 | 详细的规格、计划、任务 |

| **测试** | 事后补充（可能遗漏） | TDD 强制测试先行 |

| **一致性** | 难以保证 | 自动检查（/analyze） |

| **可维护性** | 取决于开发者水平 | 标准化模板约束 |

| **团队协作** | 风格各异 | Constitution 统一规范 |

| **适合场景** | 快速原型、探索性开发 | 企业级应用、长期项目 |

  

**何时使用 Vibe Coding：**

- 快速验证一个想法（< 1 小时）
    
- 一次性脚本或工具
    
- 个人实验项目
    

**何时使用 Spec Kit：**

- 需要长期维护的项目
    
- 团队协作开发
    
- 对代码质量有要求
    
- 需要完整的测试覆盖
    

### **Q5: 如何处理 AI 生成的错误代码？**

  

**步骤 1: 复制完整的错误信息**

```Plain
# 编译错误
error: cannot find 'UserDefaults' in scope

# 运行时错误
Thread 1: Fatal error: Index out of range

# 测试失败
TimerViewModelTests.testStartTimer(): XCTAssertEqual failed:
("running") is not equal to ("paused")
```

  

**步骤 2: 提供上下文给 AI**

```Plain
"在 TimerViewModel.swift 第 45 行出现错误：
[粘贴错误信息]

相关代码：
[可选：粘贴出错的代码片段]

请修复这个问题。"
```

  

**步骤 3: 验证修复**

```Plain
# 重新编译
$ xcodebuild build

# 重新运行测试
$ swift test

# 如果还有错误，重复步骤 1-2
```

  

**常见错误类型和解决方案：**

  

|   |   |   |
|---|---|---|
|错误类型|常见原因|解决方法|
|编译错误|API 使用错误、语法错误|让 AI 参考官方文档修复|
|链接错误|缺少依赖、框架未导入|检查项目配置和依赖|
|运行时错误|逻辑错误、nil 解包|提供 crash log 让 AI 调试|
|测试失败|逻辑错误、测试用例错误|检查测试预期是否正确|

  

### **Q6: 可以用于商业项目吗？**

  

**A:** 可以！

  

**许可证：** MIT License（非常宽松）

- ✅ 可用于商业项目
    
- ✅ 可修改代码
    
- ✅ 可分发
    
- ✅ 无需开源你的项目
    

**但要注意：**

- 生成的代码归你所有
    
- 你需要对代码质量负责
    
- 建议进行人工代码审查
    
- 遵守相关法律法规（如数据隐私）
    

### **Q7: 如何处理快速变化的技术栈？**

  

**问题：** 某些框架（如 Next.js、React、.NET）更新很快，AI 的训练数据可能过时。

  

**解决方案：**

  

1. **在 /plan 阶段明确版本：**

```Plain
/plan 使用以下技术栈：
- Next.js 14.2（最新稳定版）
- React 18.3
- 使用 App Router（而非 Pages Router）
```

  

2. **要求 AI 从官网研究：**

```Plain
"Next.js 14 引入了很多新特性，请从 nextjs.org 官网
获取以下主题的最新文档：
1. Server Actions 的最佳实践
2. 新的 Metadata API
3. 增量静态再生成（ISR）的最新实现方式

为每个主题创建独立的研究任务。"
```

  

3. **验证生成的代码：**

```Plain
"检查生成的代码，确保：
1. 没有使用已弃用的 API
2. 使用了框架推荐的最佳实践
3. 代码示例与官方文档一致

如果发现过时的用法，请更新。"
```

  

### **Q8: 团队如何协作使用 Spec Kit？**

  

**场景 1: 多人开发不同功能**

  

```Plain
# 开发者 A
git checkout -b 001-user-system
specify init . --ai claude
/constitution ...
/specify 用户注册、登录、权限管理
/plan ...
/implement

# 开发者 B（同时进行）
git checkout -b 002-payment-system
specify init . --ai cursor
/constitution ...
/specify 支付集成、订单管理
/plan ...
/implement

# 合并时
git checkout main
git merge 001-user-system
git merge 002-payment-system
```

  

**场景 2: 统一 Constitution**

  

```Plain
# 团队负责人在根目录创建
.specify/memory/team-constitution.md

# 所有功能分支继承这个 constitution
# 或在每个 feature 的 constitution 中引用：
"继承团队 constitution（../.specify/memory/team-constitution.md）
并补充以下本功能特定的规则：..."
```

  

**场景 3: Code Review 流程**

  

```Plain
1. 开发者完成 /implement
2. 运行 /analyze 确保一致性
3. 让 AI 创建 PR
4. 团队成员人工审查：
   - Constitution 合规性
   - 代码质量
   - 测试覆盖率
   - 安全问题
5. 合并到 main
```

  

### **Q9: 如何升级或维护现有项目？**

  

**场景：在现有代码库中添加新功能**

  

```Bash
# 1. 在现有项目中初始化 Spec Kit
cd existing-project
specify init . --here --force --ai claude

# 2. 创建新功能分支
/specify 添加新功能：社交分享
# Spec Kit 会创建新分支：001-social-sharing

# 3. 在 /plan 中考虑现有代码
/plan 集成到现有架构：
- 现有项目使用 Vue 3 + Pinia
- 需要与现有的认证系统集成
- 复用 utils/api.js 中的 HTTP 客户端
- 遵循现有的 UI 组件库风格
```

  

**迁移现有项目到 Spec Kit：**

  

```Plain
# 步骤 1: 为现有代码创建规格文档
/specify 根据现有代码反向工程规格：
[复制关键代码文件或提供代码库概述]

# 步骤 2: 建立 Constitution
/constitution 基于现有代码风格和架构建立规范

# 步骤 3: 逐步重构
为每个模块创建独立的 feature 规格
使用 /implement 重构单个模块
保持现有功能运行的同时逐步替换
```

  

### **Q10: Spec Kit 的局限性是什么？**

  

**当前局限：**

  

1. **需要人工验证**

- AI 生成的代码可能有 bug
    
- 测试可能不覆盖所有边界情况
    
- 需要开发者最终检查和调试
    

2. **依赖 AI 能力**

- 不同 AI 工具生成质量不同
    
- 复杂业务逻辑可能理解不准确
    
- 对快速变化的技术栈可能过时
    

3. **不适合的场景**

- 极其复杂的算法实现（如机器学习模型）
    
- 需要深度性能优化的底层代码
    
- 特定领域的专业软件（如医疗、金融）
    

4. **工具链依赖**

- 需要安装对应的开发工具（如 Xcode、Node.js）
    
- 某些 AI 工具可能需要付费订阅
    
- 网络连接稳定性影响体验
    

**未来改进方向：**

- 更智能的一致性检查
    
- 更好的错误恢复机制
    
- 支持更多编程语言和框架
    
- 更强的多人协作功能
    

---

  

## **总结**

  

Spec Kit 是一个**革命性的开发工具**，它通过规格驱动开发（SDD）和测试驱动开发（TDD）的理念，将 AI 编程从"随意编码"提升到"工程化开发"。

  

### **核心价值：**

  

1. **效率提升数倍**：7 条命令完成从需求到代码的全流程

2. **质量有保障**：强制 TDD + 一致性检查确保代码质量

3. **学习曲线平缓**：结构化流程，零基础也能上手

4. **企业级支持**：constitution 统一团队规范，适合大型项目

  

### **关键成功因素：**

  

- ✅ 详细的 Constitution（治理原则）
    
- ✅ 清晰的 Specify（功能规格）
    
- ✅ 完善的 Clarify（需求澄清）
    
- ✅ 合理的 Plan（技术方案）
    
- ✅ 严格的 Analyze（一致性检查）
    

### **最佳实践：**

  

- 🎯 规格阶段不涉及技术细节
    
- 🎯 计划阶段要求 AI 从官网研究最新文档
    
- 🎯 实现前必须运行 /analyze 检查一致性
    
- 🎯 生成的代码需要人工审查和测试
    

### **开始你的第一个项目：**

  

```Bash
# 1. 安装 Spec Kit
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 2. 初始化项目
specify init my-awesome-app --ai claude

# 3. 启动 AI 工具
cd my-awesome-app
claude

# 4. 开始开发！
/constitution ...
/specify ...
/clarify
/plan ...
/tasks
/analyze
/implement
```

  

---

  

## **参考资源**

  

- 📺 **视频教程（B站）：** https://www.bilibili.com/video/BV1aKxEzHEy9/

- 📝 **官方仓库：** https://github.com/github/spec-kit

- 📖 **完整方法论：** https://github.com/github/spec-kit/blob/main/spec-driven.md

- 🎓 **笔记分享：** https://www.aivi.fyi/llms/introduce-spec-kit

  

---

  

**License:** MIT License

**Maintained by:** GitHub

**Community:** 欢迎贡献和反馈！

  

🚀 **开始使用 Spec Kit，让 AI 成为你真正的编程搭档！**