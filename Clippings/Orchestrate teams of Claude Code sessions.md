---
title: "Orchestrate teams of Claude Code sessions"
source: "https://code.claude.com/docs/en/agent-teams"
author:
  - "[[Claude Code Docs]]"
published:
created: 2026-02-06
description: "Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management."
tags:
  - "clippings"
---
Agent teams are experimental and disabled by default. Enable them by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to your [settings.json](https://code.claude.com/docs/en/settings) or environment. Agent teams have [known limitations](https://code.claude.com/docs/en/#limitations) around session resumption, task coordination, and shutdown behavior.  
代理团队是实验性功能，默认禁用。通过在 settings.json 或环境变量中添加 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` 来启用。代理团队在会话恢复、任务协调和关闭行为方面存在已知限制。

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other.  
代理团队让你协调多个协同工作的 Claude Code 实例。一个会话充当团队领导，负责协调工作、分配任务和综合结果。团队成员独立工作，每个成员拥有自己的上下文窗口，并直接相互沟通。 Unlike [subagents](https://code.claude.com/docs/en/sub-agents), which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead.  
与在单个会话中运行且只能向主代理汇报的子代理不同，你也可以直接与个别团队成员互动，无需通过领导。 This page covers:本页面涵盖：
- [When to use agent teams](https://code.claude.com/docs/en/#when-to-use-agent-teams), including best use cases and how they compare with subagents  
	何时使用代理团队，包括最佳使用案例以及它们与子代理的比较
- [Starting a team 启动团队](https://code.claude.com/docs/en/#start-your-first-agent-team)
- [Controlling teammates](https://code.claude.com/docs/en/#control-your-agent-team), including display modes, task assignment, and delegation  
	控制团队成员，包括显示模式、任务分配和委派
- [Best practices for parallel work  
	并行工作的最佳实践](https://code.claude.com/docs/en/#best-practices)

## When to use agent teams何时使用代理团队

Agent teams are most effective for tasks where parallel exploration adds real value. See [use case examples](https://code.claude.com/docs/en/#use-case-examples) for full scenarios. The strongest use cases are:  
代理团队在并行探索能真正增加价值的工作中最为有效。查看完整场景的用例示例。最强大的用例包括：
- **Research and review**: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other’s findings  
	研究和评审：多个团队成员可以同时调查问题的不同方面，然后分享并质疑彼此的发现
- **New modules or features**: teammates can each own a separate piece without stepping on each other  
	新模块或功能：团队成员可以各自拥有独立的部分，而不会相互干扰
- **Debugging with competing hypotheses**: teammates test different theories in parallel and converge on the answer faster  
	竞争性假设的调试：团队成员并行测试不同的理论，更快地收敛到答案
- **Cross-layer coordination**: changes that span frontend, backend, and tests, each owned by a different teammate  
	跨层协调：涉及前端、后端和测试的变更，每个部分由不同的团队成员负责
Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or [subagents](https://code.claude.com/docs/en/sub-agents) are more effective.  
代理团队增加了协调开销，并且比单个会话使用更多的 token。当团队成员可以独立工作时，它们效果最佳。对于顺序任务、同一文件编辑或处理大量依赖关系的工作，单个会话或子代理更有效。

### Compare with subagents 与子代理比较

Both agent teams and [subagents](https://code.claude.com/docs/en/sub-agents) let you parallelize work, but they operate differently. Choose based on whether your workers need to communicate with each other:  
代理团队和子代理都允许你并行化工作，但它们的工作方式不同。根据你的工作是否需要相互通信来选择： Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.  
当需要快速、专注的工人并汇报时使用子代理。当队友需要分享发现、互相挑战并自行协调时使用代理团队。

## Enable agent teams 启用代理团队

Agent teams are disabled by default. Enable them by setting the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable to `1`, either in your shell environment or through [settings.json](https://code.claude.com/docs/en/settings):  
代理团队默认是禁用的。通过将 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` 环境变量设置为 `1` 来启用它们，可以在您的 shell 环境中或通过 settings.json 进行设置：

settings.json

## Start your first agent team开始您的第一个代理团队

After enabling agent teams, tell Claude to create an agent team and describe the task and the team structure you want in natural language. Claude creates the team, spawns teammates, and coordinates work based on your prompt.  
在启用代理团队后，告诉 Claude 创建一个代理团队，并用自然语言描述你想完成的任务和团队结构。Claude 会创建团队，生成队友，并根据你的提示进行工作协调。 This example works well because the three roles are independent and can explore the problem without waiting on each other:  
这个例子效果很好，因为这三个角色是独立的，可以不互相等待就探索问题： From there, Claude creates a team with a [shared task list](https://code.claude.com/docs/en/interactive-mode#task-list), spawns teammates for each perspective, has them explore the problem, synthesizes findings, and attempts to [clean up the team](https://code.claude.com/docs/en/#clean-up-the-team) when finished.  
从那里开始，Claude 创建一个具有共享任务列表的团队，为每个视角生成队友，让他们探索问题，综合发现，并在完成后尝试清理团队。 The lead’s terminal lists all teammates and what they’re working on. Use Shift+Up/Down to select a teammate and message them directly.  
领导的终端列出了所有队友及其正在处理的工作。使用 Shift+上/下键选择队友并直接向他们发送消息。 If you want each teammate in its own split pane, see [Choose a display mode](https://code.claude.com/docs/en/#choose-a-display-mode).  
如果你希望每个队友都在自己的分割窗格中，请参阅选择显示模式。

## Control your agent team 控制你的代理团队

Tell the lead what you want in natural language. It handles team coordination, task assignment, and delegation based on your instructions.  
用自然语言告诉负责人你想做什么。它会根据你的指令处理团队协调、任务分配和委托。

### Choose a display mode 选择显示模式

Agent teams support two display modes:  
代理团队支持两种显示模式：
- **In-process**: all teammates run inside your main terminal. Use Shift+Up/Down to select a teammate and type to message them directly. Works in any terminal, no extra setup required.  
	进程内：所有队友都在你的主终端内运行。使用 Shift+上/下键选择队友，直接输入消息给他们。适用于任何终端，无需额外设置。
- **Split panes**: each teammate gets its own pane. You can see everyone’s output at once and click into a pane to interact directly. Requires tmux, or iTerm2.  
	分割窗格：每位团队成员都有自己的窗格。你可以同时查看所有人的输出，并点击某个窗格进行直接交互。需要 tmux 或 iTerm2。

`tmux` has known limitations on certain operating systems and traditionally works best on macOS. Using `tmux -CC` in iTerm2 is the suggested entrypoint into `tmux`.  
`tmux` 在某些操作系统上有已知限制，传统上在 macOS 上表现最佳。建议使用 `tmux -CC` 在 iTerm2 中作为进入 `tmux` 的入口。

The default is `"auto"`, which uses split panes if you’re already running inside a tmux session, and in-process otherwise. The `"tmux"` setting enables split-pane mode and auto-detects whether to use tmux or iTerm2 based on your terminal. To override, set `teammateMode` in your [settings.json](https://code.claude.com/docs/en/settings):  
默认情况下是 `"auto"` ，如果你已经在 tmux 会话中运行，则使用分割窗格；否则使用进程内。 `"tmux"` 设置启用分割窗格模式，并根据你的终端自动检测是使用 tmux 还是 iTerm2。要覆盖此设置，请在 settings.json 中设置 `teammateMode` 。 To force in-process mode for a single session, pass it as a flag:  
为单个会话强制使用进程内模式，将其作为标志传递： Split-pane mode requires either [tmux](https://github.com/tmux/tmux/wiki) or iTerm2 with the [`it2` CLI](https://github.com/mkusaka/it2). To install manually:  
分屏模式需要 tmux 或 iTerm2 以及 `it2` CLI。手动安装方法：
- **tmux**: install through your system’s package manager. See the [tmux wiki](https://github.com/tmux/tmux/wiki/Installing) for platform-specific instructions.  
	tmux：通过系统包管理器安装。查看 tmux 维基获取特定平台的说明。
- **iTerm2**: install the [`it2` CLI](https://github.com/mkusaka/it2), then enable the Python API in **iTerm2 → Settings → General → Magic → Enable Python API**.  
	iTerm2：安装 `it2` CLI，然后在 iTerm2 → 设置 → 常规 → 魔法 → 启用 Python API。

### Specify teammates and models指定队友和模型

Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want:  
Claude 根据您的任务决定生成多少队友，或者您可以精确指定您想要的内容：

### Require plan approval for teammates要求队友计划审批

For complex or risky tasks, you can require teammates to plan before implementing. The teammate works in read-only plan mode until the lead approves their approach:  
对于复杂或风险较高的任务，你可以要求团队成员在实施前进行规划。该成员在获得负责人批准其方案前，将以只读规划模式工作： When a teammate finishes planning, it sends a plan approval request to the lead. The lead reviews the plan and either approves it or rejects it with feedback. If rejected, the teammate stays in plan mode, revises based on the feedback, and resubmits. Once approved, the teammate exits plan mode and begins implementation.  
当一名团队成员完成规划后，会向负责人发送计划审批请求。负责人会审查计划，并决定批准或驳回并给出反馈。如果被驳回，该成员将保持在规划模式，根据反馈进行修改，然后重新提交。一旦批准，该成员将退出规划模式并开始实施。 The lead makes approval decisions autonomously. To influence the lead’s judgment, give it criteria in your prompt, such as “only approve plans that include test coverage” or “reject plans that modify the database schema.”  
负责人会自主做出批准决策。若要影响负责人的判断，可以在提示中给出标准，例如“仅批准包含测试覆盖的方案”或“拒绝修改数据库模式的方案。”

### Use delegate mode 使用代理模式

Without delegate mode, the lead sometimes starts implementing tasks itself instead of waiting for teammates. Delegate mode prevents this by restricting the lead to coordination-only tools: spawning, messaging, shutting down teammates, and managing tasks.  
如果没有代理模式，负责人有时会自己开始执行任务，而不是等待队友。代理模式通过将负责人限制在仅用于协调的工具中来防止这种情况：生成、发送消息、关闭队友和管理任务。 This is useful when you want the lead to focus entirely on orchestration, such as breaking down work, assigning tasks, and synthesizing results, without touching code directly.  
当你希望负责人能完全专注于编排工作时，这会很有用，例如分解工作、分配任务和综合结果，而无需直接接触代码。 To enable it, start a team first, then press Shift+Tab to cycle into delegate mode.  
要启用它，首先开始一个团队，然后按下 Shift+Tab 进入代理模式。

### Talk to teammates directly直接与队友交谈

Each teammate is a full, independent Claude Code session. You can message any teammate directly to give additional instructions, ask follow-up questions, or redirect their approach.  
每个团队成员都是一个完整、独立的 Claude Code 会话。你可以直接给任何团队成员发送消息，以提供额外指示、询问后续问题或重新引导他们的方法。
- **In-process mode**: use Shift+Up/Down to select a teammate, then type to send them a message. Press Enter to view a teammate’s session, then Escape to interrupt their current turn. Press Ctrl+T to toggle the task list.  
	进程内模式：使用 Shift+上/下箭头键选择一个团队成员，然后输入消息发送给他们。按 Enter 键查看团队成员的会话，然后按 Escape 键中断他们当前的回合。按 Ctrl+T 键切换任务列表。
- **Split-pane mode**: click into a teammate’s pane to interact with their session directly. Each teammate has a full view of their own terminal.  
	分屏模式：点击队友的窗格可直接与其会话交互。每位队友都能完整查看自己的终端。

### Assign and claim tasks 分配和认领任务

The shared task list coordinates work across the team. The lead creates tasks and teammates work through them. Tasks have three states: pending, in progress, and completed. Tasks can also depend on other tasks: a pending task with unresolved dependencies cannot be claimed until those dependencies are completed.  
共享任务列表协调团队的工作。负责人创建任务，队友们处理这些任务。任务有三种状态：待处理、进行中、已完成。任务还可以依赖其他任务：一个有未解决依赖的任务，在依赖任务完成之前不能被认领。 The lead can assign tasks explicitly, or teammates can self-claim:  
负责人可以明确分配任务，或者团队成员可以自行认领：
- **Lead assigns**: tell the lead which task to give to which teammate  
	领导分配：告诉领导将哪个任务分配给哪个队友
- **Self-claim**: after finishing a task, a teammate picks up the next unassigned, unblocked task on its own  
	自主认领：完成任务后，队友自行认领下一个未分配且未阻塞的任务
Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously.  
任务认领使用文件锁来防止多个队友同时尝试认领同一任务时的竞态条件。

### Shut down teammates 关闭队友

To gracefully end a teammate’s session:  
要优雅地结束队友的会话： The lead sends a shutdown request. The teammate can approve, exiting gracefully, or reject with an explanation.  
负责人发送关闭请求。队友可以批准以优雅退出，或拒绝并说明理由。

### Clean up the team 清理团队

When you’re done, ask the lead to clean up:  
完成后，请请求负责人清理： This removes the shared team resources. When the lead runs cleanup, it checks for active teammates and fails if any are still running, so shut them down first.  
这会移除共享的团队资源。当负责人运行清理时，它会检查活跃的队友，如果仍有队友在运行，就会失败，所以应先关闭他们。

Always use the lead to clean up. Teammates should not run cleanup because their team context may not resolve correctly, potentially leaving resources in an inconsistent state.  
始终使用负责人来清理。队友不应运行清理，因为他们的团队上下文可能无法正确解析，可能会使资源处于不一致的状态。

## How agent teams work 代理团队的工作原理

This section covers the architecture and mechanics behind agent teams. If you want to start using them, see [Control your agent team](https://code.claude.com/docs/en/#control-your-agent-team) above.  
本节涵盖了代理团队的架构和机制。如果您想开始使用它们，请参阅上文的“控制您的代理团队”。

### How Claude starts agent teamsClaude 如何启动代理团队

There are two ways agent teams get started:  
有两种方式让代理团队开始工作：
- **You request a team**: give Claude a task that benefits from parallel work and explicitly ask for an agent team. Claude creates one based on your instructions.  
	您请求一个团队：给 Claude 一个可以从并行工作中受益的任务，并明确要求一个代理团队。Claude 根据您的指示创建一个团队。
- **Claude proposes a team**: if Claude determines your task would benefit from parallel work, it may suggest creating a team. You confirm before it proceeds.  
	Claude 提议一个团队：如果 Claude 确定您的任务可以从并行工作中受益，它可能会建议创建一个团队。在它继续之前，您需要确认。
In both cases, you stay in control. Claude won’t create a team without your approval.  
在两种情况下，你都能保持控制权。Claude 不会未经你的批准就创建团队。

### Architecture 架构

An agent team consists of:  
一个代理团队由以下组成： See [Choose a display mode](https://code.claude.com/docs/en/#choose-a-display-mode) for display configuration options. Teammate messages arrive at the lead automatically.  
请参阅“选择显示模式”以查看显示配置选项。队友的消息会自动发送给负责人。 The system manages task dependencies automatically. When a teammate completes a task that other tasks depend on, blocked tasks unblock without manual intervention.  
系统会自动管理任务依赖关系。当队友完成其他任务依赖的任务时，被阻塞的任务会自动解除阻塞，无需人工干预。 Teams and tasks are stored locally:  
团队和任务存储在本地：
- **Team config**: `~/.claude/teams/{team-name}/config.json` 团队配置： `~/.claude/teams/{team-name}/config.json`
- **Task list**: `~/.claude/tasks/{team-name}/` 任务列表： `~/.claude/tasks/{team-name}/`
The team config contains a `members` array with each teammate’s name, agent ID, and agent type. Teammates can read this file to discover other team members.  
团队配置包含一个 `members` 数组，其中包含每位团队成员的姓名、代理 ID 和代理类型。团队成员可以读取此文件来发现其他团队成员。

### Permissions 权限

Teammates start with the lead’s permission settings. If the lead runs with `--dangerously-skip-permissions`, all teammates do too. After spawning, you can change individual teammate modes, but you can’t set per-teammate modes at spawn time.  
团队成员的权限设置以领导者的权限设置为准。如果领导者使用 `--dangerously-skip-permissions` 运行，所有团队成员也会这样运行。生成后，你可以更改单个团队成员的模式，但在生成时无法设置每个成员的模式。

### Context and communication上下文与沟通

Each teammate has its own context window. When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills. It also receives the spawn prompt from the lead. The lead’s conversation history does not carry over.  
每个团队成员都有自己的上下文窗口。生成时，团队成员加载与常规会话相同的工程上下文：CLAUDE.md、MCP 服务器和技能。它还会收到领导者的生成提示。领导者的对话历史不会延续。 **How teammates share information:  
团队成员如何共享信息：**
- **Automatic message delivery**: when teammates send messages, they’re delivered automatically to recipients. The lead doesn’t need to poll for updates.  
	自动消息传递：当团队成员发送消息时，它们会自动传递给接收者。领导者无需轮询更新。
- **Idle notifications**: when a teammate finishes and stops, they automatically notify the lead.  
	空闲通知：当队友完成并停止时，他们会自动通知负责人。
- **Shared task list**: all agents can see task status and claim available work.  
	共享任务列表：所有代理都可以查看任务状态并认领可用工作。
**Teammate messaging:同事间消息：**
- **message**: send a message to one specific teammate  
	message：向一位特定的同事发送消息
- **broadcast**: send to all teammates simultaneously. Use sparingly, as costs scale with team size.  
	broadcast：同时向所有同事发送。请谨慎使用，因为成本会随着团队规模的增长而增加。

### Token usage 令牌使用

Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates. For research, review, and new feature work, the extra tokens are usually worthwhile. For routine tasks, a single session is more cost-effective. See [agent team token costs](https://code.claude.com/docs/en/costs#agent-team-token-costs) for usage guidance.  
代理团队比单个会话使用更多的 token。每位同事都有自己的上下文窗口，token 使用量会随着活跃同事数量的增加而增加。对于研究、审核和新功能开发，额外的 token 通常物有所值。对于常规任务，单个会话更具成本效益。请参考代理团队 token 成本以获取使用指导。

## Use case examples 用例示例

These examples show how agent teams handle tasks where parallel exploration adds value.  
这些示例展示了代理团队如何处理那些并行探索能增加价值的任务。

### Run a parallel code review运行并行代码审查

A single reviewer tends to gravitate toward one type of issue at a time. Splitting review criteria into independent domains means security, performance, and test coverage all get thorough attention simultaneously. The prompt assigns each teammate a distinct lens so they don’t overlap:  
单个审阅者往往会专注于某一类问题。将审阅标准划分为独立领域意味着安全、性能和测试覆盖率都能同时得到充分关注。提示为每个团队成员分配了独特的视角，以避免重叠： Each reviewer works from the same PR but applies a different filter. The lead synthesizes findings across all three after they finish.  
每个审阅者基于同一个 PR 但应用不同的筛选器。负责人在完成审阅后，整合所有三个领域的发现。

### Investigate with competing hypotheses用竞争性假设进行调查

When the root cause is unclear, a single agent tends to find one plausible explanation and stop looking. The prompt fights this by making teammates explicitly adversarial: each one’s job is not only to investigate its own theory but to challenge the others’.  
当根本原因不明确时，单个代理往往会找到一个看似合理的解释就停止寻找。提示通过让队友们明确地形成对抗来对抗这种情况：每个人的工作不仅是要调查自己的理论，还要挑战其他人的理论。 The debate structure is the key mechanism here. Sequential investigation suffers from anchoring: once one theory is explored, subsequent investigation is biased toward it.  
辩论结构是这里的关键机制。顺序调查会受锚定效应的影响：一旦一个理论被探索，后续的调查就会倾向于它。 With multiple independent investigators actively trying to disprove each other, the theory that survives is much more likely to be the actual root cause.  
当多个独立的调查者积极试图推翻彼此时，存活下来的理论更有可能是真正的根本原因。

## Best practices 最佳实践

### Give teammates enough context给队友们足够的背景信息

Teammates load project context automatically, including CLAUDE.md, MCP servers, and skills, but they don’t inherit the lead’s conversation history. See [Context and communication](https://code.claude.com/docs/en/#context-and-communication) for details. Include task-specific details in the spawn prompt:  
队友会自动加载项目上下文，包括 CLAUDE.md、MCP 服务器和技能，但他们不会继承领导的对话历史。详情请参阅上下文和沟通。在生成提示中包含特定任务的详细信息：

### Size tasks appropriately 合理分配任务大小

- **Too small**: coordination overhead exceeds the benefit  
	太小：协调成本超过收益
- **Too large**: teammates work too long without check-ins, increasing risk of wasted effort  
	太大：团队成员长时间工作缺乏检查，增加努力浪费的风险
- **Just right**: self-contained units that produce a clear deliverable, such as a function, a test file, or a review  
	刚刚好：自包含的单元，能产出明确的成果，如一个函数、一个测试文件或一次评审

The lead breaks work into tasks and assigns them to teammates automatically. If it isn’t creating enough tasks, ask it to split the work into smaller pieces. Having 5-6 tasks per teammate keeps everyone productive and lets the lead reassign work if someone gets stuck.  
领导将工作分解为任务并自动分配给团队成员。如果任务不够多，可以要求它将工作拆分成更小的部分。每个团队成员有 5-6 个任务可以保持大家高效，并允许领导在有人遇到困难时重新分配工作。

### Wait for teammates to finish等待团队成员完成

Sometimes the lead starts implementing tasks itself instead of waiting for teammates. If you notice this:  
有时领导会自己开始实施任务而不是等待队友。如果你注意到这种情况：

### Start with research and review从研究和评审开始

If you’re new to agent teams, start with tasks that have clear boundaries and don’t require writing code: reviewing a PR, researching a library, or investigating a bug. These tasks show the value of parallel exploration without the coordination challenges that come with parallel implementation.  
如果你对代理团队不熟悉，可以从那些有明确边界且不需要编写代码的任务开始：评审一个 PR、研究一个库或调查一个 bug。这些任务展示了并行探索的价值，而无需面对并行实现带来的协调挑战。

### Avoid file conflicts 避免文件冲突

Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.  
两名队友同时编辑同一个文件会导致覆盖。将工作拆分，让每个队友负责不同的文件集。

### Monitor and steer 监控和引导

Check in on teammates’ progress, redirect approaches that aren’t working, and synthesize findings as they come in. Letting a team run unattended for too long increases the risk of wasted effort.  
检查队友的进度，调整不奏效的方法，并随着进展综合发现。让团队无人照管过久会增加浪费精力的风险。

## Troubleshooting 故障排除

### Teammates not appearing 队友未出现

If teammates aren’t appearing after you ask Claude to create a team:  
如果你让 Claude 创建团队后队友仍未出现：
- In in-process mode, teammates may already be running but not visible. Press Shift+Down to cycle through active teammates.  
	在处理中模式，队友可能已经在运行但不可见。按 Shift+向下箭头键切换活跃队友。
- Check that the task you gave Claude was complex enough to warrant a team. Claude decides whether to spawn teammates based on the task.  
	确认你给 Claude 的任务足够复杂，值得组建一个团队。Claude 会根据任务决定是否生成队友。
- If you explicitly requested split panes, ensure tmux is installed and available in your PATH:  
	如果你明确要求分割面板，请确保已安装 tmux 并且它在你的 PATH 中可用：
- For iTerm2, verify the `it2` CLI is installed and the Python API is enabled in iTerm2 preferences.  
	对于 iTerm2，请确认 `it2` CLI 已安装，并在 iTerm2 偏好设置中启用了 Python API。
Teammate permission requests bubble up to the lead, which can create friction. Pre-approve common operations in your [permission settings](https://code.claude.com/docs/en/permissions) before spawning teammates to reduce interruptions.  
同事的权限请求会冒泡到负责人那里，这可能会产生摩擦。在生成同事之前，在您的权限设置中预先批准常见操作，以减少中断。 Teammates may stop after encountering errors instead of recovering. Check their output using Shift+Up/Down in in-process mode or by clicking the pane in split mode, then either:  
队友在遇到错误时可能会停止而不是恢复。使用进程内模式中的 Shift+上/下键或分割模式中点击面板来检查他们的输出，然后：
- Give them additional instructions directly  
	直接给他们额外的指令
- Spawn a replacement teammate to continue the work  
	生成一个替代队友继续工作

### Lead shuts down before work is done领导在工作完成前关闭了

The lead may decide the team is finished before all tasks are actually complete. If this happens, tell it to keep going. You can also tell the lead to wait for teammates to finish before proceeding if it starts doing work instead of delegating.  
负责人可能会在所有任务实际完成前就决定团队已经结束。如果发生这种情况，告诉它继续进行。你也可以告诉负责人在开始工作而不是分配任务之前等待队友完成。

### Orphaned tmux sessions 遗弃的 tmux 会话

If a tmux session persists after the team ends, it may not have been fully cleaned up. List sessions and kill the one created by the team:  
如果一个 tmux 会话在团队结束后仍然存在，它可能没有被完全清理。列出会话并杀死团队创建的那个会话：

## Limitations 限制

Agent teams are experimental. Current limitations to be aware of:  
代理团队是实验性的。需要注意的当前限制：
- **No session resumption with in-process teammates**: `/resume` and `/rewind` do not restore in-process teammates. After resuming a session, the lead may attempt to message teammates that no longer exist. If this happens, tell the lead to spawn new teammates.  
	无法与进程内队友恢复会话： `/resume` 和 `/rewind` 不会恢复进程内队友。恢复会话后，负责人可能会尝试联系不再存在的队友。如果发生这种情况，告诉负责人生成新的队友。
- **Task status can lag**: teammates sometimes fail to mark tasks as completed, which blocks dependent tasks. If a task appears stuck, check whether the work is actually done and update the task status manually or tell the lead to nudge the teammate.  
	任务状态可能滞后：队友有时会失败标记任务为已完成，这会阻塞依赖的任务。如果任务看起来卡住了，检查工作是否真的完成，手动更新任务状态或告诉负责人提醒队友。
- **Shutdown can be slow**: teammates finish their current request or tool call before shutting down, which can take time.  
	关闭可能较慢：团队成员在关闭前会完成当前请求或工具调用，这可能需要时间。
- **One team per session**: a lead can only manage one team at a time. Clean up the current team before starting a new one.  
	每个会话一个团队：负责人一次只能管理一个团队。开始新团队前请先清理当前团队。
- **No nested teams**: teammates cannot spawn their own teams or teammates. Only the lead can manage the team.  
	不允许嵌套团队：团队成员不能自行创建团队或团队成员。只有负责人可以管理团队。
- **Lead is fixed**: the session that creates the team is the lead for its lifetime. You can’t promote a teammate to lead or transfer leadership.  
	负责人固定：创建团队的会话在其整个生命周期中都是负责人。你不能将团队成员提升为负责人或转移领导权。
- **Permissions set at spawn**: all teammates start with the lead’s permission mode. You can change individual teammate modes after spawning, but you can’t set per-teammate modes at spawn time.  
	在生成时设置的权限：所有队友都以领导权限模式开始。生成后，您可以更改单个队友的模式，但在生成时无法设置每个队友的模式。
- **Split panes require tmux or iTerm2**: the default in-process mode works in any terminal. Split-pane mode isn’t supported in VS Code’s integrated terminal, Windows Terminal, or Ghostty.  
	分割窗格需要 tmux 或 iTerm2：默认的进程内模式在任何终端中都能工作。分割窗格模式不受 VS Code 的集成终端、Windows Terminal 或 Ghostty 支持。

**`CLAUDE.md` works normally**: teammates read `CLAUDE.md` files from their working directory. Use this to provide project-specific guidance to all teammates.  
`CLAUDE.md` 正常工作：队友从他们的工作目录读取 `CLAUDE.md` 文件。使用此功能向所有队友提供项目特定的指导。

Explore related approaches for parallel work and delegation:  
探索并行工作和委托的相关方法：
- **Lightweight delegation**: [subagents](https://code.claude.com/docs/en/sub-agents) spawn helper agents for research or verification within your session, better for tasks that don’t need inter-agent coordination  
	轻量级委托：子代理在你的会话中为研究或验证生成助手代理，更适合不需要代理间协调的任务
- **Manual parallel sessions**: [Git worktrees](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) let you run multiple Claude Code sessions yourself without automated team coordination  
	手动并行会话：Git 工作树允许您自行运行多个 Claude Code 会话，无需自动团队协调
- **Compare approaches**: see the [subagent vs agent team](https://code.claude.com/docs/en/features-overview#compare-similar-features) comparison for a side-by-side breakdown  
	对比方法：查看子代理与代理团队的对比，以进行并排分析

[Create custom subagents 创建自定义子代理](https://code.claude.com/docs/en/sub-agents) [Create plugins 创建插件](https://code.claude.com/docs/en/plugins)