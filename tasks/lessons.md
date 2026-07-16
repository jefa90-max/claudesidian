# Lessons

- 讨论教程载体时，要区分“内容模块化”和“拆成多个文件”。飞书文档支持目录导航，因此用户要求单文档时，可以采用“前部总教程、后部分步骤手册”的分层结构，不要擅自拆成多篇文档。
- 用户要求“通用连接教程”时，只解释连接链路和工具入口，不要擅自加入 Docker、Git、Node.js、数据库或 AI 编程协作方法。当前约定是 Claude Code 作为 Mac mini 上的 CLI，通过 VS Code Remote SSH 终端使用；Codex 通过 Codex 桌面端的远程连接功能使用。
- 手机端要按真实链路分别描述：Claude Code 通过手机 Tailscale 和 Termius SSH 进入 Mac mini，再恢复 tmux 中的 CLI 会话；Codex 在手机界面中直接进入 Remote，但底层仍经过已配对的桌面主机及其 Mac mini SSH 连接。不要把手机 App 写成 SSH 客户端，也不要省略 Termius 或桌面主机。
- 面向非技术读者介绍 VS Code Remote SSH 时，不能只说“访问远程文件”。必须明确说明连接后左侧资源管理器会像本地文件夹一样显示 Mac mini 的目录和文件，可以点击、展开、搜索和编辑，并提示如何识别当前是远程窗口。
