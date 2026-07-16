---
title: 把 Mac mini 变成随时在线的远程工作主机
subtitle: 出差不断线、多设备连接、远程使用 AI 工具与微信真机调试完整教程
date: 2026-07-16
status: 样稿待确认
source: "[[Mac mini 远程开发工作流完全手册]]"
tags:
  - Mac-mini
  - 远程连接
  - AI编程
  - 教程
---

# 把 Mac mini 变成随时在线的远程工作主机

> 出差不断线、多设备连接、远程使用 AI 工具与微信真机调试完整教程

## 开始之前：这篇教程适合谁

如果你平时只在一台电脑上工作，很少出差，也不需要让任务持续运行，那么没有必要照搬这套方案。

这篇教程主要写给下面这些人：

- 经常出差，不能一直守在固定电脑旁边；
- 笔记本性能或续航有限，但又需要长时间运行 AI 工具和本地服务；
- 会在多台电脑之间切换，不想反复同步文件和软件环境；
- 希望在手机上查看 Claude Code 或 Codex 的远程会话；
- 希望其他电脑或手机能访问 Mac mini 上尚未正式部署的 Web 或小程序。

我实际使用的设备组合是：一台长期在线的 Mac mini、一台随身携带的 Windows 笔记本和一部手机。正文以这套组合为主线，其他设备的对应方式放在最后说明。

> [!note] 这篇教程讲什么、不讲什么
> 本文只讲设备之间如何连接、如何恢复远程会话，以及如何访问 Mac mini 上正在运行的服务，不延伸到开发配置或编程方法。

## 按你的目标选择阅读路线

### 我只想尽快从电脑连接 Mac mini

依次阅读第 6、7、8、9、10 章。

### 我只想在手机上查看 Claude Code 或 Codex

依次阅读第 8、9、12、13、19 章。

### 我只想让手机访问尚未部署的 Web 或小程序

依次阅读第 8、10、11、14、15 章。

## 第一篇：先看懂这套工作流

### 第 1 章　我为什么需要一台持续在线的远程工作主机

我以前把笔记本当作唯一的工作电脑。代码、软件、AI 对话和正在运行的服务都在笔记本里。坐在办公室时，这种方式没有明显问题；真正麻烦的是开始频繁出差以后。

笔记本既要负责计算，又要负责显示和操作。只要它断网、合盖、没电或者卡死，我正在做的事情就会一起停下来。换一台电脑，也意味着重新同步文件、重新安装软件，有时还要重新寻找上一台电脑里的运行状态。

后来我意识到，我真正需要解决的不是“再买一台更强的笔记本”，而是把**负责持续运行的电脑**和**随身携带的操作设备**分开。

#### 1.1 问题一：任务被绑在随身笔记本上

出差途中，网络中断并不可怕。可怕的是所有任务都运行在随身笔记本上：电脑没电，任务就停；合上屏幕，某些进程也可能暂停；到酒店重新开机后，还要重新寻找刚才做到哪里。

尤其是 Claude Code 这类运行在终端里的 CLI 工具，它的实际工作发生在运行它的电脑上。仅仅能在手机上看到一个聊天界面，并不代表原来的本地进程还在继续运行。

我希望达到的效果是：即使笔记本暂时断网，Mac mini 上已经启动的会话和服务仍然继续运行。网络恢复后，我只需要重新连接，而不是重新开始。

#### 1.2 问题二：笔记本同时承担太多工作

轻薄笔记本适合携带，但不一定适合长期同时运行多个终端、AI 工具、浏览器和本地服务。任务一多，风扇、发热、卡顿和续航都会变成问题。

把这些持续运行的工作交给固定供电的 Mac mini 后，笔记本只需要显示界面、输入命令和查看结果。这样做不只是为了更快，也是为了让随身设备变得更轻、更稳定。

#### 1.3 问题三：多台电脑之间的同步越来越麻烦

如果每台电脑都保存一套完整环境，就要不断处理这些问题：

- 哪台电脑上的文件是最新的；
- 某个软件到底装在哪台电脑上；
- 上一次会话在哪台电脑里；
- 为什么同一个操作换台电脑就不能用了。

我的做法是只保留一台真正的远程工作主机。无论使用办公室电脑、出差笔记本还是手机，最终连接的都是同一台 Mac mini。

设备变了，入口会变，但文件、会话和服务的位置不变。

#### 1.4 问题四：本地内容不能方便地给其他设备看

很多时候，我只是想在另一台电脑或手机上看看当前效果，并不想为了看一眼就先部署到服务器。

Web 页面相对简单，可以通过端口转发让其他设备访问。微信小程序稍微复杂一些：我需要远程操作 Mac mini 上的微信开发者工具生成二维码，同时让手机访问经过笔记本转发的本地 API。

这套流程跑通以后，我在外面也能完成真机预览，而不需要每次都先进行正式部署。

#### 1.5 从“带着环境走”变成“连接同一个环境”

改变前后的区别可以概括成下面这张表：

| 以前 | 现在 |
|---|---|
| 笔记本同时负责运行和操作 | Mac mini 负责运行，其他设备负责操作 |
| 电脑没电，任务一起停止 | 连接中断，但 Mac mini 上的任务可以继续 |
| 每台电脑维护一套环境 | 所有设备连接同一台 Mac mini |
| 手机只能查看已经部署的内容 | 手机可以进入远程会话，也能访问转发后的服务 |

这并不是把 Mac mini 变成一台真正的云服务器。它仍然需要稳定供电、联网和基础维护。区别在于：以后出门时，我不再把整个工作环境装进背包，而是只带一个能够连接它的入口。

### 第 2 章　最终要搭成什么样

在开始安装软件之前，先把整套关系看懂。否则 Tailscale、SSH、远程桌面、Termius 和 tmux 会像一串互不相关的工具名，很容易装完以后仍然不知道什么时候该打开哪一个。

#### 2.1 三类设备各自负责什么

```text
Mac mini：持续在线的远程主机
├─ 保存文件和远程工作环境
├─ 运行 Claude Code CLI、长期任务和本地服务
└─ 运行微信开发者工具等 macOS 图形界面软件

Windows 笔记本：随身控制台
├─ 通过 Tailscale 找到 Mac mini
├─ 通过 VS Code Remote SSH 使用远程文件和终端
├─ 通过 VS Code 转发端口
├─ 通过 ToDesk 或网易 UU 操作 Mac mini 桌面
└─ 通过 Codex 桌面端的 SSH 连接使用 Mac mini

手机：移动入口和预览设备
├─ 通过 Tailscale 和 Termius SSH 进入 Mac mini
├─ 恢复 tmux 中的 Claude Code CLI 会话
├─ 通过手机 App 的 Remote 进入已经配对的 Codex 主机
├─ 访问经过笔记本转发的 Web 或 API
└─ 扫描微信开发者工具生成的二维码
```

这里最重要的原则是：**Mac mini 负责持续运行，Windows 和手机负责连接。**

#### 2.2 为什么不能只安装一个远程控制软件

不同工具解决的问题并不相同。

- **Tailscale**解决“外面的设备如何安全找到家里的 Mac mini”；
- **VS Code Remote SSH**解决“如何从电脑使用 Mac mini 上的文件、终端和端口”；
- **Termius**解决“如何从手机通过 SSH 进入 Mac mini”；
- **ToDesk 或网易 UU**解决“如何操作微信开发者工具这类图形界面软件”；
- **tmux**解决“SSH 断开以后，终端会话如何继续存在”；
- **Codex 桌面 App**通过 SSH Connection 使用 Mac mini，手机 App 再通过 Remote 进入已配对的桌面主机；它们不使用 Termius 界面。

它们不是互相替代的同类软件，而是整条连接链路中的不同环节。

#### 2.3 从电脑使用 Claude Code 的路径

Claude Code 在这套方案中是运行在 Mac mini 上的 CLI。Windows 并不是直接运行另一份 Claude Code，而是通过 VS Code Remote SSH 打开 Mac mini 的终端。

```text
Windows 上的 VS Code
→ Remote SSH
→ Mac mini 终端
→ tmux
→ Claude Code CLI
```

这样一来，笔记本断开连接时，Claude Code CLI 仍然可以留在 Mac mini 的 tmux 会话中。重新连上后，再回到原来的终端会话。

#### 2.4 从手机查看 Claude Code 的路径

手机访问 Claude Code 时走的是 SSH，而不是 Codex App，也不是普通网页。

```text
手机 Tailscale
→ Termius SSH
→ Mac mini
→ tmux
→ Claude Code CLI 会话
```

这条路径特别适合在路上查看 Claude 对话、确认任务状态，或者继续进行少量输入。真正执行命令的仍然是 Mac mini。

#### 2.5 从电脑和手机使用 Codex 的路径

Codex 不走 Termius SSH。电脑端先通过 SSH 把 Codex 桌面端连接到 Mac mini；手机端再通过 Remote 进入已配对的桌面主机和同一远程环境。

```text
电脑：Codex 桌面端 → SSH 连接 → Mac mini

手机：Codex/ChatGPT App 的 Remote → 已配对的桌面主机 → Mac mini
```

所以，手机上有两条完全不同的 AI 工具入口：Termius 用来通过 SSH 进入 Mac mini 的 Claude Code CLI 会话；Codex/ChatGPT App 的 Remote 用来进入已经配对的 Codex 主机。后面的教程会分别配置，不能混在一起。

> [!note] 手机里看起来只有一步，底层仍然有配对链路
> 从手机界面看，你可以直接选择远程任务并继续操作；但按照当前官方连接方式，手机要先与桌面 App 所在的主机配对。如果桌面端又通过 SSH 连接了 Mac mini，手机会沿用这台桌面主机连接到同一个 Mac mini 环境。

#### 2.6 Web 和微信小程序如何到达手机

当手机要访问 Mac mini 上的本地服务时，请求不是凭空穿过互联网直接到达 Mac mini，而是沿着已经建立好的连接链路转发。

```text
手机
→ 笔记本地址
→ VS Code Remote SSH 转发端口
→ Mac mini 上的本地 Web 或 API
```

微信小程序还多一个界面操作步骤：通过 ToDesk 或网易 UU 打开 Mac mini 上的微信开发者工具，生成预览二维码，再用手机扫码。

到这里，你只需要先记住三件事：Mac mini 是持续运行的主机；不同入口负责不同类型的操作；连接断开不应等于远程任务停止。接下来再逐个安装工具，就不会变成没有目标地照抄命令。

### 第 3 章　不同场景应该打开哪个工具

第一次看到这套方案时，很容易产生一个误解：既然都是“远程连接”，是不是挑一个远程控制软件就够了？

实际上，不同工具解决的是不同问题。你不需要每次把所有软件都打开，而是先判断自己现在要做什么，再进入对应的连接入口。

#### 3.1 我在外面，首先要让设备找到 Mac mini

这时使用 **Tailscale**。

普通家庭网络里的 Mac mini 通常没有一个适合直接暴露到互联网的固定地址。Tailscale 会在你的 Mac mini、Windows 和手机之间建立一个只有这些设备能够加入的私有网络。

它解决的是“设备如何互相找到”，不是“如何操作桌面”或“如何打开终端”。所以 Tailscale 通常是第一层：没有这层网络，后面的 SSH、Termius 和端口访问都没有稳定入口。

可以把它理解成一条只对自己设备开放的内部道路。Mac mini 仍然放在家里，但你的笔记本和手机像是进入了同一个内网。

#### 3.2 我在电脑上，要查看文件、使用终端或转发端口

这时使用 **VS Code Remote SSH**。

VS Code 的窗口开在 Windows 上，但你打开的是 Mac mini 里的远程目录，终端也实际运行在 Mac mini 上。你不需要把同一份文件和运行环境复制到 Windows。

连接成功后，VS Code 左侧的资源管理器会像打开本地文件夹一样，直观地显示 Mac mini 上的文件夹和文件。你可以直接点击文件打开、逐层展开目录，也可以使用 VS Code 的搜索功能查找文件或内容，不需要先学会用终端命令在目录之间寻找。

这正是 VS Code Remote SSH 对非技术用户最友好的地方：文件实际保存在 Mac mini 上，但查看和编辑方式与平时在 VS Code 中打开本地文件几乎一样。连接后，窗口底部状态栏会显示远程主机名，帮助你分清自己正在操作 Windows 本地文件，还是 Mac mini 上的远程文件。

它还承担一个重要职责：端口转发。当 Mac mini 上有一个只能本机访问的 Web 或 API 时，VS Code 可以把这个端口带到 Windows，再让浏览器或手机访问。

VS Code Remote SSH 是电脑上的主入口，但它不适合操作微信开发者工具等完整的 macOS 图形界面。

#### 3.3 我只有手机，要进入 Mac mini 的终端

这时使用 **Tailscale + Termius**。

Tailscale 先让手机找到 Mac mini，Termius 再通过 SSH 登录。进入以后，你看到的是 Mac mini 的终端，而不是 Mac 桌面。

这条路径主要用来恢复 tmux 中已经存在的 Claude Code CLI 会话，查看 Claude 对话、任务输出和当前状态。真正的程序仍然运行在 Mac mini 上，手机只是一个随身终端。

手机屏幕和键盘不适合长时间输入，因此它更适合查看、确认和少量操作，而不是代替电脑完成所有工作。

#### 3.4 我需要操作微信开发者工具等图形界面

这时使用 **ToDesk 或网易 UU**。

SSH 只能提供文件和终端，不能完整显示 Mac mini 的桌面。微信开发者工具、系统设置等软件需要图形界面，因此必须额外准备远程桌面入口。

远程桌面的作用很明确：只在需要操作 GUI 软件时打开。平时查看文件和终端仍然优先使用 VS Code Remote SSH，因为画面传输对网络和流量的要求更高。

#### 3.5 我希望终端断开以后，会话仍然存在

这时使用 **tmux**。

SSH、VS Code 和 Termius 都是连接入口。连接断开时，如果任务只运行在普通终端里，终端关闭后任务可能随之结束。

tmux 像是保存在 Mac mini 上的“终端房间”。你可以从 Windows 进入这个房间，也可以稍后从手机进入。外面的连接换了，房间里的 Claude Code CLI 和其他长期任务仍然留在原处。

所以，Tailscale 解决“能不能找到”，SSH 解决“能不能进去”，tmux 解决“离开以后还在不在”。

#### 3.6 我要使用 Claude Code 或 Codex

两者都可以远程使用，但入口不同。

**Claude Code 是 Mac mini 上的 CLI：**

- 电脑通过 VS Code Remote SSH 进入 Mac mini 终端；
- 手机通过 Tailscale 和 Termius SSH 进入 Mac mini；
- 两端都可以恢复 tmux 中的 Claude Code CLI 会话。

**Codex 使用自己的 Remote 入口：**

- 电脑通过 Codex 桌面端的 SSH Connection 进入 Mac mini；
- 手机通过 Codex/ChatGPT App 的 Remote 进入已经配对的主机。

这里不讨论两个工具分别适合完成什么任务，只需要记住它们的连接方式不同。Termius 是手机 SSH 客户端；Codex/ChatGPT App 的 Remote 不是通用 SSH 客户端。

#### 3.7 我要在其他设备上查看 Web 或小程序

查看 Web 时，主要使用 **VS Code 端口转发**。Mac mini 负责运行目标服务，Windows 把对应端口转发出来，其他设备再访问 Windows 上的地址。

查看微信小程序时，还需要 **远程桌面**。因为预览二维码由 Mac mini 上的微信开发者工具生成，所以要先远程操作桌面，再使用手机扫码。

这两条路径最终都可能访问 Mac mini 上的本地 API，但入口不同：Web 从浏览器进入，小程序从开发者工具生成的预览版本进入。

> [!tip] 最简单的判断方法
> 要找设备，打开 Tailscale；要用电脑终端，打开 VS Code Remote SSH；要用手机终端，打开 Termius；要看 Mac 桌面，打开 ToDesk 或网易 UU；要恢复长期终端会话，进入 tmux；要使用 Codex，打开 Codex 桌面端或手机 App。

### 第 4 章　你是否适合使用这套方案

这套方案并不是所有人都需要。它解决的是“固定主机持续运行，其他设备随时连接”的问题，而不是让每个人都把简单操作变得更复杂。

#### 4.1 哪些人会明显受益

如果你符合下面两三项，这套方案通常值得搭建：

- 经常出差，不能一直使用同一台电脑；
- 需要让 Claude Code CLI 或其他终端任务持续运行；
- 随身笔记本性能、续航或散热有限；
- 会在办公室电脑、出差笔记本和手机之间切换；
- 必须使用微信开发者工具等 macOS 图形界面软件；
- 希望在外面查看 Mac mini 上的 Web、API 或小程序预览。

它尤其适合“设备很多，但希望远程工作环境只有一份”的个人用户。

#### 4.2 哪些情况没必要完整照搬

如果你只是偶尔在一台电脑上查看文件，或者所有任务几分钟内就能结束，那么直接使用本机通常更简单。

下面这些情况也可以只搭其中一部分：

- 不需要手机终端：可以暂时不安装 Termius；
- 不需要操作 GUI 软件：可以暂时不配置远程桌面；
- 不需要长期终端会话：可以先不使用 tmux；
- 不使用 Codex：可以跳过 Codex 桌面端和手机 App；
- 不需要跨设备预览：可以跳过端口转发和小程序章节。

教程虽然写出了完整链路，但不要求每个人安装所有工具。

#### 4.3 搭建前必须接受的几个现实

**Mac mini 必须能够持续开机和联网。**它断电、休眠或网络中断时，外面的设备无法凭空连接它。

**远程连接无法替代所有现场操作。**某些系统更新、权限弹窗、重启后的异常状态，仍可能需要人在 Mac mini 旁处理。因此第一次搭建最好在本地完成，并准备一种备用远程入口。

**连接速度取决于两端网络。**SSH 和文字终端对网络要求较低，远程桌面和图形界面对延迟更敏感。网络较差时，应优先使用终端入口。

**手机适合应急和查看，不适合承担全部操作。**Termius 可以让你进入 Claude Code CLI 会话，Codex App 可以进入 Codex 远程连接，但小屏幕仍会限制复杂操作。

**这是一台个人远程主机，不是一套高可用云服务。**它能提高连续性，却不会自动解决断电、硬盘损坏、账号丢失和备份问题。后面的安全与恢复章节仍然需要认真处理。

#### 4.4 不要一开始追求“最完整配置”

新手最容易犯的错误，是看到一长串工具以后一次性全部安装。这样做的问题是：出现连接失败时，你不知道故障发生在哪一层。

更稳妥的方式是逐层建立连接：先确认 Mac mini 持续在线，再确认 Tailscale 能找到它，然后配置 SSH，最后才加入 VS Code、Termius、远程桌面和其他入口。

每增加一个工具，都应该知道它解决了哪个已经存在的问题。没有对应使用场景的工具，可以先跳过。

### 第 5 章　搭建路线与完成目标

整套流程按照依赖关系分成三个阶段。前一阶段没有正常工作时，不要急着进入下一阶段。

#### 5.1 第一阶段：先让设备能够互相找到并连接

这一阶段只解决最基础的问题：Windows 和手机能否从外面找到 Mac mini，并通过 SSH 进入。

顺序是：

1. 在本地完成 Mac mini 的设备命名、电源、网络和 Remote Login 设置；
2. 在 Mac mini、Windows 和手机登录同一个 Tailscale 网络；
3. 从 Windows 使用 SSH 连接 Mac mini；
4. 从手机使用 Termius 连接 Mac mini。

完成这一阶段后，你已经拥有电脑和手机两种文字终端入口。即使 VS Code、远程桌面和 AI 工具还没有配置，最基本的远程通道也已经成立。

#### 5.2 第二阶段：建立适合日常使用的入口

基础 SSH 跑通以后，再配置更方便的操作方式：

1. 使用 VS Code Remote SSH 打开 Mac mini 的远程目录和终端；
2. 配置 ToDesk 或网易 UU，作为图形界面入口；
3. 使用 tmux 保存长期终端会话；
4. 从电脑和手机分别进入 Claude Code CLI 会话；
5. 使用 Codex 桌面端和手机 App 建立 Codex 远程连接。

这一阶段的重点不是“多装几个软件”，而是让每个入口都承担明确职责。电脑适合完整操作，手机适合查看和应急，Mac mini 始终负责实际运行。

#### 5.3 第三阶段：让其他设备访问 Mac mini 上的内容

连接和会话稳定以后，再处理跨设备预览：

1. 确认需要访问的 Web 或 API 端口；
2. 通过 VS Code Remote SSH 把端口转发到 Windows；
3. 让浏览器或手机访问 Windows 上的转发地址；
4. 通过远程桌面操作 Mac mini 上的微信开发者工具；
5. 生成二维码，在手机上完成小程序真机预览。

这一阶段解决的是“如何看到 Mac mini 上正在运行的内容”，不是“如何开发这个项目”。教程只讲连接路径，不进入项目配置和编程细节。

#### 5.4 推荐的最短搭建顺序

如果你不想一开始阅读所有内容，可以按下面的顺序推进：

```text
Mac mini 保持在线
→ 三台设备连接 Tailscale
→ Windows SSH
→ 手机 Termius SSH
→ VS Code Remote SSH
→ tmux
→ 远程桌面
→ Claude Code / Codex 远程入口
→ Web 与小程序访问
```

这个顺序有意把网络和 SSH 放在最前面。底层连接稳定以后，上层工具出现问题时才容易判断：到底是 Mac mini 不在线、Tailscale 不通、SSH 配置错误，还是某个具体应用没有连接成功。

## 第二篇：从零开始搭建

### 第 6 章　准备设备、账号和网络

这一章不安装任何东西，只把后面会用到的设备、账号和名称准备好。提前记录这些信息，可以避免你在不同设备之间来回确认“用户名到底是什么”“哪台机器才是 Mac mini”。

#### 6.1 需要准备的三台设备

本文按照下面这套实际组合演示：

| 设备 | 主要作用 | 第一次设置时需要什么 |
|---|---|---|
| Mac mini | 持续在线的远程主机 | 显示器、键盘和鼠标 |
| Windows 笔记本 | 电脑端控制入口 | 能正常联网 |
| 手机 | 移动 SSH、Codex 连接和真机预览 | 能安装 Tailscale、Termius 和 Codex App |

第一次搭建必须在 Mac mini 旁边完成。不要在只剩远程连接的情况下修改睡眠、网络、SSH 或磁盘加密设置，否则一步操作出错就可能失去连接。

#### 6.2 固定主机需要稳定的电源和网络

Mac mini 要长期放在一个固定位置，并保持供电。网络优先使用下面的连接方式：

```text
Mac mini
→ 网线
→ 家庭或办公室路由器的 LAN 口
```

Wi-Fi 也能使用，但有线连接通常更稳定。Tailscale 不要求你拥有公网 IP，也不需要在路由器上开放 SSH 端口。

如果所在地偶尔停电，可以以后增加 UPS，但它不是完成第一次连接的前提。

#### 6.3 需要准备的账号和应用

| 工具 | 安装在哪些设备 | 是否要求同一账号 |
|---|---|---|
| Tailscale | Mac mini、Windows、手机 | 三台设备必须进入同一个 tailnet |
| VS Code | Windows | 不要求与 Tailscale 使用同一账号 |
| Termius | 手机 | 可以先不注册同步账号，但要保护好连接凭据 |
| ToDesk 或网易 UU | Mac mini、Windows | 两端需要建立可用的远程控制关系 |
| Claude Code | Mac mini | 在远程终端中使用 |
| Codex | Windows 桌面端和手机 App | 手机 Remote 与桌面主机需要使用同一个 ChatGPT 账号和 workspace |
| 微信开发者工具 | Mac mini | 需要微信开发者账号 |

这一批章节只配置 Tailscale、SSH 和 Termius。其他应用会在后面的对应章节处理。

#### 6.4 统一设备名称

设备名称应该短、容易输入，并且一眼能看出是哪台设备。本文统一使用：

```text
Mac mini：macmini-dev
Windows：win-laptop
手机：phone-joe
```

你可以换成自己的名称，但后面看到 `macmini-dev` 时，要知道它代表你的 Mac mini，而不是一条可以原样照抄的固定名称。

名称尽量只使用英文字母、数字和连字符，不要使用空格和中文。这样在 SSH 和其他工具里输入时更省事。

#### 6.5 记录 Mac mini 用户名

SSH 登录不仅需要设备名称，还需要 Mac mini 上的用户账号。这个用户名不一定等于你在登录界面看到的中文全名。

**在 Mac mini 的“终端”中执行：**

```bash
whoami
```

假设输出是：

```text
yourname
```

把它记录下来。后面的 `yourname` 都要替换为这个真实用户名。

> [!warning] 不要记录在公开文档里的信息
> 不要把 Mac 登录密码、SSH 私钥、Tailscale 登录凭据或恢复密钥写进这篇教程。教程只记录设备名、用户名和操作路径。

### 第 7 章　让 Mac mini 适合作为长期远程主机

普通 Mac 默认以“有人坐在机器前使用”为前提。作为远程主机后，它需要保持在线、允许 SSH 登录，并且在关闭显示器后仍然继续运行。

#### 7.1 给 Mac mini 设置容易识别的名称

**在 Mac mini 上操作：**

```text
苹果菜单
→ 系统设置
→ 通用
→ 关于本机
→ 名称
```

把名称改成前面确定的 `macmini-dev`。

这个名称用于 Finder 和共享服务。macOS 还会生成一个本地网络名称，例如：

```text
macmini-dev.local
```

在同一个局域网内，你可能会看到 `.local` 名称；通过 Tailscale MagicDNS 连接时，后面主要使用 `macmini-dev`。

#### 7.2 防止 Mac mini 自动睡眠

显示器可以关闭，但 Mac mini 本身不能因为长时间无人操作而自动睡眠。

**在 Mac mini 上操作：**

```text
苹果菜单
→ 系统设置
→ 能源
```

打开下面两个选项：

- **显示器关闭时防止自动睡眠**；
- **唤醒以供网络访问**。

不同机型和 macOS 版本显示的选项可能略有差异。最关键的是第一项：关闭显示器不等于让整台 Mac 进入睡眠。

Apple 提醒，阻止睡眠会增加耗电。对于长期远程主机，这是为了保持可连接而接受的取舍。

#### 7.3 设置断电恢复后的启动方式

仍然在“能源”设置中，查看是否有下面其中一个选项：

- **接通电源时启动**；
- **断电后自动启动**。

较新的 Mac mini 和 macOS 可能提供“接通电源时启动”，可以选择“总是”或“断电后”。其他机型可能显示“断电后自动启动”。如果你的设置中没有这个选项，不要为了追求一致而执行不理解的系统命令。

这个设置只能帮助 Mac mini 在恢复供电后开机，不能保证所有远程软件已经登录并可用。完成整套配置后，还要实际重启一次确认。

#### 7.4 开启 Remote Login

Remote Login 是 macOS 自带的 SSH 服务。Tailscale 负责建立私网，真正接收 SSH 连接的是这里。

**在 Mac mini 上操作：**

```text
苹果菜单
→ 系统设置
→ 通用
→ 共享
→ 远程登录右侧的信息按钮
→ 打开“远程登录”
```

在“允许访问”中选择：

```text
仅这些用户
→ 添加你自己的 Mac 用户
```

不要为了省一步直接允许所有用户。本文也不需要打开“允许远程用户完全访问磁盘”；只有确认某项功能确实需要时再单独授权。

打开后，页面会显示一条类似下面的 SSH 地址：

```text
ssh yourname@macmini-dev.local
```

先把这条地址记下来，下一章安装 Tailscale 后会改用更适合外出连接的设备名。

#### 7.5 打开防火墙，但不要公开 22 端口

**在 Mac mini 上操作：**

```text
苹果菜单
→ 系统设置
→ 网络
→ 防火墙
→ 打开
```

开启 Remote Login 后，macOS 的共享服务可以按系统规则接收连接。本文使用 Tailscale 私网访问 SSH，不需要在家庭路由器中把公网 22 端口转发给 Mac mini。

> [!danger] 不要照着网上教程开放公网 SSH
> 路由器端口转发、DMZ 主机和公网暴露都不属于本文方案。后面如果 SSH 连不上，应先检查 Tailscale、Remote Login 和用户名，而不是把 22 端口直接暴露到互联网。

#### 7.6 谨慎处理 FileVault 和系统更新

FileVault 可以提高磁盘数据安全，但远程主机在重启后是否能远程解锁，取决于 Mac 机型、macOS 版本和网络条件。macOS 26 或更新版本的部分 Apple 芯片 Mac 已支持在符合条件时通过 SSH 解锁 FileVault，但不要假设自己的机器一定满足条件。

更稳妥的做法是：

1. 把 FileVault 恢复密钥安全保存在 Mac mini 以外的位置；
2. 在本地重启 Mac mini；
3. 不触碰本机键盘，分别测试 Tailscale、SSH 和备用远程桌面；
4. 确认真正能恢复连接后再出门。

系统大版本更新也应在本地进行。不要在出差前一天更新 macOS、Tailscale 和所有远程工具，否则出现问题时很难判断是哪一层发生了变化。

#### 7.7 现在应该看到什么

完成本章后，Mac mini 应该保持开机和联网；显示器关闭后机器仍然运行；“远程登录”处于开启状态，并且只有你指定的用户可以登录。

下一章才会建立外出使用的私网入口。此时不要急着从手机流量连接，也不要改动 SSH 的高级配置。

> [!info] 官方参考
> - [Apple：更改 Mac 的电脑名称或本地主机名](https://support.apple.com/guide/mac-help/mchlp2322/mac)
> - [Apple：设置 Mac 的睡眠与唤醒](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)
> - [Apple：设置 Mac mini 接通电源时启动](https://support.apple.com/en-us/125517)
> - [Apple：允许远程电脑访问 Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)
> - [Apple：更改 Mac 防火墙设置](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh11783/mac)
> - [Apple：FileVault 与 SSH 解锁说明](https://support.apple.com/guide/deployment/dep82064ec40/web)

### 第 8 章　安装 Tailscale，建立安全私网

这一章要让 Mac mini、Windows 和手机进入同一个 Tailscale 私网。完成后，即使三台设备不在同一个 Wi-Fi 下，也能使用 Tailscale 分配的名称或地址互相找到。

#### 8.1 先理解“同一个 tailnet”

第一次在某台设备登录 Tailscale 时，Tailscale 会创建或加入一个名为 **tailnet** 的私有网络。

三台设备必须使用同一种身份登录到同一个 tailnet。例如，Mac mini 使用某个 Google 账号登录，Windows 和手机也要使用同一个账号和同一个登录入口。

仅仅在三台设备上都安装 Tailscale 还不够。如果登录到了不同账号，它们仍然看不到彼此。

#### 8.2 在 Mac mini 安装 Tailscale

Tailscale 官方当前推荐 macOS 使用 standalone 版本。当前客户端要求 macOS 12 Monterey 或更高版本。

**在 Mac mini 上操作：**

1. 打开 [Tailscale macOS 安装页面](https://tailscale.com/docs/install/mac)；
2. 选择官方标注为推荐的 **Standalone variant**；
3. 下载并安装；
4. 打开 Tailscale，按引导允许安装 VPN 配置；
5. 使用你准备好的账号登录。

macOS 弹出的 VPN 配置授权是正常步骤。Tailscale 需要它来建立私网连接。

登录完成后，Tailscale 菜单中应该能看到这台 Mac 已连接。暂时不要关闭应用，也不要切换到其他登录账号。

#### 8.3 在 Windows 安装 Tailscale

**在 Windows 上操作：**

1. 打开 [Tailscale Windows 安装页面](https://tailscale.com/docs/install/windows)；
2. 下载最新的 `.exe` 安装程序；
3. 完成安装后，在任务栏右下角找到 Tailscale 图标；
4. 如果图标没有直接显示，点击向上的箭头展开托盘图标；
5. 右键点击 Tailscale，选择登录；
6. 浏览器打开后，使用与 Mac mini 相同的账号完成登录。

Windows 客户端登录成功后，托盘菜单会显示当前账号和连接状态。

#### 8.4 在手机安装 Tailscale

**在 iPhone 上：**从 App Store 安装 Tailscale。当前官方客户端要求 iOS 15 或更高版本。

**在 Android 上：**从 Google Play 安装 Tailscale。当前官方客户端要求 Android 8 或更高版本。

打开应用后：

1. 点击开始；
2. 允许创建 VPN 配置；
3. 允许必要的系统提示；
4. 使用与 Mac mini、Windows 相同的账号登录；
5. 打开 Tailscale 连接开关。

手机状态栏出现 VPN 标识是正常现象。它表示手机已经启用 Tailscale 网络连接，不代表所有手机流量都会经 Mac mini 转发。本文不会把 Mac mini 配置为出口节点。

#### 8.5 在管理后台确认三台设备

在浏览器打开 Tailscale 管理后台的 **Machines** 页面。你应该看到 Mac mini、Windows 和手机三台设备。

给它们设置容易识别的名称：

```text
macmini-dev
win-laptop
phone-joe
```

通常可以在设备行右侧的菜单中编辑 machine name。改名后，后面的 MagicDNS 名称也会跟着变化。

如果 Machines 页面只有两台设备，先不要继续配置 SSH。回到缺失的那台设备，检查它是否使用了同一个 Tailscale 登录账号。

#### 8.6 使用 MagicDNS 设备名

MagicDNS 会把设备名注册成 tailnet 内可使用的地址。2022 年 10 月 20 日以后创建的 tailnet 默认启用 MagicDNS；如果你的网络较早，可以在 Tailscale 管理后台的 **DNS** 页面检查。

启用后，不需要记住一串 `100.x.x.x` 地址。后面可以直接使用：

```text
macmini-dev
```

如果设备名暂时无法解析，也可以打开 Tailscale 设备详情，记录 Mac mini 的 `100.x.x.x` 地址作为排错备用。日常连接仍然优先使用设备名。

#### 8.7 检查三台设备是否在线

最直观的检查方式是查看 Tailscale 应用或 Machines 页面：三台设备都应显示在线或最近在线。

如果 Windows 的 Tailscale 命令行可用，可以在 **Windows PowerShell** 中执行：

```powershell
tailscale status
```

你应该在输出中看到 `macmini-dev` 和手机名称。

也可以在 **Windows PowerShell** 中测试 Tailscale 网络：

```powershell
tailscale ping macmini-dev
```

如果 Windows 客户端没有提供命令行，就使用托盘菜单和 Machines 页面检查，不必为了这一步安装其他工具。

#### 8.8 只对可信的 Mac mini 关闭 key expiry

Tailscale 设备密钥会定期要求重新认证。密钥过期后，这台设备与其他设备之间的 Tailscale 连接会停止。

Mac mini 长期放在固定位置，适合在确认设备可信后关闭 key expiry：

```text
Tailscale 管理后台
→ Machines
→ 找到 macmini-dev
→ 右侧菜单
→ Disable Key Expiry
```

不要顺手对 Windows 和手机也关闭过期。它们是随身设备，更容易丢失。关闭密钥过期会降低安全性，只应针对难以现场重新认证、并且由你长期控制的 Mac mini。

#### 8.9 本文使用 OpenSSH over Tailscale

从这一章开始，连接关系是：

```text
Tailscale：提供三台设备之间的私网
macOS Remote Login：提供 SSH 服务
Windows / Termius：通过 Tailscale 设备名连接 SSH
```

这叫做普通 OpenSSH 运行在 Tailscale 私网上。本文不启用 Tailscale SSH，也不修改 tailnet policy。这样与 VS Code Remote SSH、Windows OpenSSH 和 Termius 的配合更直接，也更容易排查。

> [!info] 官方参考
> - [Tailscale：在 macOS 安装](https://tailscale.com/docs/install/mac)
> - [Tailscale：在 Windows 安装](https://tailscale.com/docs/install/windows)
> - [Tailscale：在 iOS 安装](https://tailscale.com/docs/install/ios)
> - [Tailscale：在 Android 安装](https://tailscale.com/docs/install/android)
> - [Tailscale：MagicDNS](https://tailscale.com/docs/features/magicdns)
> - [Tailscale：Key expiry](https://tailscale.com/docs/features/access-control/key-expiry)

### 第 9 章　配置 SSH，让电脑和手机进入 Mac mini

Tailscale 让三台设备处于同一个私网，但它本身不会把 Mac mini 终端显示出来。现在需要使用 SSH 真正登录 Mac mini。

这一章分成两条路径：

```text
Windows → OpenSSH → Mac mini
手机 → Tailscale → Termius → Mac mini
```

#### 9.1 检查 Windows 的 OpenSSH Client

Windows 只需要 **OpenSSH Client**，不需要安装 OpenSSH Server。

**在 Windows PowerShell 中执行：**

```powershell
ssh -V
```

如果能看到 OpenSSH 版本号，说明客户端已经可用。

如果提示找不到 `ssh`，在 Windows 中打开：

```text
设置
→ 系统
→ 可选功能
→ 查看功能或添加可选功能
→ 搜索 OpenSSH Client
→ 安装
```

安装完成后重新打开 PowerShell，再执行一次 `ssh -V`。

#### 9.2 第一次从 Windows 使用密码登录

开始前确认：

- Mac mini 已开启 Remote Login；
- Mac mini 和 Windows 的 Tailscale 都处于连接状态；
- 你已经知道 Mac mini 的真实用户名；
- Tailscale 中的 Mac 名称是 `macmini-dev`。

**在 Windows PowerShell 中执行：**

```powershell
ssh yourname@macmini-dev
```

把 `yourname` 换成第 6 章记录的 Mac 用户名。

第一次连接会显示主机指纹，并询问是否继续。确认你连接的是自己的 `macmini-dev` 后输入：

```text
yes
```

接着输入 Mac mini 的登录密码。输入密码时屏幕不会显示星号或字符，这是终端的正常安全行为，输入完成后直接按回车。

登录成功后执行：

```bash
whoami
hostname
pwd
```

这里的命令已经在 Mac mini 上执行。如果 `whoami` 显示你的 Mac 用户名，说明基础 SSH 链路已经成立。

#### 9.3 在 Windows 生成专用 SSH 密钥

每次输入 Mac 登录密码既不方便，也不适合作为长期连接方式。接下来为这台 Windows 生成一对只用于连接 Mac mini 的 SSH 密钥。

**在 Windows PowerShell 中执行：**

```powershell
New-Item -ItemType Directory -Force $HOME\.ssh
ssh-keygen -t ed25519 -f $HOME\.ssh\id_ed25519_macmini -C "windows-to-macmini"
```

命令会询问是否设置 passphrase。设置后更安全，但以后连接时可能需要输入这段口令；不设置则操作更方便。无论选择哪一种，都不能把私钥发给别人。

生成后会得到两个文件：

```text
C:\Users\你的用户名\.ssh\id_ed25519_macmini
C:\Users\你的用户名\.ssh\id_ed25519_macmini.pub
```

- 带 `.pub` 的文件是公钥，可以放到 Mac mini；
- 不带 `.pub` 的文件是私钥，只能保存在 Windows 自己的账户中。

#### 9.4 把 Windows 公钥加入 Mac mini

下面的命令会先用 Mac 登录密码连接，然后把 Windows 公钥加入 Mac mini 的授权列表。

**在 Windows PowerShell 中执行：**

```powershell
Get-Content $HOME\.ssh\id_ed25519_macmini.pub | ssh yourname@macmini-dev "umask 077; mkdir -p ~/.ssh; cat >> ~/.ssh/authorized_keys; chmod 600 ~/.ssh/authorized_keys"
```

替换 `yourname`，输入最后一次 Mac 登录密码。

然后测试密钥登录：

```powershell
ssh -i $HOME\.ssh\id_ed25519_macmini yourname@macmini-dev
```

如果你设置了密钥 passphrase，这里输入的是密钥口令，不是 Mac 登录密码。成功进入 Mac 终端，说明公钥配置完成。

#### 9.5 配置一个容易记住的 SSH 名称

打开 Windows 用户目录中的文件：

```text
C:\Users\你的用户名\.ssh\config
```

如果文件不存在，可以新建一个名为 `config`、没有扩展名的文本文件。

写入下面内容：

```sshconfig
Host macmini
    HostName macmini-dev
    User yourname
    IdentityFile ~/.ssh/id_ed25519_macmini
    IdentitiesOnly yes
    ServerAliveInterval 30
    ServerAliveCountMax 6
```

需要替换两处：

- `HostName macmini-dev`：换成你的 Tailscale machine name；
- `User yourname`：换成你的 Mac 用户名。

以后在 **Windows PowerShell** 中只需要执行：

```powershell
ssh macmini
```

这个 `macmini` 是你在 SSH config 中定义的快捷名称。后面的 VS Code Remote SSH 也会直接读取它。

#### 9.6 在手机安装 Termius

在 iPhone App Store 或 Android Google Play 中搜索并安装 Termius。

安装后先完成两件事：

1. 打开手机上的 Tailscale，并确认处于连接状态；
2. 打开 Termius，允许必要的本地通知和生物识别保护。

Termius 是 SSH 客户端。它不会代替 Tailscale，也不会自动知道 Mac mini 在哪里。

#### 9.7 在 Termius 中添加 Mac mini 主机

Termius 将一台要连接的设备称为 **Host**。新建 Host 时填写：

| 字段 | 填写内容 |
|---|---|
| Label | `Mac mini` |
| Address | `macmini-dev` |
| Port | `22` |
| Username | 你的 Mac 用户名 |
| Password | 第一次连接可临时填写 Mac 登录密码 |

不同版本的 Termius 入口可能显示为 **New Host**、**Add Host** 或加号按钮，但需要填写的核心信息相同。

保存后点击这个 Host。第一次连接同样会显示主机指纹，确认设备名称后继续。进入终端后执行：

```bash
whoami
hostname
```

输出应该来自 Mac mini，而不是手机。

如果 `macmini-dev` 无法解析，可以临时把 Address 改成 Tailscale 中显示的 Mac mini `100.x.x.x` 地址。设备名能正常工作后，再改回更容易记忆的名称。

#### 9.8 给手机单独准备 SSH 密钥

不要把 Windows 私钥发送到手机。更安全、也更容易撤销的做法，是在 Termius 的 Keychain 中生成一把手机专用密钥，例如：

```text
macmini-phone
```

复制这把密钥的**公钥**。私钥留在手机的 Termius 中，不要通过聊天软件发送。

先使用密码登录 Mac mini，然后在 **Termius 连接的 Mac 终端**中执行：

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cat >> ~/.ssh/authorized_keys
```

把刚才复制的公钥粘贴为完整一行，按回车，然后按 `Ctrl+D` 结束输入。继续执行：

```bash
chmod 600 ~/.ssh/authorized_keys
```

回到 Termius 的 Host 设置，把 `macmini-phone` 密钥指定为 SSH 凭据，然后重新连接。

确认密钥登录成功前，不要删除 Host 中的密码，也不要修改 Mac mini 的密码登录设置。

#### 9.9 从 Termius 回到 Claude Code 会话

本章只确认手机能够进入 Mac mini。第 12 章配置 tmux 后，手机的实际路径会变成：

```text
手机 Tailscale
→ Termius Host：Mac mini
→ tmux 会话
→ Claude Code CLI
```

届时断开 Termius 不会结束 tmux 中的 Claude Code CLI。重新连接后，使用第 12 章的 `tmux attach` 命令回到原会话。

#### 9.10 常见连接问题先检查什么

**提示 `Could not resolve hostname`：**先确认手机或 Windows 的 Tailscale 已连接，并检查 `macmini-dev` 是否与 Machines 页面名称一致。

**提示 `Connection timed out`：**检查 Mac mini 是否开机、联网，Tailscale 是否在线，以及 Remote Login 是否仍然开启。

**提示 `Permission denied`：**先检查 Mac 用户名是否正确；使用密钥时，再检查是否选中了对应私钥。

**Termius 用 Tailscale IP 能连、设备名不能连：**说明 SSH 本身正常，问题更可能在 MagicDNS 或设备名称，不要重新生成密钥。

> [!info] 官方参考
> - [Apple：允许远程电脑访问 Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)
> - [Microsoft：开始使用 Windows OpenSSH](https://learn.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse)
> - [Termius：移动端使用 AI Agent 的连接建议](https://termius.com/blog/8-tips-for-using-ai-agents-on-mobile-in-termius)

### 第 10 章　配置 VS Code Remote SSH

Windows PowerShell 已经能够执行 `ssh macmini` 后，再配置 VS Code Remote SSH。它不会建立一套新的连接，而是读取第 9 章的 SSH config，把已经跑通的 SSH 变成更直观的文件、终端和端口界面。

#### 10.1 在 Windows 安装 VS Code 和 Remote - SSH

**在 Windows 上操作：**

1. 从 [VS Code 官网](https://code.visualstudio.com/)安装 Visual Studio Code；
2. 打开 VS Code；
3. 点击左侧 **Extensions（扩展）**图标，或按 `Ctrl+Shift+X`；
4. 搜索 **Remote - SSH**；
5. 确认发布者是 Microsoft，然后点击 **Install**。

如果你看到的是 **Remote Development** 扩展包，也可以安装，但本文真正需要的是其中的 Remote - SSH。

#### 10.2 使用 SSH config 连接 Mac mini

先在 Windows PowerShell 再确认一次：

```powershell
ssh macmini
```

这一步失败时，不要在 VS Code 里反复重试。先回到第 9 章修复 SSH。

PowerShell 能连接后，在 VS Code 中：

```text
Ctrl+Shift+P
→ 输入 Remote-SSH: Connect to Host
→ 选择 macmini
```

首次连接时，VS Code 可能询问远程主机的操作系统。Mac mini 选择：

```text
macOS
```

VS Code 随后会在 Mac mini 上准备远程组件。这个过程可能持续一段时间，期间不要关闭窗口。

连接完成后，窗口底部状态栏会显示类似：

```text
SSH: macmini
```

它表示这个 VS Code 窗口正在操作 Mac mini，而不是 Windows 本地环境。

#### 10.3 像本地文件夹一样打开 Mac mini 文件

连接完成后选择：

```text
File
→ Open Folder
```

此时文件选择窗口显示的是 **Mac mini 的文件系统**。第一次可以先打开自己的主目录：

```text
/Users/yourname
```

打开后，VS Code 左侧资源管理器会显示 Mac mini 上的文件夹和文件。你可以：

- 点击文件直接打开；
- 展开和收起目录；
- 新建、重命名或移动文件；
- 使用 `Ctrl+P` 按文件名查找；
- 使用 `Ctrl+Shift+F` 搜索远程目录中的文字。

文件仍然保存在 Mac mini 上，只是通过 Windows 上的 VS Code 直观显示。不要因为界面看起来像本地文件，就误以为文件已经复制到了 Windows。

> [!tip] 每次先看状态栏
> 编辑前先确认窗口底部显示 `SSH: macmini`。如果没有远程主机名，你可能打开的是 Windows 本地窗口。

#### 10.4 打开真正运行在 Mac mini 上的终端

在远程 VS Code 窗口中选择：

```text
Terminal
→ New Terminal
```

然后执行：

```bash
whoami
hostname
pwd
```

这些命令运行在 Mac mini 上。后面安装 tmux、启动 Claude Code CLI，都要在这个远程终端里操作。

如果终端提示符或 `hostname` 显示的是 Windows，说明你打开的不是远程窗口。

#### 10.5 通过 Ports 面板转发端口

假设 Mac mini 上已经有一个服务监听 `3000` 端口。本文不讨论这个服务如何安装或启动，只处理如何访问它。

在 VS Code 远程窗口中：

1. 打开底部面板；
2. 找到 **Ports（端口）**标签；
3. 点击 **Forward a Port（转发端口）**或 **Add Port**；
4. 输入远程端口，例如 `3000`；
5. VS Code 会显示一个 Windows 本地地址，例如 `127.0.0.1:3000`；
6. 点击地址，或复制到 Windows 浏览器中打开。

默认情况下，VS Code 把转发端口绑定到 Windows 的 `localhost`。这意味着 Windows 自己能访问，但手机通常不能直接访问。

#### 10.6 让手机访问笔记本上的转发端口

你的实际流程需要手机访问“笔记本地址”，因此要明确允许 VS Code 将转发端口绑定到 Windows 的所有网络接口。

**在 Windows 的 VS Code 中操作：**

```text
File
→ Preferences
→ Settings
→ 搜索 remote.localPortHost
→ 选择 allInterfaces
```

也可以在 VS Code 用户设置 JSON 中加入：

```json
{
  "remote.localPortHost": "allInterfaces"
}
```

重新建立端口转发后，手机有两种访问方式。

手机和 Windows 在同一个可信局域网时，可以使用 Windows 的局域网地址，例如：

```text
http://192.168.1.20:3000
```

手机不在同一个局域网时，先让手机和 Windows 都连接 Tailscale，再使用 Windows 的 Tailscale 设备名或 `100.x.x.x` 地址，例如：

```text
http://win-laptop:3000
```

或者：

```text
http://100.x.x.x:3000
```

`192.168.1.20` 和 `100.x.x.x` 都只是示例，必须替换为 Windows 当前的实际地址。本文真实链路中的“笔记本地址”，优先指 Windows 的 Tailscale 设备名或 Tailscale IP，这样手机不必与笔记本处于同一个 Wi-Fi。

Windows 防火墙可能第一次弹出网络访问提示。只允许可信的**专用网络**。如果使用 Tailscale 地址仍无法访问，先检查 Windows 防火墙是否拦截该端口，不要为了省事直接关闭整个防火墙。

> [!warning] allInterfaces 会扩大访问范围
> 启用后，Windows 可达网络中的其他设备也可能访问这个端口。只在手机真机调试期间使用，并优先让手机通过 Tailscale 地址访问。调试完成后可以关闭转发，或把 `remote.localPortHost` 改回 `localhost`。

#### 10.7 断开和重新连接

关闭 VS Code 远程窗口会断开 Remote SSH，临时端口转发也可能随之消失，但这不一定会停止 tmux 中的任务。

重新连接时仍然使用：

```text
Ctrl+Shift+P
→ Remote-SSH: Connect to Host
→ macmini
```

然后重新打开远程目录、检查 Ports 面板，并进入第 12 章创建的 tmux 会话。

> [!info] 官方参考
> - [VS Code：Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)
> - [VS Code：Remote SSH 故障排查](https://code.visualstudio.com/docs/remote/troubleshooting)

### 第 11 章　配置远程桌面，操作图形界面软件

VS Code Remote SSH 能操作文件和终端，却不会显示完整的 Mac 桌面。微信开发者工具、系统设置、权限弹窗等图形界面，需要单独的远程桌面入口。

本文使用你已经跑通的 **ToDesk 或网易 UU 远程**。二选一即可；如果担心某个服务临时不可用，也可以把另一个保留为备用入口。

#### 11.1 分清控制端和被控端

```text
Mac mini：被控端，画面和软件都在这里
Windows：控制端，负责显示并操作 Mac mini 桌面
```

两台电脑都需要安装同一种远程桌面软件。只在 Windows 安装控制端，无法凭空连接没有安装被控端的 Mac mini。

#### 11.2 在 Mac mini 安装被控端

**在 Mac mini 上操作：**

1. 从你选择的软件官网下载 macOS 客户端；
2. 安装并打开；
3. 登录账号，或记录软件显示的设备代码；
4. 打开“允许远程控制”“无人值守”或意思相同的设置；
5. 设置独立的安全密码，不要使用过短或与 Mac 登录密码相同的密码。

ToDesk 和网易 UU 远程的版本更新较快，按钮名称可能略有变化。判断标准不是按钮必须与教程一字不差，而是 Mac mini 在无人操作时仍能接受你授权的 Windows 连接。

#### 11.3 授予 macOS 必需权限

macOS 会限制第三方软件查看屏幕和模拟键盘鼠标。至少检查：

```text
苹果菜单
→ 系统设置
→ 隐私与安全性
→ 屏幕与系统音频录制（或“屏幕录制”）
→ 允许所选远程桌面软件
```

以及：

```text
苹果菜单
→ 系统设置
→ 隐私与安全性
→ 辅助功能
→ 允许所选远程桌面软件
```

- 没有屏幕录制权限：常见现象是黑屏或看不到完整画面；
- 没有辅助功能权限：常见现象是能看到画面，却无法点击或输入。

某些版本还会申请输入监控、麦克风、文件与文件夹或完全磁盘访问。本文只要求正常显示和控制桌面，不要在不理解用途时把所有权限全部打开。

权限变更后，macOS 可能要求退出并重新打开远程桌面软件。

#### 11.4 在 Windows 安装控制端并绑定设备

**在 Windows 上操作：**

1. 安装与 Mac mini 相同的远程桌面软件；
2. 登录同一账号，或输入 Mac mini 的设备代码；
3. 完成设备绑定；
4. 使用无人值守安全密码连接；
5. 确认能看到 Mac mini 桌面，并能点击菜单和输入文字。

如果使用同一账号免输设备代码，也仍然应该开启账号的多因素认证，并给无人值守访问设置独立密码。

#### 11.5 测试真正的无人值守连接

不要在 Mac mini 旁边看着屏幕就宣布成功。完成设置后：

1. 关闭 Mac mini 显示器，但不要让电脑睡眠；
2. 退出 Windows 远程桌面连接；
3. 使用 Windows 重新连接；
4. 打开 Mac mini 上的微信开发者工具；
5. 确认鼠标、键盘和剪贴板能够正常使用。

如果 Mac mini 在没有物理显示器连接时分辨率异常、黑屏或无法显示桌面，先检查远程软件是否支持虚拟显示器。不要在出差以后才第一次测试无显示器模式。

#### 11.6 远程桌面只负责 GUI

日常使用可以按下面的原则分工：

```text
文件、终端、Claude Code CLI、端口转发：VS Code Remote SSH
微信开发者工具、系统设置、权限弹窗：ToDesk 或网易 UU 远程
```

远程桌面需要持续传输画面，网络较差时更容易卡顿。只查看 Claude Code 对话时，Termius SSH 通常比远程桌面更轻。

> [!info] 参考
> - [Apple：控制 App 对 Mac 的辅助功能访问](https://support.apple.com/guide/mac-help/mh43185/mac)
> - [Apple：控制屏幕与系统音频录制权限](https://support.apple.com/guide/mac-help/mchld6aa7d23/mac)
> - [ToDesk：帮助中心](https://www.todesk.com/helpcenter.html)

### 第 12 章　安装 tmux，让任务断线后继续运行

SSH、VS Code 和 Termius 都可能因为网络切换、电脑合盖或 App 进入后台而断开。tmux 的作用，是让终端会话继续留在 Mac mini 上。

#### 12.1 安装 tmux

先在 **VS Code 的 Mac mini 远程终端**中执行：

```bash
tmux -V
```

如果已经显示版本号，跳过安装。

如果提示找不到命令，本文使用 Homebrew 安装。先检查：

```bash
brew --version
```

如果 Homebrew 已安装，执行：

```bash
brew install tmux
tmux -V
```

如果 Homebrew 也不存在，先在 Mac mini 远程终端执行官方安装命令：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装脚本会先说明准备执行的操作并要求确认。完成后，严格照终端最后显示的命令把 Homebrew 加入 PATH，再执行 `brew install tmux`。

Homebrew 当前正式支持 macOS 14 Sonoma 或更高版本，并可能要求 Xcode Command Line Tools。如果安装器要求安装这些组件，按系统提示完成即可。这里安装 Homebrew 只是为了获得 tmux，不展开其他开发环境。

#### 12.2 创建第一个长期会话

在 **VS Code 的 Mac mini 远程终端**中执行：

```bash
tmux new -As remote-work
```

这个命令的含义是：

- 如果 `remote-work` 不存在，就创建；
- 如果已经存在，就重新进入。

进入 tmux 后，终端底部会出现一条状态栏。此时你看到的不是另一个远程连接，而是 Mac mini 上由 tmux 保存的终端会话。

#### 12.3 正确离开，不要关闭会话

先按：

```text
Ctrl+b
```

松开后，再按：

```text
d
```

屏幕会显示类似：

```text
[detached (from session remote-work)]
```

这叫 **detach**：你离开了会话，但会话里的程序仍在 Mac mini 上运行。

不要把 detach 与下面的命令混淆：

```bash
tmux kill-session -t remote-work
```

`kill-session` 会真正关闭整个会话和其中的程序，日常恢复连接时不要执行。

#### 12.4 从 Windows 重新进入

在 VS Code 重新连接 Mac mini 后，打开远程终端，执行：

```bash
tmux ls
```

看到 `remote-work` 后执行：

```bash
tmux attach -t remote-work
```

也可以继续使用更省事的命令：

```bash
tmux new -As remote-work
```

两种方式都会回到原来的终端状态。

#### 12.5 从手机 Termius 进入同一个会话

手机先连接 Tailscale，再打开第 9 章创建的 Termius Host。进入 Mac mini 后执行：

```bash
tmux attach -t remote-work
```

现在 Windows 和手机进入的是 Mac mini 上的同一个 tmux 会话。终端宽度会随设备变化，手机上显示可能更紧凑，这是正常现象。

如果提示会话已经在别处连接，可以使用：

```bash
tmux attach -d -t remote-work
```

它会把另一个客户端从该会话中分离，再让当前设备进入。不要在 Windows 和手机同时输入，以免操作互相干扰。

#### 12.6 给 Claude Code 单独使用一个会话

为了容易识别，可以为 Claude Code 创建单独会话：

```bash
tmux new -As claude
```

以后连接路径就是：

```text
Windows VS Code 或手机 Termius
→ Mac mini SSH
→ tmux 会话 claude
→ Claude Code CLI
```

第 13 章会在这个会话中启动 Claude Code。

#### 12.7 tmux 能防什么，不能防什么

tmux 可以防止：

- Windows 合盖导致 SSH 断开；
- 手机在 Wi-Fi 和蜂窝网络之间切换；
- VS Code 远程窗口关闭；
- Termius 进入后台。

tmux 不能防止：

- Mac mini 关机或重启；
- tmux 会话被手动关闭；
- 运行中的程序自身退出；
- 硬盘或系统故障。

> [!info] 官方参考
> - [tmux：Getting Started](https://github.com/tmux/tmux/wiki/Getting-Started)
> - [Homebrew：安装说明](https://brew.sh/)
> - [Homebrew：tmux Formula](https://formulae.brew.sh/formula/tmux.html)

### 第 13 章　远程使用 Claude Code 与 Codex

这一章只讲两种 AI 工具如何从电脑和手机连接到 Mac mini，不讨论它们如何编程，也不比较谁更适合某类任务。

先记住两条完全不同的路线：

```text
Claude Code：SSH 终端 → tmux → Mac mini 上的 Claude Code CLI

Codex：桌面 App 通过 SSH 连接 Mac mini → 手机 Remote 进入已配对主机
```

#### 13.1 在 Mac mini 安装 Claude Code CLI

在 **VS Code 的 Mac mini 远程终端**中执行官方安装命令：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

安装完成后执行：

```bash
claude --version
```

然后进入你希望 Claude Code 访问的远程目录，再启动：

```bash
cd /你要打开的目录
claude
```

第一次运行时，按终端引导完成登录。目录路径必须替换为 Mac mini 上真实存在的目录，不要原样复制示例中文。

#### 13.2 在 tmux 中启动 Claude Code

更适合远程连接的启动方式是：

```bash
tmux new -As claude
cd /你要打开的目录
claude
```

需要离开时按 `Ctrl+b`，松开后按 `d`。不要使用 `Ctrl+C` 把 Claude Code 结束掉，也不要关闭 tmux 会话。

#### 13.3 从 Windows 继续 Claude Code 对话

在 Windows 上：

```text
VS Code
→ Remote-SSH: Connect to Host
→ macmini
→ Terminal → New Terminal
```

然后执行：

```bash
tmux attach -t claude
```

看到原来的 Claude Code 终端界面，就说明你回到了 Mac mini 上保存的会话。VS Code 只是入口，对话和命令实际仍在 Mac mini 上。

#### 13.4 从手机继续 Claude Code 对话

手机端顺序是：

1. 打开 Tailscale，确认已连接；
2. 打开 Termius；
3. 连接第 9 章保存的 Mac mini Host；
4. 执行：

```bash
tmux attach -t claude
```

手机适合查看 Claude 对话、确认是否需要输入，以及进行少量回复。手机锁屏或 Termius 断开时，tmux 中的 Claude Code CLI 仍留在 Mac mini 上。

> [!note] 本文不用 Claude Remote Control
> Claude Code 也提供基于 Claude App 或网页的 Remote Control，但本文已经使用 Tailscale + Termius + tmux 跑通手机 SSH，因此不再引入另一条连接路径。

#### 13.5 先理解 Codex Remote 的真实结构

本文沿用“Codex 桌面端”和“Codex 手机 App”的说法。按照当前官方界面，它们可能显示在 **ChatGPT 桌面 App**和**ChatGPT 手机 App**中，并通过 **Codex**或 **Remote**入口使用。

电脑端连接 Mac mini 的底层仍然是 SSH：

```text
Windows 上的桌面 App
→ 读取 Windows SSH config 中的 macmini
→ 通过 SSH 启动 Mac mini 上的 Codex app server
→ 使用 Mac mini 的远程文件和终端
```

手机端不是用 SSH 直接连接 Mac mini，而是先与桌面 App 所在主机配对，再进入同一个远程环境：

```text
手机 App 的 Remote
→ 已配对的 Windows 桌面主机
→ Windows 桌面 App 已配置的 macmini SSH 连接
→ Mac mini
```

从使用感受上，你是在手机里打开 Mac mini 上的 Codex 任务；但排错时必须知道中间的桌面主机和 SSH 连接仍然存在。

#### 13.6 在 Mac mini 准备 Codex 命令

Codex 桌面端通过 SSH 连接 Mac mini 时，需要远程登录 shell 能找到 `codex` 命令。

先在 **Windows PowerShell**中确认：

```powershell
ssh macmini "codex --version"
```

如果返回版本号，可以继续下一节。

如果提示找不到 `codex`，按照当前官方 CLI 方式在 **Mac mini 远程终端**安装：

```bash
npm install --global @openai/codex
codex --version
```

如果安装命令提示缺少运行条件，请按照 Codex CLI 当前官方安装页处理。本文不展开相关环境配置，只要求最终在 `ssh macmini` 的登录 shell 中能直接执行 `codex --version`。

然后在 Mac mini 上完成登录：

```bash
codex login
```

远程环境无法正常打开浏览器回调时，可以使用设备码登录：

```bash
codex login --device-auth
```

#### 13.7 在 Windows 桌面 App 添加 Mac mini SSH 连接

先确认 Windows PowerShell 中的 `ssh macmini` 正常，再打开 Codex/ChatGPT 桌面 App：

```text
Settings
→ Connections
→ 添加或启用 SSH host：macmini
→ 选择 Mac mini 上的远程目录
```

桌面 App 会从 Windows 的 `~/.ssh/config` 读取具体的 Host 别名。第 9 章配置的 `macmini` 因此可以被发现。

连接后选择 Mac mini 上的目录。此后 Codex 读取的文件、执行的 shell 命令都来自 Mac mini，而不是 Windows 本地目录。

> [!warning] 不要公开 Codex app server 端口
> 官方远程连接会通过 SSH 启动和管理远程 app server。不要把 app server 的端口直接暴露到局域网或公网；跨网络访问继续使用已经配置好的 SSH/Tailscale 链路。

#### 13.8 配对手机 Remote

手机 Remote 的首次设置从桌面 App 开始：

1. 在桌面 App 侧边栏选择 **Set up Remote**；
2. 桌面 App 显示二维码；
3. 使用手机扫码，打开 ChatGPT/Codex 手机 App；
4. 确认手机与桌面端使用同一个 ChatGPT 账号和 workspace；
5. 完成多因素认证、SSO 或 passkey 提示；
6. 设置成功后，在手机 App 的 **Remote** 中看到已配对主机。

如果要从手机进入 Mac mini 上的远程目录，Windows 桌面 App 必须已经配置好 `macmini` SSH host。手机沿用的正是这台桌面主机的远程环境。

在桌面 App 中可以通过：

```text
Settings
→ Connections
```

查看和管理已连接设备，以及远程控制是否开启。

#### 13.9 Codex Remote 依赖哪些设备在线

手机能否继续 Codex Remote，至少取决于：

- Mac mini 开机、联网且 SSH 可用；
- Mac mini 的 `codex` 命令可用并已认证；
- 作为配对主机的桌面 App 在线，远程控制处于开启状态；
- 手机 App 使用正确账号和 workspace；
- Windows 到 Mac mini 的 SSH/Tailscale 连接仍然可用。

如果桌面主机睡眠、断网或关闭 App，手机远程访问会停止，直到该主机恢复。手机界面能打开，不代表 Mac mini 一定在线。

> [!info] 官方参考
> - [Claude Code：安装与终端指南](https://code.claude.com/docs/en/terminal-guide)
> - [Claude Code：CLI reference](https://code.claude.com/docs/en/cli-reference)
> - [OpenAI：Remote connections](https://learn.chatgpt.com/docs/remote-connections)
> - [OpenAI：Codex CLI](https://developers.openai.com/codex/cli)

### 第 14 章　让其他设备访问 Mac mini 上的 Web 服务

这一章不讲如何开发或启动项目，只解决一个连接问题：Mac mini 上已经运行的 Web 或 API，怎样在 Windows 和手机上打开。

整条链路是：

```text
Mac mini 上的服务端口
→ VS Code Remote SSH 隧道
→ Windows 上的转发端口
→ Windows 浏览器或手机
```

#### 14.1 先确认目标服务和端口

端口可以理解为一扇带编号的门。只有知道服务使用哪一个端口，VS Code 才知道应该转发哪一扇门。

如果启动服务时终端显示了类似地址：

```text
http://localhost:3000
```

其中 `3000` 就是目标端口。不同项目可能使用 `3000`、`5173`、`8080` 或其他数字，不能根据教程猜测。

如果不知道端口，可以在 **VS Code 的 Mac mini 远程终端**中查看正在监听的 TCP 端口：

```bash
lsof -nP -iTCP -sTCP:LISTEN
```

这条命令可能列出多个端口。你仍然需要根据服务启动时的提示，或询问维护这个项目的人，确认哪一个才是要访问的 Web 或 API。

> [!warning] 本文只转发 Web 或测试 API
> 不要因为看到端口就把所有端口都转发。尤其不要把不理解的系统服务或敏感服务开放给其他设备。

#### 14.2 先让 Windows 自己访问成功

在 Windows 上打开已经连接 Mac mini 的 VS Code 远程窗口：

```text
底部面板
→ Ports（端口）
→ Forward a Port（转发端口）
→ 输入目标端口
```

假设远程服务使用 `3000`，VS Code 会显示一个 Windows 本地地址。先在 Windows 浏览器打开这个地址。

如果 Windows 自己都打不开，先检查：

- Mac mini 上的服务是否仍在运行；
- 转发的端口号是否正确；
- VS Code 是否仍显示 `SSH: macmini`；
- Ports 面板里的转发是否仍然存在。

Windows 访问成功后，再处理手机。这样可以把“远程端口没通”和“手机到 Windows 没通”分开排查。

#### 14.3 让转发端口可以从手机访问

第 10 章已经把 VS Code 设置 `remote.localPortHost` 改为：

```json
"allInterfaces"
```

它让 Windows 不只在 `localhost` 接收请求，也允许其他能够到达 Windows 的设备访问这个转发端口。

修改设置后，删除旧的端口转发，再重新添加一次。已经存在的转发不一定会自动改用新监听方式。

#### 14.4 优先使用 Windows 的 Tailscale 地址

手机和 Windows 都打开 Tailscale 后，手机可以使用 Windows 的 Tailscale 设备名：

```text
http://win-laptop:3000
```

如果设备名无法解析，打开 Tailscale 查看 Windows 的 `100.x.x.x` 地址：

```text
http://100.x.x.x:3000
```

这里的 `3000` 要替换成 Ports 面板实际显示的 Windows 本地端口。VS Code 有时会因为端口冲突，将远程 `3000` 映射成另一个本地端口，所以不要只看远程端口一列。

手机与 Windows 在同一个可信 Wi-Fi 时，也可以使用 Windows 的局域网 IP，但出差场景优先使用 Tailscale 地址。这样手机不需要和笔记本处于同一个 Wi-Fi。

#### 14.5 Windows 防火墙弹窗怎么选

Windows 可能在第一次监听端口时询问是否允许网络访问。只允许可信的专用网络，不要为了排错直接关闭整个防火墙。

如果 Windows 浏览器能打开，手机却打不开，依次检查：

1. 手机和 Windows 的 Tailscale 是否都已连接；
2. 手机访问的是 Windows 地址，而不是 Mac mini 地址；
3. URL 里的端口是否为 VS Code 显示的本地端口；
4. `remote.localPortHost` 是否为 `allInterfaces`；
5. Windows 防火墙是否阻止该端口。

#### 14.6 端口转发不是正式发布

VS Code 远程窗口关闭、SSH 断开或 Ports 面板中的转发被删除后，手机入口就会消失。这种方式适合自己临时查看和真机调试，不适合给普通用户长期使用。

调试完成后，关闭不再需要的转发。下次重连时，重新确认本地端口，不要假设它永远不变。

> [!info] 官方参考
> - [VS Code：Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)
> - [Tailscale：MagicDNS](https://tailscale.com/docs/features/magicdns)

### 第 15 章　完成微信小程序远程真机调试

这一章描述的是你已经跑通的真实场景：微信开发者工具运行在 Mac mini 上，Windows 负责远程桌面和端口转发，手机扫描开发者工具生成的二维码，同时通过 Windows 的 Tailscale 地址访问 Mac mini 上的 API。

它不是正式部署，也不是让普通用户打开正式版小程序。

#### 15.1 先看清两条同时发生的链路

二维码与 API 请求是两件不同的事情。

**打开小程序的链路：**

```text
Windows 远程桌面
→ Mac mini 上的微信开发者工具
→ 生成预览或真机调试二维码
→ 手机微信扫码
→ 打开开发版本小程序
```

**小程序访问本地 API 的链路：**

```text
手机中的开发版本小程序
→ Windows 的 Tailscale 地址和转发端口
→ VS Code Remote SSH 隧道
→ Mac mini 上的本地 API
```

二维码只负责把开发版本打开到手机上，不会自动替你建立 API 隧道。端口转发必须提前配置好。

#### 15.2 开始前确认四个入口都在线

开始操作前确认：

- Mac mini 上的目标 API 已经运行，并且端口明确；
- Windows 的 VS Code 已连接 `macmini`，Ports 面板已转发 API 端口；
- Windows 的 ToDesk 或网易 UU 远程能够操作 Mac mini 桌面；
- Mac mini、Windows 和手机的 Tailscale 都处于连接状态。

手机先用浏览器访问一次 Windows 的转发地址。如果浏览器访问不通，小程序也不会因为扫码而自动变通。

#### 15.3 确认小程序使用的是笔记本地址

小程序中的 API 地址需要指向 Windows 的 Tailscale 设备名或 Tailscale IP，例如：

```text
http://win-laptop:8080
```

或者：

```text
http://100.x.x.x:8080
```

这里的地址和端口都只是示例。端口必须与 VS Code Ports 面板中的 Windows 本地端口一致。

本文不讲项目里在哪里修改 API 地址。不同项目可能使用设置页面、环境文件或启动参数。如果当前项目不能切换 API 地址，需要先让项目维护者提供入口；这不是 SSH 或端口转发能够自动解决的问题。

> [!warning] 不要填 `localhost`
> 手机小程序中的 `localhost` 指手机自己，不是 Mac mini，也不是 Windows。填 Mac mini 的本地地址同样无法自动穿过 VS Code 隧道；这里必须使用手机能够到达的 Windows 地址。

#### 15.4 远程操作微信开发者工具

在 Windows 上打开 ToDesk 或网易 UU 远程，进入 Mac mini 桌面，然后：

1. 打开微信开发者工具；
2. 登录拥有该小程序开发权限的微信账号；
3. 打开目标小程序；
4. 等待编译完成；
5. 确认模拟器中没有立即出现连接错误。

开发者工具界面和按钮位置会随版本变化，但常见入口仍然是顶部工具栏中的**预览**或**真机调试**。

#### 15.5 预览与真机调试怎么选

- 只想在手机上看看当前效果：选择**预览**；
- 需要让开发者工具继续显示手机端日志和调试信息：选择**真机调试**。

点击后，Mac mini 上会出现二维码。这个二维码会通过远程桌面画面显示到 Windows，因此手机可以直接扫描 Windows 屏幕上的二维码，不需要人在 Mac mini 旁边。

二维码通常有有效期。如果扫码提示失效，回到远程桌面重新生成，不要继续排查 SSH。

#### 15.6 手机扫码后观察哪两处

手机扫码后同时观察：

1. 手机是否成功打开开发版本小程序；
2. Mac mini 上的 API 终端是否出现来自手机的新请求。

如果小程序打开了，但 API 终端没有任何新请求，优先检查小程序中的 API 地址、Windows 转发端口和防火墙。

如果 API 已收到请求，但小程序仍报错，说明三段网络链路大概率已经成立，问题更可能来自接口返回、权限或小程序本身。本文不进入业务代码排查。

#### 15.7 微信平台限制要单独看待

微信小程序对请求域名、协议、账号权限和调试方式有自己的限制。你已经跑通的本地链路适用于有开发权限的预览或真机调试，不代表正式版小程序和所有体验成员都能访问同一个本地地址。

如果开发者工具或手机提示“合法域名”“HTTPS”“无开发权限”等错误，不要把它误判成 Tailscale 故障。应根据当前微信开放文档和项目设置确认调试权限。

不要为了绕开平台限制，把本地端口直接暴露到公网。

#### 15.8 这条链路断在哪里，现象就是什么

| 断点 | 常见现象 |
|---|---|
| 远程桌面不可用 | 无法操作开发者工具、无法生成二维码 |
| 二维码失效或账号无权限 | 手机无法打开开发版本 |
| VS Code 转发消失 | 手机能打开小程序，但本地 API 请求失败 |
| 手机访问了错误的 Windows 地址 | 浏览器和小程序都访问不到 API |
| Mac mini API 已停止 | 转发仍在，但目标端口拒绝连接 |

> [!info] 官方入口
> - [微信开放文档：小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/)
> - [微信开发者工具下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)

## 第三篇：日常怎么用

### 第 16 章　出差时建立远程连接

整套配置完成后，日常使用不需要每次重新安装。出差时按从底层到上层的顺序连接，可以最快判断哪一层出现问题。

#### 16.1 电脑端最短连接流程

在 Windows 上依次执行：

1. 连接当前可用网络；
2. 打开 Tailscale，确认 `macmini-dev` 在线；
3. 在 PowerShell 执行：

```powershell
ssh macmini
```

4. 确认 SSH 可用后退出；
5. 打开 VS Code，连接 Remote SSH 主机 `macmini`；
6. 打开 Mac mini 上需要使用的远程目录；
7. 打开 VS Code 远程终端；
8. 恢复需要的 tmux 会话。

恢复 Claude Code 会话时执行：

```bash
tmux attach -t claude
```

只有需要微信开发者工具或系统设置时，才打开 ToDesk 或网易 UU 远程桌面。

#### 16.2 使用 Codex 时的连接顺序

Codex 桌面端使用 Mac mini 时，先确认：

```powershell
ssh macmini "codex --version"
```

然后打开桌面 App，在已保存的连接中选择 `macmini` 和对应远程目录。

如果手机也要使用 Remote，桌面主机必须保持在线，Remote Control 也要处于开启状态。

#### 16.3 要预览页面时再恢复端口

VS Code Remote SSH 重连后，打开 Ports 面板检查目标端口。不要只因为昨天使用过，就假设今天的转发仍然存在或本地端口没有变化。

需要手机访问时，再确认 `remote.localPortHost` 为 `allInterfaces`，并使用 Windows 的 Tailscale 地址。

#### 16.4 网络较差时优先保住文字通道

连接质量较差时，优先级建议是：

```text
Tailscale
→ SSH / Termius
→ VS Code Remote SSH
→ Codex Remote
→ 远程桌面
```

远程桌面需要持续传输画面，最容易受到延迟影响。SSH 能正常使用时，不必因为远程桌面卡顿就判断整套远程主机已经失效。

### 第 17 章　网络中断后如何继续任务

网络中断时，先区分两件事：是随身设备与 Mac mini 的**连接断了**，还是 Mac mini 上的**任务真的停了**。

#### 17.1 只有笔记本或手机断网

如果 Claude Code CLI 运行在 tmux 中，客户端断网通常只会中断画面。Mac mini 上的 tmux 会话仍然存在。

网络恢复后按顺序操作：

1. 恢复 Windows 或手机网络；
2. 确认 Tailscale 已重新连接；
3. 重新使用 VS Code Remote SSH 或 Termius 登录 Mac mini；
4. 执行：

```bash
tmux ls
tmux attach -t claude
```

看到原来的对话界面后，再继续输入。

#### 17.2 VS Code 窗口断开

VS Code 提示连接丢失时，可以先点击重连。失败后关闭当前远程窗口，重新执行：

```text
Remote-SSH: Connect to Host
→ macmini
```

重新连接后检查三处：远程目录是否正确、tmux 会话是否还在、Ports 面板是否需要重新转发。

#### 17.3 Termius 在手机后台断开

重新打开 Tailscale，再打开 Termius Host。进入 Mac mini 后执行：

```bash
tmux attach -t claude
```

不要因为 Termius 显示一个新的空终端，就再次启动一份 Claude Code。先执行 `tmux ls` 查找原会话。

#### 17.4 Codex 手机 Remote 断开

Codex Remote 断开时依次检查：

1. 手机网络是否恢复；
2. 手机 App 是否仍登录正确账号和 workspace；
3. 已配对的 Windows 桌面主机是否在线、桌面 App 是否运行；
4. Windows 是否还能 `ssh macmini`；
5. Mac mini 是否在线，远程 `codex` 命令是否可用。

重新登录 ChatGPT 后，Remote Control 可能需要重新打开，但原有设备配对不一定会被删除。

#### 17.5 Mac mini 自己离线

如果 Tailscale Machines 页面显示 `macmini-dev` 离线，Windows 和手机都无法 SSH，问题通常已经不在客户端。

可能原因包括：

- Mac mini 断电或重启后没有正常启动；
- Mac mini 进入睡眠；
- 家庭或办公室网络中断；
- Tailscale 退出或需要重新认证；
- FileVault 或系统登录阻挡了服务启动。

这类问题无法靠反复刷新 VS Code 修复。尝试备用远程桌面；如果所有入口都失效，就需要现场人员检查电源、网络和登录状态。

### 第 18 章　如何在电脑之间切换而不搬运行环境

使用新电脑时，目标不是把 Mac mini 的全部内容复制一份，而是给新电脑增加一把独立的“门钥匙”。

#### 18.1 新电脑只安装连接工具

新电脑需要准备：

- Tailscale；
- Windows OpenSSH Client；
- VS Code 与 Remote - SSH；
- 你选择的远程桌面控制端；
- 需要时安装 Codex/ChatGPT 桌面 App。

文件、Claude Code CLI、tmux 会话和运行中的服务仍然留在 Mac mini。

#### 18.2 每台电脑生成自己的 SSH 密钥

不要把旧电脑的 SSH 私钥通过网盘或聊天软件复制给新电脑。

在**新电脑的 PowerShell**中生成新的专用密钥，例如：

```powershell
ssh-keygen -t ed25519 -f $HOME\.ssh\id_ed25519_macmini -C "new-windows-to-macmini"
```

把新电脑的公钥加入 Mac mini 的 `~/.ssh/authorized_keys`，再为新电脑创建自己的 SSH config。

这样旧电脑丢失或停用时，只需从 Mac mini 删除对应的那一行公钥，不会影响其他设备。

#### 18.3 可以迁移什么，不应该迁移什么

可以安全迁移或重新创建：

- SSH config 中不含秘密的主机名称和用户名；
- VS Code 的普通界面设置；
- 远程桌面设备绑定；
- 重新创建 Codex Remote 的设备配对。

不要随意复制：

- SSH 私钥；
- Termius 中的私钥；
- Mac 登录密码；
- Tailscale 或 AI 工具的认证文件；
- Mac mini 上整套运行目录。

#### 18.4 更换电脑后，会话为什么还在

新电脑连接的仍然是同一台 Mac mini，所以执行：

```bash
tmux ls
tmux attach -t claude
```

看到的是原来的 tmux 会话。连续性来自固定主机，而不是来自把会话同步到了新电脑。

#### 18.5 旧电脑丢失时立即撤销入口

如果旧电脑丢失：

1. 在 Tailscale Machines 页面移除或禁用旧设备；
2. 在 Mac mini 的 `~/.ssh/authorized_keys` 删除旧电脑公钥；
3. 在远程桌面账号中移除旧设备并修改无人值守密码；
4. 在 Codex/ChatGPT 桌面 App 的 Connections 中撤销对应配对；
5. 检查相关账号登录记录并修改必要密码。

不要只修改 Windows 开机密码。远程入口需要逐层撤销。

### 第 19 章　在手机上继续 Claude Code 与 Codex 会话

手机上有两个入口，分别对应两套不同的连接方式：

```text
Claude Code：Tailscale + Termius + SSH + tmux
Codex：手机 App 的 Remote + 已配对的桌面主机
```

#### 19.1 用 Termius 查看 Claude Code

依次操作：

1. 打开手机 Tailscale；
2. 确认 `macmini-dev` 在线；
3. 打开 Termius；
4. 连接 Mac mini Host；
5. 执行：

```bash
tmux attach -t claude
```

进入后可以查看最近的 Claude 对话、确认任务是否等待输入，并进行少量回复。

#### 19.2 手机键盘操作的注意事项

tmux 快捷键需要先输入 `Ctrl+b`。手机软键盘不方便时，可以使用 Termius 的特殊按键栏。

如果只想退出但保留会话，仍然使用：

```text
Ctrl+b
然后按 d
```

不要用 `exit` 或 `tmux kill-session` 代替 detach，也不要因为手机显示拥挤就重新创建同名任务。

#### 19.3 用手机 Remote 继续 Codex

第一次已经完成配对后：

1. 打开 Codex/ChatGPT 手机 App；
2. 进入 **Remote**；
3. 选择已配对的桌面主机；
4. 选择桌面 App 已配置好的 Mac mini 远程项目或任务；
5. 查看输出、发送后续消息或处理需要确认的操作。

如果列表中没有主机，回到第 13 章检查桌面 App 的 **Set up Remote** 和 **Settings → Connections**。

#### 19.4 为什么两条路径不能混用

Termius 显示的是 Mac mini 的普通 SSH 终端，因此它能进入 tmux 中的 Claude Code CLI。

手机 App 的 Remote 显示的是 Codex 远程任务，由已配对的桌面主机及其 SSH 连接提供环境。它不会列出 tmux 中的 Claude Code 会话。

所以：

- Termius 里找不到 Codex Remote 任务是正常的；
- Codex Remote 里看不到 Claude Code 的 tmux 界面也是正常的。

#### 19.5 手机适合做什么

手机适合：

- 查看长任务是否完成；
- 回答一个等待确认的问题；
- 补充少量说明；
- 在电脑暂时没电时保持连接连续性。

复杂的文件浏览、大量文字输入和图形界面操作仍然更适合 Windows。手机是随身入口，不是必须取代电脑。

### 第 20 章　如何远程查看 Web 和小程序

这一章把前面的操作压缩成几张场景卡。遇到具体需求时，直接选择对应路线，不要把所有工具全部打开。

#### 20.1 在 Windows 浏览器查看 Web

```text
Windows Tailscale
→ VS Code Remote SSH 连接 macmini
→ Ports 面板转发目标端口
→ Windows 浏览器打开 VS Code 提供的本地地址
```

这一场景不需要远程桌面，也不需要手机 Termius。

#### 20.2 在手机浏览器查看 Web

```text
手机和 Windows 都连接 Tailscale
→ VS Code 转发端口绑定 allInterfaces
→ 手机打开 http://win-laptop:端口
```

先在 Windows 浏览器确认转发可用，再从手机访问。

#### 20.3 在手机查看微信小程序

```text
Windows 远程桌面进入 Mac mini
→ 微信开发者工具生成预览二维码
→ 手机微信扫码打开开发版本

同时：
手机小程序
→ Windows Tailscale 地址和端口
→ VS Code Remote SSH 隧道
→ Mac mini API
```

这个场景需要远程桌面、VS Code 端口转发和手机扫码三部分同时成立。

#### 20.4 在手机查看 Claude Code

```text
手机 Tailscale
→ Termius SSH
→ Mac mini
→ tmux attach -t claude
```

这一场景不需要 VS Code 保持打开，也不需要远程桌面。

#### 20.5 在手机查看 Codex

```text
手机 App 的 Remote
→ 已配对的桌面主机
→ 桌面 App 的 macmini SSH 连接
→ Mac mini 远程环境
```

这一场景依赖桌面主机和桌面 App 在线，不能用 Termius 替代。

#### 20.6 最容易混淆的三个地址

| 地址 | 代表什么 | 手机能否直接使用 |
|---|---|---|
| `localhost:端口` | 当前这台设备自己 | 在手机里只代表手机，不代表电脑 |
| `macmini-dev` | Mac mini 的 Tailscale 设备名 | 可用于 SSH，但不能代替 VS Code 转发后的 Windows 端口 |
| `win-laptop:端口` | Windows 的 Tailscale 设备名和转发端口 | 本文手机访问 Web/API 的推荐入口 |

当手机无法访问时，先确认地址指向谁，再检查工具。很多“网络故障”其实只是把 `localhost` 写在了错误的设备上。

## 第四篇：安全、恢复与故障排查

### 第 21 章　远程连接必须守住的安全边界

远程主机的方便，来自“只要通过认证，就能从外面进入”。安全问题也来自同一个入口。

本章不讨论企业级权限体系，只给个人使用场景设置一条最低安全线：不把入口公开到互联网、每台设备使用独立凭据、账号开启额外验证、设备丢失后能够单独撤销。

#### 21.1 不要在路由器上公开 SSH 端口

本文使用 Tailscale，让自己的设备先进入同一个加密私网，再通过 SSH 连接 Mac mini。因此，通常不需要在家里或办公室的路由器上配置：

```text
端口映射
端口转发
公网开放 22 端口
DMZ 主机
```

这些设置会让陌生的互联网设备也能找到登录入口，风险和维护成本都会明显增加。

同样不要公开：

- Codex app server 的端口；
- VS Code Remote SSH 内部使用的端口；
- 远程桌面软件自行监听的未知端口；
- 为了临时调试而转发出来的 Web 或 API 端口。

> [!warning] Tailscale 在线不等于可以关闭其他保护
> Tailscale 解决的是“哪些设备能够在网络上找到彼此”，SSH 密钥、Mac 账号、远程桌面密码和 AI 工具账号仍然需要分别保护。

#### 21.2 每台客户端使用自己的 SSH 密钥

Windows 和手机应分别生成 SSH 密钥，不要共用同一个私钥：

```text
Windows 私钥：只留在 Windows
手机私钥：只留在 Termius
Mac mini：只保存两台设备各自的公钥
```

这样某台设备丢失时，只需要从 Mac mini 的 `~/.ssh/authorized_keys` 删除对应公钥，不会影响其他设备。

保护 SSH 密钥时遵守四条原则：

1. 私钥不通过微信、邮件、网盘或普通笔记发送；
2. 能接受每次输入口令时，为私钥设置 passphrase；
3. 公钥注释写清设备来源，例如 `windows-to-macmini`；
4. 不再使用的设备及时删除公钥，不把旧钥匙一直留在门上。

在 Mac mini 的：

```text
系统设置
→ 通用
→ 共享
→ 远程登录
→ 允许访问
```

优先选择**仅这些用户**，只加入真正需要远程登录的账号。不要为了省一步而允许所有本机用户远程登录，也不要随意打开“允许远程用户完全磁盘访问”。

本文不要求初学者直接修改 `sshd_config` 或关闭密码登录。配置错误可能把自己锁在门外。先依靠 Tailscale、限定用户和独立 SSH 密钥建立基础保护，再考虑更复杂的加固。

#### 21.3 保护 Tailscale 和远程控制账号

Tailscale 使用登录时所选的身份提供商，例如 Google、Microsoft 或 Apple。应该在这个账号上开启多因素认证或 passkey，因为它也是进入 tailnet 的身份入口。

定期打开 Tailscale 管理后台的 **Machines** 页面，移除不再使用或不认识的设备。对随身携带的 Windows 和手机保留 key expiry；如果按第 8 章只对固定的 Mac mini 关闭了过期，也要定期确认它仍然属于自己并保持更新。

远程桌面的无人值守访问需要额外注意：

- 使用独立且足够长的无人值守密码；
- 不与 Mac 登录密码、Tailscale 登录账号或其他网站共用；
- 开启远程桌面账号支持的多因素认证；
- 不使用时关闭文件传输、剪贴板同步等非必要能力；
- 旧设备丢失或出售后，从设备列表移除并更换无人值守密码。

手机和 Windows 本身也要设置锁屏密码，并启用系统支持的生物识别。Termius 中保存着手机专用 SSH 私钥，设备锁屏就是第一道保护。

#### 21.4 保护 AI 工具的远程入口

Claude Code CLI 通过普通 SSH 终端访问，安全边界主要来自 Tailscale、SSH 密钥和 Mac 用户权限。

Codex 手机 Remote 还依赖 ChatGPT 账号和设备配对：

```text
桌面 App
→ Settings
→ Connections
→ Devices that can control this computer
```

定期查看能够控制桌面主机的设备，移除不再使用的手机。退出账号后，Remote Control 可能会关闭；重新登录时不要因为急着恢复连接，就忽略账号异常或陌生设备。

无论使用哪一种工具，都不要在对话中粘贴：

- SSH 私钥；
- FileVault 恢复密钥；
- Time Machine 加密密码；
- Tailscale auth key；
- 远程桌面无人值守密码；
- 账号恢复码或长期有效的访问令牌。

VS Code、终端和远程 AI 工具能看到的文件范围都来自当前 Mac 用户权限。日常打开具体工作目录，不要为了方便长期把整个个人主目录当成唯一入口。

#### 21.5 端口只在需要时转发

VS Code 的 `allInterfaces` 让手机能够访问 Windows 转发端口，也意味着 Windows 正在接受来自其他网络接口的请求。

因此：

1. 只转发当前需要查看的 Web 或 API 端口；
2. Windows 防火墙只允许可信网络；
3. 调试结束后，在 Ports 面板停止转发；
4. 不把这条临时链路当成正式发布地址；
5. 不在公共场所把地址和端口发给无关人员。

#### 21.6 客户端设备丢失后的处理顺序

如果 Windows 或手机丢失，不要只修改设备的开机密码。应使用仍然可信的设备按下面顺序撤销入口：

1. 使用系统提供的查找、锁定或抹除功能处理丢失设备；
2. 在 Tailscale **Machines** 中移除丢失设备；
3. 从 Mac mini 的 `~/.ssh/authorized_keys` 删除该设备的公钥；
4. 在远程桌面账号中移除设备，并更换无人值守密码；
5. 在桌面 App 的 **Settings → Connections** 中撤销对应配对；
6. 注销 Termius、ChatGPT 和相关身份提供商的异常登录会话；
7. 如果任何私钥、密码或恢复码可能已经泄露，立即重新生成或更换。

每台客户端都使用独立密钥，正是为了让第 3 步可以精准撤销，而不需要把所有设备全部重新配置。

> [!info] 官方参考
> - [Apple：允许远程电脑访问 Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)
> - [Tailscale：保护 tailnet 的最佳实践](https://tailscale.com/docs/reference/best-practices/security)
> - [OpenAI：Remote connections](https://learn.chatgpt.com/docs/remote-connections)

### 第 22 章　连接配置与整机恢复准备

备份的目标不是保存一堆安装包，而是让设备故障后能够回答三个问题：要连接哪台 Mac、使用哪个账号、如何重新建立每一层入口。

#### 22.1 建立一份不含密码的连接记录

在密码管理器的安全备注或离线文档中记录以下信息：

| 项目 | 示例 | 是否属于秘密 |
|---|---|---|
| Mac mini 的 Tailscale 设备名 | `macmini-dev` | 否 |
| Windows 的 Tailscale 设备名 | `win-laptop` | 否 |
| Mac mini 用户名 | `yourname` | 否，但不必公开 |
| Windows SSH Host 别名 | `macmini` | 否 |
| SSH 公钥注释 | `windows-to-macmini` | 否 |
| 手机 Termius Host 名称 | `macmini-dev` | 否 |
| 远程桌面产品和设备名称 | `Mac mini 工作主机` | 否，但不必公开 |
| Codex 配对主机 | `Windows 桌面主机` | 否 |

这份记录只描述连接关系，不要把私钥、密码、恢复密钥和验证码写在普通文档中。

#### 22.2 备份 Windows SSH config

Windows SSH config 一般位于：

```text
C:\Users\你的用户名\.ssh\config
```

它通常只包含主机别名、设备名、用户名和私钥文件路径，可以保存到加密的个人备份中。恢复到新电脑时，先检查里面的 Windows 用户目录是否已经变化。

公钥文件也可以备份，例如：

```text
id_ed25519_macmini.pub
```

私钥文件：

```text
id_ed25519_macmini
```

不建议放入普通云盘。个人场景下，旧私钥丢失后在新设备生成新密钥、再把新公钥加入 Mac mini，通常比四处复制私钥更安全。

#### 22.3 记录 Termius 主机配置

记录 Termius Host 的非敏感字段：

```text
Label：macmini-dev
Address：macmini-dev
Port：22
Username：yourname
Key：macmini-phone
```

不要在截图中保留密码、私钥正文、指纹解锁界面或账号恢复信息。

如果换手机，推荐在新手机生成新的 SSH 密钥，再把新公钥加入 Mac mini。这样可以同时从 `authorized_keys` 删除旧手机公钥，不需要把旧私钥迁移到新设备。

#### 22.4 使用 Time Machine 保存 Mac mini 数据

Time Machine 可以自动备份 Mac 上的个人文件、应用和账号数据。它不是“永远不会出错”的保证，也不是把正在运行的 tmux 会话冻结下来，但能显著降低磁盘故障、误删文件或更换 Mac 时的恢复成本。

在 Mac mini 上打开：

```text
系统设置
→ 通用
→ 时间机器
→ 添加备份磁盘
```

推荐：

- 使用独立的外置磁盘或可信网络备份位置；
- 为备份开启加密；
- 把加密密码保存到 Mac mini 之外；
- 完成第一次备份后确认“上次备份”时间；
- 不要只依赖 Mac 内部磁盘上的本地快照。

需要恢复整套用户文件和应用时，可以在新装好的 Mac 上使用**迁移助理**读取 Time Machine 备份。不要把 Time Machine 理解成完全不需要重新安装 macOS 的磁盘克隆。

#### 22.5 保存 FileVault 和账号恢复信息

需要单独保存的恢复信息包括：

- FileVault 恢复密钥，或确认用于恢复的 Apple 账号可登录；
- Time Machine 加密密码；
- Tailscale 所用身份提供商的恢复方式；
- 远程桌面账号恢复方式；
- ChatGPT/OpenAI 账号的多因素认证恢复码；
- 密码管理器自己的恢复信息。

这些内容应放在受保护的密码管理器或离线安全位置，不能只保存在 Mac mini 自己里面。否则 Mac 无法启动时，恢复资料也会一起拿不到。

> [!warning] FileVault 会改变断电后的恢复条件
> FileVault 能保护磁盘数据，但 Mac mini 重启后可能需要先完成解锁，Tailscale、SSH 和远程桌面才会恢复。按照第 7 章在本地实测重启后的连接路径，并准备现场协助或可靠的电源保护，不要到出差后才第一次验证。

#### 22.6 定期做一次小型恢复测试

“看到备份成功”不等于“肯定能够恢复”。每隔一段时间做一次低风险测试：

1. 在 Mac mini 建立一个没有敏感内容的测试文件；
2. 等待 Time Machine 完成备份；
3. 删除或修改测试文件；
4. 从 Time Machine 恢复它；
5. 确认恢复后的内容正确；
6. 检查连接记录中的设备名和账号是否仍然有效。

不需要为了测试而抹掉 Mac。能找回一个测试文件、能找到恢复密钥、能说明重启后如何重新上线，已经比“从未验证过的整机备份”可靠得多。

#### 22.7 真正故障时按什么顺序恢复

如果需要更换或重装 Mac mini，建议顺序是：

```text
安装或恢复 macOS
→ 使用迁移助理恢复 Time Machine 数据
→ 完成 FileVault 解锁和本机登录
→ 恢复网络与 Tailscale
→ 开启 Remote Login
→ 检查 authorized_keys
→ 从 Windows 测试 ssh macmini
→ 恢复 VS Code、tmux、远程桌面和 AI 工具入口
```

不要一开始就排查微信二维码或端口转发。底层 SSH 尚未恢复时，上层入口不可能正常。

> [!info] 官方参考
> - [Apple：使用 Time Machine 备份文件](https://support.apple.com/guide/mac-help/back-up-files-mh35860/mac)
> - [Apple：从备份恢复 Mac](https://support.apple.com/en-us/102551)
> - [Apple：使用 FileVault 保护 Mac 数据](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac)

### 第 23 章　常见故障排查

远程连接由很多层组成。最有效的排查方式不是把所有软件都重装一遍，而是从最底层开始，找到第一处失败的位置。

固定顺序如下：

```text
电源与网络
→ Tailscale
→ SSH
→ VS Code 或 Termius
→ tmux
→ Codex Remote
→ 目标端口
→ VS Code 端口转发
→ 手机地址
→ 微信预览
```

#### 23.1 第一步：Mac mini 是否真的在线

先看三个现象：

1. Tailscale 管理后台中的 `macmini-dev` 是否在线；
2. ToDesk 或网易 UU 是否还能看到设备；
3. Windows 和手机是否同时无法连接。

如果 Tailscale 和远程桌面都离线，而且所有客户端同时失败，优先怀疑：

- Mac mini 断电；
- 固定地点网络中断；
- 系统重启后停在 FileVault 或登录界面；
- Mac 进入睡眠；
- Tailscale 没有启动或需要重新认证。

这时反复重装 VS Code 没有意义。需要通过备用远程桌面、智能电源的状态或现场人员确认 Mac mini。

#### 23.2 第二步：Tailscale 是否能够到达 Mac mini

在 **Windows PowerShell**中执行：

```powershell
tailscale status
tailscale ping macmini-dev
```

如果 `macmini-dev` 不在列表或显示离线：

- 确认 Windows 登录了正确的 Tailscale 账号和 tailnet；
- 查看 Machines 页面是否移除了 Mac mini；
- 检查 Mac mini 的 key expiry 是否已经到期；
- 检查 Windows 自己是否已经退出 Tailscale；
- 网络恢复后等待片刻，再重新测试。

不要先用公网 IP 尝试绕过 Tailscale，也不要临时在路由器上公开 22 端口。

#### 23.3 第三步：SSH 是否能独立连接

在 **Windows PowerShell**中先执行最简单的测试：

```powershell
ssh macmini
```

需要查看更多连接过程时执行：

```powershell
ssh -v macmini
```

常见提示可以这样理解：

| 提示 | 常见原因 | 先检查什么 |
|---|---|---|
| `Connection timed out` | 找不到主机或网络不通 | Tailscale 在线状态和 SSH config 的 HostName |
| `Connection refused` | 找到了主机，但 SSH 服务没有接收连接 | Mac 的 Remote Login 是否开启 |
| `Permission denied (publickey)` | 公钥不匹配或使用了错误账号 | User、IdentityFile 和 `authorized_keys` |
| `Could not resolve hostname` | 设备名无法解析 | MagicDNS、拼写或改用 Tailscale IP 测试 |
| Host key changed 警告 | 主机密钥与以前不同 | 先确认 Mac 是否重装或更换，不要直接忽略 |

如果出现主机密钥变化警告，先通过现场信息、Tailscale Machines 和设备身份确认自己连接的仍是那台 Mac。只有明确知道 Mac 重装或主机密钥已经改变时，才更新本地记录。

#### 23.4 第四步：VS Code Remote SSH 是否正常

PowerShell 的 `ssh macmini` 成功后，再处理 VS Code：

1. 确认当前窗口左下角显示 `SSH: macmini`；
2. 重新执行 **Remote-SSH: Connect to Host**；
3. 连接成功后重新打开 Mac mini 上的目标目录；
4. 在左侧资源管理器点击文件，确认看到的是远程目录；
5. 打开 VS Code 的 Remote - SSH 日志查看具体失败位置。

如果 PowerShell 也失败，问题不是 VS Code 扩展造成的，应回到第 23.2 和 23.3 节。

#### 23.5 第五步：手机 Termius 与 tmux 会话是否正确

Termius 无法连接时检查：

- 手机 Tailscale 是否已连接；
- Host 的 Address 是否为 `macmini-dev` 或正确的 Tailscale IP；
- Username 是否与 Mac 用户名一致；
- 是否选中了手机自己的 `macmini-phone` 密钥；
- Mac mini 的 `authorized_keys` 中是否仍有对应公钥。

SSH 登录成功后，在 **Mac mini 终端**执行：

```bash
tmux ls
```

如果看到 `claude`，执行：

```bash
tmux attach -t claude
```

如果提示没有 tmux server 或找不到会话，说明该会话不存在。可能是 Mac 重启、会话被主动结束，或者之前启动 Claude Code 时没有进入 tmux。tmux 能抵抗客户端断线，不能抵抗关机和被主动终止。

#### 23.6 第六步：Codex 桌面端和手机 Remote

先在 **Windows PowerShell**确认两件事：

```powershell
ssh macmini
ssh macmini "codex --version"
```

第一条成功、第二条失败，通常说明远程登录 shell 找不到 `codex`，或远程 Codex 尚未准备好。回到第 13.6 节检查。

桌面 App 再检查：

```text
Settings
→ Connections
→ SSH
→ macmini
```

确认主机仍然启用，远程项目目录仍然存在。

手机 Remote 无法进入时继续检查：

- 手机和桌面 App 是否登录同一个 ChatGPT 账号和 workspace；
- Windows 桌面主机是否开机、联网且桌面 App 正在运行；
- Remote Control 是否因退出账号而关闭；
- 手机是否仍在已配对设备列表；
- Windows 到 Mac mini 的 SSH 是否仍然正常。

手机 App 不是直接绕过 Windows 登录 Mac mini。已配对的桌面主机离线时，这条 Remote 路径会中断。

#### 23.7 第七步：目标服务和 VS Code 端口转发

先在 **VS Code 的 Mac mini 远程终端**确认目标端口仍在监听：

```bash
lsof -nP -iTCP -sTCP:LISTEN
```

然后在 Windows 的 VS Code **Ports** 面板确认：

- 远程端口是否正确；
- 转发是否仍然存在；
- Windows 本地端口实际是多少；
- `remote.localPortHost` 是否仍为 `allInterfaces`。

按下面顺序测试：

```text
Mac mini 上的服务
→ Windows 浏览器打开本地转发地址
→ 手机浏览器打开 Windows Tailscale 地址
```

Windows 浏览器打不开时，不要先排查手机。Windows 能打开、手机不能打开时，再检查 Tailscale、Windows 防火墙、Windows 地址和本地端口。

#### 23.8 第八步：手机是否访问了正确地址

手机访问 API 时，最常见错误仍然是地址指向了错误设备：

```text
错误：http://localhost:8080
正确示例：http://win-laptop:8080
```

同时确认 `8080` 是 VS Code 显示的 Windows **本地端口**，不一定与 Mac mini 的远程端口相同。

如果设备名无法解析，暂时改用 Windows 的 Tailscale `100.x.x.x` 地址测试。IP 能访问而设备名不能访问时，再检查 MagicDNS，而不是修改项目代码。

#### 23.9 第九步：微信预览是否只是上层失败

开始扫码前，先用手机浏览器打开一次 Windows 转发地址。浏览器都无法访问时，微信小程序也不会自动打通网络。

浏览器成功后再检查：

1. Mac mini 上的微信开发者工具是否登录正确账号；
2. 当前项目是否编译成功；
3. 预览或真机调试二维码是否仍在有效期；
4. 手机微信账号是否有开发或体验权限；
5. 小程序中的 API 地址是否指向 Windows；
6. 报错是否来自微信的请求域名、HTTPS 或权限限制。

小程序能打开、API 终端没有任何请求，通常是地址或端口问题。API 已收到请求但页面仍报错，网络链路大概率已经打通，应交给项目本身继续排查，本文到此为止。

#### 23.10 用“第一处失败”确定问题归属

| 第一处失败 | 问题大致位于 |
|---|---|
| Tailscale 看不到 Mac mini | 电源、固定网络、Tailscale 登录或密钥 |
| Tailscale 可达但 SSH 失败 | Remote Login、账号或 SSH 密钥 |
| SSH 成功但 VS Code 失败 | Remote - SSH 配置或远程窗口 |
| SSH 成功但 tmux 会话不存在 | Mac 重启、会话被关闭或之前未使用 tmux |
| 桌面 SSH 成功但手机 Codex Remote 失败 | 桌面主机、设备配对或 Remote Control |
| Windows Web 成功但手机 Web 失败 | `allInterfaces`、Windows 防火墙或手机地址 |
| 手机 Web 成功但小程序失败 | 小程序 API 配置、二维码、微信权限或平台限制 |

一次只修复第一处失败。底层恢复后，再向上测试下一层。

### 第 24 章　其他设备的替代接入方式

这套方案的核心不是某个品牌的软件，而是保留五类能力：私网、SSH、远程文件、图形界面和移动入口。设备变化时，只需要找到对应入口，不必重做整个架构。

#### 24.1 Windows 客户端换成另一台 Mac

整体关系不变：

```text
客户端 Mac 的 Tailscale
→ 客户端 Mac 的 SSH
→ VS Code Remote SSH
→ 远程 Mac mini
```

macOS 自带 `ssh`，SSH config 仍然位于：

```text
~/.ssh/config
```

在新客户端 Mac 上生成自己的 SSH 密钥，不要从 Windows 复制私钥。VS Code 打开远程文件、转发端口和识别远程窗口的方式基本相同。

远程桌面控制端改为该产品的 macOS 客户端即可。具体按钮可能不同，但 Mac mini 仍然是被控端。

#### 24.2 手机从 iPhone 换成 Android，或反过来

基本链路不变：

```text
Tailscale
→ Termius SSH
→ Mac mini
→ tmux
```

以及：

```text
手机 App Remote
→ 已配对的桌面主机
→ Mac mini 远程环境
```

系统之间主要差别是后台保活、通知、剪贴板和生物识别权限。换手机时生成新的 SSH 密钥，确认新手机能够连接后，从 Mac mini 删除旧手机公钥，并从 Tailscale 和 Codex 配对列表移除旧设备。

#### 24.3 不需要图形界面时可以省略远程桌面

如果从不需要操作微信开发者工具、系统设置或其他 GUI 软件，可以不安装 ToDesk 或网易 UU。

保留：

- Tailscale；
- SSH；
- VS Code Remote SSH；
- Termius 和 tmux；
- 实际使用的 AI 工具连接。

省略远程桌面不会影响普通 SSH 和远程文件访问，但 Mac mini 出现系统弹窗、权限确认或登录界面时，会少一条备用恢复路径。

#### 24.4 不需要手机 SSH 时可以省略 Termius

如果手机只用于微信扫码、查看 Web 或进入 Codex Remote，可以不安装 Termius。

代价是：电脑不在身边时，无法通过普通 SSH 查看 Mac mini，也不能进入 tmux 中的 Claude Code CLI 会话。

#### 24.5 只使用一个 AI 工具时可以删掉另一条连接

只使用 Claude Code 时，保留：

```text
VS Code Remote SSH
→ Mac mini 终端
→ tmux
→ Claude Code CLI
```

手机需要时再增加 Termius。

只使用 Codex 时，保留桌面 App 到 Mac mini 的 SSH Connection；手机需要时再配置 Remote 和桌面主机配对。

这里只删除不用的连接入口，不讨论工具之间的功能比较。

#### 24.6 当前方案仍然依赖 Windows 的两个场景

本教程解决了“主要文件和任务不再绑在随身电脑上”，但并不表示 Windows 可以在所有场景中离线。

当前两条链路仍然经过 Windows：

```text
手机访问 Web/API
→ Windows 的 VS Code 转发端口
→ Mac mini
```

```text
手机 Codex Remote
→ 已配对的 Windows 桌面主机
→ Windows 桌面 App 的 Mac mini SSH 连接
```

因此 Windows 断电时：

- Mac mini 上已经运行的普通任务仍可继续；
- 手机仍可通过 Tailscale + Termius + SSH 进入 Mac mini；
- Windows 提供的 Web/API 转发会消失；
- 以 Windows 为配对主机的 Codex Remote 会停止。

> [!important] 这是当前架构的真实边界
> 如果你的目标升级为“Windows 完全关机时，手机仍能访问 Web/API 和 Codex Remote”，就需要把这些入口迁到持续在线的主机上，或设计新的安全代理方案。这已经属于另一套架构，不在本通用连接教程中展开。

#### 24.7 选择替代方式时只问五个问题

面对新设备或新工具时，不用重新比较所有产品，只要确认：

1. 它如何加入同一个可信私网？
2. 它如何使用独立凭据连接 SSH？
3. 它能否直观浏览 Mac mini 的远程文件？
4. 它是否需要操作 Mac 图形界面？
5. 手机入口是否依赖另一台必须在线的桌面主机？

回答清楚这五个问题，就能判断它应该替代 Tailscale、SSH、VS Code、远程桌面、Termius，还是 Codex Remote 中的哪一层。

## 附录 A　最短搭建清单

这份清单用于第一次搭建或更换设备时快速回顾。具体解释和注意事项仍以对应章节为准。

### A.1 固定主机

- [ ] Mac mini 使用稳定电源和网络（第 6–7 章）
- [ ] 设置清楚的设备名，例如 `macmini-dev`（第 6–7 章）
- [ ] 防止自动睡眠，并了解重启后的登录条件（第 7 章）
- [ ] 开启 Remote Login，只允许必要用户（第 7、21 章）
- [ ] 不在路由器上公开 22 端口（第 7、21 章）

### A.2 私网与 SSH

- [ ] Mac mini、Windows 和手机加入同一个 Tailscale tailnet（第 8 章）
- [ ] Machines 页面能看到三台设备（第 8 章）
- [ ] Windows 为 Mac mini 生成独立 SSH 密钥（第 9 章）
- [ ] Windows 的 `ssh macmini` 能成功登录（第 9 章）
- [ ] 手机 Termius 使用自己的 SSH 密钥（第 9 章）
- [ ] Windows 和手机不共用私钥（第 9、21 章）

### A.3 日常连接入口

- [ ] VS Code Remote SSH 能连接并在资源管理器打开远程文件（第 10 章）
- [ ] ToDesk 或网易 UU 能无人值守进入 Mac mini 桌面（第 11 章）
- [ ] tmux 能创建、detach 和重新 attach 会话（第 12 章）
- [ ] Windows 能进入 Claude Code CLI 所在的 tmux 会话（第 13 章）
- [ ] 手机 Termius 能进入同一个 tmux 会话（第 13、19 章）
- [ ] 桌面 App 能通过 SSH Connection 打开 Mac mini 远程项目（第 13 章）
- [ ] 手机 App 已与桌面主机配对并能进入 Remote（第 13、19 章）

### A.4 Web 与小程序

- [ ] 已确认目标服务实际监听端口（第 14 章）
- [ ] VS Code Ports 面板能让 Windows 浏览器访问服务（第 14 章）
- [ ] `remote.localPortHost` 已按需设为 `allInterfaces`（第 10、14 章）
- [ ] 手机能通过 Windows 的 Tailscale 地址访问转发端口（第 14 章）
- [ ] 远程桌面能操作 Mac mini 上的微信开发者工具（第 15 章）
- [ ] 手机扫码后，小程序使用的是 Windows 地址而不是 `localhost`（第 15 章）

### A.5 安全与恢复

- [ ] Tailscale 身份提供商、远程桌面和 ChatGPT 账号已开启额外验证（第 21 章）
- [ ] 能按设备识别并撤销 SSH 公钥（第 21 章）
- [ ] 已保存不含密码的连接记录（第 22 章）
- [ ] Time Machine 已完成第一次备份（第 22 章）
- [ ] FileVault 恢复密钥和备份密码保存在 Mac mini 之外（第 22 章）
- [ ] 已测试恢复一个无敏感内容的文件（第 22 章）

## 附录 B　常用命令速查表

### B.1 Windows PowerShell

| 目的 | 命令 |
|---|---|
| 连接 Mac mini | `ssh macmini` |
| 查看 SSH 详细连接过程 | `ssh -v macmini` |
| 查看 Tailscale 设备状态 | `tailscale status` |
| 测试 Tailscale 到 Mac mini | `tailscale ping macmini-dev` |
| 检查远程 Codex 命令 | `ssh macmini "codex --version"` |
| 打开 SSH config | `notepad $HOME\.ssh\config` |

### B.2 VS Code 的 Mac mini 远程终端

| 目的 | 命令 |
|---|---|
| 查看当前用户 | `whoami` |
| 查看当前目录 | `pwd` |
| 查看 Mac 主机名 | `hostname` |
| 查看正在监听的 TCP 端口 | `lsof -nP -iTCP -sTCP:LISTEN` |
| 查看 tmux 会话 | `tmux ls` |
| 创建 Claude 会话 | `tmux new -s claude` |
| 进入 Claude 会话 | `tmux attach -t claude` |
| 检查 Codex 命令位置 | `which codex` |
| 查看 Codex 版本 | `codex --version` |

### B.3 手机 Termius 中的 Mac mini 终端

| 目的 | 命令或按键 |
|---|---|
| 查看 tmux 会话 | `tmux ls` |
| 进入 Claude 会话 | `tmux attach -t claude` |
| 离开但保留会话 | 先按 `Ctrl+b`，再按 `d` |
| 查看当前目录 | `pwd` |
| 确认当前用户 | `whoami` |

> [!warning] 不要把 detach 写成 exit
> `Ctrl+b` 后按 `d` 是离开 tmux 画面并保留任务；在程序中输入 `exit` 可能会结束当前 shell 或程序。

## 附录 C　术语解释

| 术语 | 非技术解释 |
|---|---|
| 固定主机 | 长期放在一个地点、负责保存文件和执行任务的电脑。本文指 Mac mini。 |
| 客户端 | 用来连接固定主机的设备。本文主要指 Windows 笔记本和手机。 |
| SSH | 一条加密的远程命令通道，让另一台设备登录 Mac mini 的终端。 |
| SSH 公钥 | 可以放到 Mac mini 上的“锁芯信息”，用于识别某台客户端。 |
| SSH 私钥 | 只应保存在客户端的“钥匙”。拿到它的人可能冒充这台设备。 |
| SSH config | 保存主机名、用户名和密钥路径的连接地址簿。 |
| Host 别名 | 给一组 SSH 配置起的短名称，例如 `macmini`。 |
| 终端 | 输入命令并查看文字输出的界面。 |
| CLI | Command Line Interface，主要通过文字命令操作的程序。 |
| GUI | Graphical User Interface，通过窗口、按钮和鼠标操作的图形界面。 |
| IP 地址 | 一台设备在网络中的数字地址。Tailscale 常见地址以 `100.` 开头。 |
| 设备名 | 比数字 IP 更容易记的名称，例如 `macmini-dev`。 |
| 端口 | 一台设备上某项网络服务使用的编号入口，例如 `3000`。 |
| 端口转发 | 把远程设备的某个端口，通过连接通道映射到当前电脑的另一个入口。 |
| SSH 隧道 | 利用 SSH 加密连接传递其他网络请求。VS Code 端口转发使用了这一思路。 |
| `localhost` | “当前这台设备自己”。在手机中写 `localhost`，指的是手机，不是电脑。 |
| Tailscale | 让经过授权的设备像在同一个安全私网中互相访问的工具。 |
| tailnet | 由同一个 Tailscale 账号或组织管理的一组设备。 |
| MagicDNS | 让设备可以使用 `macmini-dev` 之类名称互相访问的 Tailscale 功能。 |
| Remote Login | macOS 中开启 SSH 登录的系统设置。 |
| Remote SSH | VS Code 通过 SSH 打开远程目录、终端和端口的功能。 |
| 远程桌面 | 把 Mac mini 的图形画面传到另一台电脑，并远程操作鼠标键盘。 |
| tmux | 在 Mac mini 上保存终端会话的工具，客户端断开后会话仍可继续存在。 |
| tmux session | tmux 中一个可以离开并重新进入的终端工作空间。 |
| detach | 暂时离开 tmux 会话，但不结束里面的程序。 |
| attach | 重新进入已经存在的 tmux 会话。 |
| Web 服务 | 通过浏览器地址访问的页面或接口。 |
| API | 供页面、小程序或其他程序请求数据的网络接口。 |
| Tailscale 地址 | 设备加入 tailnet 后获得的私网设备名或 `100.x.x.x` 地址。 |
| 预览二维码 | 微信开发者工具生成的临时二维码，用于在手机打开开发版本小程序。 |
| 真机调试 | 在手机运行开发版本，同时让开发者工具继续提供调试信息。 |
| Codex Remote | 手机 App 通过已配对桌面主机查看和控制 Codex 任务的入口。 |
| 配对主机 | 已经与手机 Remote 建立信任关系、并实际提供工作环境的桌面电脑。 |
