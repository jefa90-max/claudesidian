## 目录

  

1. [准备工作](#准备工作)
    
2. [在 Supabase 启用 GitHub Provider](#在-supabase-启用-github-provider)
    
3. [在 GitHub Developer Settings 创建 OAuth App](#在-github-developer-settings-创建-oauth-app)
    
4. [把 GitHub 凭据回填到 Supabase](#把-github-凭据回填到-supabase)
    
5. [前端代码实现](#前端代码实现)
    
6. [本地开发与 CLI 调试](#本地开发与-cli-调试)
    
7. [多环境 / 上线域名配置](#多环境--上线域名配置)
    
8. [常见错误与排查](#常见错误与排查)
    

  

---

  

## 准备工作

  

```Plain
✅ 已有 Supabase 项目
✅ 拥有可登录 github.com 的账号
✅ 本地已安装 supabase-js v2 与所用前端框架
```

  

---

  

## 在 Supabase 启用 GitHub Provider

  

1. 登录 **Supabase Dashboard** → 选择项目。
    

  

2. 侧栏 **Authentication ▸ Providers ▸ GitHub**。
    

  

3. 页面顶部会显示「回调地址（Redirect URL）」**只读**字段，格式为：
    

  

```Plain
https://<PROJECT_REF>.supabase.co/auth/v1/callback
```

  

4. **复制**这条地址，后面在 GitHub OAuth App 要 _一字不差_ 填入。
    

  

---

  

## 在 GitHub Developer Settings 创建 OAuth App

  

> ⚠️ GitHub **一份 OAuth App 只能填 *****一个***** 回调 URL**。
> 
> 如果你有本地 + 生产两套环境，建议分别建两个 App，或用环境变量切换。

  

### 1. 打开 OAuth Apps 页面

  

1. 登录 GitHub → 右上角头像 → **Settings**。
    
2. 左侧 **Developer settings ▸ OAuth Apps**。
    
3. 点击 **New OAuth App**。
    

  

### 2. 填写 App 信息

  

|   |   |
|---|---|
|字段|建议填写|
|**Application name**|例如 `Supabase Auth`|
|**Homepage URL**|`https://your-site.com` 或 `http://localhost:3000`|
|**Authorization callback URL**|粘贴刚才复制的 `https://<PROJECT_REF>.supabase.co/auth/v1/callback`|

  

> 本地 CLI 环境登录时，需要另建一份 App，`Authorization callback URL` 填 `http://localhost:54321/auth/v1/callback`。

  

4. 点击 **Register application**，GitHub 即生成：
    

  

- **Client ID**（公开）
    
- **Client secret**（私密，点击 *Generate a new client secret*）
    

  

---

  

## 把 GitHub 凭据回填到 Supabase

  

1. 回到 **Supabase Dashboard ▸ GitHub Provider** 页面。
    
2. 填入 **Client ID** 和 **Client secret** → **Save**。
    
3. （可选）到 **Auth ▸ Settings ▸ Redirect URLs**，添加登陆后跳转地址，例如：
    

  

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

export async function signInWithGitHub() {
  await supabase.auth.signInWithOAuth({
    provider: 'github',
    options: {
      // 可省略；如要自定义回调路径需在 Settings ▸ Redirect URLs 先登记
      redirectTo: `${location.origin}/auth/callback`
    }
  });
}
```

  

```TypeScript
// auth/callback 页面 – 处理登录
import { useEffect } from 'react';
import { supabase } from '@/utils/supabase';

export default function AuthCallback() {
  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      if (data.session) {
        window.location.replace('/');
      }
    });
  }, []);

  return <p>正在登录…</p>;
}
```

  

---

  

## 本地开发与 CLI 调试

  

1. 安装并启动 Supabase CLI（可选）
    

  

```Bash
npm i -g supabase
supabase start
```

  

- Auth 服务监听 `http://localhost:54321`.
    

  

2. 为本地地址 _单独_ 创建一份 GitHub OAuth App：
    

  

```Plain
Authorization callback URL => http://localhost:54321/auth/v1/callback
```

  

3. 把该 App 的 **Client ID/Secret** 填到本地 `.env` 或 Supabase `dev` 项目中。
    

  

---

  

## 多环境 / 上线域名配置

  

- **GitHub 只能填一个回调 URL**：
    

  

- 生产、预发布、本地各建一份 OAuth App ⇒ 用不同凭据。
    
- **切换环境**：
    

  

- 在 CI/CD 或 `.env` 中用 `GITHUB_CLIENT_ID`、`GITHUB_SECRET` 环境变量切换。
    
- **更换域名**：
    

  

- 更新对应 OAuth App 的 **Homepage URL** 与 **Callback URL**，同时在 Supabase 侧保持 `https://<PROJECT_REF>.supabase.co/auth/v1/callback` 不变（除非换项目）。
    

  

---

  

## 常见错误与排查

  

|   |   |
|---|---|
|报错 / 现象|解决思路|
|`400 Bad Verification Code`|**Client secret** 与 App 不对应；或 App 被重置后忘记更新 Supabase|
|浏览器弹窗提示 `redirect_uri_mismatch`|OAuth App 的 **Authorization callback URL** 与 Supabase 固定 URL 不一致（末尾 `/`、协议、大小写任何差异都会失败）|
|本地 OK，生产登录白屏|生产前端 URL 未在 Supabase 👉 Auth ▸ Settings ▸ Redirect URLs 列表中|
|用户邮箱字段为空|GitHub 用户将邮箱设为 Private；在 `supabase.auth.signInWithOAuth` 的 `options.scopes` 加上 `user:email` 即可让 Supabase 自动抓取|
|“device verification” 重复出现|浏览器拦截第三方 Cookie；检查 `SameSite` 策略或改用重定向而非弹窗模式|

  

---

  

完成以上配置后，即可通过 **“使用 GitHub 登录”** 正常授权。

若仍遇到问题，先核对「GitHub OAuth App ↔ Supabase 固定 URL」是否完全一致，再查看浏览器 Network → `callback?code=` 请求返回内容定位错误原因。祝接入顺利！