---
title: "How to Build a Software Factory with Claude Code That Ships Features While You Sleep"
source: "https://x.com/sairahul1/status/2058832033628241931"
author:
  - "[[@sairahul1]]"
published: 2026-05-25
created: 2026-05-26
description: "I thought I was using AI to code.I was actually just typing faster.Here is the difference — and the 7-agent system that changed everything.S..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HJJdb6laMAAMIpe?format=jpg&name=large)

I thought I was using AI to code.

I was actually just typing faster.

Here is the difference — and the 7-agent system that changed everything.

Save this. It will save you months.

## THE PROBLEM NOBODY TALKS ABOUT

**The loop that feels productive but isn't:**

![图像](https://pbs.twimg.com/media/HJJZuz-bUAAIciP?format=jpg&name=large)

→ Ask Claude to build a feature → It generates code → Something breaks → Paste the error back → It patches it → Something else breaks → Ask again

Day 1: this feels like magic.

Day 30: you're spending more time supervising AI than you used to spend writing code.

Same logic appears in 3 different places.

Claude forgot the convention you set up two weeks ago.

New features break old ones.

Tests are missing or shallow.

You wake up and realize: the AI isn't failing.

Your workflow is.

**The real problem is structural.**

When you type "build this feature" into Claude Code, you're asking one AI session to be:

→ Product analyst → Architect → Backend engineer → Frontend engineer → Test engineer → Code reviewer

All at once.

In the same messy conversation.

Wrong assumptions in the plan become wrong database models.

Wrong database models become wrong APIs.

Wrong APIs become wrong UIs.

By the time you notice, the mistake has spread everywhere.

This is called vibe coding.

And it has a hard ceiling.

## THE SHIFT: FROM VIBE CODING TO A SOFTWARE FACTORY

**What actually changes everything:**

![图像](https://pbs.twimg.com/media/HJJZ1qDaYAANkx0?format=jpg&name=large)

Real engineering teams don't work in one big conversation.

Different people own different jobs:

→ Someone clarifies the user problem → Someone thinks about architecture → Someone builds the API → Someone builds the UI → Someone thinks about edge cases → Someone reviews

When you collapse all of that into one AI session, mistakes compound silently.

The fix is to split the work across **specialized agents**.

Each agent gets: → One focused job → Its own clean context window → Only the tools it actually needs → Strict rules about what it cannot touch

The result: a software factory.

One developer + seven focused agents = a coordinated team.

Here are the seven agents that make it work.

## THE 7 AGENTS

## Agent 1: The Codebase Researcher

![图像](https://pbs.twimg.com/media/HJJakAcbsAAEelQ?format=jpg&name=large)

The biggest mistake developers make with AI?

Asking for code as the first move.

The AI accepts the prompt, makes guesses to fill the gaps, and starts generating.

That's when bad designs sneak in.

The Codebase Researcher fixes this.

Its only job: **inspect the codebase and explain how things work — before a single line is written.**

What it does: → Maps the relevant files and their roles → Documents existing patterns to follow → Finds similar features already built → Flags risks (timezone, multi-tenant, retry logic) → Lists what tests will need updating

What it cannot do: → Edit files (read-only access only) → Run any command that modifies state → Make assumptions — it asks instead

Tools: Read, Grep, Glob only.

The rule: **explore before you build, every single time.**

The Researcher runs first. Always.

## Agent 2: The Story Writer

![图像](https://pbs.twimg.com/media/HJJasbubsAA7kJn?format=jpg&name=large)

Most features fail not because the code was wrong.

But because the problem was never clearly defined.

The Story Writer turns a rough feature idea into a real user story before any technical decisions are made.

Input it receives: → Your rough feature description → The Researcher's findings

What it produces:

**One user story:**"As a \[role\], I want \[behaviour\], so that \[outcome\]."

**Acceptance criteria:**Statements a test can verify directly. Happy path. Failure paths. Business rules.

**Edge cases:**Boundaries, retries, multi-tenant concerns.

**Out of scope:**What is explicitly NOT being built.

**Open questions:**Things it genuinely doesn't know — never guesses.

What it cannot do: → Invent business rules → Write any code or technical design → Move forward if something is genuinely unclear

Tools: Read only.

The rule: **you read this story and approve it before anything else happens.**

This is the human checkpoint that saves everything downstream.这是人类检查点，它保存了下游的一切。

## Agent 3: The Spec WriterAgent 3: 规格编写者

![图像](https://pbs.twimg.com/media/HJJa0pra4AAE8NU?format=jpg&name=large)

Once the story is approved, the Spec Writer turns it into a technical brief.故事获批后，规格撰写人将其转化为技术简报。

This is the blueprint every build agent follows.这是每个构建代理遵循的蓝图。

Input it receives: → Your approved user story → The Researcher's findings → Your project's CLAUDE.md rules接收的输入：→ 你已批准的用户故事 → 研究员的发现 → 你项目的 CLAUDE.md 规则

What it produces:它产生的内容：

→ Data model changes (fields, types, migrations) → Background flow / process flow → API changes (endpoints, request/response shapes) → Frontend changes (components, pages, hooks) → Tests required (success, failure, edge cases) → Risks and open questions → Every file that will change→ 数据模型变更（字段、类型、迁移）→ 后台流程/处理流程 → API 变更（端点、请求/响应结构）→ 前端变更（组件、页面、钩子）→ 所需测试（成功、失败、边界情况）→ 风险与待定问题 → 所有将变更的文件

What it cannot do: → Edit any file → Invent new infrastructure — calls it out explicitly instead → Skip tenant isolation or timezone concerns → Leave questions unanswered无法做到的事：→ 编辑任何文件 → 凭空创造新基础设施——而是明确指出来 → 忽略租户隔离或时区问题 → 对问题置之不理

Tools: Read, Grep, Glob only.工具：仅限读取、搜索、通配匹配。

The rule: **this brief is the second human checkpoint.**规则：这份简报是第二个人工检查点。

You read it and approve it before a single file is touched.在触及任何文件之前，你需要阅读并批准它。

If you see "store IDs in memory" — that's your red flag.如果你看到“将 ID 存储在内存中”——那就是你的警示信号。

Catch it now. Not after 10 files have been changed.现在就抓住它，别等到改了 10 个文件之后。

## Agent 4: The Backend Builder智能体 4：后端构建者

![图像](https://pbs.twimg.com/media/HJJa6daacAAhfq5?format=jpg&name=large)

Now the building starts.现在开始建造。

The Backend Builder implements the backend half of the feature — and only the backend half.后端构建器实现了该功能的后端部分——且仅实现后端部分。

Input it receives: → Approved technical brief → Researcher's findings → Your project's CLAUDE.md它接收的输入：→ 已批准的技术简报 → 研究人员的发现 → 你项目的 CLAUDE.md

What it builds: → API routes → Services and business logic → Database access and migrations → Background jobs → Unit tests for everything it writes构建内容：→ API 路由 → 服务与业务逻辑 → 数据库访问与迁移 → 后台任务 → 为其所写内容编写的单元测试

What it cannot do: → Touch React components, pages, or client-side hooks (that's Agent 5) → Invent new dependencies without instruction → Modify files outside agreed scope → Stop without running typecheck, lint, and the test suite无法做到：→ 操作 React 组件、页面或客户端钩子（那是 Agent 5 的职责）→ 未经指示擅自引入新依赖项→ 修改约定范围外的文件→ 未运行类型检查、代码检查和测试套件就停止工作

After finishing, it returns a summary: → Every file added or edited → Every existing helper or pattern reused → Any CLAUDE.md rule that would have helped完成后，它会返回一个摘要：→ 每个新增或编辑的文件 → 每个被复用的现有辅助工具或模式 → 任何本应有所帮助的 CLAUDE.md 规则

Tools: Read, Edit, Write, Bash — scoped to backend folders only.工具：读取、编辑、写入、Bash——仅限后端文件夹范围。

The separation is the point.分离即是关键。

**Backend Builder cannot accidentally break the frontend. Ever.后端构建者绝不能意外破坏前端。永远不能。**

## Agent 5: The Frontend BuilderAgent 5：前端构建者

![图像](https://pbs.twimg.com/media/HJJbDHRaYAAWqpz?format=jpg&name=large)

The Frontend Builder implements the UI half — and only the UI half.前端构建器实现了 UI 部分——且仅实现 UI 部分。

It reads the Backend Builder's summary first.它首先阅读后端构建者的摘要。

This matters.这很重要。

It consumes the API exactly as the backend produced it.它完全按照后端生成的 API 格式进行消费。

It does not invent new endpoints.它不会凭空创造新的端点。

If the API shape is wrong for the UI, it surfaces the mismatch as feedback — not as a patch.如果 API 的结构对 UI 来说不合适，它会将这种不匹配作为反馈呈现出来，而不是进行修补。

Input it receives: → Approved technical brief → Researcher's findings → Backend Builder's summary (the API contract)接收的输入：→ 已批准的技术简报 → 研究人员的发现 → 后端构建者的总结（API 合约）

What it builds: → React components and pages → Client-side hooks and state → Loading and error states → Component and unit tests for everything it writes构建内容：→ React 组件与页面 → 客户端钩子与状态 → 加载与错误状态 → 为其编写的所有内容提供组件与单元测试

What it cannot do: → Touch services, API routes, workers, or migrations (that's Agent 4) → Invent endpoints or response shapes → Add dependencies without instruction → Stop without running typecheck, lint, and the test suite它不能做的事：→ 触及服务、API 路由、工作进程或迁移（那是 Agent 4 的职责）→ 凭空创建端点或响应结构→ 未经指示添加依赖项→ 在未运行类型检查、代码检查和测试套件的情况下停止

Tools: Read, Edit, Write, Bash — scoped to frontend folders only.工具：读取、编辑、写入、Bash —— 仅限前端文件夹范围。

Two builders.两位建造者。

Two clean context windows.两个干净的上下文窗口。

Zero chance one breaks the other's work.绝无可能一方破坏另一方的工作。

## Agent 6: The Test VerifierAgent 6：测试验证器

![图像](https://pbs.twimg.com/media/HJJbJ2SbIAEmcNL?format=jpg&name=large)

Both builders wrote unit tests for their own code.两位开发者都为自己的代码编写了单元测试。

That's not enough.这还不够。

The Test Verifier does one thing only: **prove that the feature actually does what the user story said it should.**测试验证器只做一件事：证明该功能确实实现了用户故事所描述的功能。

It writes acceptance tests.它编写验收测试。

Not unit tests.不是单元测试。

Acceptance tests.验收测试。

These test the feature from the outside — the way a real user would experience it.这些测试从外部检验功能——就像真实用户会体验到的那样。

Input it receives: → Approved user story (with all acceptance criteria) → Approved technical brief → Both builders' summaries输入内容：→ 已批准的用户故事（包含所有验收标准）→ 已批准的技术概要 → 两位开发者的总结

What it produces: → One acceptance test file covering every acceptance criterion → A report: which criteria passed, which failed, which can't be covered cleanly

What it cannot do: → Modify any backend or frontend code → Invent workarounds for untestable criteria → Mark a criterion as covered if it genuinely isn't

If a test fails: **the feature doesn't satisfy the story.**如果测试失败：该功能不符合用户故事的要求。

It reports exactly which criterion failed.

It does not patch the code.

That goes back to the right builder.

Tools: Read, Edit, Write (test files only), Bash.

The rule: **you don't have a feature until the acceptance tests pass.**规则：在验收测试通过之前，你并不拥有该功能。

## Agent 7: The Implementation Validator

![图像](https://pbs.twimg.com/media/HJJbQW2awAAyrBn?format=jpg&name=large)

This is the agent that catches everything everyone else missed.

The Validator compares the current implementation against the approved story and brief — and reports gaps.

It never fixes anything.

It just tells the truth.

Every check it runs, every time:

→ Acceptance criteria from the story not yet implemented → Failure paths with no test coverage → Security issues: missing auth checks, tenant isolation gaps, secrets in logs, raw errors exposed to clients → Files changed outside agreed scope → Patterns inconsistent with CLAUDE.md or existing code → Duplicate logic that should reuse existing helpers → Timezone or multi-tenant concerns from the brief that were quietly skipped

Output is always grouped by severity:

**Critical** — must fix before merge **Important** — should fix before merge **Minor** — opinion-based, reviewer's call严重 — 合并前必须修复 重要 — 合并前应修复 次要 — 基于意见，由审阅者决定

Every finding includes the file path and line number.

If there's nothing wrong, it says so plainly.

It doesn't invent issues to look thorough.

Tools: Read, Grep, Glob only.

This agent is why the factory is trustworthy.

A self-graded paper is worthless.

A validator that sees only what's on disk — not how it was written — is honest.

## HOW THE CHAIN RUNS

**The full flow — one prompt starts it all:**

![图像](https://pbs.twimg.com/media/HJJcDPQbsAA61t6?format=jpg&name=large)

You open Claude Code and type:

"Build invoice reminders for invoices unpaid for more than 7 days."

Here's what happens without you typing anything else:

**Step 1 → Researcher** maps your invoice, payment, and email code. Returns relevant files, existing patterns, risks.步骤 1 → 研究人员映射你的发票、支付和邮件代码。返回相关文件、现有模式及风险。

**Step 2 → Story Writer** produces the user story and acceptance criteria.步骤 2 → 故事编写者生成用户故事和验收标准。

**⏸** **PAUSE: You read and approve the story.**⏸ 暂停：你阅读并批准了故事。

**Step 3 → Spec Writer** turns the approved story into a technical brief.步骤 3 → 规格撰写人将已批准的故事转化为技术简报。

**⏸** **PAUSE: You read and approve the brief.**(Catch that "store IDs in memory" mistake right here.)⏸ 暂停：你阅读并批准了简报。（就在这里发现那个“将 ID 存储在内存中”的错误。）

**Step 4 → Backend Builder** implements the service, API route, BullMQ job, and unit tests. Returns: files changed, patterns reused, all tests green.步骤 4 → 后端构建者实现服务、API 路由、BullMQ 任务和单元测试。返回：已更改的文件、复用的模式、所有测试通过。

**Step 5 → Frontend Builder** reads the Backend Builder's API summary, builds the admin UI tile and reminder button, writes component tests. All tests green.步骤 5 → 前端构建器读取后端构建器的 API 摘要，构建管理界面磁贴和提醒按钮，编写组件测试。所有测试通过。

**Step 6 → Test Verifier** writes acceptance tests for all six acceptance criteria. Reports: 7 passing, 1 failing — manual trigger doesn't check tenant ownership.步骤 6 → 测试验证者为全部六项验收标准编写验收测试。报告显示：7 项通过，1 项失败——手动触发未检查租户所有权。

**Step 7 → Validator** finds it. Reports as Critical with file path and line number.步骤 7 → 验证者发现问题。报告为严重问题，并附上文件路径和行号。

**→ Loop back to Backend Builder.** Fix applied. All 8 acceptance tests pass. Validator runs again. Clean.→ 返回后端构建者。修复已应用。全部 8 项验收测试通过。验证者再次运行。结果干净。

**⏸** **PAUSE: You review and open the PR.**⏸ 暂停：你审查并打开 PR。

Three human checkpoints.

Everything else runs on its own.

## THE FOUNDATION: BEFORE AGENTS WORK, YOU NEED THIS

**CLAUDE.md — the memory that survives every session:**

![图像](https://pbs.twimg.com/media/HJJcHnxaMAEPefe?format=jpg&name=large)

Every time you open Claude Code, it starts with zero memory.

CLAUDE.md fixes this.

It's a Markdown file at your repo root that loads automatically every session.

It's where permanent project facts live:

→ Your stack (Next.js App Router, Node.js, Prisma, BullMQ, Resend) → Your commands (npm run dev, npm test, npx prisma migrate dev) → Architecture rules ("Business logic lives in services. API routes stay thin.") → What not to do ("Do not add cron — use BullMQ. Do not log raw payment payloads.") → Pointers to deeper docs (docs/billing.md, docs/architecture.md)

Keep it 100-300 lines.

Every time AI makes a mistake that surprises you, ask: would a rule in CLAUDE.md have prevented this?

Add the rule.

In a few weeks, your CLAUDE.md becomes a record of every assumption the AI got wrong — and your sessions get noticeably better.

**Context drift — the silent killer:**

Most Claude Code sessions don't fail dramatically.

They drift.

A wrong assumption enters the context.

The model keeps building on top of it.

You ask Claude to build subscription management.

It designs: User → Subscription.

You remember: subscriptions belong to the company, not the user.

If you just say "no, subscriptions belong to companies" — Claude patches.

Now you have both user.subscriptionId and company.subscriptionId floating around.

**Rule:**

→ Small typo? Correct it inline. → Wrong architectural assumption? Throw the conversation away and start fresh with the right assumption baked into the first prompt.

A clean session with the right mental model beats a patched session every time.

## THE RESULTS: WHAT ACTUALLY CHANGES

**Before the factory:**

→ Vibe coding loop: prompt → generate → error → patch → repeat → Session context fills up with noise → Wrong assumptions compound into broken features → One engineer can only do one thing at a time → Every feature waits for the right person to be available

**After the factory:**

→ Structured chain: research → story → brief → build → verify → validate → Each agent gets a clean context window with only what it needs → Wrong assumptions get caught at the brief approval — not after 10 files → One engineer ships a complete vertical slice: backend, frontend, tests, validation → The team's best knowledge lives in the agents — not trapped in people

**The real shift:**

The payments specialist builds a payments-integration agent.

Now every engineer on the team can ship a feature that touches billing.

Without waiting.

Without a handoff.

The frontend lead's component patterns live in the frontend-builder agent.

The DevOps engineer's CI checks live in a hook.

The QA lead's edge cases live in the test-verifier rules.

**Expert knowledge, shared as agents.**

Not trapped in availability.

## HOW TO BUILD YOURS THIS WEEKEND

**8-step setup checklist:**

![图像](https://pbs.twimg.com/media/HJJcLzybIAAGyJo?format=jpg&name=large)

**1.** Install Claude Code → [code.claude.com](https://code.claude.com/)

**2.** Create the folder structure: → .claude/agents/ → .claude/skills/feature-factory/ → .claude/skills/build-with-tests/ → .claude/hooks/2. 创建文件夹结构：→ .claude/agents/ → .claude/skills/feature-factory/ → .claude/skills/build-with-tests/ → .claude/hooks/

**3.** Write your CLAUDE.md (100–300 lines: stack, commands, architecture rules, don't-do list)3. 编写你的 CLAUDE.md 文件（100-300 行：技术栈、命令、架构规则、禁止事项清单）

**4.** Create the 7 agents using the /agents command in Claude Code. Describe each agent's role. Claude writes the file. You review and commit.4. 在 Claude Code 中使用 /agents 命令创建 7 个智能体。描述每个智能体的角色。Claude 编写文件。你进行审查并提交。

**5.** Create the feature-factory orchestrator skill. Ask Claude to write it — it reads your 7 agent files and wires the chain.5. 创建特性工厂编排器技能。让 Claude 来编写——它会读取你的 7 个代理文件并串联整个流程。

**6.** Create the build-with-tests skill. Describes how your team builds: match existing patterns, write tests alongside code, run typecheck at the end.6. 创建“测试驱动构建”技能。描述你的团队如何构建：遵循现有模式，在编写代码的同时编写测试，最后运行类型检查。

**7.** Add a pre-commit hook. Blocks commits that include .env, .key, .pem, or secrets.json files. Takes 5 minutes. Prevents disasters.7. 添加预提交钩子。阻止包含 .env、.key、.pem 或 secrets.json 文件的提交。耗时 5 分钟，可避免灾难性后果。

**8.** Run one real feature through the full chain. Pick something small. Watch where it stumbles. Add rules. The factory tunes itself.8. 将一项真实功能完整跑通整个流程。选择一个小功能，观察它在何处卡壳，然后补充规则。工厂会自行调优。

**Total time: 2–3 hours.**

Then run a few features.

After 3–4, the factory knows your codebase.

You'll spend less time supervising.

More time deciding what to build next.

## THE 7 AGENTS — QUICK REFERENCE

→ **Researcher** — maps the code before anything is built (Read only) → **Story Writer** — turns idea into user story with acceptance criteria (Read only) → **Spec Writer** — turns story into technical brief (Read only) → **Backend Builder** — builds API, services, jobs, unit tests (backend folders only) → **Frontend Builder** — builds components, pages, hooks, UI tests (frontend folders only) → **Test Verifier** — writes acceptance tests against the user story (test files only) → **Validator** — compares implementation against story and brief, reports gaps (Read only)→ 研究员 — 在构建任何内容之前绘制代码地图（仅读取） → 故事撰写者 — 将想法转化为包含验收标准的用户故事（仅读取） → 规格编写者 — 将故事转化为技术简报（仅读取） → 后端构建者 — 构建 API、服务、任务、单元测试（仅限后端文件夹） → 前端构建者 — 构建组件、页面、钩子、UI 测试（仅限前端文件夹） → 测试验证者 — 根据用户故事编写验收测试（仅限测试文件） → 验证者 — 将实现与故事和简报进行对比，报告差距（仅读取）

**3 human checkpoints:**→ Approve the story → Approve the brief → Approve the PR3 个人工检查点：→ 批准故事 → 批准简报 → 批准公关

Everything else runs on its own.

Most developers using Claude Code are still vibe coding.

Prompting → generating → patching → hoping.

That's not wrong.

It's just a ceiling.

The factory doesn't remove you from the process.

It removes you from the parts that don't need you.

You stay in the loop where your judgment matters:

Is this the right problem? Is this the right design? Is this safe to ship?

The agents handle everything in between.

That's the difference between using AI as a faster keyboard —

and using AI as a coordinated team.

If this was useful:

→ Repost to share it with your network → Follow [@sairahul1](https://x.com/@sairahul1) for more breakdowns like this → Bookmark this — you'll want to reference the 7 agents

I write about AI, building products, and systems that work while you sleep.