

  > 适用场景：本地环境一切正常，部署到 Vercel 后 Fal.ai 语音生成成功，但 **Webhook** 没有回调到 `/api/webhook/fal`。

  

---

  

## **背景现象**

1. 前端提交文本，API 日志显示：
    
    1. 生成请求成功返回 `request_id`。
        
    2. 但 Redis 中任务一直停留在 `pending / processing`。
        

2. Fal.ai 后台 **Webhook Requests** 栏为空。

3. 本地 (`localhost:<port>`) 测试可以收到 Webhook，线上（Vercel Preview 域名）不行。
    

  

---

  

## **核心结论**

- **Fal.ai 并未向目标** **URL** **发送****回调**，问题不在我们的 `/api/webhook/fal` 处理逻辑。

- 失败原因：Fal.ai 无法访问 `preview.vocalstage.org` 这一 Preview 域名，常见原因包括：
    
    - 域名过长 / 路由过长 → 某些服务对 Webhook URL 长度有限制。
        
    - 域名经过 Cloudflare/WAF，阻断了来自 Fal.ai（GCP）的 BOT 流量。
        
    - TLS/证书链或 DNS AAAA 记录异常。
        

  

---

  

## **逐步排查流程**

  

1. **打印关键日志** （`generate` / `generate-line` route）：

```TypeScript
console.log('[generate] Webhook URL =', webhookUrl);
console.log('[generate] Fal response =', falResponse);
```

2. **用 RequestBin/Pipedream 验证**：

- 将 `fal_webhook` 改为临时地址，如 `https://eo9e...m.pipedream.net/api/webhook/fal`。
    
- 若能收到回调，说明 Fal.ai 正常 → URL 无法访问。
    

3. **curl / HEAD 自检**：

```Bash
curl -I -X POST https://preview.vocalstage.org/api/webhook/fal
```

- 期待 4xx/2xx；若超时或证书错误，即可定位。
    

4. **检查域名链路**：

- Cloudflare **橙云**→ 改为 **灰云 (DNS Only)** 或关闭 WAF 规则。

- 使用短域名（如 `vocalstage.vercel.app` 或自定义 `api.vocalstage.org`）。
    
- 运行 SSL Labs 检测，保证证书完整。
    

5. ****统一 `NEXT_PUBLIC_APP_URL`****：

- `.env.production` / `.env.preview` 均设置：
    
    ```Plain
    NEXT_PUBLIC_APP_URL=https://vocalstage.vercel.app
    ```
    
- 后端严格依赖该变量生成 Webhook URL，避免混用 `VERCEL_URL`。
    

6. **共用持久化资源**：

- Redis、Blob 等必须指向同一实例，确保 Preview/Production 互通任务状态。
    

  

---

  

## **解决方案**

1. **绑定简洁的自定义域**

```Plain
api.vocalstage.org → CNAME cname.vercel-dns.com
```

2. **Preview 也用生产域名接收 Webhook**

- `NEXT_PUBLIC_APP_URL=https://vocalstage.vercel.app`
    
- 生成任务时即指向主域 Webhook。
    

3. **移除/放行 Cloudflare WAF**

- 将子域设为 **DNS Only** 或为 `/api/webhook/fal` 创建白名单规则。

4. **代码层自检**

```TypeScript
// 在发送给 Fal.ai 之前
await fetch(webhookUrl, { method: 'HEAD' });
```

- 可在日志中立即暴露 URL 不可达问题。
    

  

---

  

## **经验教训**

- SaaS Webhook 场景中，**首要排查外网能否访问回调 URL**，而不是先看业务代码。

- Vercel Preview 域名虽方便，但可能过长且经常变动，不适合作为第三方回调入口。
    
- Cloudflare/WAF 会默认拦截非浏览器流量，务必为 API/Webhook 路径单独放行或使用不经过 Cloudflare 的域名。
    

- 在任务型 API 中，**即时返回 + 后台提交** 可以避免 Serverless 冷启动/超时问题。

- 任何外部回调依赖都要提供 **日志、可重复的测试地址**（RequestBin）与 **自检脚本**，减少排查成本。

  

---

  

**Happy debugging!**