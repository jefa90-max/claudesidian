|目标|命令|
|---|---|
|创建或进入会话|`tmux new -As dev`|
|查看所有会话|`tmux ls`|
|进入已有会话|`tmux attach -t dev`|
|简写进入会话|`tmux a -t dev`|
|退出 tmux 但保持运行|`Ctrl+b` 然后 `d`|
|关闭某个会话|`tmux kill-session -t dev`|
|创建新窗口|`Ctrl+b` 然后 `c`|
|切到下一个窗口|`Ctrl+b` 然后 `n`|
|切到上一个窗口|`Ctrl+b` 然后 `p`|
|查看窗口列表|`Ctrl+b` 然后 `w`|
