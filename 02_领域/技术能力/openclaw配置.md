# 1.更新openclaw
- 更新到最新版本（不轮换 token，只保证 token 不再写在 unit 里）：
    

`openclaw-update`

- 更新到指定版本 + 顺便轮换 token：
    

`openclaw-update --version 2026.2.3-1 --rotate-token`

- 如果你极少数情况下不想动 token 相关逻辑：
    

`openclaw-update --no-secure-token`

# 2.相关配置
API_KEY=d54d860a2699b74a56e452f5c954e0e10d7adfb21024240e 给 openclaw 用
WEB_PASSWORD=aRQvTMyzL96m20Q4WUppaH1BR4lZO3  给你网页登录管理后台用

反代API KEY=sk-a83b0814c5c040bdbe28f360a6e282bc