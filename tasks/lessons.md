# Lessons

- 讨论教程载体时，要区分“内容模块化”和“拆成多个文件”。飞书文档支持目录导航，因此用户要求单文档时，可以采用“前部总教程、后部分步骤手册”的分层结构，不要擅自拆成多篇文档。
- 用户要求“通用连接教程”时，只解释连接链路和工具入口，不要擅自加入 Docker、Git、Node.js、数据库或 AI 编程协作方法。当前约定是 Claude Code 作为 Mac mini 上的 CLI，通过 VS Code Remote SSH 终端使用；Codex 通过 Codex 桌面端的远程连接功能使用。
- 手机端要按真实链路分别描述：Claude Code 通过手机 Tailscale 和 Termius SSH 进入 Mac mini，再恢复 tmux 中的 CLI 会话；Codex 通过 Codex 手机 App 直接使用远程连接。不要把 Codex App 写成 SSH 客户端，也不要省略 Termius。
