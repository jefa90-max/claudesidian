---

title: "Mac mini 远程开发工作流完全手册"

subtitle: "VS Code Remote SSH、tmux、Tailscale、Docker、Claude Code、Codex、Web + 小程序测试发布"

author: "为 乔 定制"

date: "2026-06-15"

lang: zh-CN

---

  
  

# 目录（速览）

  

- 0. 这份手册怎么用

- 1. 总体路线图

- 2. 重要名词解释

- 3. Mac mini 基础系统配置

- 4. 安装基础命令行工具

- 5. SSH 配置：Windows 远程进入 Mac mini

- 6. Tailscale 配置：把 Mac mini 变成安全私网主机

- 7. VS Code Remote SSH：主力开发入口

- 8. tmux 完全入门

- 9. Docker Desktop 安装与配置

- 10. Docker Compose：Postgres + Redis 开发环境

- 11. Docker 的高级但常用配置

- 12. Web 端本地开发流程

- 13. 小程序端开发与体验版流程

- 14. Git 和分支工作流

- 15. GitHub Actions：CI 和自动化部署

- 16. Claude Code 配置和使用

- 17. Codex 配置和使用

- 18. 日常使用场景手册

- 19. 安全清单

- 20. 备份和恢复

- 21. 常见故障排查

- 22. 推荐的每周维护

- 23. 推荐别名

- 24. 一键检查脚本

- 25. 最佳实践总表

- 26. 官方资料来源

- 27. 最短操作清单

  

# 0. 这份手册怎么用

  

这份手册按“先能连上，再能稳定开发，再能安全测试发布”的顺序写。你可以从头照着做，也可以把它当成以后排查问题的说明书。

  

你的目标架构是：

  

```text

Windows 外出电脑

  ├─ VS Code Remote SSH：舒服地打开 Mac mini 上的项目

  ├─ Windows Terminal / PowerShell：备用 SSH 入口

  └─ 浏览器：访问本地转发端口、staging、Claude/Codex 页面

  

Mac mini，常在线开发主机

  ├─ 项目代码、node_modules、Docker 数据都在这里

  ├─ Claude Code / Codex 在这里读写代码、跑命令

  ├─ tmux 保存长期会话，断线不死

  ├─ Docker Desktop 跑 Postgres/MySQL、Redis 等开发依赖

  └─ Tailscale 提供安全私网入口

  

云端 / 平台

  ├─ GitHub / GitLab：代码仓库、CI、PR、Issue

  ├─ Web staging：用户测试站点

  └─ 微信小程序后台：体验版、审核、正式版

```

  

核心原则只有三条：

  

1. Mac mini 是唯一主开发环境，Windows 只是遥控器和驾驶舱。

2. 长任务必须放进 tmux，避免 SSH 或 VS Code 断线后任务蒸发。

3. 用户测试不要依赖 Mac mini 本地服务，要走 staging 和小程序体验版。

  

> 本文里的命令大量使用占位符，例如 `yourname`、`myapp`、`macmini`。复制前先替换成你自己的用户名、项目名和设备名。

  

# 1. 总体路线图

  

## 1.1 第一阶段：能远程登录

  

你要完成：

  

```text

Mac mini 开启 Remote Login

Windows 生成 SSH key

Windows 能 ssh 到 Mac mini

Tailscale 上 Mac mini 和 Windows 能互相看到

VS Code Remote SSH 能打开 Mac mini 上的项目目录

```

  

验收命令：

  

```bash

ssh macmini

whoami

hostname

pwd

```

  

如果能看到 Mac mini 上的用户名、主机名、当前路径，就说明远程入口通了。

  

## 1.2 第二阶段：能稳定开发

  

你要完成：

  

```text

安装 Homebrew、Git、tmux、Node/pnpm

安装 Docker Desktop

配置 Docker 资源

项目目录放到 ~/projects

用 tmux 创建项目会话

在 tmux 里跑 pnpm dev、docker compose、Claude、Codex

```

  

验收命令：

  

```bash

tmux new -As myapp

# Ctrl+b 然后 d 退出

  

tmux ls

tmux attach -t myapp

```

  

## 1.3 第三阶段：能测试发布

  

你要完成：

  

```text

Web 端部署到 staging 域名

小程序上传体验版

后端分 local / staging / production

GitHub Actions 跑 lint/test/build

miniprogram-ci 上传体验版

```

  

验收标准：

  

```text

Web 用户打开 https://staging.xxx.com 测试

小程序体验成员用微信打开体验版测试

正式数据和测试数据隔离

CI 失败时能从 Windows 远程进入 Mac mini 排查

```

  

# 2. 重要名词解释

  

## 2.1 SSH 是什么

  

SSH 是远程登录电脑的协议。你在 Windows 上输入命令，实际是在 Mac mini 上执行。它传文字和命令，不传整块屏幕，所以比远程桌面轻很多。

  

## 2.2 VS Code Remote SSH 是什么

  

VS Code Remote SSH 让你在 Windows 上用 VS Code 界面打开 Mac mini 的文件夹。代码仍然在 Mac mini，依赖仍然在 Mac mini，终端也运行在 Mac mini。你得到的是本地 IDE 手感，远程机器算力。

  

## 2.3 Tailscale 是什么

  

Tailscale 是一层私有网络。你把 Mac mini 和 Windows 都登录到同一个 Tailscale 账号，它们就像在同一个安全内网里，可以用设备名互相访问。

  

## 2.4 tmux 是什么

  

tmux 是终端里的“会话保险柜”。你在 tmux 里启动的任务会留在 Mac mini 上。Windows 断网、VS Code 重连、SSH 退出，任务还在。

  

## 2.5 Docker 是什么

  

Docker 用容器跑数据库、Redis、消息队列、后端依赖。好处是每个项目有自己的开发依赖，少污染系统。

  

## 2.6 local、staging、production

  

```text

local       你自己开发用，通常在 Mac mini 本地

staging     测试/验收用，给产品、测试用户、小范围用户用

production  正式线上环境

```

  

不要让体验版小程序连 production 数据库，不要让正式版连 staging API。这个边界非常重要。

  

# 3. Mac mini 基础系统配置

  

## 3.1 建议的设备命名

  

建议把 Mac mini 的名字改成容易记的名字，例如：

  

```text

macmini-dev

```

  

图形界面路径：

  

```text

系统设置

→ 通用

→ 关于本机

→ 名称

```

  

也可以在 Mac mini 终端执行：

  

```bash

sudo scutil --set ComputerName "macmini-dev"

sudo scutil --set LocalHostName "macmini-dev"

sudo scutil --set HostName "macmini-dev"

dscacheutil -flushcache

hostname

```

  

说明：

  

```text

ComputerName     在 Finder、共享服务里显示的名字

LocalHostName    局域网 .local 名称，例如 macmini-dev.local

HostName         Unix 主机名，可选但建议统一

```

  

## 3.2 让 Mac mini 不要自动睡眠

  

远程开发最怕 Mac mini 睡着。先用图形界面设置：

  

```text

系统设置

→ 能源

→ 打开“显示器关闭时防止自动睡眠”

```

  

然后可以用命令确认和强化：

  

```bash

pmset -g

```

  

建议设置：

  

```bash

sudo pmset -a sleep 0

sudo pmset -a displaysleep 15

sudo pmset -a disksleep 0

sudo pmset -a womp 1

sudo pmset -a tcpkeepalive 1

sudo pmset -a autorestart 1

pmset -g

```

  

含义：

  

```text

sleep 0        系统不自动睡眠

displaysleep   显示器可以关闭，机器继续运行

disksleep 0    磁盘不自动睡眠

womp 1         网络唤醒

tcpkeepalive   保持部分网络活动能力

autorestart 1  断电恢复后自动开机，适合长期放在家里/办公室

```

  

临时让机器保持清醒，可以用：

  

```bash

caffeinate -dimsu

```

  

退出 `caffeinate`：按 `Ctrl+C`。

  

## 3.3 有线网络优先

  

如果 Mac mini 要长期作为远程开发机，建议用网线接路由器。Wi-Fi 能用，但有线网络更稳。

  

建议：

  

```text

Mac mini → Cat 6 网线 → 路由器 LAN 口

```

  

路由器里可以给 Mac mini 做 DHCP 地址保留，让它在局域网里总是拿到同一个 IP。即使你主要用 Tailscale，固定内网 IP 也方便本地排查。

  

## 3.4 系统更新策略

  

建议：

  

```text

安全更新：尽量及时装

大版本系统更新：不要在出门前一天装

Docker / Tailscale / VS Code：留意更新，但不要在赶项目时同时大升级

```

  

一次只升级一个大件。否则出问题时，你不知道是 Docker、系统、Tailscale，还是 VS Code 插件在扮演小妖怪。

  

## 3.5 FileVault 加密要不要开

  

如果 Mac mini 上有客户数据、业务代码、密钥，建议开启 FileVault。路径：

  

```text

系统设置

→ 隐私与安全性

→ FileVault

→ 打开

```

  

但要知道一个远程开发坑：开启 FileVault 后，机器重启后可能需要在本机登录解锁磁盘，某些远程服务可能要等登录后才完全可用。外出前一定要测试：

  

```text

重启 Mac mini

不碰本机

从 Windows 试 SSH / Tailscale / VS Code

确认能连再出门

```

  

恢复密钥必须保存好。不要只存在 Mac mini 自己里面。

  

## 3.6 防火墙建议

  

可以开启 macOS 防火墙：

  

```text

系统设置

→ 网络

→ 防火墙

→ 打开

```

  

如果只通过 Tailscale 访问 SSH，建议不要把 SSH 暴露到公网。普通家用路由器不需要做端口转发到 Mac mini 的 22 端口。

  

推荐原则：

  

```text

允许：Tailscale 私网访问 SSH

避免：公网直接开放 SSH

避免：把数据库端口暴露给局域网/公网

```

  

## 3.7 Time Machine 备份

  

你是 512GB 内置 SSD，建议准备 1TB 或 2TB 外接盘做 Time Machine。

  

路径：

  

```text

系统设置

→ 通用

→ Time Machine

→ 添加备份磁盘

```

  

建议：

  

```text

备份盘专盘专用

开启加密备份

至少每周插一次备份

重要项目还要推到 Git 远程仓库

```

  

Time Machine 是“整机后悔药”，Git 是“代码时光机”。两者都要。

  

# 4. 安装基础命令行工具

  

## 4.1 安装 Xcode Command Line Tools

  

打开 Mac mini 终端：

  

```bash

xcode-select --install

```

  

如果提示已经安装，可以跳过。

  

## 4.2 安装 Homebrew

  

Homebrew 是 macOS 常用包管理器。安装命令以官网显示为准，常见命令是：

  

```bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

  

Apple Silicon 的 Homebrew 默认路径一般是：

  

```text

/opt/homebrew

```

  

安装完成后，按终端提示把 Homebrew 加到 PATH。常见是：

  

```bash

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"

```

  

验证：

  

```bash

brew --version

brew doctor

```

  

## 4.3 安装常用工具

  

```bash

brew update

brew install git tmux htop jq wget tree gh ripgrep fd watchman

```

  

说明：

  

```text

git       版本控制

tmux      长任务会话

htop      看 CPU/内存

jq        处理 JSON

wget      下载工具

tree      查看目录树

gh        GitHub CLI

ripgrep   快速搜索代码

fd        快速找文件

watchman  前端项目文件监听常用

```

  

## 4.4 Node 和 pnpm

  

简单方案：

  

```bash

brew install node pnpm

node -v

pnpm -v

```

  

更稳的团队方案是用 `mise` 或 `nvm` 管理 Node 版本。新手先用 Homebrew 也可以，项目成熟后再切到版本管理。

  

建议在项目 `package.json` 写清包管理器：

  

```json

{

  "packageManager": "pnpm@9.15.0"

}

```

  

启用 corepack：

  

```bash

corepack enable

```

  

如果项目指定 pnpm 版本，执行：

  

```bash

corepack prepare pnpm@9.15.0 --activate

pnpm -v

```

  

# 5. SSH 配置：Windows 远程进入 Mac mini

  

## 5.1 在 Mac mini 开启 Remote Login

  

路径：

  

```text

系统设置

→ 通用

→ 共享

→ 远程登录 Remote Login

→ 打开

```

  

建议选择：

  

```text

仅允许你的用户登录

```

  

开启后，系统会显示类似命令：

  

```bash

ssh yourname@macmini-dev.local

```

  

先在 Mac mini 上确认用户名：

  

```bash

whoami

```

  

假设输出是：

  

```text

yourname

```

  

## 5.2 Windows 检查 OpenSSH 客户端

  

在 Windows PowerShell 里执行：

  

```powershell

ssh -V

```

  

如果没有 ssh 命令，在 Windows 设置里安装 OpenSSH Client：

  

```text

设置

→ 系统

→ 可选功能

→ 添加可选功能

→ OpenSSH Client

```

  

## 5.3 第一次用密码登录测试

  

如果 Windows 和 Mac mini 在同一个局域网，可以先试：

  

```powershell

ssh yourname@macmini-dev.local

```

  

如果你已经装了 Tailscale，也可以用 Tailscale 设备名：

  

```powershell

ssh yourname@macmini-dev

```

  

第一次连接会提示是否信任主机指纹，输入：

  

```text

yes

```

  

然后输入 Mac mini 登录密码。

  

## 5.4 在 Windows 生成 SSH key

  

在 Windows PowerShell 执行：

  

```powershell

New-Item -ItemType Directory -Force $HOME\.ssh

ssh-keygen -t ed25519 -f $HOME\.ssh\id_ed25519_macmini -C "windows-to-macmini"

```

  

建议给 key 设置 passphrase。怕麻烦也可以先不设置，但安全性会低一点。

  

生成后会有：

  

```text

C:\Users\你的用户名\.ssh\id_ed25519_macmini

C:\Users\你的用户名\.ssh\id_ed25519_macmini.pub

```

  

`.pub` 是公钥，可以给 Mac mini。没有 `.pub` 的那个是私钥，不要发给任何人。

  

## 5.5 把 Windows 公钥复制到 Mac mini

  

在 Windows PowerShell 执行，替换 `yourname` 和 `macmini-dev.local`：

  

```powershell

type $HOME\.ssh\id_ed25519_macmini.pub | ssh yourname@macmini-dev.local "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"

```

  

然后测试免密码登录：

  

```powershell

ssh -i $HOME\.ssh\id_ed25519_macmini yourname@macmini-dev.local

```

  

如果直接进去了，说明 key 成功。

  

## 5.6 配置 Windows SSH config

  

编辑：

  

```text

C:\Users\你的用户名\.ssh\config

```

  

可以用 VS Code 打开：

  

```powershell

code $HOME\.ssh\config

```

  

写入：

  

```sshconfig

Host macmini-lan

  HostName macmini-dev.local

  User yourname

  IdentityFile ~/.ssh/id_ed25519_macmini

  IdentitiesOnly yes

  ServerAliveInterval 30

  ServerAliveCountMax 6

  

Host macmini

  HostName macmini-dev

  User yourname

  IdentityFile ~/.ssh/id_ed25519_macmini

  IdentitiesOnly yes

  ServerAliveInterval 30

  ServerAliveCountMax 6

```

  

说明：

  

```text

macmini-lan  局域网 .local 方式

macmini      Tailscale MagicDNS 方式

```

  

以后就可以：

  

```powershell

ssh macmini

```

  

## 5.7 不建议立刻关闭密码登录

  

等你确认下面三种方式都能连以后，再考虑关闭密码登录：

  

```text

Windows Terminal ssh macmini

VS Code Remote SSH macmini

手机或备用电脑能连 Tailscale / SSH

```

  

如果你要关闭密码登录，务必先开两个终端。一个保持已登录，另一个测试新配置。不要把自己锁在门外。

  

高级用户可编辑：

  

```bash

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

sudo nano /etc/ssh/sshd_config

```

  

可以考虑添加或确认：

  

```text

PubkeyAuthentication yes

PasswordAuthentication no

KbdInteractiveAuthentication no

PermitRootLogin no

AllowUsers yourname

```

  

重启 SSH 服务前，先确认公钥登录一定可用。macOS 的 SSH 配置随系统版本可能有差异，新手阶段可以暂时保留密码登录，只允许 Tailscale 私网访问。

  

## 5.8 常见 SSH 报错

  

### Permission denied publickey

  

检查：

  

```bash

ls -la ~/.ssh

cat ~/.ssh/authorized_keys

```

  

Mac mini 上权限应是：

  

```bash

chmod 700 ~/.ssh

chmod 600 ~/.ssh/authorized_keys

```

  

Windows 上测试详细日志：

  

```powershell

ssh -vvv macmini

```

  

### Could not resolve hostname

  

说明设备名解析失败。解决：

  

```powershell

ping macmini-dev.local

ping macmini

```

  

如果 Tailscale MagicDNS 不工作，先用 Tailscale IP：

  

```powershell

ssh yourname@100.x.y.z

```

  

### Connection timed out

  

检查：

  

```text

Mac mini 是否开机

Mac mini 是否睡眠

Remote Login 是否打开

Tailscale 是否在线

Windows 是否连上 Tailscale

路由器/防火墙是否拦截

```

  

# 6. Tailscale 配置：把 Mac mini 变成安全私网主机

  

## 6.1 安装 Tailscale

  

在 Mac mini 和 Windows 上都安装 Tailscale。macOS 建议使用 Tailscale 官方推荐的 standalone 版本。Windows 使用官方 Windows 客户端。

  

安装后，两台设备都登录同一个账号。

  

## 6.2 给设备命名

  

建议设备名：

  

```text

Mac mini：macmini-dev

Windows：win-laptop

手机：iphone-joe

```

  

Tailscale 管理后台：

  

```text

Machines

→ 选择设备

→ Edit machine name

```

  

启用 MagicDNS 后，你就可以用设备名连接：

  

```powershell

ssh macmini

```

  

或：

  

```powershell

ssh yourname@macmini

```

  

## 6.3 检查 Tailscale 状态

  

Mac mini 上：

  

```bash

tailscale status

```

  

如果提示找不到 `tailscale`，可以试：

  

```bash

/Applications/Tailscale.app/Contents/MacOS/Tailscale status

```

  

Windows PowerShell：

  

```powershell

tailscale status

```

  

如果 Windows 装的是 GUI 客户端但没有命令行，先用系统托盘图标查看设备在线状态。

  

## 6.4 建议关闭 Mac mini 的 Tailscale key expiry

  

Mac mini 是长期远程主机。建议在 Tailscale 管理后台对它关闭 key expiry，避免某天外出时突然需要重新认证。

  

路径：

  

```text

Tailscale Admin Console

→ Machines

→ macmini-dev

→ 右侧 ... 菜单

→ Disable key expiry

```

  

这是给长期可信设备的便利设置。不要对临时设备随便关闭过期。

  

## 6.5 推荐方式：OpenSSH over Tailscale

  

对你最简单稳定的是：

  

```text

Tailscale 提供私网

macOS Remote Login 提供 SSH 服务

Windows 通过 Tailscale 设备名 ssh 到 Mac mini

```

  

连接：

  

```powershell

ssh macmini

```

  

优点：

  

```text

兼容 VS Code Remote SSH

和普通 SSH 完全一样

不需要公网端口转发

易排查

```

  

## 6.6 可选方式：Tailscale SSH

  

Tailscale SSH 是让 Tailscale 管理 SSH 鉴权和授权。适合想减少 SSH key 管理的人。

  

在 Mac mini 上开启：

  

```bash

sudo tailscale up --ssh

```

  

然后配置 tailnet policy。单人设备的简单示例：

  

```json

{

  "acls": [

    {

      "action": "accept",

      "src": ["autogroup:member"],

      "dst": ["autogroup:self:*"]

    }

  ],

  "ssh": [

    {

      "action": "accept",

      "src": ["autogroup:member"],

      "dst": ["autogroup:self"],

      "users": ["autogroup:nonroot"]

    }

  ]

}

```

  

注意：

  

```text

如果你已经有公司/团队 Tailscale 策略，不要直接覆盖。

先备份原 policy。

个人单人 tailnet 可以用这个思路。

```

  

## 6.7 Tailscale ACL 的新手建议

  

单人使用时，先用默认策略也可以。等你确认长期稳定后，再收紧规则。

  

推荐安全层级：

  

```text

第 1 层：Tailscale 同账号设备可访问，路由器不做公网端口转发

第 2 层：SSH 只允许你的 macOS 用户

第 3 层：SSH 使用 key 登录

第 4 层：Tailscale policy 限制只允许你的设备访问 Mac mini

第 5 层：重要密钥不放在项目目录，不让 AI agent 随便读取

```

  

## 6.8 不建议把 Mac mini 当 exit node

  

你只是要远程开发，不需要让所有外出流量都从家里 Mac mini 出口走。Exit node 会增加复杂度。先不要开。

  

# 7. VS Code Remote SSH：主力开发入口

  

## 7.1 Windows 安装 VS Code 和 Remote SSH

  

Windows 上安装：

  

```text

Visual Studio Code

Remote - SSH 扩展

```

  

操作：

  

```text

VS Code

→ Extensions

→ 搜索 Remote - SSH

→ Install

```

  

## 7.2 连接 Mac mini

  

确保 `C:\Users\你\.ssh\config` 里有：

  

```sshconfig

Host macmini

  HostName macmini-dev

  User yourname

  IdentityFile ~/.ssh/id_ed25519_macmini

  IdentitiesOnly yes

  ServerAliveInterval 30

  ServerAliveCountMax 6

```

  

然后：

  

```text

VS Code

→ Ctrl+Shift+P

→ Remote-SSH: Connect to Host

→ macmini

```

  

首次连接会在 Mac mini 上安装 VS Code Server。完成后，左下角会显示类似：

  

```text

SSH: macmini

```

  

## 7.3 打开远程项目目录

  

建议项目统一放在：

  

```text

~/projects

```

  

Mac mini 上创建：

  

```bash

mkdir -p ~/projects

cd ~/projects

```

  

VS Code 里：

  

```text

File

→ Open Folder

→ /Users/yourname/projects/myapp

```

  

## 7.4 扩展应该装在哪里

  

连接 Remote SSH 后，很多扩展会提示：

  

```text

Install in SSH: macmini

```

  

推荐在远程环境安装：

  

```text

ESLint

Prettier

Docker

Playwright Test

Claude Code

Codex

GitLens，可选

```

  

原因：项目文件、Node、Docker、Git 都在 Mac mini 上，工作区相关扩展装远程更顺。

  

## 7.5 VS Code 终端里仍然建议进 tmux

  

打开 VS Code 远程终端：

  

```text

Terminal

→ New Terminal

```

  

此终端运行在 Mac mini 上。不要直接裸跑长任务，先进入 tmux：

  

```bash

cd ~/projects/myapp

tmux new -As myapp

```

  

然后再跑：

  

```bash

pnpm dev

docker compose up

claude

codex

```

  

## 7.6 端口转发

  

如果 Mac mini 上跑：

  

```bash

pnpm dev

```

  

服务监听：

  

```text

localhost:5173

```

  

VS Code 可以把远程端口转发到 Windows。本机浏览器打开转发地址即可。

  

常见端口：

  

```text

5173   Vite

3000   Next.js / Nuxt / Node

8080   后端 API

5432   PostgreSQL，不建议长期转发

6379   Redis，不建议长期转发

```

  

数据库端口不要暴露到公网。开发时只绑定：

  

```text

127.0.0.1:5432:5432

127.0.0.1:6379:6379

```

  

## 7.7 VS Code 推荐设置

  

项目里可创建：

  

```text

.vscode/settings.json

```

  

示例：

  

```json

{

  "terminal.integrated.defaultProfile.osx": "zsh",

  "files.watcherExclude": {

    "**/node_modules/**": true,

    "**/.git/objects/**": true,

    "**/.next/**": true,

    "**/dist/**": true,

    "**/coverage/**": true

  },

  "search.exclude": {

    "**/node_modules": true,

    "**/.next": true,

    "**/dist": true,

    "**/coverage": true

  },

  "editor.formatOnSave": true

}

```

  

不要把个人密钥、上传密钥、生产 `.env` 放进项目工作区。

  

# 8. tmux 完全入门

  

## 8.1 安装 tmux

  

```bash

brew install tmux

tmux -V

```

  

## 8.2 tmux 的三个概念

  

```text

session  会话：一个长期工作区，例如 myapp

window   窗口：一个会话里的多个标签页，例如 web、docker、logs

pane     面板：一个窗口里分屏出来的多个终端区域

```

  

建议你采用：

  

```text

一个项目 = 一个 tmux session

一个任务 = 一个 tmux window

临时对比 = 用 pane 分屏

```

  

## 8.3 常用命令

  

创建或进入会话：

  

```bash

tmux new -As myapp

```

  

查看会话：

  

```bash

tmux ls

```

  

重新进入会话：

  

```bash

tmux attach -t myapp

```

  

退出但保持任务运行：

  

```text

Ctrl+b 然后按 d

```

  

关闭会话：

  

```bash

tmux kill-session -t myapp

```

  

关闭所有 tmux：

  

```bash

tmux kill-server

```

  

`kill-server` 很猛，像拉下整栋楼的电闸。慎用。

  

## 8.4 常用快捷键

  

所有快捷键先按：

  

```text

Ctrl+b

```

  

然后按第二个键：

  

```text

d      detach，退出但保持运行

c      新建窗口

n      下一个窗口

p      上一个窗口

,      重命名当前窗口

w      窗口列表

%      左右分屏

"      上下分屏

方向键 切换 pane

x      关闭 pane

[      进入复制/滚动模式

```

  

## 8.5 推荐窗口命名

  

在 `myapp` 会话里：

  

```text

1 shell     普通命令

2 web       pnpm dev

3 api       后端服务

4 docker    docker compose up / logs

5 claude    Claude Code CLI

6 codex     Codex CLI

7 git       git diff / git status

```

  

重命名窗口：

  

```text

Ctrl+b 然后 ,

```

  

## 8.6 推荐 ~/.tmux.conf

  

在 Mac mini 上：

  

```bash

nano ~/.tmux.conf

```

  

写入：

  

```tmux

set -g mouse on

set -g history-limit 50000

setw -g mode-keys vi

set -g base-index 1

setw -g pane-base-index 1

set -g renumber-windows on

set -g detach-on-destroy off

set -g default-shell /bin/zsh

bind r source-file ~/.tmux.conf \; display-message "tmux config reloaded"

```

  

重新加载：

  

```bash

tmux source-file ~/.tmux.conf

```

  

以后在 tmux 里按：

  

```text

Ctrl+b 然后 r

```

  

即可重新加载配置。

  

## 8.7 复制和滚动

  

进入滚动模式：

  

```text

Ctrl+b 然后 [

```

  

滚动：

  

```text

方向键 / PageUp / PageDown

```

  

退出滚动模式：

  

```text

q

```

  

## 8.8 给项目做启动脚本

  

创建脚本目录：

  

```bash

mkdir -p ~/bin

```

  

编辑：

  

```bash

nano ~/bin/dev-myapp

```

  

写入，替换项目路径：

  

```bash

#!/usr/bin/env bash

set -e

  

SESSION="myapp"

PROJECT="$HOME/projects/myapp"

  

if ! tmux has-session -t "$SESSION" 2>/dev/null; then

  tmux new-session -d -s "$SESSION" -c "$PROJECT" -n shell

  tmux new-window -t "$SESSION":2 -n web -c "$PROJECT" "pnpm dev; exec zsh"

  tmux new-window -t "$SESSION":3 -n docker -c "$PROJECT" "docker compose up; exec zsh"

  tmux new-window -t "$SESSION":4 -n logs -c "$PROJECT" "docker compose logs -f; exec zsh"

  tmux new-window -t "$SESSION":5 -n ai -c "$PROJECT" "zsh"

fi

  

tmux attach -t "$SESSION"

```

  

授权：

  

```bash

chmod +x ~/bin/dev-myapp

```

  

把 `~/bin` 加入 PATH：

  

```bash

echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zprofile

source ~/.zprofile

```

  

以后只要：

  

```bash

dev-myapp

```

  

## 8.9 tmux 和 VS Code 的正确关系

  

推荐：

  

```text

VS Code 负责编辑、看 diff、端口转发、插件

VS Code 终端进入 tmux

长任务全部在 tmux 里跑

普通短命令可以直接在 VS Code 终端执行

```

  

一句话：VS Code 是驾驶舱，tmux 是黑匣子。驾驶舱舒服，黑匣子保命。

  

# 9. Docker Desktop 安装与配置

  

## 9.1 安装 Docker Desktop

  

你的 Mac mini 是 Apple Silicon，下载 Docker Desktop for Mac - Apple Silicon。

  

安装后打开 Docker Desktop，等状态变成：

  

```text

Docker Desktop is running

```

  

验证：

  

```bash

docker version

docker compose version

docker run hello-world

```

  

## 9.2 Docker Desktop 资源建议，32GB 内存版

  

你的配置是 32GB + 512GB。建议：

  

```text

Memory：8GB - 12GB

CPU：4 - 6 cores

Swap：2GB

Disk image limit：120GB - 180GB

```

  

路径大致是：

  

```text

Docker Desktop

→ Settings

→ Resources

→ Advanced

```

  

不要一开始给 Docker 16GB。你的 VS Code、浏览器、Claude、Codex、微信开发者工具也要吃内存。

  

## 9.3 Docker 文件共享

  

如果项目在：

  

```text

/Users/yourname/projects

```

  

确认 Docker Desktop 允许访问这个路径。路径：

  

```text

Docker Desktop

→ Settings

→ Resources

→ File Sharing

```

  

一般默认 `/Users` 已经允许，但如果容器挂载失败，就回来检查这里。

  

## 9.4 Apple Silicon 镜像注意事项

  

优先使用支持 ARM64 的镜像：

  

```text

postgres:16-alpine

redis:7-alpine

mysql:8

nginx:alpine

node:20-alpine

```

  

只有在镜像不支持 ARM64 时，才考虑：

  

```yaml

platform: linux/amd64

```

  

但 x86/amd64 模拟会更慢。不要默认给所有服务都加 `platform: linux/amd64`。

  

## 9.5 推荐项目目录结构

  

```text

~/projects/myapp

├── apps/

│   ├── web/

│   └── miniprogram/

├── packages/

├── docker/

│   ├── postgres/

│   │   └── init/

│   └── redis/

├── scripts/

├── backups/

├── compose.yaml

├── .env

├── .env.example

├── package.json

└── README.md

```

  

原则：

  

```text

compose.yaml 放开发依赖

.env 存本地开发变量，不提交

.env.example 提交，用来告诉别人需要哪些变量

backups 存导出的本地备份，通常不提交

```

  

`.gitignore` 里写：

  

```gitignore

.env

.env.*

!.env.example

backups/

node_modules/

.DS_Store

```

  

# 10. Docker Compose：Postgres + Redis 开发环境

  

## 10.1 compose.yaml 示例

  

在项目根目录创建：

  

```bash

nano compose.yaml

```

  

写入：

  

```yaml

name: myapp-dev

  

services:

  postgres:

    image: postgres:16-alpine

    container_name: myapp-postgres

    restart: unless-stopped

    ports:

      - "127.0.0.1:5432:5432"

    environment:

      POSTGRES_DB: ${POSTGRES_DB:-myapp}

      POSTGRES_USER: ${POSTGRES_USER:-myapp}

      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-dev_password_change_me}

      TZ: Asia/Shanghai

    volumes:

      - postgres_data:/var/lib/postgresql/data

      - ./docker/postgres/init:/docker-entrypoint-initdb.d:ro

    healthcheck:

      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]

      interval: 10s

      timeout: 5s

      retries: 5

    mem_limit: 2g

  

  redis:

    image: redis:7-alpine

    container_name: myapp-redis

    restart: unless-stopped

    command:

      - redis-server

      - --appendonly

      - "yes"

      - --requirepass

      - ${REDIS_PASSWORD:-dev_redis_password}

    ports:

      - "127.0.0.1:6379:6379"

    volumes:

      - redis_data:/data

    healthcheck:

      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD:-dev_redis_password}", "ping"]

      interval: 10s

      timeout: 5s

      retries: 5

    mem_limit: 512m

  

volumes:

  postgres_data:

  redis_data:

```

  

## 10.2 .env 示例

  

创建 `.env`：

  

```bash

nano .env

```

  

写入：

  

```env

POSTGRES_DB=myapp

POSTGRES_USER=myapp

POSTGRES_PASSWORD=dev_password_change_me

REDIS_PASSWORD=dev_redis_password

DATABASE_URL=postgresql://myapp:dev_password_change_me@127.0.0.1:5432/myapp

REDIS_URL=redis://:dev_redis_password@127.0.0.1:6379

```

  

创建 `.env.example`，不要写真实密码：

  

```env

POSTGRES_DB=myapp

POSTGRES_USER=myapp

POSTGRES_PASSWORD=change_me

REDIS_PASSWORD=change_me

DATABASE_URL=postgresql://myapp:change_me@127.0.0.1:5432/myapp

REDIS_URL=redis://:change_me@127.0.0.1:6379

```

  

## 10.3 启动和停止

  

启动：

  

```bash

docker compose up -d

```

  

查看：

  

```bash

docker compose ps

```

  

看日志：

  

```bash

docker compose logs -f

```

  

停止但保留数据：

  

```bash

docker compose down

```

  

停止并删除数据卷，危险：

  

```bash

docker compose down -v

```

  

`down -v` 会删数据库数据。除非你确定不需要，否则别用。

  

## 10.4 进入数据库和 Redis

  

Postgres：

  

```bash

docker compose exec postgres psql -U myapp -d myapp

```

  

Redis：

  

```bash

docker compose exec redis redis-cli -a dev_redis_password

```

  

Redis 里测试：

  

```text

PING

SET hello world

GET hello

```

  

## 10.5 备份数据库

  

创建备份目录：

  

```bash

mkdir -p backups

```

  

导出：

  

```bash

docker compose exec -T postgres pg_dump -U myapp myapp > backups/myapp_$(date +%F_%H%M).sql

```

  

恢复，先确认你真的要覆盖：

  

```bash

cat backups/myapp_2026-06-15_1200.sql | docker compose exec -T postgres psql -U myapp -d myapp

```

  

## 10.6 查看 Docker 空间

  

```bash

docker system df

```

  

清理没用的构建缓存：

  

```bash

docker builder prune

```

  

清理未使用镜像：

  

```bash

docker image prune

```

  

谨慎清理所有未使用资源：

  

```bash

docker system prune

```

  

非常谨慎，可能清 volume：

  

```bash

docker system prune -a --volumes

```

  

如果你没备份数据库，不要用带 `--volumes` 的清理命令。

  

## 10.7 为什么端口写 127.0.0.1

  

这个写法：

  

```yaml

ports:

  - "127.0.0.1:5432:5432"

```

  

表示只允许 Mac mini 本机访问数据库端口。VS Code 远程终端、Mac mini 上的应用可以访问。外部设备不能直接访问。

  

不要写成：

  

```yaml

ports:

  - "5432:5432"

```

  

除非你明确知道风险。这个可能让局域网设备访问数据库。

  

# 11. Docker 的高级但常用配置

  

## 11.1 named volume 和 bind mount 区别

  

named volume：

  

```yaml

volumes:

  - postgres_data:/var/lib/postgresql/data

```

  

适合数据库数据。Docker 管理，稳定。

  

bind mount：

  

```yaml

volumes:

  - ./src:/app/src

```

  

适合代码热更新。主机目录直接映射到容器。

  

建议：

  

```text

数据库数据：named volume

源代码：bind mount

初始化脚本：bind mount 只读

```

  

## 11.2 给容器限制内存

  

你的机器是 32GB，Docker Desktop 总内存建议 8GB - 12GB。每个容器也可以设上限。

  

```yaml

services:

  api:

    build: .

    mem_limit: 2g

  

  worker:

    build: .

    mem_limit: 1g

```

  

容器默认可能尽量吃资源。开发环境给小碗，整台机器更稳。

  

## 11.3 健康检查 healthcheck

  

健康检查能让你看服务是否真正可用：

  

```bash

docker compose ps

```

  

如果看到：

  

```text

healthy

```

  

说明服务自检通过。

  

## 11.4 Docker 自动启动

  

Docker Desktop 设置里可以开启：

  

```text

Start Docker Desktop when you sign in

```

  

项目容器不建议一开始就设置开机自动启动。新手阶段手动：

  

```bash

cd ~/projects/myapp

docker compose up -d

```

  

如果以后想自动启动，再考虑 launchd 或脚本。自动化越多，排查越像翻一柜子袜子，先简单跑稳。

  

## 11.5 以后空间不够，Docker 数据搬外接 SSD

  

你现在 512GB 内置盘可以先用。以后 Docker 占用大于 100GB 或系统可用空间长期低于 100GB，再考虑把 Docker disk image 移到高速外接 SSD。

  

正确路径：

  

```text

Docker Desktop

→ Settings

→ Resources

→ Advanced

→ Disk image location

→ 选择外接 SSD 目录

→ Apply & Restart

```

  

不要用 Finder 手动拖 Docker 数据文件。

  

# 12. Web 端本地开发流程

  

## 12.1 推荐启动顺序

  

从 Windows 打开 VS Code Remote SSH，打开项目后：

  

```bash

cd ~/projects/myapp

tmux new -As myapp

```

  

tmux 窗口建议：

  

```text

1 shell

2 docker

3 web

4 api

5 logs

6 ai

```

  

启动 Docker：

  

```bash

docker compose up -d

```

  

安装依赖：

  

```bash

pnpm install

```

  

启动 Web：

  

```bash

pnpm dev

```

  

## 12.2 Windows 浏览器访问 Mac mini dev server

  

如果服务监听远程 5173：

  

```text

VS Code Ports

→ Forward Port

→ 5173

```

  

然后 Windows 浏览器打开 VS Code 给出的本地地址。

  

也可以手动 SSH 转发：

  

```powershell

ssh -L 5173:127.0.0.1:5173 macmini

```

  

然后 Windows 打开：

  

```text

http://127.0.0.1:5173

```

  

## 12.3 API 地址管理

  

建议：

  

```text

local：      http://127.0.0.1:3000

staging：    https://api-staging.xxx.com

production： https://api.xxx.com

```

  

前端不要硬编码生产 API。用环境变量：

  

```env

VITE_API_BASE_URL=http://127.0.0.1:3000

```

  

或：

  

```env

NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:3000

```

  

## 12.4 本地开发不要连 production 数据库

  

强制原则：

  

```text

本地开发只连本地 Docker 数据库或 staging 数据库

体验版只连 staging API

正式版才连 production API

```

  

推荐在后端启动时打印当前环境：

  

```bash

NODE_ENV=development

APP_ENV=local

DATABASE_URL=...

```

  

如果检测到本地环境连了生产库，可以直接拒绝启动。

  

# 13. 小程序端开发与体验版流程

  

## 13.1 小程序环境建议

  

```text

开发版 develop：开发者工具、本地调试

体验版 trial：用户测试、产品验收

正式版 release：线上用户

```

  

小程序里建议根据版本环境自动切 API：

  

```ts

export function getMiniProgramEnv() {

  const accountInfo = wx.getAccountInfoSync()

  return accountInfo.miniProgram.envVersion

}

  

export function getApiBaseUrl() {

  const envVersion = getMiniProgramEnv()

  

  if (envVersion === 'release') {

    return 'https://api.xxx.com'

  }

  

  return 'https://api-staging.xxx.com'

}

```

  

如果你用 Taro / uni-app，API 名称可能是框架封装，例如 `Taro.getAccountInfoSync()` 或 `uni.getAccountInfoSync()`，思路一样。

  

## 13.2 不要把 appsecret 放进小程序前端

  

小程序前端代码会被分发到用户设备。不要放：

  

```text

小程序 appsecret

数据库密码

Redis 密码

支付私钥

云服务 AccessKey Secret

上传密钥 private key

```

  

这些只能在后端或 CI 的安全密钥管理里。

  

## 13.3 miniprogram-ci 用途

  

`miniprogram-ci` 可以在不打开微信开发者工具的情况下做小程序上传、预览等操作。适合 CI 自动上传体验版。

  

安装：

  

```bash

pnpm add -D miniprogram-ci

```

  

## 13.4 小程序上传密钥

  

在微信公众平台下载代码上传密钥，通常路径类似：

  

```text

微信公众平台

→ 开发

→ 开发管理 / 开发设置

→ 小程序代码上传

→ 下载上传密钥

```

  

注意：

  

```text

上传密钥不要提交到 Git

上传密钥不要放在小程序前端目录里

CI 里用 GitHub Secrets 保存

如果开启 IP 白名单，要考虑 CI 出口 IP 是否固定

```

  

## 13.5 上传脚本示例

  

创建：

  

```bash

mkdir -p scripts

nano scripts/upload-miniprogram.js

```

  

示例：

  

```js

const ci = require('miniprogram-ci')

const path = require('path')

  

const appid = process.env.WX_APPID

const privateKeyPath = process.env.WX_PRIVATE_KEY_PATH

const projectPath = process.env.WX_PROJECT_PATH || path.resolve(__dirname, '../dist/miniprogram')

const version = process.env.VERSION || require('../package.json').version || '0.0.0'

const desc = process.env.DESC || `ci upload ${new Date().toISOString()}`

const robot = Number(process.env.WX_ROBOT || 1)

  

if (!appid) {

  console.error('Missing WX_APPID')

  process.exit(1)

}

  

if (!privateKeyPath) {

  console.error('Missing WX_PRIVATE_KEY_PATH')

  process.exit(1)

}

  

const project = new ci.Project({

  appid,

  type: 'miniProgram',

  projectPath,

  privateKeyPath,

  ignores: ['node_modules/**/*'],

})

  

ci.upload({

  project,

  version,

  desc,

  robot,

  setting: {

    es6: true,

  },

  onProgressUpdate: console.log,

})

  .then((res) => {

    console.log('Upload success')

    console.log(res)

  })

  .catch((err) => {

    console.error('Upload failed')

    console.error(err)

    process.exit(1)

  })

```

  

本地测试，先不要把 private key 放进仓库：

  

```bash

WX_APPID=wx_your_appid \

WX_PRIVATE_KEY_PATH=$HOME/secrets/wechat/private.wx_your_appid.key \

WX_PROJECT_PATH=$PWD/dist/miniprogram \

VERSION=0.1.0 \

DESC="local test upload" \

node scripts/upload-miniprogram.js

```

  

# 14. Git 和分支工作流

  

## 14.1 推荐分支

  

```text

main        正式生产分支

develop     日常集成 / staging 分支

feature/*   功能分支

fix/*       修复分支

release/*   发版准备，可选

```

  

单人项目也可以简单：

  

```text

main      稳定版本

feature/* 功能开发

```

  

但只要有 staging，就建议不要直接在 main 上乱改。

  

## 14.2 每次让 AI 改代码前先建分支

  

```bash

git switch -c feature/order-flow

```

  

让 Claude/Codex 改前先看状态：

  

```bash

git status

git diff

```

  

改完后：

  

```bash

pnpm lint

pnpm test

pnpm build

git diff

```

  

## 14.3 常用安全命令

  

查看改了什么：

  

```bash

git status

git diff

git diff --stat

```

  

只暂存某些文件：

  

```bash

git add path/to/file

```

  

交互式暂存：

  

```bash

git add -p

```

  

撤销未暂存修改，危险：

  

```bash

git restore path/to/file

```

  

回到上一个分支：

  

```bash

git switch -

```

  

## 14.4 让 AI 不要乱提交

  

给 AI 的默认要求：

  

```text

请先修改代码并运行测试，但不要 commit，不要 push。

完成后总结改动文件、测试结果、风险点，等我确认。

```

  

等你看过 diff 后再提交。

  

# 15. GitHub Actions：CI 和自动化部署

  

## 15.1 基础 CI 示例

  

创建：

  

```text

.github/workflows/ci.yml

```

  

示例：

  

```yaml

name: CI

  

on:

  pull_request:

  push:

    branches:

      - main

      - develop

  

jobs:

  test:

    runs-on: ubuntu-latest

  

    steps:

      - name: Checkout

        uses: actions/checkout@v4

  

      - name: Setup Node

        uses: actions/setup-node@v4

        with:

          node-version: 20

          cache: pnpm

  

      - name: Enable Corepack

        run: corepack enable

  

      - name: Install dependencies

        run: pnpm install --frozen-lockfile

  

      - name: Lint

        run: pnpm lint

  

      - name: Test

        run: pnpm test

  

      - name: Build

        run: pnpm build

```

  

## 15.2 staging 部署思路

  

推荐：

  

```text

push develop

→ CI lint/test/build

→ deploy web staging

→ upload miniprogram trial / 体验版

→ 发测试说明

```

  

Web 端部署方式取决于你的平台：

  

```text

Vercel / Netlify / Cloudflare Pages

阿里云 / 腾讯云 / 自己服务器

Docker 镜像推送到云端

```

  

这份手册不绑定平台，但原则是：用户测试访问 staging 域名，不访问你 Mac mini 的 localhost。

  

## 15.3 GitHub Secrets

  

常见 Secrets：

  

```text

STAGING_API_BASE_URL

DEPLOY_HOST

DEPLOY_USER

DEPLOY_SSH_KEY

WX_APPID

WX_UPLOAD_PRIVATE_KEY

```

  

不要把这些写进仓库。

  

路径：

  

```text

GitHub Repository

→ Settings

→ Secrets and variables

→ Actions

```

  

有 staging / production 时，建议使用 Environment Secrets：

  

```text

Environments

→ staging

→ secrets

  

Environments

→ production

→ secrets

```

  

## 15.4 小程序上传 GitHub Actions 示例

  

```yaml

name: Upload MiniProgram Trial

  

on:

  workflow_dispatch:

  push:

    branches:

      - develop

  

jobs:

  upload-miniprogram:

    runs-on: ubuntu-latest

    environment: staging

  

    steps:

      - name: Checkout

        uses: actions/checkout@v4

  

      - name: Setup Node

        uses: actions/setup-node@v4

        with:

          node-version: 20

          cache: pnpm

  

      - name: Enable Corepack

        run: corepack enable

  

      - name: Install dependencies

        run: pnpm install --frozen-lockfile

  

      - name: Build mini program

        run: pnpm build:miniprogram

  

      - name: Write WeChat private key

        run: |

          mkdir -p private

          printf "%s" "${{ secrets.WX_UPLOAD_PRIVATE_KEY }}" > private/upload.key

          chmod 600 private/upload.key

  

      - name: Upload trial version

        env:

          WX_APPID: ${{ secrets.WX_APPID }}

          WX_PRIVATE_KEY_PATH: private/upload.key

          WX_PROJECT_PATH: ${{ github.workspace }}/dist/miniprogram

          VERSION: ${{ github.run_number }}-${{ github.sha }}

          DESC: staging upload ${{ github.sha }}

          WX_ROBOT: 1

        run: node scripts/upload-miniprogram.js

```

  

## 15.5 小程序 IP 白名单问题

  

如果微信小程序上传密钥开启了 IP 白名单，而你用 GitHub-hosted runner，可能会遇到出口 IP 不固定的问题。

  

选择：

  

```text

方案 A：关闭上传密钥 IP 白名单，靠密钥保管和 GitHub Secrets 控制

方案 B：用 GitHub larger runner 固定 IP，成本更高

方案 C：在 Mac mini 或固定云服务器上跑 self-hosted runner

方案 D：使用云厂商 CI，配置固定出口 IP

```

  

如果你是个人项目，先用 A 方案最简单，但要把密钥保护好。如果是商业项目，优先 B/C/D。

  

# 16. Claude Code 配置和使用

  

## 16.1 安装 Claude Code

  

在 Mac mini 上安装。官方常见安装命令：

  

```bash

curl -fsSL https://claude.ai/install.sh | bash

```

  

安装后验证：

  

```bash

claude --version

```

  

进入项目：

  

```bash

cd ~/projects/myapp

claude

```

  

## 16.2 VS Code 扩展

  

在 VS Code Remote SSH 的远程窗口中安装 Claude Code 扩展。建议安装到：

  

```text

SSH: macmini

```

  

使用方式：

  

```text

小改动、读代码、看 diff：Claude VS Code 插件

长任务、多命令、多文件重构：tmux 里的 claude CLI

```

  

## 16.3 Remote Control

  

如果你想用手机或浏览器继续控制本地 Claude Code 会话，可以在 Mac mini 的项目目录启动：

  

```bash

claude --remote-control

```

  

或在 Claude Code 会话里按官方说明开启 Remote Control。

  

注意：

  

```text

本地 claude 进程要保持运行

终端/VS Code/tmux 不要关掉

Mac mini 不要睡眠

远程控制不是云端执行，实际命令还是在 Mac mini 本地跑

```

  

## 16.4 Claude 权限建议

  

在 Claude Code 里使用：

  

```text

/permissions

```

  

建议默认策略：

  

```text

允许读项目文件

修改前先给计划

运行危险命令前确认

不要默认允许删除文件、清数据库、访问生产密钥

```

  

项目根目录可以放说明文件：

  

```text

CLAUDE.md

```

  

示例：

  

```md

# Project instructions

  

- Do not commit or push unless explicitly asked.

- Never modify production environment variables.

- Never read files under ~/secrets.

- Before changing code, summarize the plan.

- After changes, run pnpm lint and pnpm test.

- For database changes, create migration files and explain rollback.

```

  

## 16.5 给 Claude 的任务模板

  

```text

请在当前分支上处理这个任务。

目标：修复订单列表分页异常。

约束：

1. 不要改生产环境配置。

2. 不要提交，不要 push。

3. 如果需要改数据库，请先给方案，不要直接执行迁移。

4. 完成后运行 pnpm lint、pnpm test、pnpm build。

5. 最后总结：改动文件、测试结果、风险点、需要我确认的事项。

```

  

# 17. Codex 配置和使用

  

## 17.1 Codex 的几种入口

  

你会用到：

  

```text

Codex IDE extension：VS Code 里并排使用

Codex CLI：终端里使用，适合放 tmux

Codex app：桌面体验，可配合移动端远程控制

Codex cloud：把任务交给云端环境，适合 PR、CI、并行任务

```

  

## 17.2 Codex CLI

  

在 Mac mini 上安装和使用时，以 OpenAI 官方文档为准。验证：

  

```bash

codex --version

```

  

进入项目：

  

```bash

cd ~/projects/myapp

codex

```

  

建议放在 tmux：

  

```bash

tmux new -As codex

cd ~/projects/myapp

codex

```

  

## 17.3 Codex VS Code 扩展

  

在 VS Code Remote SSH 的远程工作区安装 Codex 扩展。它适合：

  

```text

解释代码

补测试

做 code review

修小 bug

委托 Codex Cloud 做较长任务

```

  

## 17.4 Codex 配置文件

  

Codex 配置通常在：

  

```text

~/.codex/config.toml

```

  

项目级配置可以放：

  

```text

.codex/config.toml

```

  

建议原则：

  

```text

默认不要全权限

按任务使用合适权限

敏感目录排除

生产密钥不放工作区

```

  

## 17.5 Claude 和 Codex 怎么分工

  

推荐：

  

```text

Claude：主力写功能、理解业务、重构

Codex：代码审查、补测试、定位 CI 失败、第二意见

```

  

不要让它们同时改同一批文件。推荐流程：

  

```text

1. Claude 改功能

2. 你看 git diff

3. Codex review

4. Claude 或你修 review 问题

5. pnpm test/build

6. 你确认后 commit

```

  

# 18. 日常使用场景手册

  

## 18.1 外出开始工作

  

Windows 上：

  

```powershell

ssh macmini

```

  

或打开 VS Code：

  

```text

Remote-SSH: Connect to Host

→ macmini

→ Open Folder ~/projects/myapp

```

  

进入 tmux：

  

```bash

cd ~/projects/myapp

tmux new -As myapp

```

  

启动依赖：

  

```bash

docker compose up -d

```

  

启动开发服务：

  

```bash

pnpm dev

```

  

## 18.2 继续昨天的 Claude/Codex 会话

  

```bash

ssh macmini

tmux ls

tmux attach -t myapp

```

  

切换到 AI 窗口：

  

```text

Ctrl+b 然后 w

选择 claude / codex 窗口

```

  

## 18.3 网络断了怎么办

  

重新连：

  

```powershell

ssh macmini

```

  

接回 tmux：

  

```bash

tmux attach -t myapp

```

  

如果 VS Code Remote SSH 断了：

  

```text

重新连接 SSH host

打开项目目录

终端里 tmux attach -t myapp

```

  

## 18.4 查看机器压力

  

```bash

htop

```

  

Docker 容器：

  

```bash

docker stats

```

  

磁盘：

  

```bash

df -h

```

  

Docker 占用：

  

```bash

docker system df

```

  

内存压力如果长期很高：

  

```text

关掉不用的浏览器标签

停止不用的 Docker 服务

Claude/Codex 不要同时跑重活

微信开发者工具不用就关

```

  

## 18.5 拉新代码并更新依赖

  

```bash

git status

git pull --rebase

pnpm install

```

  

数据库迁移：

  

```bash

pnpm db:migrate

```

  

重启服务：

  

```bash

docker compose restart

pnpm dev

```

  

## 18.6 开新功能

  

```bash

git switch -c feature/new-checkout

```

  

让 AI 做：

  

```text

请实现新结算流程。不要 commit，不要 push。完成后运行 lint/test/build 并总结风险点。

```

  

你检查：

  

```bash

git diff --stat

git diff

pnpm test

```

  

提交：

  

```bash

git add -p

git commit -m "feat: add new checkout flow"

git push -u origin feature/new-checkout

```

  

## 18.7 修 CI 失败

  

从 GitHub 复制失败日志，给 Codex 或 Claude：

  

```text

请根据下面 CI 失败日志定位问题。

优先判断是依赖、类型、测试、构建还是环境变量问题。

先解释原因，再给修复方案。不要 push。

```

  

本地复现：

  

```bash

pnpm install --frozen-lockfile

pnpm lint

pnpm test

pnpm build

```

  

## 18.8 上传小程序体验版

  

本地测试构建：

  

```bash

pnpm build:miniprogram

```

  

本地上传，替换变量：

  

```bash

WX_APPID=wx_your_appid \

WX_PRIVATE_KEY_PATH=$HOME/secrets/wechat/private.wx_your_appid.key \

WX_PROJECT_PATH=$PWD/dist/miniprogram \

VERSION=0.1.0 \

DESC="trial test" \

node scripts/upload-miniprogram.js

```

  

CI 上传：

  

```text

push develop

或手动 workflow_dispatch

```

  

然后去微信公众平台：

  

```text

版本管理

→ 开发版本

→ 设为体验版

→ 添加体验成员

```

  

# 19. 安全清单

  

## 19.1 不要提交这些文件

  

```text

.env

.env.local

.env.production

private.*.key

*.pem

*.p12

id_ed25519

id_rsa

数据库 dump

客户数据导出

```

  

`.gitignore` 示例：

  

```gitignore

.env

.env.*

!.env.example

*.pem

*.p12

private.*.key

id_ed25519*

id_rsa*

backups/

```

  

## 19.2 密钥存放建议

  

Mac mini 上：

  

```text

~/secrets/wechat/private.wx_xxx.key

~/secrets/ssh/deploy_key

```

  

设置权限：

  

```bash

chmod 700 ~/secrets

chmod 600 ~/secrets/wechat/private.wx_xxx.key

```

  

项目里只放路径说明，不放密钥本体。

  

## 19.3 AI agent 安全边界

  

给 Claude/Codex 的规则：

  

```text

不要读取 ~/secrets

不要修改 .env.production

不要执行 docker compose down -v

不要执行 rm -rf

不要 push 到 main

不要访问生产数据库

```

  

可以在 `CLAUDE.md`、Codex 项目说明、README 中重复写。

  

## 19.4 SSH 安全

  

```text

不要开放路由器 22 端口到公网

优先通过 Tailscale 访问

使用 SSH key

只允许你的 macOS 用户登录

定期检查 ~/.ssh/authorized_keys

```

  

检查 authorized_keys：

  

```bash

cat ~/.ssh/authorized_keys

```

  

## 19.5 Docker 安全

  

开发环境也要注意：

  

```text

数据库端口绑定 127.0.0.1

Redis 设置密码

不要把 Docker socket 暴露给不可信容器

不要运行来路不明镜像

生产数据不要直接导入本地，除非已脱敏

```

  

# 20. 备份和恢复

  

## 20.1 三层备份

  

```text

代码：GitHub / GitLab 远程仓库

整机：Time Machine

数据库：定期 pg_dump / 导出测试数据

```

  

## 20.2 备份点建议

  

每周至少：

  

```bash

cd ~/projects/myapp

mkdir -p backups

docker compose exec -T postgres pg_dump -U myapp myapp > backups/myapp_$(date +%F_%H%M).sql

```

  

把 `backups` 放外接盘或云盘，但不要提交到 Git。

  

## 20.3 新机器恢复流程

  

```text

1. 安装 macOS、Homebrew、Git、Docker、Tailscale、tmux

2. 从 Git 拉项目

3. 复制 .env 或根据 .env.example 重建

4. docker compose up -d

5. 恢复数据库 dump

6. pnpm install

7. pnpm dev

8. 配置 VS Code Remote SSH

```

  

恢复数据库：

  

```bash

cat backups/myapp.sql | docker compose exec -T postgres psql -U myapp -d myapp

```

  

# 21. 常见故障排查

  

## 21.1 VS Code 连不上，但 ssh 能连

  

解决顺序：

  

```text

1. Windows Terminal 先 ssh macmini

2. VS Code Remote SSH 重新连接

3. Ctrl+Shift+P → Remote-SSH: Kill VS Code Server on Host

4. 重新连接

5. 检查远程磁盘空间 df -h

```

  

Mac mini 上查看：

  

```bash

df -h

ps aux | grep vscode

```

  

## 21.2 ssh macmini 解析不了名字

  

试 Tailscale IP：

  

```powershell

tailscale status

ssh yourname@100.x.y.z

```

  

检查 MagicDNS：

  

```text

Tailscale Admin Console

→ DNS

→ MagicDNS enabled

```

  

## 21.3 tmux 里乱码或快捷键怪

  

确认终端是 UTF-8。Windows Terminal 通常没问题。

  

Mac mini 上：

  

```bash

echo $LANG

```

  

建议是：

  

```text

en_US.UTF-8

zh_CN.UTF-8

```

  

## 21.4 Docker 起不来

  

检查 Docker Desktop 是否运行：

  

```bash

docker version

```

  

如果报错找不到 daemon，打开 Docker Desktop。

  

检查容器：

  

```bash

docker compose ps

docker compose logs -f

```

  

如果端口冲突：

  

```bash

lsof -i :5432

lsof -i :6379

```

  

## 21.5 数据库连接不上

  

检查容器：

  

```bash

docker compose ps

```

  

检查端口：

  

```bash

lsof -i :5432

```

  

进入数据库：

  

```bash

docker compose exec postgres psql -U myapp -d myapp

```

  

检查 `.env`：

  

```bash

cat .env

```

  

注意密码、数据库名、端口是否一致。

  

## 21.6 pnpm dev 文件监听不更新

  

尝试：

  

```bash

brew install watchman

pnpm dev

```

  

如果项目文件在外接盘或网络盘，文件监听可能更容易出问题。建议活跃项目放内置 SSD。

  

## 21.7 磁盘空间突然很少

  

查看整体：

  

```bash

df -h

```

  

查看 Docker：

  

```bash

docker system df

```

  

查看大目录：

  

```bash

du -sh ~/Library/* 2>/dev/null | sort -h | tail

  

du -sh ~/projects/* 2>/dev/null | sort -h | tail

```

  

清理：

  

```bash

docker builder prune

pnpm store prune

```

  

谨慎：

  

```bash

docker system prune

```

  

非常谨慎：

  

```bash

docker system prune -a --volumes

```

  

## 21.8 Mac mini 重启后远程连不上

  

可能原因：

  

```text

机器睡眠

Tailscale 没自启

Docker Desktop 没自启

FileVault 需要本机登录解锁

网络未连接

路由器断网

```

  

出门前做一次完整演练：

  

```text

1. 重启 Mac mini

2. 不用本机键鼠

3. Windows 连接 Tailscale

4. ssh macmini

5. VS Code Remote SSH 连接

6. docker version

7. tmux ls

```

  

# 22. 推荐的每周维护

  

```bash

brew update

brew outdated

```

  

不要盲目升级所有包。先看项目有没有紧急需求。

  

每周检查：

  

```bash

df -h

docker system df

tmux ls

```

  

每周备份：

  

```bash

# Time Machine 插盘备份

# Git push 所有重要分支

# 数据库 dump 到外接盘

```

  

每月检查：

  

```text

Tailscale 设备是否都认识

Mac mini key expiry 是否关闭

GitHub Secrets 是否过期

微信上传密钥是否还有效

Docker Desktop 是否占用过大

```

  

# 23. 推荐别名

  

编辑：

  

```bash

nano ~/.zshrc

```

  

加入：

  

```bash

alias tls='tmux ls'

alias ta='tmux attach -t'

alias tn='tmux new -As'

alias dps='docker compose ps'

alias dlog='docker compose logs -f'

alias dup='docker compose up -d'

alias ddown='docker compose down'

alias gst='git status'

alias gd='git diff'

alias gl='git pull --rebase'

alias gp='git push'

alias proj='cd ~/projects/myapp'

alias tproj='cd ~/projects/myapp && tmux new -As myapp'

```

  

加载：

  

```bash

source ~/.zshrc

```

  

以后：

  

```bash

tproj

dup

dlog

gst

```

  

# 24. 一键检查脚本

  

创建：

  

```bash

nano ~/bin/check-dev

```

  

写入：

  

```bash

#!/usr/bin/env bash

  

echo "== System =="

hostname

whoami

uptime

  

echo ""

echo "== Disk =="

df -h /

  

echo ""

echo "== Tailscale =="

if command -v tailscale >/dev/null 2>&1; then

  tailscale status | head -20

else

  echo "tailscale command not found"

fi

  

echo ""

echo "== SSH =="

pgrep -lf sshd || true

  

echo ""

echo "== tmux =="

tmux ls || true

  

echo ""

echo "== Docker =="

docker version --format '{{.Server.Version}}' 2>/dev/null || echo "Docker not running"

docker system df 2>/dev/null || true

  

echo ""

echo "== Project =="

cd "$HOME/projects/myapp" 2>/dev/null && git status --short || echo "Project not found"

```

  

授权：

  

```bash

chmod +x ~/bin/check-dev

```

  

运行：

  

```bash

check-dev

```

  

# 25. 最佳实践总表

  

| 场景 | 推荐做法 | 不推荐 |

|---|---|---|

| 外出开发 | VS Code Remote SSH + Tailscale | 长期远程桌面 |

| 长任务 | tmux | 裸 VS Code 终端 |

| 数据库 | Docker named volume | 直接装满系统全局服务 |

| Redis/Postgres 端口 | 绑定 127.0.0.1 | 暴露到 0.0.0.0 |

| 用户测试 | staging + 小程序体验版 | 用户访问 Mac mini localhost |

| AI 改代码 | 先分支，后 diff，再测试 | 让 AI 直接 push main |

| 小程序密钥 | GitHub Secrets / ~/secrets | 提交到仓库 |

| 远程入口 | Tailscale 私网 SSH | 路由器公网转发 22 |

| Docker 空间 | 定期 docker system df | 盲目 prune --volumes |

| 备份 | Git + Time Machine + DB dump | 只靠本机硬盘 |

  

# 26. 官方资料来源

  

本手册参考了以下官方或一手资料。实际界面和命令可能随版本变化，遇到差异时以官方页面为准。

  

- Apple：Remote Login / SSH 设置  

  https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac

- Apple：睡眠与唤醒设置  

  https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac

- Apple：Time Machine 备份  

  https://support.apple.com/en-us/104984

- Apple：FileVault  

  https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac

- Apple：macOS 防火墙  

  https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac

- VS Code：Remote Development using SSH  

  https://code.visualstudio.com/docs/remote/ssh

- VS Code：Port Forwarding  

  https://code.visualstudio.com/docs/debugtest/port-forwarding

- Tailscale：macOS 安装  

  https://tailscale.com/docs/install/mac

- Tailscale：MagicDNS  

  https://tailscale.com/docs/features/magicdns

- Tailscale：Tailscale SSH  

  https://tailscale.com/docs/features/tailscale-ssh

- Tailscale：ACL / Grants 和 policy file  

  https://tailscale.com/docs/features/access-control/acls

- Tailscale：Key expiry  

  https://tailscale.com/docs/features/access-control/key-expiry

- Docker：Install Docker Desktop on Mac  

  https://docs.docker.com/desktop/setup/install/mac-install/

- Docker：Docker Desktop settings  

  https://docs.docker.com/desktop/settings-and-maintenance/settings/

- Docker：Compose file reference  

  https://docs.docker.com/reference/compose-file/

- Docker：Resource constraints  

  https://docs.docker.com/engine/containers/resource_constraints/

- tmux 官方 Wiki  

  https://github.com/tmux/tmux/wiki

- Homebrew 官方文档  

  https://docs.brew.sh/Installation

- Claude Code 文档  

  https://code.claude.com/docs/en/quickstart

- Claude Code VS Code  

  https://code.claude.com/docs/en/vs-code

- Claude Code Remote Control  

  https://code.claude.com/docs/en/remote-control

- OpenAI Codex CLI  

  https://developers.openai.com/codex/cli

- OpenAI Codex IDE extension  

  https://developers.openai.com/codex/ide

- OpenAI Codex Remote Connections  

  https://developers.openai.com/codex/remote-connections

- GitHub Actions 文档  

  https://docs.github.com/actions

- GitHub Actions Secrets  

  https://docs.github.com/actions/security-guides/using-secrets-in-github-actions

- GitHub Self-hosted runners  

  https://docs.github.com/actions/hosting-your-own-runners

- miniprogram-ci npm 包  

  https://www.npmjs.com/package/miniprogram-ci

  

# 27. 最短操作清单

  

新手只记这一版：

  

```text

1. Mac mini：关闭自动睡眠，开 Remote Login，装 Tailscale。

2. Windows：装 Tailscale，生成 SSH key，配置 ~/.ssh/config。

3. VS Code：装 Remote SSH，连接 macmini，打开 ~/projects/myapp。

4. Mac mini：装 Homebrew、tmux、Docker Desktop、Node/pnpm。

5. 每次开发：VS Code 远程打开项目，终端 tmux new -As myapp。

6. Docker：docker compose up -d 跑 Postgres/Redis。

7. Web：pnpm dev，VS Code 转发端口给 Windows 浏览器。

8. AI：Claude/Codex 放在 tmux 或 VS Code 插件里，用分支保护代码。

9. 测试：Web 部署 staging，小程序上传体验版。

10. 备份：Git push + Time Machine + 数据库 dump。

```

  

这套搭好后，你的 Mac mini 就是一台安静的远程开发母舰。Windows 是驾驶舱，tmux 是船舱隔水门，Tailscale 是隐形航道，Docker 是装在甲板下的小型数据库工厂。