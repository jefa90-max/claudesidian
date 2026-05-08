---
title: "用好 AI 跟上时代"
source: "https://scys.com/course/detail/172?chapterId=11410"
author:
published:
created: 2026-05-08
description: "生财有术是专注普通人学习 AI 与创业的实战型社区，推崇真诚、务实、可落地的学习氛围，通过情报挖掘、会员分享、系统课程、项目实战与同行者圈子，帮助你学会用 AI、看懂趋势、抓住创业机会。自 2017 年创立以来，已有 7 万多人受益。"
tags:
  - "clippings"
---
## 超级 AI 大航海丨实战手册丨2026年5月航海

## 04\. 产品能力：AI 编程

💡

本章概要

产品能力，是把想法做成别人可以使用的产品。AI 编程降低了开发门槛，但真正决定结果的不是会不会写代码，而是能不能把需求、边界和验收标准说清楚。

本章将带你完成两件事：

1.

理解 AI 编程的人机分工：人负责想清楚需求、检查结果和做决策，AI 负责生成代码和处理细节

2.

用 Coze 编程做一个 AI 个人介绍页：先通过问答把页面目标、展示内容、结构风格和功能边界聊清楚，整理成 PRD 文档，再生成页面、补充资料并部署上线

⚠️需要特别注意：

•

第一版页面不完美是正常的，AI 编程本来就需要反复预览、截图标注、反馈修改

•

需求没聊清楚前，先用问答模式，不要直接切 Agent 模式开做，否则很容易跑偏

•

AI 问答是进阶功能，不是必做项；先把个人主页生成、资料替换和部署上线跑通更重要

学完本章，你能够跑通一次从想法到可访问网页的 AI 编程流程，做出一个可以公开展示的个人介绍主页。

💡

本章航线图

完成本章节的学习和操作，即可完成航线图的：

1.

用 coze 编程做一个个人介绍主页（约 3 天）

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Els8bPv11op4uNx0ptXcusI6nLg_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=6b35e6b2c3b5068f6c9d4b86950a5bba69b706e5fef6362907d33d636a2424ba&x-oss-signature-version=OSS4-HMAC-SHA256)

产品能力，就是把一个需求或想法做成产品的能力。

AI 编程，是其中一种做法：借助 AI 去完成开发。

人和 AI 的分工就变成：

•

人负责：想清楚要什么，检查做得行不行，最后做决定。

•

AI 负责：干活，出东西，处理细节。

现在为什么值得学 AI 编程？是因为 AI 变强了，做产品的门槛大大降低。

你可以掌握主动权，从消费者转变为创造者：

•

找不到顺手的工具，你可以自己做一个

•

脑子里那些一直搁着的想法，你有机会把它做出来，拿出去，让别人用，甚至为它买单

💡

文中关于 Spec 介绍内容引用自：生财深海圈·AI 编程 付费课程，已通过刘小排授权

对 AI 编程进一步学习感兴趣的同学，可考虑加入 AI 编程深海圈

AI 编程刚开始时，很多人习惯边聊边改，想到哪做到哪。功能简单、技术不复杂的项目这样还能跑，需求一多、逻辑一复杂，就很容易乱。

AI 编程最核心的技能，是把需求说清楚。

假设朋友叫你帮她买生日蛋糕，她是这么跟你说的：

帮我买个蛋糕，要好看的，甜一点，不太贵，清新风格，最好草莓口味，芒果也行……

你知道要买怎样的蛋糕吗？

如果她这么说：

8 寸草莓蛋糕，100 块以内，下午 5 点前到，写"生日快乐小明"，不要奶油边框。

这样清晰多了是吧。

给 AI 写需求也是一回事。

在 AI 编程里，这种“先把需求说清楚，再开始开发”的做法，通常叫 Spec 编程范式，也可以理解为规范驱动编程（Specification-Driven Development）。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PpRcbUIqwojLA4xK7P4cES44nAb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=c48a46f0afc8fce29837793631623611542915cd20b9924c846142ef778e53de&x-oss-signature-version=OSS4-HMAC-SHA256)

它的核心是写代码前，先把需求整理成一份结构化、可验证的规范，再让 AI 按这份规范去生成和修改代码。

它的作用，是减少需求歧义，让开发过程更可控，也更方便 AI 参与实现。

你可以先把 Spec 理解成一份写给 AI 的开发说明书。

它至少要说清几件事：要解决什么问题，准备怎么做，有什么约束，哪些不要做，怎样才算做成了。

所以，Spec 不是一句模糊想法，也不是随手写的一段 Prompt。

它更像是开发前的说明书：先把目标、边界和标准讲清楚，再让 AI 开始干活。

对新手来说，不用一上来写得很复杂。

先把下面这 5 件事说清楚，就已经够用了：

检查项

问自己

问题陈述

用户要什么体验？一句话能说清楚吗？

方案描述

功能、数量、交互、视觉，具体到数字了吗？

技术约束

技术栈写了吗？

红线

说清楚"不要什么"了吗？

交付标准

怎么算做完？手机能用吗？有闭环吗？

看到这里肯定会犯嘀咕，我作为一个编程新手，根本写不出这么专业的 Spec。 ——那么如何能快速提升写 Spec 能力呢？

答案是：直接和 AI 讨论，让 AI 提问你，来帮你梳理需求。

比如，可以复制下面的提示词

经过多轮对话，最终可以让 AI 输出完整规范的 SPEC。

```
我要做一个：  …………这里只用一句话，把你的想法说个大概……
请你先不要写代码，你需要
1. 像苏格拉底一样，帮助我梳理需求，
2. 你需要一个问题一个问题地问，每次都给出带编号的选项
3. 直到我们能够形成一份完整的SPEC，符合以下标准
• Problem Statement（问题陈述）
• Proposed Solution（方案描述）
• Technical Constraints（技术约束）
• Non-goals（明确不做的事）
• Success Criteria（成功标准）
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Or1obxju3oBdgkx2p8ZcLksdnqc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=b2a6fe2515c5bb3cb37c49b268891001711ccbda8e125aa9953eb6b4f2f859a0&x-oss-signature-version=OSS4-HMAC-SHA256)

3\. 实操案例：做一个能对话的 AI 个人介绍页

这次我们会做一个 能对话的 AI 个人介绍页。

这个案例做完就能直接用。

线下活动、自我介绍、投简历、认识新朋友的时候，别人还在一字一句打字介绍自己时，你不妨把自己的主页链接发给大家。

大家点开以后，就能很快看到你是谁、做过什么、现在在关注什么。这种有趣的介绍方式，不仅可以让大家更加了解你，还可以为你打开社交话题。

借着这个有意思的案例，我们也会把 SPEC 深入贯彻实操一遍。

个人主页实操案例主要分为以下四个步骤：

1.

项目需求讨论（可以理解为这个网站用来干啥，功能要哪些等实际功能需求）

2.

项目 UI 确认（可以理解为网站的风格、排版等美化互动方面的需求）

3.

项目开发测试（就是 AI 做好了这个网站，去看用起来符不符合预期，需要修改的，和 AI 说清楚）

4.

项目上线部署（让所有的人都能看到你的网页要做的必要动作）

其中项目需求讨论 和 项目 UI 确认可以理解为都是说清楚需求，只不过是不同方面的需求，一个是功能方面的，另一个是设计方面的。

我们还会有一个进阶功能，AI 问答的接入，但这个不作为必须动作，学有余力的船员可以选择做一下，这个同样涉及说需求讨论和开发测试的过程。

个人主页的案例实操样例如下：

https://nrmqk62rjz.coze.site/ （讨论需求后直接生成的版本）

https://8stfh9pyqq.coze.site （调整了网站风格后的版本）

案例的个人介绍资料教练给了一个通用的版本，抛砖引玉，推荐大家都使用自己介绍资料和信息

实操会教如何做出不同风格样式的个人主页，期待大家的各色样式的个人主页诞生！

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/YETebxcS7oUkLdxJ7r4cjLNynef_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=33b205c55a153291e3bd6b2c5edcf68f424b260eba07ba409eede7803951ebb6&x-oss-signature-version=OSS4-HMAC-SHA256)

3.0 案例使用工具：Coze 编程介绍

本次案例选用的工具是 Coze 编程。

Coze 编程是字节跳动推出的 AI 应用开发工具，支持在网页里直接完成生成、修改和部署等操作。

这次我们沿用了 AI 编程深海圈已经验证过的工具选择。刘小排老师在升级 生财深海圈 AI 编程内容时，测试过不少国内外 AI 编程工具，最后把 Coze 编程纳入了实际教学使用。

之所以沿用这个选择，是因为它对初学者更友好。你可以直接在网页里开始，通过对话先把需求说清楚，再一步一步完成页面生成、修改和上线。对于第一次接触 AI 编程的人来说，这样更容易先把从一个想法到一个能访问的网页这条路径跑通，也更容易获得第一轮正反馈。

如果你之前关注过 2025 年 12 月、2026 年 3 月的 AI 编程相关内容，会发现 AI 编程这条线已经在持续沉淀。等你先把这次案例跑通，后面如果想继续进阶，也会接触到 Claude Code、Codex 这类更偏专业场景的 AI 编程工具；相关进阶内容，也会在后续 2026 年 6 月航海实战里继续展开。

接下来，我们先把 Coze 编程这个工具认识清楚，再开始动手做页面。

Coze 编程 地址：https://code.coze.cn/home

第 1 步：打开注册地址 Coze 编程 ，点击右上角免费开始进行登录注册。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PV6Sb5dC2oDMXlxuf00cEHWCnA4_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=b0ecd224b77c2d06c00fcd26fda3a7c53ff46e38fc78a46c7f6da1f6b3ee31ad&x-oss-signature-version=OSS4-HMAC-SHA256)

第 2 步：直接如图操作使用手机号登录。

注：如果以前没注册，会自动注册；如果注册过，会直接登录。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PngmbUbANo5BPIxHjTkcVAKLnRb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=cad372421e70cd75ad5e0f43fb1cd639f11eb2830e4f21918fe063fa92da3812&x-oss-signature-version=OSS4-HMAC-SHA256)

第 3 步：登录完成后会跳转回 Coze 编程首页。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/MT01bNlxUoIWUNxzJXXcaSC1nob_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=22c0b9f124cb1182932e354f1dc545ca4a7ffad20b6753b6ca1ced10f7877a1d&x-oss-signature-version=OSS4-HMAC-SHA256)

关于积分：

•

如果你是 Coze 新用户，通过注册会获得 3000 积分。

•

另外每日成功登录还可获赠 1500 积分。

•

如果不是新用户，也可以直接开始使用。积分用完后如果还要继续开发，需要按平台当前的付费规则充值，最低 19.9 元/月。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/T0h3bhLQnoWL5mx8MYEcwDkznNc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=bbad7a88df8278be3ac6dce812019df41b9afb99583f61a5777d9bfce51afafb&x-oss-signature-version=OSS4-HMAC-SHA256)

3.0.2 先认识首页和主要工作区

下面这张图主要标注了我们常用的 3 个功能：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/F9dpbwML5oOqkWxHrCqccBXVnnd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=8a6df82d357c45dbe671de239174ef21c449a3fb1f417b7ea34a6cd5eeb7f857&x-oss-signature-version=OSS4-HMAC-SHA256)

•

① 新建应用入口（网页应用功能介绍有展开讲解，这里先做个概览）

怎么用？ 选择你想要创建的应用（我们案例属于网页应用），接着在下方空白处，输入文字（你的需求），就可以开发啦。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/UfiYbAk8SoE6MGxYpbScEeCvnkd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=8aa26c0e37be32d744ed3e4979c000867bd6d19e92f289052632212cde237fcf&x-oss-signature-version=OSS4-HMAC-SHA256)

•

② 项目管理

干嘛的？

管理已有项目：做到一半的东西可以在这里找回来，项目多也可以点击并选择切换

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/E243b8FPJo7gWBxp0xhcLlzinud_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=9305fbe8aff80d38a165efadd3b4f927575245cf59bbeae971ae2533811781b0&x-oss-signature-version=OSS4-HMAC-SHA256)

•

③ 个人信息/充值

干嘛的？

订阅和充值在这里管理，额度不够了去这里

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/CfeSbwOZkoaiK6xX5I4cY6Fenhb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=473f8097b6523e79a985571e47d0197f425e65bd7e4f3bfb3da2b4f3d4a4b976&x-oss-signature-version=OSS4-HMAC-SHA256)

主要就是下面红色框里面的四个按钮的功能。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PbAxbhWR1ooRT9x7whHcE0xjned_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=449a2d4271019b9b30293aa8ae8e2d0759e6b3bc0bd950c6da2e4fc42cf2335d&x-oss-signature-version=OSS4-HMAC-SHA256)

① 上传附件

你有一些文档/图片/视频什么的，就通过这个加号按钮来上传，但是会有文件大小的限制，目前单个文件不超过 20MB。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/XtGZbM1ezoY69KxUbZccJet3nPh_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ded6b48aecedc6dc8a232361476c158b7c19df494172907ddfd96fdf84d870b6&x-oss-signature-version=OSS4-HMAC-SHA256)

② 协作模式/工具

协作模式：问答模式 / Agent 模式

•

Agent 模式：干活模式。你发一句提示词过去，他可能就开始嘎嘎给你写代码、写应用了。

•

问答模式：只对话，不干活。适合需求还没想清楚的时候，用来讨论和澄清。

工具：联网搜索、图片生成

•

联网搜索：需要最新的一些网络资料和数据的时候，这次暂时不涉及

•

图片生成：主要用于在对话过程中让它生成一些图片，或者生成一些网站的高保真 UI 交互图。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/SA5Fb2mMPoyAZoxQeI1c5l77njh_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ad1398b76d43ea8172912ced045855a7a310b2fb67b52fa16bf0161761d30940&x-oss-signature-version=OSS4-HMAC-SHA256)

③ 技能（需要你跟着操作一下）

这是开始做个人页面前需要提前配置好的步骤

可以看到技能这个按钮右上角有一个数字 14，代表着已经选择安装的技能有 14 个。

当然，你可能看到这里的时候，你的技能显示的数目和我的不一样，比如 17，这个是正常的，因为平台都在迭代优化升级。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/IhXcbi0cNosOrLxiYxqcLS1bnrf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=8931946f3af797c1f56d503a24eb7da6e78d4f19bfb93250f633bce83bdb5deb&x-oss-signature-version=OSS4-HMAC-SHA256)

点开技能以后，就可以看见技能列表。

因为我们案例属于网页应用，已经在这里选中了

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/RZLdbnBZhoR2nrx0SPUc3VVjnNF_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=6f632c2ee726da9542d2e4f7deb4dcab29e77d7a9fae053106e840d0728c1412&x-oss-signature-version=OSS4-HMAC-SHA256)

可以看到左侧的按使用场景筛选，默认就是【网页开发】

右侧向下滑动，找到以下 7 个技能，点击添加按钮，完成技能添加

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/A0rxbwyrmoUr1bxLLcUcGOlsnvj_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=93d5566d3b22bd9c805ccdf431d148c826b4372405b2ae9c70a0ba722d9629a0&x-oss-signature-version=OSS4-HMAC-SHA256)

添加完上面截图的 7 个就好了

完以后，这里的数目你可能跟我的不一样。首先保证上面截图的那些前端的技能都添加上就可以。

如果后续有变动，我们再更新手册或者群里通知。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/SFwjbntUkoWzxTxPCsmcDuyanhf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=2751b6bb6627f1598a3e849f16db3af4b555b4410cd5350f4642b68fb0d87c32&x-oss-signature-version=OSS4-HMAC-SHA256)

④ 模型选择

现在知道入口在哪里就可以，不用在一开始花时间研究，当前我们就使用【自动】即可。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/HAq0bS63poiOWWx2COzcbLpSn9g_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ea477fb47a6c628b4b859cd9f09684dbe13412e889076eb64effd3c1a4cb0ca9&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/YKulbagaLoA4D0xmYc0ce6S9ntf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=08fb1bd7055eecf20e044a7b7970633ad387f9d09fc3ed86d0ac9e40cb2b9e6f&x-oss-signature-version=OSS4-HMAC-SHA256)

3.1 第一步：项目需求讨论

这一节要完成的是：把一个模糊想法整理成 Coze 编程 能执行的开发说明书。

💡

我们要开始做一个项目的第一件事就是需求讨论。

也就是说，你做这个东西要做成什么样子？你有什么样的需求。

所以第一件事情绝对不是拿到编程就开始写代码

💡

AI 编程小技巧 ：

1.

先讨论需求，再让 AI 动手写代码。

（这里需求讨论分成两步进行：页面展示内容需求讨论、设计风格需求讨论，最后合成完整的需求文档）

2.

需求讨论的目的，就是产出一份给 AI 看的开发说明书，我们通常叫它为 PRD 文档，通常以 markdown 的形式输出（ prd.md ）。

\-PRD 是“Product Requirement Document”的缩写，意为产品需求文档，用于详细描述产品功能、目标用户和开发需求。

3.1.1 先说清楚主页给谁看、放什么

💡

这一小节先把这三件事说清楚：主页是拿来做什么的、主要给谁看、要展示哪些内容。

技术实现、页面美化、AI 问答，这些等页面展示内容需求聊清楚了再说。

现在正式开始整理需求，先切到问答模式（新版应该是对话模式）。在没有搞清楚所有需求之前，都要一直保持问答模式。

当你对自己要什么很模糊的时候，就是没办法给 AI 说清楚的，这个时候可以和 AI 做个讨论。

接下来展示 2 种讨论需求的过程，按自己情况选择 1 种即可：

•

第 1 种，最简单，从一句你能说出的简单的提示词开始，适合超级新手刚起步的阶段，感受到自然语言编程的完整流程，降低心理门槛。

•

第 2 种，给一个结构化的提示词，让 AI 在这个限定范围内来提问你，把这个需求澄清清楚，适合想要快速聊清楚需求的人。

3.1.1.1 需求讨论方法 1：从你能说出的提示词开始

开始可以是一句很简单的提示词，

比如下面的这个，你想到什么就发什么。

```
我想创建一个个人介绍的网站，我现在跟你讨论一下具体的需求
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/FD6abZPRfofSYqxDGHVcAToGnU8_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=4b8e4c07742d0344b9e6d580355d1516238c76aaad7ea62bd2c685be4ca1411f&x-oss-signature-version=OSS4-HMAC-SHA256)

点击发送后，就可以看到下面的界面。

我们稍等一下，等到左边回复你的消息。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PdoAbXmUmouO4qx8c0Ncn9qhn9e_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=0ede7580fc213e06f00d46e7a23f65f744113ffd4a757b2eda01a8d268a4dcf4&x-oss-signature-version=OSS4-HMAC-SHA256)

因为我们发的需求比较简单，Coze 会开始追问目标受众、展示内容等。

设计偏好、设计风格等，不是我们当前的讨论重点，可以略过

我们优先把整个页面需要展示什么内容讨论清楚

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/P4X4ba6GhoHTKMxZofwcQJ2MnHc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=5a6529f0484aab8899566f3016a105fadfa07931aabad97aafd265228c0dc9b3&x-oss-signature-version=OSS4-HMAC-SHA256)

根据追问，把你知道的部分说清楚：

```
我的网站目的主要用于个人作品集展示，以及个人品牌建设。
我的目标受众是可能和我合作的人、对我项目感兴趣的人、以及想了解我过往经历的人。

我希望展示的内容包括：
1. 个人简介
2. 工作经历
3. 技能专长
4. 项目作品集
5. 航海案例集（在一个叫做“生财有术”副业赚钱线上社区里，参与官方实战项目的个人做出来的案例呈现，主要是写1篇文章和1个视频）
6. 联系方式和社交媒体链接
```

展示的内容这里，我们添加了一份“航海案例集”，我们在表达能力：内容生产中生成了一些案例，比方说文章、视频等，我们可以把这些作品放到个人介绍页里，当然你可以换成其他你想展示的内容，只要修改提示词即可。

说清楚表现形式一：遇到 AI 不明白的词，需要和 AI 解释清楚： 比如“航海案例集”明显是 AI 不理解的词，要及时解释：

```
航海案例集是一个项目案例集合，来自我参加的生财有术航海项目。
这里面可以放我在航海里完成的文章、视频。
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Eh6GbSip4oGKhwxH5EmcojlSnUd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=5b8bd80cc60efc210f9e4a8f8c20a0fa7ee1d1413ef5458e402d5003a5fcb463&x-oss-signature-version=OSS4-HMAC-SHA256)

说清楚表现形式二：遇到有歧义的内容，和 AI 把边界说清楚：

如果 Coze 追问项目作品集和航海案例集要不要分开，把边界说清楚：

```
项目作品集和航海案例集，我希望分开展示。
项目作品集放我平时做过的项目，航海案例集放我参加航海项目时做出的作品和练习。
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/CpiJbCuvmoeaX9xqCZ2coQgCnmx_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=d5090e323497d8334008687bab59c5e49181e308937226ac78293b77bccc6b02&x-oss-signature-version=OSS4-HMAC-SHA256)

3.1.1.2 需求讨论方法 2：结构化提示词，让 AI 提问

💡

这里要说的是另外种讨论需求的方式，如果前面讨论的还不错，可以跳过这个环节

放在这里是让大家在前面先体会简单的讨论需求过程（其实也能聊出来）

然后用前面“AI 编程的核心技能”这边提到的结构化提示词，来约束讨论需求的过程，帮你整理需求

直接把下面的提示词，发给扣子编程，让 AI 帮你梳理结构化需求规格文档

注意：需要使用「问答模式」

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Rl95bdheloGhBTxYsg0ce9U2nyb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=04092ef47a785f012bb8b77ea9d01045816df63b2bffef145b7f84fcdd982141&x-oss-signature-version=OSS4-HMAC-SHA256)

```
我要做一个：  …………这里只用一句话，把你的想法说个大概……
请你先不要写代码，你需要
1. 像苏格拉底一样，帮助我梳理需求，
2. 你需要一个问题一个问题地问，每次都给出带编号的选项
3. 直到我们能够形成一份完整的SPEC，符合以下标准
• Problem Statement（问题陈述）
• Proposed Solution（方案描述）
• Technical Constraints（技术约束）
• Non-goals（明确不做的事）
• Success Criteria（成功标准）
```

如下图，它会主动给我们一些提问，下面就会是一轮一轮的问题

后面的都是一问一答，我们准备好自己的答案就行

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/V4xZbBGRhozb3fx5WZUcTUcqnOd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=dab39f4c896a5c2e6915f5d6df6eae531c7ad00310219766aee69ca8114dde83&x-oss-signature-version=OSS4-HMAC-SHA256)

如下图类似的，如果你觉得不满意，还可以继续调整，没有调整的就进行下一步

如图所示，就可以有一份完整的 SPEC 规范文档啦

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/WATFbRBSeoVzTqxaw33cZ4TOn2e_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=fa07b159427cd733402d79291cc1887180f6a7fc96f836162834c8077b5dee92&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/EhuKbJs9uomCXcxyhY3c1xJpn4v_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=4ae437936bfe9f2db26fd6231dc162f772d71b144808e13798c46fa98a1bcc21&x-oss-signature-version=OSS4-HMAC-SHA256)

3.1.2 再确定页面结构和风格

这里千万记得用问答模式

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/TrtCbRF07oSUDoxnlLZcJSM4nnb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=01a0e2073bef3ca3f6cac5317748b8edc966a3ed120460a1442bec47aa92c8ee&x-oss-signature-version=OSS4-HMAC-SHA256)

💡

这一部分讨论的就是整体的风格、版式布局这些。 一共有 3 个方法，供你选择：

方法一直接说的你的需求比如最简单的一个风格词，让 AI 发挥，好处是操作非常简单，你只需要顺着 AI 自然对话，就可以看到 AI 给你的灵感和惊喜，缺点就是不可控，抽卡式。

方法二使用网站风格提示词，你可以让 AI 根据提示词限制去生成，好处是稳定发挥，缺点就是不够灵活。

方法三借鉴网页风格，可以根据你希望的网页风格去生成，优点是灵活，缺点是找寻适合的案例较为费时，复刻的细节有些是没办法还原的。

当然，这 3 个方法是可以综合起来使用的，如果你感兴趣就试试。

建议：这节和上节生成的需求放在一起，合成一个 prd 文档。

3.1.2.1 方法一：直接和 AI 对话需求

需求讲清楚以后，再来讨论页面结构和风格。

可以看到前面对话的的时候 Coze 给我们列出了一些风格选项，比如：

如果前面 AI 编程工具没有提到设计风格，那我们这部分可以主动开始。

这个是手册案例中 AI 罗列的风格，你实际聊的可能跟手册里的不一样，没关系

1.

海洋风

2.

极简专业

3.

创意动线

4.

温暖亲和

你和 AI 对话，可以顺着挑选一个 coze 给你推荐的风格去生成

如果你不喜欢 coze 给你的风格，也可以指定风格或者自己的需求，请你往下面看

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/P152bSEfzoBD16xzvhocdWMbnkd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=e11bc49bbef224a48c4e68ebb21beebef137ac7be98301c832d7318381baca7f&x-oss-signature-version=OSS4-HMAC-SHA256)

比如，我想使用像素风，我下面跟扣子编程聊一下：

```
我想使用像素风格，帮我推荐一下适合我这个网站的像素风格怎么样？
```

具体的交互如下，Coze 会给出颜色搭配、字体方向，以及用 ASCII 字符展示的页面布局预览。

截图比较长，可以多往下翻一点。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/VW0LbnW1goTt2wx3rdmc8ouDn1i_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=47f333caf185cf7836b65e587a4a20b822a567f8861c66c41e932eebd5ee129f&x-oss-signature-version=OSS4-HMAC-SHA256)

你也可以让它生成 demo 图大概看看效果：

```
可以给我生成 demo 图片，我大概看一下长什么样子吗？
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Ca6Ebf2gCoTHMgxIqfncLn24nke_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=a26aafc25adce5f3cdc0a2c7830a8c37cefbe1d71cacbd9c937e38f204313c52&x-oss-signature-version=OSS4-HMAC-SHA256)

到这里我觉得是可以的，如果你觉得不行，可以继续往下，再次讨论，修改你喜欢的样式。

这里你生成的有可能是跟手册里面的不一样的，这个是正常的哈，这个是跟你的选择风格有关系，并且跟当前平台模型的智商也有关系

3.1.2.2 方法二：网站风格提示词

如果你喜欢特定风格的网页，可以给 AI 特定风格的提示词

比如这个免费网站： design-lab-yanliu.vercel.app （这个网站需要配置网络环境）

有具体的网站案例和提示词

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/W7p7blzCZoE5LlxAJpJckSoJn2y_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=255dcb6975f2812910aaba9ba4663f35f372247219fd0f9e02793bb5b96ab0a7&x-oss-signature-version=OSS4-HMAC-SHA256)

你们也可以自己在网站里面找合适的网站风格提示词

我这里提供 3 种风格的提示词

你可以直接发给扣子编程

1）苹果官网感 / 极简高级风

```
目标是做一个具有 Apple 审美倾向的暗色 Liquid Glass 个人主页：克制、纯净、精密、通透、安静、昂贵。

     整体风格要求：
     - 采用 Apple-like Liquid Glass 视觉语言，而不是常规 glassmorphism 模板风
     - 整体基调为深色，但不是死黑；背景应有极深的灰黑、冷调渐变、微弱环境光和柔和景深层次
     - 玻璃质感要像高端系统 UI：通透、轻薄、精致、低噪音、边缘控制严格
     - 所有玻璃面板都要有 subtle blur、柔和高光、极细描边、轻微反射感和精准分层
     - 视觉重点不是炫酷，而是精密、优雅、安静、未来感
     - 避免高饱和 neon、避免复杂纹理、避免夸张发光、避免赛博朋克堆砌
     - 色彩要克制，整体以深灰、冷灰、柔白为主，只允许极少量高质量强调色
     - 强调高级留白、对齐秩序、清晰层级、精致圆角、自然过渡

     设计气质参考：
     - 像 Apple 高级产品发布页面、visionOS / iOS / macOS 某些界面的未来化延展
     - 像一位审美极强的创意技术人士的个人官网
     - 有技术感，但不冷硬；有未来感，但不廉价；有玻璃感，但不花哨

     信息架构要求：
     - Hero 首屏：名字、身份、一句极有辨识度的个人介绍，必须简洁有力
     - About：高度精炼地呈现背景、能力、关注方向
     - Selected Work / Projects：展示最重要项目，重质量、重视觉呈现、重节奏
     - Writing / Notes / Content：如果上下文中有文章或内容输出，做成极简但高级的内容区
     - Links / Contact：社交链接、联系方式、行动入口
     - 页面结构必须自然流动，像经过精心编排的产品叙事，不是模块硬拼接

     视觉细节要求：
     - 导航栏像悬浮在背景上的玻璃层，轻薄、圆润、半透明
     - Hero 区可以加入非常轻微的流动光斑、模糊环境光、柔和渐变，但必须极其克制
     - 各区块容器可采用不同层级的玻璃透明度与模糊度，营造前后景深
     - 卡片不要堆太多，宁可少而精，避免“满屏玻璃卡片”
     - 按钮应有系统级的精致感，像 Apple 的未来界面组件，而不是通用 Web 组件
     - 图文排版要像设计系统产物：干净、均衡、呼吸感强
     - 悬停、过渡、出现动画要非常顺滑、柔和、精确，像原生系统 UI
     - 可以加入轻微视差或层叠感，但必须服务于沉浸感与高级感

     实现要求：
     - 直接输出完整可运行代码
     - 不要留 TODO、placeholder、示意文案、假数据提示
     - 不要只给布局骨架，要给高完成度成品
     - 优先保证整体审美统一、玻璃质感、排版质量、层次控制和细节完整性
     - 页面必须看起来像真实可上线作品，而不是 AI 概念稿
     - 所有内容都基于上下文里的真实信息生成，不要泛化

     最终效果标准：
     打开页面后，第一感受应该是：这像一个带有 Apple 式未来审美的高端个人主页，极度克制、非常高级、信息清晰，而且能明显感受到这个人的品味、专业度和独特气质。
```

大概做出来的样子如下：

你生产的可能跟我的保持不一样，看下你的风格就可以。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ERuDbSuq7oKqj1xClLkccr3vnqe_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=230e7d6c8a1da9986981166c996cd5dbe10601163decf99e014a350bc6f7ccb7&x-oss-signature-version=OSS4-HMAC-SHA256)

2）AI 科技感 / 深色炫酷风

```
目标是做一个真正高级的 futuristic cyberpunk personal
     homepage：强科技感、强视觉识别、强空间层次、强未来感，但仍然精致、可读、可上线。

     核心风格要求：
     - 整体视觉基调为 ultra-dark dark high-tech aesthetic，背景以深黑、冷灰、深蓝紫渐变为主
     - 使用高质量 neon accents，但必须克制，建议以 electric blue、cyan、violet、magenta 作为局部强调色
     - 可以融合 cinematic、futuristic、cyber-minimal、3D web 几种方向
     - 允许使用 layered particles、reactive lights、glow、parallax depth、floating glass panels、smooth scroll animations、subtle grid、data-like micro detAIls
     - 可以加入 WebGL / Three.js / shader-like 背景或 3D 几何主体，但必须服务于整体气质，不能只是技术堆砌
     - 要营造数字空间感、速度感、精密感、能量感，但不能脏乱、不能廉价、不能过度朋克涂鸦化
     - 整体更像高端未来创意技术人物主页，而不是游戏启动页或黑客论坛风

     信息架构要求：
     - Hero 首屏：直接呈现名字、身份、一句极有辨识度的个人介绍，必须有强冲击力
     - About：简洁介绍背景、能力、研究方向、关注领域
     - Selected Work / Projects：突出最重要的作品或项目，强调质量、影响力与独特性
     - Writing / Notes / Content：如果上下文中有写作或内容输出，做成带有科技感的内容模块
     - Experiments / Lab：如果上下文适合，可加入实验性项目或探索模块
     - Links / Contact：社交链接、联系方式、行动入口
     - 页面必须有叙事流动感，像一段未来技术人物的数字名片叙事，而不是模块拼盘

     视觉细节要求：
     - Hero 区要非常强：可使用动态背景、3D 几何体、光晕、粒子、扫描感渐变、深度雾化、远近层次
     - 标题排版要有科技感和气势，但保持高级，不要过度机甲感
     - 可使用玻璃层、半透明 HUD 风格信息层、轻量数据线、细网格、数字化边界、微弱发光描边
     - 项目卡片需要有深度、反射感、微弱 glow、hover 反馈和空间层次
     - 页面滚动过程中可以加入 camera-like movement、parallax、section reveal、reactive transitions
     - 按钮和交互控件要像未来系统界面，但仍然优雅、易读、可用
     - 允许局部使用 glassmorphism，但要偏未来科技质感，而不是 Apple 风

     - 页面必须统一、有秩序、有节奏，避免元素过多导致噪音

     设计参考方向整合：
     - Animated Futuristic Portfolio Landing Page
     - Dark high-tech aesthetic with neon accents
     - Smooth microinteractions and elastic scroll transitions
     - Floating glass panels and modern typography
     - Glow, parallax, and depth
     - 3D aesthetic websites
     - Apple-level UI quality, but translated into a darker futuristic cyberpunk tone
     - Dither + Shaders / WebGL + Three.js if they truly improve the atmosphere
     - Premium frontend presence, not template output

     实现要求：
     - 直接输出完整可运行代码
     - 不要留 TODO、placeholder、示意文案
     - 不要只做结构，要做成高完成度成品
     - 优先保证视觉完成度、未来科技氛围、排版质量、层次感和细节一致性
     - 页面必须看起来像真实可上线作品，而不是 AI 概念稿
     - 内容必须基于上下文中已有的真实信息生成，不要泛化成假大空文案

     最终效果标准：
     页面打开后，第一感受应该是：这是一个未来感极强、科技审美很高级、极具个人辨识度的主页；这个人既有技术实力，也有审美判断，而且他的作品、表达和实验都值得继续深入探索。
```

比如我生成的就如下类似页面

你生产的可能跟我的保持不一样，看下你的风格就可以。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Ggcxb8CHcoav3hxRXAkcl8ItnZe_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=f7d51b621fb488d47e0ccc6439270a72222c879222b5e218c6c6336c0d934e83&x-oss-signature-version=OSS4-HMAC-SHA256)

3）Editorial 杂志感个人主页

```
目标是做一个具有高质量出版物气质的个人主页：克制、知性、安静、精致、有内容密度、有版式审美，像一本被认真设计过的当代杂志或独立出版物网站。

     核心风格要求：
     - 整体视觉方向为 editorial、premium、calm、intellectual、modern
     - 页面应有明显的杂志感与出版物气质，而不是产品官网气质
     - 版式要强调留白、节奏、层级、编排感和阅读体验
     - 视觉上可以使用 soft ivory、warm white、paper-like light gray、graphite、charcoal 等高级中性色
     - 排版建议采用 serif + sans 组合，营造“标题有气质、正文可阅读、细节有编辑感”的效果
     - 允许适度使用引言、编号、小标题、caption、注释、小标签、分栏、目录感结构，但必须克制
     - 整体必须安静、成熟、清晰，不要花哨，不要 startup 风，不要满屏卡片堆叠

     设计气质要求：
     - 像高质量独立杂志、设计年鉴、文化出版物、创作者年报、个人文集主页
     - 更强调内容气质、表达方式和审美判断，而不是营销转化
     - 页面应让人感觉“这个人很有思考、有文字感、有作品判断力”

     信息架构要求：
     - Hero 首屏：直接呈现名字、身份、一句极有辨识度的个人介绍，像杂志封面或卷首语
     - About：像人物简介页，用克制但有力量的方式介绍背景、方向、方法论
     - Selected Work / Projects：像精选案例页，强调代表性和叙事节奏，而不是项目列表堆积
     - Writing / Notes / Essays：如果上下文中有写作、文章、内容输出，必须做成重要模块，呈现出版物感
     - Links / Contact：整合社交链接、联系方式、行动入口，但表达方式保持克制
     - 页面结构要像经过编辑编排的内容流，而不是模块化拼装

     视觉细节要求：
     - 大标题要像杂志封面标题：有气势，但不粗暴
     - 副标题、导语、注释、小标签、分类文字要有明显编辑系统感
     - 可以加入细分隔线、编号系统、边注、日期、期刊感信息层，但必须优雅
     - 图片与文字关系要讲究构图与呼吸感，可以适度出现图文交错、留白包围、局部放大
     - 内容卡片尽量少，用更高级的编排方式替代普通卡片堆叠
     - Hover 与动画要轻微、柔和、安静，像高质量数字出版物，不要科技炫技
     - 如果有项目展示，应更像“编辑精选”而不是“功能模块”
     - 如果有文章列表，应强调标题、摘要、日期、分类、阅读氛围

     内容生成要求：
     - 所有页面内容都基于上下文里的真实信息生成
     - 文案不要泛化、不要空洞、不要套话
     - 语气可以克制、自信、有判断力，但不要夸张营销
     - 如果上下文里有写作或长期输出内容，要把它作为个人气质的一部分来设计，而不是附属模块

     实现要求：
     - 直接输出完整可运行代码
     - 不要留 TODO、placeholder、示意假文案
     - 不要只给布局骨架，要做成高完成度成品
     - 优先保证排版质量、留白控制、阅读节奏、编辑感和整体统一性
     - 页面必须像真实可上线作品，而不是 AI 概念图

     最终效果标准：
     打开页面后，第一感受应该是：这是一个像高质量数字杂志一样的个人主页，这个人有审美、有思考、有表达能力，而且他的作品与文字都值得认真读下去。
```

做出来的风格如下：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ZSgVbBBwxoa1Z6x4XnicDbazn8t_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=91296c99ce4cbee4e359ca0530608998cd683cde5c857d207eaa095e94f5a66f&x-oss-signature-version=OSS4-HMAC-SHA256)

💡

这个方案的好处：直接用用提示词就可以出来一个比较稳定的效果

不好的地方就是：灵活性较差，毕竟能提供完整提示词的不多

有什么灵活性比较好的方式呢？请看下面 借鉴网页风格

3.1.2.3 方法三：借鉴网页风格

这个操作比较灵活，属于你看到什么就可以借鉴什么。

方法也比较简单，就是通过截图发给扣子编程，然后让扣子编程推断出你截图里面的风格，然后让它把这个风格应用或者融合到你当前的这个网站

网站： https://onepagelove.com 。

可以在菜单里面找到 Personal 的菜单，基本就是个人页的模板风格

具体链接如下： https://onepagelove.com/genre/personal

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/JmodbS8Cwo9UMRx0EfWcrEFunCf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=21b853b4844a443225578da5c0bc4b311c7d1545c5de0bf20dfa24e20cc0dc45&x-oss-signature-version=OSS4-HMAC-SHA256)

💡

小技巧：

可以找个滚动截图的工具，滚动截图，就可以截到全部网站风格

比如我找到了案例，地址如下： https://onepagelove.com/akash-tyagi

截图如下：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/H1tQbQtq8oo4c1xhn5eczPWwn4f_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=64bb996635f2da6075337be3aade1c01d0de46e052d4e5b9a830773c10974c46&x-oss-signature-version=OSS4-HMAC-SHA256)

然后把截图直接粘贴到扣子编程上，附带下面的类似提示词就可以

```
识别截图里的UI风格，融合到我的网站里
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/NnXEb67kBoTdkKx1Ipicwrrgnzc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=c334234c24c77ec0e763d56bc02628b25fc98d24022ed0d29f50c4d054f3bf1f&x-oss-signature-version=OSS4-HMAC-SHA256)

做出来网站差不多这样：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/EZ1mblpC5osso5x6dcZc4QHQnlg_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ca58e2ea92ed7ceada314cfa324871d127583a11e55489cf7e794cf584675172&x-oss-signature-version=OSS4-HMAC-SHA256)

💡

这个方案的好处：就是看到你想模仿的网站，随便截图复刻就可以

不好的地方就是：复刻的细节有些是没办法还原的

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ARAFbw8Lkojwvlxh1mRcnTK0nkf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=c1be8f42ad2589b126a339f9a34601fda32f53bfebd5b01679c289480fc23bed&x-oss-signature-version=OSS4-HMAC-SHA256)

当需求、内容、结构、风格、功能范围都聊清楚后，让 Coze 整理成一份需求文档（prd.md）：

```
整理成最终的方案，给我输出成到  docs 目录下的 prd.md 文档。
```

截图比较长，可以看下面，就开始输出 PRD 文档了。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/OOb3bG8X1oz9Q4xyGA9cqXwOnl1_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=e5a9aeb39f79b33775cae07b6d102980f1b9a1fb9d72077e7e1a7b1b3f8fc040&x-oss-signature-version=OSS4-HMAC-SHA256)

生成的 prd 文档可以点击右上角的文件夹图标看到

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/OrEWbZbBKoyq5sxJSJtcmiJunnc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=f2ddb328c19cce4126b46920a3f747896dad759e70a89f3d1bc48131d161cd38&x-oss-signature-version=OSS4-HMAC-SHA256)

输出后，先快速检查有没有明显缺项：主页目标是否清楚、展示内容是否完整、页面结构是否写明、风格方向是否写明、功能范围是否写明、AI 问答是否被放在进阶选做里。

只有确认这份文档把做给谁看、放什么内容、页面怎么排、风格往哪边走、这一版先做到哪里、哪些功能先不做都说实了，才进入下一步。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/CXrybKxrdokboZxa2uqc44Qinob_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=9fe4d66578b4bdd5fb98e2598d167007c9353c2df7fa6d4827532942fa04bb94&x-oss-signature-version=OSS4-HMAC-SHA256)

这一节要完成的是：从需求文档进入正式生成，让 Coze 按 docs/prd.md 做出一个可预览的主页。

需求文档确认后，切换到 Agent 模式。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/SWvYbTApboQihUxmLWHc4XDPnNp_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=faf329fdd2f93b3bfef43362803d65356677c412103354bc58bcf649c100ea12&x-oss-signature-version=OSS4-HMAC-SHA256)

顺延上面 Coze 的对话，“开始”就可以让 Coze 按照需求文档工作：

```
开始
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/CJGxblA3douXF5xFBi6cH3lYnic_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=473836396045a997daeae524fe6ae74b6fba61306ea8d0e9c099d4a894cfc6c3&x-oss-signature-version=OSS4-HMAC-SHA256)

Coze 会开始创建文件、写代码，左侧对话框会持续滚动输出。

等待过程中有几件事要注意：

•

等它跑完再说。边看边插想法，需求很容易被自己改乱。

•

如下图所示，看到 。tsx、.css、Next.js 这类技术名词（其实就是技术栈），当前不需要读懂。 重点是看最终页面效果是否符合需求文档。

拓展信息：

.tsx、.css、Next.js 这些是技术选型，AI 编程还有一个比较重要的需求确认，那就是确认技术选型。

对于非程序员、非技术出身的人来说，这些技术框架肯定是不懂的。比如像截图里面的 。tsx、.css 这些结尾的文件，这都是代码文件。

对于 Coze 编程这个软件来说，它直接帮你固化了这些网页编程的常见框架，也就是你不懂编程，他能给你把这些框架在具体开发的时候补上。

但如果你使用的是一些更通用的编程框架，比如 Claude Code 或者是图形界面的 Cursor 之类的编程工具，在写页面的功能时，它有可能会选用一些其他的框架。

因为网页呈现的形式和最后的实现技术框架有很多种，如果不指定的话，它可能会走偏。

以下是不同应用类型使用的技术框架提示词：（你在使用通用编程框架开发应用的时候可以照着抄）

•

网页端的应用：“需要使用 nextjs、shadcn/ui、TAIlwind”

•

小程序：“就使用官方的 wxml、wxss、wxjs”

•

IOS App：“使用 swift 原生应用开发”

•

需要前后端分离的架构：“后端服务可以使用 go 语言实现”

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/M80JbeoACoQAjsxOT38ccBX2nvb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=d9ea7479ed816bd4b54277cc3cd150e9d4a84fe6565663c724d2e1b747578091&x-oss-signature-version=OSS4-HMAC-SHA256)

页面生成完成后，右侧预览区就能看到效果。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Fi2Vb7crwoCczdxwwDicFsNHnbc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=509c490c3af04f871f9808543f15912ad0ec91a159fd83bb45d0a8373acf5853&x-oss-signature-version=OSS4-HMAC-SHA256)

话说，其实扣子编程默认做出来的网页 UI 样式确实还不错。

并且一次性的功能完成后，页面都能正常显示。

对于很多刚入门的来说，确实会很友好，因为这个，如果你用 Cursor 或者 ClaudeCode/Codex 等工具，可能到不了这个效果。

其实到这里，我的整个开发就已经完成一个小功能了，并且初始化了和我们的页面。

我们可以先看一下整个网站的要求，看符不符合。

先整体看一遍，确认这几件事：

•

页面能不能正常打开和预览

•

大的板块有没有到位：简介、经历、项目、案例、联系方式

•

整体风格是不是朝需求文档定的方向走

•

有没有明显的空白区域或乱码

如果发现问题，先记下来，进入 3.3 再处理。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/HM0QbK9mVo3Io5xbGrXcjIn2nAc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=aaef9d15b21e50700e63621fb1edd76b2742b9ec1d09a3218a7c8b199b771702&x-oss-signature-version=OSS4-HMAC-SHA256)

这一节要完成的是：用新手能操作的方法检查页面、提出修改，并在必要时回退版本。 \*如果你觉得当前需要修改的内容不太明朗，也可以跳到 3.4 补充真实资料 ，完成了资料补充，再来统一修改调优

3.3.1 用截图标注说清楚要改哪里

改页面时最容易踩的坑，是说不清楚位置。比如你想把头像移到左边，如果只发一句头像位置不对，Coze 不一定明白是哪里、往哪改。

更有效的方法是：截图 + 标注 + 提示词。

具体做法：

1.

截一张当前页面的截图（Mac 用 Command+Shift+4，Windows 用 Win+Shift+S）

2.

在截图上用红框或箭头标出要改的位置

3.

把截图粘贴进对话框（Ctrl+V 或 Cmd+V），同时写清楚要怎么改

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/DCwYbCI8GoZuNXxEFTJcDUGPnpc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=4f48dbeb176ab0b557b4bc1299b858fea4512bcbae06d76b8582ae425655524e&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/VtGCbY4XAoglW3xIAo4chLhFnKH_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=78d50f71c48db2daf1e24a079bcb552b3b3d4ee906b973bbfc4634d11b080204&x-oss-signature-version=OSS4-HMAC-SHA256)

示例提示词：

```
如图所示，我想把我的头像按照截图里红色方框和红色箭头标注的位置移动，
然后把我的名字和一些简短的介绍放到头像的右边。
```

3.3.2 判断用 Agent 改还是先回问答讨论

不是所有改动都适合直接让 Agent 执行。

小改动可以直接用 Agent 模式，比如：

•

调整某个元素的位置

•

修改一段文字

•

换一个按钮文案

复杂改动建议先切回问答模式，把方案讨论清楚再执行，比如：

•

改整个页面的布局结构

•

新增一个板块或功能

•

改了两三次还没成功的问题

切回问答模式的好处是：先把方案说清楚，确认可行后再切 Agent 执行，减少来回返工。

3.3.3 右侧工具栏的四个实用操作

不同尺寸显示

点击预览区顶部的尺寸按钮，切换桌面端、平板端、手机端的显示效果。个人主页很可能被别人在手机上打开，建议每改完一轮都切一次手机端确认。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/WWHlbThnDoOxlMxrZjycrSEunPg_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=812487640ecf6b8aecc4e9b1cea33ed840e9045d3f11c565184ddb774a8a3f3c&x-oss-signature-version=OSS4-HMAC-SHA256)

刷新

页面样式一时没有更新，或者预览显示有点异常，先刷新试一下。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/QJUJbYsWiocoY2x4LvKceRQRnfc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=349a45ba56b46724706f2050fe9accc8d89bb06c69800f153351d0b8d18a20fd&x-oss-signature-version=OSS4-HMAC-SHA256)

重启

刷新没用时，可以尝试重启服务。适合页面完全不响应、或者做了比较大的修改之后。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PJflb2JgAopu2Fx1llqcI7n2nac_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=a5b3c63730aadecbee0e703c4965e30aba1acfd43b1874c45a3dfd69b6a1c886&x-oss-signature-version=OSS4-HMAC-SHA256)

版本控制

这是四个操作里最重要的，但新手经常不知道在哪里找到它。

点击右侧区域右上角的新标签页按钮，在打开的页面里进入版本控制。每条记录包括：改了哪些文件、这次改动做了什么。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Qs1obq6tsoX3rrxiHNvcje8insZ_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=4c238f0634d19e8a50049d2e58b86e42d8db3dc04d2b9d20bd551801bd93cf58&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Soc5bW0p7oKIPVx5ElhcMtd9nkd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=21a8af7f5a8acffbb4b1cd277a84320e3dbde8a7d776a2c5540411e2693a3d23&x-oss-signature-version=OSS4-HMAC-SHA256)

你看到的版本号和文件列表和别人的不一样，这是正常的。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/XpNWbU62woHz9Bxa6MPccKXYnDh_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=d459b8cfcf9a29536618e7f1318a2363fca6448170bce63b5178cd36b9aab8dc&x-oss-signature-version=OSS4-HMAC-SHA256)

如果越改越乱，或者改完发现不如上一版，来这里找到想回退的版本，直接回退。

把版本控制理解成打游戏时的存档，改错了就不用怕。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/UmDPbMISJoKsbux56a1cQPzQnRd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=38687d4947e2e230b564e1e74b7e2c1c0c89879229fe571b67ca9a2133b83be9&x-oss-signature-version=OSS4-HMAC-SHA256)

3.4 第四步：补充真实资料

这一节要完成的是：把前面页面里的占位内容替换成真实资料，让它从练习页变成你的个人主页。前面的页面里，很多内容可能还是占位符。这很正常，一开始不要求准备完整资料，是为了先跑通流程。

现在页面结构有了，再补资料会更轻松。

提前准备好一组个人介绍 Markdown 文件统一喂给 Coze，比一条一条手动改省事得多。

名词解释：

Markdown 文件就是文件后缀以 。md 结尾的文本文件，你可以理解成就是一个特殊的 。txt 文件，只不过比如 # 这些特殊符号会显示为一级标题这种。有不懂的，可以找豆包问一下，就会很清楚了。

可以准备这五个文件：

```
01-about-me.md    个人简介、工作经历、目前在做什么
02-skills.md      技能专长，可以按方向分类列出
03-projects.md    项目作品集，每个项目写标题、背景、做了什么、结果
04-cases.md       航海案例集，每个案例写航海案例名称、做的作品简介
05-faq.md         常见问题，比如怎么联系你、能合作什么
```

如果暂时没有完整的真实资料，可以先让豆包或其他 AI 工具帮你生成一版模拟内容，先把流程跑通，后面再替换成真实信息。

当然，如果你不想自己去生成，也可以直接用我下面的。先让扣子编程给我们把真实的信息占位上，你后面想要修改的时候，直接在对话框里面跟他说直接修改哪些信息。[01-about-me.md](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/JLNibB2B9oLmiux81CXceMkynRb?response-content-disposition=attachment%3B%20filename%3D%2201-about-me.md%22&x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=2e790605b0d4f6afd819e8c582640a412fafb731dff3ccf1dc9c9f0462835786&x-oss-signature-version=OSS4-HMAC-SHA256)[02-skills.md](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/SwcvbZGMzocDLpxxmP9cLVzPnFg?response-content-disposition=attachment%3B%20filename%3D%2202-skills.md%22&x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=e9ea611ac7b5b86508a5b98df5f11d888b129deefa0cec8dc040ca47a9013a39&x-oss-signature-version=OSS4-HMAC-SHA256)[03-projects.md](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/BOokbnaimoEU2DxbY7BcqiiDnFb?response-content-disposition=attachment%3B%20filename%3D%2203-projects.md%22&x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=fc8e2cb2492abc96addd723cc12c5e17bf64492f0c1986db24b03b9b972dacc4&x-oss-signature-version=OSS4-HMAC-SHA256)[04-blog-react-performance.md](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/N3j6b8xWsoIbc1xana4c5dtPn7g?response-content-disposition=attachment%3B%20filename%3D%2204-blog-react-performance.md%22&x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=31004fc9d5766b43095cc7909c8a2acbe3ae46411b4c6435b1ac63875acaf94b&x-oss-signature-version=OSS4-HMAC-SHA256)[05-faq.md](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ACrcbvugNozcTzxTAvacluRLnLd?response-content-disposition=attachment%3B%20filename%3D%2205-faq.md%22&x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=dfccfcadf2d6bdc07d00b0a9847b3a7da0895809450bdc7295b1948c82b6704d&x-oss-signature-version=OSS4-HMAC-SHA256)

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Co0tbvsXZo6xytxn6SIcMJWwnGe_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=42c7204135e55bf7337252730bca55f207e1a0051272cfc594967f31775e8037&x-oss-signature-version=OSS4-HMAC-SHA256)

3.4.2 上传文件，让 Coze 替换占位内容

文件准备好之后，把这些 Markdown 文件粘贴到扣子编程的对话框，然后告诉它：

```
这是我的一些个人信息，还有项目信息，帮我整理补齐到网站上，让网站显示真实的数据。
```

这一步用 Agent 模式就可以，目标明确，不需要重新讨论需求。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/KkVHbIMNloPRENxPKKAcSah4nmh_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=9a5187bf93fd2ca97dc1bcc0e6cb68c9592ab0ef00ebf2c94050e9aad238a456&x-oss-signature-version=OSS4-HMAC-SHA256)

等 Coze 跑完，检查一遍主要内容有没有正确替换进来：名字、简介、经历、项目、案例、联系方式。

下面是一些详细的扣子编程的思考的过程。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Rq63bgJcuovkVLxnSrSc35xqnQc_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=26282bb1926b0e06ac205009f302a08164a954ac9dc04638ae0b14dadcbb46c1&x-oss-signature-version=OSS4-HMAC-SHA256)

这个就是最后呈现的页面，发现名字还有介绍都已经改成我们实际的信息了。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/WYGxbra67ouA6YxSOL8cChOMn8d_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ffc561152bcc610e850023634e4d40e7e40d2d09ee8cd5749fab9d2e85427e11&x-oss-signature-version=OSS4-HMAC-SHA256)

3.4.3 补充视频和图片素材

如果你有视频案例，也可以在这里一起上传。

直接把视频从电脑里复制，粘贴进对话框（Ctrl+V 或 Cmd+V），再告诉 Coze 把它放到哪个板块：

```
这是我的两个航海案例集的视频，帮我补充在网页里面。
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ZzIGbwAkaoESBCxAStrcSsvlnTn_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=e6254c1979744ca3dafe131eee924d6e753d0cc7e97963a6d513a401b4b06afb&x-oss-signature-version=OSS4-HMAC-SHA256)

这里有个限制要知道：单个文件不能超过 20MB。如果视频太大，先压缩一下，或者先用一个小文件测试流程能不能跑通。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/VpOYbCbrropVyDxU60VcN9RQnMe_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=c0d5ccece01919f962b6175e273588f94779828e38ddf18a1bece6ef20d17633&x-oss-signature-version=OSS4-HMAC-SHA256)

修改完后，左边的扣子编程对话框和右边的预览页面，如下图所示

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/WtDRbcdkBoYqvrxGVPpcQ4tXn1G_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=1a02938057eec81a4f96ca8ee483a2843830c9bd77f70567bbce4496b30d718d&x-oss-signature-version=OSS4-HMAC-SHA256)

点击播放，可以测试一下视频能否正常播放。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/DbwKbN0QforVyUxDYfvc3ZMSnMg_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=1b584fbf36ffa472b49b742f3ceaecd3267e01de92c608eaf160d9cec713b0d1&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/BZUKb4TM8oQticxHV1Uc20vnn0c_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=255350dfdfe91a142fec372d719ebe82e33f4278f82666f049f5b0680a5462b8&x-oss-signature-version=OSS4-HMAC-SHA256)

3.5 第五步：接入 AI 问答（进阶）

这一节是进阶功能，不是基础必做。只做基础主页的话，可以跳过这一节。如果你想继续升级，可以往下看。

3.5.1 先搞清楚这个功能是用来做什么的

这个功能的定位是：让别人围绕你的资料提问，不是通用聊天机器人。比如：你做过哪些项目？你擅长什么？你有哪些航海案例？怎么联系你？

这个功能有啥用呢？

•

进来的人，觉得网页介绍太长不想看，就可以和机器人对话，精准了解关注的信息

•

我们有什么数据不方便在网页上展示的，可以让访客通过对话机器人去沟通，用暗号触发某类资料

问答范围要收窄：只回答与你的资料、项目、经历相关的问题，其他话题不回答。这一点在方案讨论阶段就要说清楚。

3.5.2 先讨论方案，再执行

这是一个相对复杂的功能，不建议直接开 Agent。先切回问答模式：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/W6e9bWXrookM3Tx5BrTcKUnRnc5_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=cc26ef6ccf14314400bbc9b88239925d85dfe5f455ce8e8ee38cc38cc1a3ffa6&x-oss-signature-version=OSS4-HMAC-SHA256)

```
我现在想在整个网站上面加一个机器人问答知识库，整个知识库的内容就使用我之前上传的 markdown 文档内容，帮我想一下如何设计好。
```

具体的详细对话记录如下，截图比较长，大家可以往下多翻一点。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/PV7NbqfZcoyTFyxb5LJc0Avfn7c_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=715a10fe56e3bb582f38bf9ecf3843e25c3545144cf45250ade26a7f59d124e8&x-oss-signature-version=OSS4-HMAC-SHA256)

讨论方案时，重点确认三件事：

•

问答内容是不是只围绕你自己的资料

•

问答入口放在哪里（悬浮按钮、独立板块，还是都有）

•

第一版以简单可用为目标，不用追求大而全

方案确认后，切回 Agent 模式：

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/ZmDtbTESwoNkE9xUcPecpVxsn7c_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=0ef9b6ae95812b0caacee9aa06b04042b111aa0e515e4aabfc3f90174b41b140&x-oss-signature-version=OSS4-HMAC-SHA256)

顺延 coze 的给出的方案，很简单的一个起始词，扣子编程就可以开始干活了。

```
可以帮我实现。
```

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/URUtbpKokopB20xe9ERcaPpKn5d_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=b6595cca329712956c08e580794ec06695721b31c1b56425e8185b21d4fc31ea&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Fc3UbYnzooGKTbx0BTHcXhConnf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=347b12fbde3fbc18655e69aeb229323df909ec41f9b748d265917fe36928daea&x-oss-signature-version=OSS4-HMAC-SHA256) ![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/YJhkbtejIo7SC3xMZe1cSIIQnUe_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=c55cafb0fb793a5ee82396ead983169c89e2fa0cffb3c5388a06d57ccbababd4&x-oss-signature-version=OSS4-HMAC-SHA256)

做好后，先测试，测试通过了以后再展示给别人。

我们发现右边整个页面中间有一个问答系统，且右下角有一个快捷悬浮的问答系统，样式基本符合预期。

接下来测试一下，回答的内容是不是符合我们的真实数据。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/F974bA6pjoLjZyxqhb1cURYsnDd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=bc6f6722c75dce800a8e16b8ddb0d89a5255ba977df2558c5b981a7eb223c7a3&x-oss-signature-version=OSS4-HMAC-SHA256)

测几个只有你的资料里才有答案的问题，看它是不是在基于资料回答：

•

你做过哪些项目

•

你有哪些航海案例

•

你擅长什么

•

怎么联系你

如果回答泛泛，或者出现明显胡说，先回到问答模式，告诉 Coze 问题出在哪里，让它调整范围和资料匹配方式。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/I8GXbB0dpo8dQkxuDMJcn5TUnud_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=d85902b2242806458f80d230a54905ad66ff4dd6dcbecfaa3d1e6187cacc4df7&x-oss-signature-version=OSS4-HMAC-SHA256)

如果测试下来基本符合真实数据，就可以先上线一个版本。不追求一步到位。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/NDqEblGDEomhYPx3AzRcBugRnQf_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=edc98dc117c0c91a59aa7bbf6e170eaf3f8816938692d0a79a824db5f1273e5e&x-oss-signature-version=OSS4-HMAC-SHA256)

这一节要完成的是：把主页从预览状态发布成一个别人可以访问的链接，并做上线前自查。

3.6.1 点击部署，等待完成

点击 Coze 编程右上角的部署按钮，进入部署流程。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Pxn9bItVMoDJitxCLMCcFdJrnXb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=ac534ef6a96ed72c0565a2b67555444910d7eb585df7c75b60076859f30731d3&x-oss-signature-version=OSS4-HMAC-SHA256)

部署完成后，你会拿到一个可以访问的链接。

关于域名：不需要一开始就购买。Coze 提供的临时链接已经可以正常访问，先用它跑完整个案例。

如果你以后确定要长期使用，再考虑购买自己的域名。国内域名通常需要备案，备案流程比较长。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/YDp9bu4Ebo5CFGxhWqTcvVpInUT_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=03c5c3a78dd199e302a97978ca7695d8a985cfeab172fbf80bab98ba0d0d7c33&x-oss-signature-version=OSS4-HMAC-SHA256)

部署通常会经历三个阶段，等待完成就好，不需要手动干预。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/MxoYb9I2SoOKpQxfpKYcT8nanAd_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=e70d38f6e86f600d1eb5382cc5556264e77393739f444ae82a9c5b2837693093&x-oss-signature-version=OSS4-HMAC-SHA256)

如果部署完成以后，就会出现下面的类似的按钮，点击这个链接就可以。

这里把我的链接贴出来，大家可以参考一下这个网站。

https://nrmqk62rjz.coze.site/

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/Lta7bUuRjoDqrfxaaRocyn5wnbb_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=4692b7bf7fe768c9cf09a26da30303ed39b0a51221030dc7532359a5d7204d21&x-oss-signature-version=OSS4-HMAC-SHA256)

拿到链接后，先自己检查一遍再发。有些问题在预览区里不会出现，发布后才能看到。

逐项过一遍：

•

页面能不能正常打开

•

手机端能不能正常浏览（用手机打开链接试一下）

•

各板块的资料显示是否正确，有没有还是占位符的地方

•

视频能不能正常播放

•

如果加了 AI 问答，测几个问题看回答是否准确

•

联系方式有没有写错

如果发现问题，回到 Coze 修改后重新部署，再检查一遍。

自查没有问题后，就可以把链接发给别人看了。

到这里，你已经做出了一个可以公开访问的个人主页。不需要等到完美再发，先发出去拿第一轮反馈，之后随时可以继续迭代。

![](https://sphere-sh.oss-cn-shanghai.aliyuncs.com/private/docx/drive/media/EKnNbX1Rbo3a31x2bcUcogmtnJK_hhkc?x-oss-credential=LTAI5tDANFnEjK2qWnHwZKzr%2F20260507%2Fcn-shanghai%2Foss%2Faliyun_v4_request&x-oss-date=20260507T180422Z&x-oss-expires=86400&x-oss-signature=8aa97b2cd34c012f4afe17f544f9ae805a2de23b36646af91f4dfadd8c75606b&x-oss-signature-version=OSS4-HMAC-SHA256)

💡

布置一个小作业：

参考上面的案例讲解，制作一个属于你的个人介绍主页。

提交形式：在航海群的作业表单，上传你的主页链接