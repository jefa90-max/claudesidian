# 最稳的办法：在 Mac 本地启动 tmux + Claude，再从 Windows attach

如果你现在 Mac mini 旁边还能操作一次，我更推荐这个办法。

在 Mac mini 本地终端里执行：

```
security unlock-keychain ~/Library/Keychains/login.keychain-db
tmux new -As claude
cd ~/projects/你的项目claude
```

确认 Claude Code 正常进入后，detach：

```
Ctrl + b然后按 d
```

然后你在 Windows 上 SSH 进去：

```
ssh macminitmux attach -t claude
```

这个方式很稳，因为 Claude Code 是在 Mac 本地桌面环境里启动的，Keychain 访问通常更顺。Windows 只是接入已有 tmux 会话，不重新触碰登录流程。

关掉会话的方法
tmux kill-session -t claude