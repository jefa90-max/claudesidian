- 更新到最新版本（不轮换 token，只保证 token 不再写在 unit 里）：
    

`openclaw-update`

- 更新到指定版本 + 顺便轮换 token：
    

`openclaw-update --version 2026.2.3-1 --rotate-token`

- 如果你极少数情况下不想动 token 相关逻辑：
    

`openclaw-update --no-secure-token`