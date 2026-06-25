---
title: VPS 代理与 SSH 安全加固记录
date: 2026-06-25
tags: [VPS, 代理, s-ui, Clash, Reality, TUIC, SSH, fail2ban, 安全加固]
source: [[2026-06-25]]
---

# VPS 代理与 SSH 安全加固记录

## 1. 背景

今天发现本地 Windows 电脑上的 Clash Verge 无法正常访问外网。Clash Verge 日志中出现大量 warning / error，其中比较关键的是：

```text
REALITY: processed invalid connection
```

同时，VPS 登录提示里出现了非本人产生的 SSH 登录失败记录：

```text
There were 6 failed login attempts ...
```

因此本次处理分成两条线：

1. 排查 VPS 上 s-ui 代理服务为什么不能正常使用；
2. 对 VPS 做基础 SSH 安全加固，降低公网爆破风险。

---

## 2. 代理问题现象

### 2.1 Clash Verge 客户端现象

Clash Verge 无法访问外网，日志中出现连接失败、EOF、Reality 握手失败等信息。

其中比较关键的现象是：

```text
80.251.213.84:443 connect error: EOF
```

服务端 s-ui 日志中对应出现：

```text
TLS handshake: REALITY: processed invalid connection
```

### 2.2 服务端情况

VPS 使用的是 **s-ui** 管理代理服务，不是单独的 `xray` systemd 服务。因此：

```bash
journalctl -u xray -n 80 --no-pager
```

没有日志是正常的。

实际代理进程是 `sui`，并且端口监听正常，曾看到类似端口：

```text
tcp *:443    sui
tcp *:2095   sui
tcp *:2096   sui
udp *:443    sui
```

这说明：

- s-ui 服务没有整体挂掉；
- VPS 端口监听正常；
- 问题不是“服务完全没启动”。

---

## 3. 已做排查

### 3.1 检查 s-ui 服务与端口

确认 s-ui 服务仍在运行，相关端口仍然监听。

使用过的命令包括：

```bash
ss -lntup
systemctl status sui --no-pager
journalctl -u sui -n 120 --no-pager
journalctl -u sui -f
```

结论：s-ui 服务整体正常，至少不是进程退出或端口未监听。

### 3.2 检查 Reality 伪装目标

当前 VLESS Reality 的伪装目标 / SNI 为：

```text
th.bing.com
```

在 VPS 上测试：

```bash
curl -I --connect-timeout 8 https://th.bing.com
```

返回了 HTTP 响应，例如：

```text
HTTP/1.1 400 Bad Request
```

这个返回不代表不可达，反而说明：

- DNS 能解析；
- VPS 能连到 `th.bing.com:443`；
- TLS/HTTPS 链路是通的；
- `th.bing.com` 作为 Reality 目标暂时不是主要问题。

### 3.3 检查时间同步

因为 Reality / TLS 对客户端和服务端时间比较敏感，所以同步了：

- Windows 客户端时间；
- VPS 时间。

相关命令：

Windows PowerShell：

```powershell
w32tm /query /status
w32tm /resync
```

VPS：

```bash
date
timedatectl
```

结论：时间同步后，VLESS Reality 仍然失败。

### 3.4 检查 Clash 节点配置

核对了 VLESS Reality 的关键参数：

- `server`: `80.251.213.84`
- `port`: `443`
- `type`: `vless`
- `network`: `tcp`
- `tls`: `true`
- `flow`: `xtls-rprx-vision`
- `servername`: `th.bing.com`
- `client-fingerprint`: `firefox`
- `reality-opts.public-key`
- `reality-opts.short-id`

也尝试过调整 `short-id`，但问题仍然存在。

### 3.5 查询网上资料

检索了 `REALITY: processed invalid connection` 相关资料。网上常见判断是：

这个报错不是端口不通，而是服务端收到了 TCP 连接，但 Reality 握手没有通过。

常见原因包括：

- Reality public key / private key 不匹配；
- short-id 不匹配；
- serverName / SNI 不匹配；
- client-fingerprint 不兼容；
- 客户端 / 服务端内核版本兼容问题；
- Reality 握手被中间网络或 DPI 干扰；
- 日志中的连接不是本人客户端，而是公网扫描器。

结合本次情况，由于昨天还能用、服务端配置没有主动修改，所以不继续优先怀疑手工配置错误，而是倾向于：

- Clash Verge / mihomo 内核兼容或状态问题；
- s-ui / sing-box 对 Reality 入站状态异常；
- Reality 协议本身被网络环境干扰；
- 或 Reality 入站参数实际被面板/内核更新后改变。

---

## 4. 临时解决方案：切换到 TUIC-443

在 Clash Verge 中将节点从 VLESS Reality 切换为：

```text
TUIC-443
```

切换后外网访问恢复正常。

这说明：

- VPS 代理服务整体可用；
- Clash Verge 客户端整体可用；
- VPS 公网端口不是完全被封；
- 当前问题主要集中在 `VLESS Reality` 入站；
- `TUIC-443` 可以作为短期替代方案继续使用。

### 4.1 TUIC 与 Reality 的关系

当前 s-ui 中大概率是两个入站共用 443，但协议不同：

```text
TUIC-443       UDP 443
VLESS Reality  TCP 443
```

这两个一般可以同时存在：

- TUIC 主要走 UDP 443；
- VLESS Reality 主要走 TCP 443。

因此，切换到 TUIC 不会破坏 Reality 配置，也不会影响 s-ui 服务本身。

### 4.2 TUIC 使用注意

TUIC 可用，但依赖 UDP。如果以后在公司、酒店、校园网等环境中使用，可能遇到 UDP 被限制的问题。届时可以再修复 Reality，或增加备用节点。

---

## 5. 后续 Reality 可继续排查方向

当前没有继续强行修改服务端配置，避免把可用的 TUIC 也影响到。

后续如果要修复 VLESS Reality，可以按这个顺序：

1. 确认服务端日志里的 `process connection from x.x.x.x` 是否确实是本机公网 IP，而不是公网扫描器；
2. 用 v2rayN / NekoRay 等其他客户端测试同一组 Reality 参数；
3. 如果其他客户端能用，重点排查 Clash Verge / mihomo；
4. 如果其他客户端也不能用，重点排查 s-ui / sing-box Reality 入站；
5. 尝试将 Reality fingerprint 从 `firefox` 成对改为更常见的 `chrome`；
6. 尝试更新或回退 Clash Verge 的 mihomo core；
7. 尝试更新 s-ui / sing-box core；
8. 必要时新建一个 VLESS Reality 入站，而不是继续修旧入站。

---

## 6. SSH 安全风险

登录 VPS 时看到提示：短时间内有多次 SSH 登录失败。

这通常说明 VPS 正在被公网扫描或尝试爆破登录，尤其是：

- 公网 IP 暴露；
- SSH 端口开放；
- root 用户可登录；
- 密码登录未禁用。

虽然这些记录显示的是“失败登录”，不代表已经被攻破，但需要尽快加固。

---

## 7. SSH 安全加固方案

目标：

1. 使用 SSH key 登录；
2. 禁用密码登录；
3. 安装并启用 fail2ban；
4. 让 fail2ban 监控 `sshd`，自动封禁连续登录失败的 IP。

### 7.1 Windows 生成 SSH key

在 Windows PowerShell 执行：

```powershell
ssh-keygen -t ed25519 -C "your-vps-key"
```

生成：

```text
C:\Users\用户名\.ssh\id_ed25519
C:\Users\用户名\.ssh\id_ed25519.pub
```

其中：

- `id_ed25519` 是私钥，不能泄露；
- `id_ed25519.pub` 是公钥，可以放到 VPS。

查看公钥：

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

### 7.2 VPS 写入 authorized_keys

在 VPS 上执行：

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

将 Windows 上的公钥完整粘贴进去。

然后设置权限：

```bash
chmod 600 ~/.ssh/authorized_keys
```

### 7.3 测试 key 登录

不要关闭当前 SSH 窗口，新开一个 PowerShell 测试：

```powershell
ssh -i $env:USERPROFILE\.ssh\id_ed25519 root@80.251.213.84
```

确认能用 SSH key 成功登录后，再禁用密码登录。

### 7.4 禁用密码登录

备份 sshd 配置：

```bash
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak.$(date +%F-%H%M%S)
```

编辑：

```bash
nano /etc/ssh/sshd_config
```

确保有以下配置：

```text
PubkeyAuthentication yes
PasswordAuthentication no
PermitRootLogin prohibit-password
KbdInteractiveAuthentication no
ChallengeResponseAuthentication no
UsePAM yes
```

检查语法：

```bash
sshd -t
```

无输出表示配置语法正常。

重启 SSH：

```bash
systemctl restart sshd
```

再次开新窗口测试 key 登录是否正常。

测试密码登录是否已禁用：

```powershell
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no root@80.251.213.84
```

预期结果：密码登录失败。

---

## 8. fail2ban 安装与问题处理

### 8.1 初次安装失败

执行：

```bash
dnf install -y fail2ban
```

一开始提示找不到包：

```text
No match for argument: fail2ban
Error: Unable to find a match: fail2ban
```

原因：当前启用的不是完整 EPEL 主源，而只有类似：

```text
epel-cisco-openh264
```

这个源只提供 OpenH264 相关包，不包含 `fail2ban`。

### 8.2 启用 EPEL 主源

检查源：

```bash
dnf repolist all | grep -Ei 'epel|crb'
```

启用 EPEL 主源：

```bash
dnf config-manager --set-enabled epel
dnf clean all
dnf makecache --refresh
```

然后安装：

```bash
dnf install -y fail2ban
```

安装成功后启动：

```bash
systemctl enable --now fail2ban
systemctl status fail2ban --no-pager
```

看到：

```text
Active: active (running)
```

说明 fail2ban 服务已正常运行。

### 8.3 配置 sshd jail

创建配置：

```bash
nano /etc/fail2ban/jail.local
```

写入：

```ini
[DEFAULT]
bantime = 1h
findtime = 10m
maxretry = 5
backend = systemd

[sshd]
enabled = true
port = ssh
filter = sshd
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
```

重启 fail2ban：

```bash
systemctl restart fail2ban
```

查看状态：

```bash
fail2ban-client status
fail2ban-client status sshd
```

最终确认 `sshd` jail 已生效，输出中包含类似：

```text
Status for the jail: sshd
Currently failed: 0
Currently banned: 0
Journal matches: _SYSTEMD_UNIT=sshd.service
```

这说明 fail2ban 已经通过 systemd journal 监控 SSH 登录。

---

## 9. 当前结论

### 9.1 代理部分

当前结论：

- s-ui 服务整体正常；
- TUIC-443 可用；
- VLESS Reality 当前不可用；
- Reality 报错集中在握手阶段：`REALITY: processed invalid connection`；
- 短期继续使用 TUIC-443；
- 后续再单独修复 Reality。

### 9.2 安全部分

当前结论：

- VPS 出现过非本人 SSH 登录失败，属于常见公网扫描/爆破尝试；
- 已配置 SSH key 登录；
- 已禁用密码登录；
- 已安装并启用 fail2ban；
- `sshd` jail 已生效。

---

## 10. 后续建议

- 保留 TUIC-443 与 VLESS Reality 两个节点，避免单点失效；
- 找时间用 v2rayN / NekoRay 交叉测试 Reality，判断是 Clash Verge 问题还是 s-ui/sing-box 服务端问题；
- 定期查看 fail2ban 状态：

```bash
fail2ban-client status sshd
```

- 如需解封 IP：

```bash
fail2ban-client set sshd unbanip IP地址
```

- 后续可以考虑进一步 SSH 安全加固：
  - 更换 SSH 默认端口；
  - 禁止 root 直接登录，改用普通用户 + sudo；
  - 云厂商安全组只允许自己的固定 IP 访问 SSH；
  - 定期更新系统和 s-ui / sing-box core。

---

## 关联

- [[2026-06-25]]
