_适用于任何前端框架（Next.js / Nuxt /_ _React_ _/ Svelte / 原生_ _JS_ _等）_

  

---

  

## 目录

  

1. [准备工作](#准备工作)
    
2. [在 Supabase 启用 Google Provider](#在-supabase-启用-google-provider)
    
3. [在 Google Cloud Console 配置 OAuth](#在-google-cloud-console-配置-oauth)
    
4. [把 Google 凭据回填到 Supabase](#把-google-凭据回填到-supabase)
    
5. [前端代码实现](#前端代码实现)
    
6. [本地开发与 CLI 调试](#本地开发与-cli-调试)
    
7. [上线后的额外域名配置](#上线后的额外域名配置)
    
8. [常见错误与排查](#常见错误与排查)
    

  

---

  

## 准备工作

  

```Plain
✅ 已有 Supabase 项目（或先去 https://app.supabase.com 新建一个）
✅ 已有 Google 账号，可登录 Google Cloud Console
✅ 本地安装 supabase-js v2 及你喜欢的前端框架
```

  

---

  

## 在 Supabase 启用 Google Provider

  

1. 登录 **Supabase Dashboard** → 选中你的项目。
    
2. 侧边栏点 **Authentication ▸ Providers ▸ Google**。
    
3. **复制** 面板顶部「回调地址（Redirect URL）」——格式固定：
    

  

```Plain
https://<PROJECT_REF>.supabase.co/auth/v1/callback
```

  

> 这就是稍后要登记到 Google 的唯一回调 URI。任何字符不符都会导致 `redirect_uri_mismatch`。

  

---

  

## 在 Google Cloud Console 配置 OAuth

  

### 1. 新建 / 选择项目

  

- 打开 [Google Cloud Console](https://console.cloud.google.com/) → 右上角 **Select project** → 选择或创建新项目。
    

  

### 2. 启用 OAuth 同意屏幕

  

1. 左侧导航 **APIs & Services ▸ OAuth consent screen**。
    

  

2. 选择 *External*（对公众应用）或 *Internal*（仅限同一组织 Workspace 用户）。
    

  

3. 填写 **App name**、**User support email**、**Developer contact info**。
    

  

4. **Authorized domains** 必须加入两项：
    

  

```Plain
<PROJECT_REF>.supabase.co
your-site.com      # 如果已有自定义域
```

  

5. 保存并（可选）发布到 *Production*。
    

  

### 3. 创建 OAuth 2.0 Client ID

  

1. 左侧 **APIs & Services ▸ Credentials**，点击 **+ Create credentials ▸ OAuth client ID**。
    

  

2. 选择 **Application type: Web application**。
    

  

3. **Name** 可随意（如 “Supabase Web”）。
    

  

4. **Authorized JavaScript origins**：
    

  

```Plain
http://localhost:3000          # 本地开发端口
https://your-site.com          # 正式站点
```

  

5. **Authorized redirect URIs**：
    

  

```Plain
https://<PROJECT_REF>.supabase.co/auth/v1/callback
http://localhost:54321/auth/v1/callback    # 使用 Supabase CLI 本地服务时必填
```

  

6. 点击 **Create**，记下 **Client ID** 与 **Client Secret**。
    

  

---

  

## 把 Google 凭据回填到 Supabase

  

1. 回到 **Supabase Dashboard ▸ Authentication ▸ Google**。
    
2. 填入刚复制的 **Client ID** 与 **Client Secret**，点击 **Save**。
    
3. （可选）在 **Auth ▸ Settings ▸ Redirect URLs** 中添加 “登录后跳转地址”，例如
    

  

```Plain
https://your-site.com/auth/callback
http://localhost:3000/auth/callback
```

  

---

  

## 前端代码实现

  

```TypeScript
// utils/supabase.ts
import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);
```

  

```TypeScript
// 登录按钮
import { supabase } from '@/utils/supabase';

export async function signInWithGoogle() {
  await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      // 可省略，默认回调到上面 Settings 里的第一条 Redirect URL
      redirectTo: `${location.origin}/auth/callback`
    }
  });
}
```

  

```TypeScript
// auth/callback 页面 – 处理登录状态
import { useEffect } from 'react';
import { supabase } from '@/utils/supabase';

export default function AuthCallback() {
  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      if (data.session) {
        // 已登录，跳到首页或个人中心
        window.location.replace('/');
      }
    });
  }, []);

  return <p>正在登录…</p>;
}
```

  

---

  

## 本地开发与 CLI 调试

  

1. 安装并初始化 Supabase CLI（可选）：
    

  

```Bash
npm i -g supabase
supabase start
```

  

本地 Auth 服务监听 `http://localhost:54321`.

  

2. **再** 把 `http://localhost:54321/auth/v1/callback`
    

  

- 加到 **Google → Authorized redirect URIs**
    
- 加到 **Supabase Dashboard → Auth → Settings → Redirect URLs**
    

  

否则你在 CLI 环境下登录同样会收到 `redirect_uri_mismatch`。

  

---

  

## 上线后的额外域名配置

  

- **新增自定义域**：
    

  

1. 将 `https://new-domain.com` 加入 **Google Authorized JS origins**。
    
2. 将 `https://new-domain.com/auth/callback`
    

  

* 加入 **Google Authorized redirect URIs**

* 加入 **Supabase Redirect URLs**

- **换域不删旧域**：先加新域、确认可用，再移除旧域，避免服务中断。
    

  

---

  

## 常见错误与排查

  

|   |   |
|---|---|
|报错 / 现象|解决思路|
|`400: redirect_uri_mismatch`|核对 Google ↔ Supabase **所有回调地址** 一字不差；检查末尾是否多 `/`；大小写、协议（http/https）必须一致|
|登录对话框闪退、无提示|OAuth Consent Screen 未「发布」，或用户类型 (External/Internal) 与账号不匹配|
|本地 OK、生产 400|生产域名未加到 Google **JS origins & redirect URIs**|
|One-Tap 登录失效|本地需包含 `http://localhost`，且前端加载 `g_id_onload` 脚本；检查浏览器第三方 Cookie 设置|
|登录后重定向到 `/` 而非自定义路径|在 `supabase.auth.signInWithOAuth` 的 `options.redirectTo` 指明自定义路径，同时把该路径加入 Supabase Redirect URLs|

  

---

  

完成以上步骤，你的站点即可使用 Google 账号正常登录。若仍遇到问题，把实际跳转的 `redirect_uri` 与 Google 控制台登记项逐字比对，或查看浏览器开发者工具的网络请求详情，即可快速定位。祝接入顺利！