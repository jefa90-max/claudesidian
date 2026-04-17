## 一、前置条件（准备环境）

- 已安装 Git、Python/Node（依项目而定）、并已在项目根目录启用 Git 仓库。
    
- 已安装并能在项目根目录启动 **Claude Code**（终端版）。
    
- 你希望同时开发多项功能（前端/测试/质量工具等），并避免不同会话互相覆写。
    

> - 实现思路：用 **Git worktrees** 为每个功能创建隔离的工作副本；每个 worktree 内单独开一个 **Claude Code** 会话并行开发，最后再合并回主分支。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)
>     

---

## 二、在 `.claude/commands/` 中创建“自定义命令”

目的：用一个自定义 **slash** 命令快速给 Claude Code下达“实现某功能”的标准化提示，并把前端改动记录到变更日志里。

660. 在项目根目录创建命令目录：
    

`mkdir -p .claude/commands`

2. 新建命令文件（示例命令名：`implement-feature`）：
    

# `文件：.claude/commands/implement-feature.md` `# 说明：此处是示意内容，可按你的团队规范调整` `# 要点：` `# - 使用 $ARGUMENTS 接收命令参数（功能描述）` `# - 明确只做前端功能改动` `# - 要求把前端变更写入 frontend-changes.md` `Implement a new frontend feature: $ARGUMENTS` `Constraints:` `- Only modify frontend code and assets.` `- Document all changes in a file named "frontend-changes.md" at project root.` `- Keep commits small and descriptive.`

> 关键点：`.claude/commands` 里的自定义命令不会自动进入上下文（不同于 `CLAUDE.md` 的全局说明），仅在调用该命令时生效，适合“可选用”的工作流指令。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

3. 重新启动 Claude Code，以便扫描到新命令（或直接在终端退出/重开会话）：
    

# `关闭后在项目根目录重新启动` `claude code`

> 你应能在命令列表中看到 `implement-feature` 以及它的描述（来自该 Markdown 的首段）。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

4. 首次把 `.claude` 目录提交到仓库（也可让 Claude 帮你“Add and commit changes made.”）：
    

`git add .claude` `git commit -m "Add custom command: implement-feature"`

> 提示：允许的系统命令会记录在 `.claude/settings.local.json`；也可用 `/permissions` 管理允许列表。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 三、用 Git worktrees 搭建“三路并行”开发环境

目标：创建三个隔离的工作目录与分支，分别做“前端功能 / 测试增强 / 质量工具”。

1779. 创建专用目录并添加 worktrees：
    

`mkdir .trees` `git worktree add .trees/ui_feature -b ui_feature` `git worktree add .trees/testing_feature -b testing_feature` `git worktree add .trees/quality_feature -b quality_feature` `git worktree list`

> 如上会看到当前 `main` 与三个 worktree 列表。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

2. 在三个 worktree 目录**分别**打开终端，并在每个里启动 Claude Code：
    

# `终端 A（前端）` `cd .trees/ui_feature` `claude code` `# 终端 B（测试）` `cd .trees/testing_feature` `claude code` `# 终端 C（质量）` `cd .trees/quality_feature` `claude code`

> 现在你拥有三个互不覆写的 Claude 会话，可真正并行推进。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 四、三路并行开发：示例指令与确认流程

> 下面以课程示例为准：前端做“深浅色主题切换”、后端测试增强、质量工具接入。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

### A. 前端功能（ui_feature）

在 Claude 会话中调用自定义命令并传参（功能描述）：

`/implement-feature "Add a UI toggle to switch between dark and light themes, position it properly, and update navigation if needed. Document all changes in frontend-changes.md."`

- 等 Claude 生成变更请求，按需 **Approve / Confirm**；
    
- 完成后，再补充“Light theme variant”等细节，用同一命令继续推进：
    

`/implement-feature "Add the light theme variant and ensure consistent styles and interactions."`

> 期间可在浏览器验证 UI 行为。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

### B. 测试增强（testing_feature）

为现有 FastAPI 端点补充测试：

`/implement-feature "Enhance the existing testing framework and add additional tests for FastAPI endpoints."`

> 如果脚本或依赖未知，按提示安装或修正：

`uv pip install -r requirements-dev.txt` `pytest -q`

（依你的项目工具链调整命令）[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

### C. 代码质量工具（quality_feature）

接入/配置格式化与质量检查（示例：Black/ruff/isort 等），并在 `pyproject.toml` 中维护统一配置：

`/implement-feature "Add essential code quality tools (formatter, linter, type-check if applicable) and development scripts; update pyproject.toml accordingly."`

> 本阶段常见文件：`pyproject.toml`、`package.json`（如有前端工具）、CI 脚本等。不同 worktree 可能同时改到 `pyproject.toml`，后续合并会自动/半自动解决冲突。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 五、边做边提交流程（每个 worktree 内）

完成一个阶段就提交，保证小步快跑、信息可追溯：

`git add -A` `git commit -m "UI: add dark/light theme toggle and related components"` `# 或` `git commit -m "Tests: add FastAPI endpoint tests and fixtures"` `# 或` `git commit -m "Quality: add formatter/linter and dev scripts; update pyproject.toml"`

> 你也可以把“提交规范”做成另一条自定义命令，标准化团队 commit 风格。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 六、合并回主分支并自动解决冲突

4076. 回到主仓库根（非 .trees 内）切换到主分支：
    

`git switch main`

2. 合并三个分支（可逐个，也可循环；若愿意，也可直接让 Claude 执行并解决冲突）：
    

`git merge ui_feature` `git merge testing_feature` `git merge quality_feature`

> 课程演示是“让 Claude Code 运行 git merge，把 `.trees` 里所有 worktrees 合并并自动处理冲突”。当 `pyproject.toml` 在多处修改时，Claude 会分析差异并完成合并，然后提交解决后的结果。随后运行测试，确认一切通过。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

3. 合并完成后，验证与回归：
    

`pytest -q # 后端/接口测试` `npm run build # 或前端构建命令` `npm run dev # 本地验证 UI 行为（查看主题切换）`

> 你应能在浏览器看到“深/浅色主题切换”已生效；质量工具（如 Black）格式化也已配置完成。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 七、（可选）清理 worktrees 与分支

如果不再需要这些临时工作区，可移除以保持整洁（**务必确认改动已合并**）：

`git worktree remove .trees/ui_feature` `git worktree remove .trees/testing_feature` `git worktree remove .trees/quality_feature` `git branch -D ui_feature` `git branch -D testing_feature` `git branch -D quality_feature`

> 也可以保留 worktrees 做后续增量开发。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)

---

## 八、常见问题（Q&A）

- **为什么要用 worktrees，不直接多开终端？** 多开终端对同一工作副本会互相覆写文件，极易引发混乱；worktrees 提供“隔离副本 + 便捷合并”的并行开发体验。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)
    
- **自定义命令与** **`CLAUDE.md`** **的区别？** `CLAUDE.md` 是“全局上下文”；`commands/` 下的命令只在调用时生效，适合把“特定流程/动作”标准化。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)
    
- **权限反复确认很麻烦？** 在 `.claude/settings.local.json` 中记录已允许的命令，或用 `/permissions` 统一管理。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)
    
- **合并冲突怎么办？** 让 Claude Code 分析冲突并完成合并；配合完善的自动化测试即可保证安全落地。[DeepLearning.AI - Learning Platform](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/oo58a/adding-multiple-features-simultaneously)
    

---

## 九、一次性脚本（可选，加速搭建）

> 下面脚本把“三路并行”的基础设施一次性搭好（在项目根目录执行）。

**Bash（macOS/Linux/WSL）：**

`mkdir -p .claude/commands .trees` `cat > .claude/commands/implement-feature.md <<'EOF'` `Implement a new frontend feature: $ARGUMENTS` `Constraints:` `- Only modify frontend code and assets.` `- Document all changes in a file named "frontend-changes.md" at project root.` `- Keep commits small and descriptive.` `EOF` `git add .claude && git commit -m "Add custom command: implement-feature" || true` `git worktree add .trees/ui_feature -b ui_feature` `git worktree add .trees/testing_feature -b testing_feature` `git worktree add .trees/quality_feature -b quality_feature` `echo "Worktrees ready. Open three terminals and run 'claude code' in each."`

**PowerShell（Windows）：**

`New-Item -ItemType Directory -Force -Path .claude\commands | Out-Null` `New-Item -ItemType Directory -Force -Path .trees | Out-Null` `@'` `Implement a new frontend feature: $ARGUMENTS` `Constraints:` `- Only modify frontend code and assets.` `- Document all changes in a file named "frontend-changes.md" at project root.` `- Keep commits small and descriptive.` `'@ | Set-Content -NoNewline .\.claude\commands\implement-feature.md` `git add .claude` `git commit -m "Add custom command: implement-feature"` `git worktree add .trees/ui_feature -b ui_feature` `git worktree add .trees/testing_feature -b testing_feature` `git worktree add .trees/quality_feature -b quality_feature` `Write-Host "Worktrees ready. Open three terminals and run 'claude code' in each."`

---

## 十、教学要点回顾（与课程演示一致）

- 新建 `implement-feature` 自定义命令并通过 `$ARGUMENTS` 传入功能说明，限定仅改前端并写入 `frontend-changes.md`；
    
- 通过 `git worktree add` 建立 `ui_feature`、`testing_feature`、`quality_feature` 三个并行工作区；
    
- 在三个工作区各自运行 **Claude Code**，分别：实现主题切换、增强 FastAPI 端点测试、接入代码质量工具（修改 `pyproject.toml` 等）；
    
- 边做边提交，提交信息清晰可读；
    
- 回到主分支批量合并三路改动，Claude Code 协助自动化解决冲突并提交；
    
- 运行测试与构建验证成果，浏览器中确认前端“深/浅色主题切换”已生效；
    
- 需要时移除 worktrees 或保留以便后续增量开发。
    

  

# 在单个工作树里先跑起来再提交

192. 进入你要测试的工作树
    

`cd .trees/ui_feature # 换成你的那个工作树目录` `git status`

2. 安装依赖（每个工作树都有独立的 node_modules / venv） **Node/前端：**
    

`npm install # 或 pnpm install / yarn`

**Python/FastAPI 等：**

`uv pip install -r requirements.txt # 或 pip install -r requirements.txt`

3. 启动本地开发服务器（未提交的改动会被实时加载） **常见前端（Vite/Next 等）：**
    

`npm run dev`

如需和其它工作树的服务并行运行，记得换端口： **macOS/Linux/WSL：**

`PORT=3001 npm run dev`

**Windows PowerShell：**

`$env:PORT=3001; npm run dev`

**FastAPI（举例）：**

`uvicorn app.main:app --reload --port 8001`