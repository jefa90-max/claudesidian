  

大家好，我是钱塘江鲤，感谢七天邀请，今天我想从技术实践的角度，聊聊我这半年来的真实工作状态，我是如何使用AI的以及我用AI赚到了哪些钱。

  

如果只觉得AI就是个聊天助手，问问题那就真的暴殄天物了，当你真把它当成生产力工具后，你会发现世界完全不一样，我觉得现在一天能干完过去一周的活，一个人能搞定过去一个团队的事，这可能有些夸张，但是是我最真实的感受。

  

  

下面是我主要使用AI的几个场景

  

## 一 AI编程场景

  

编程是我使用AI最核心的场景，我的主力工具只有三个：Claude Code、Codex、Augment Code。

### Claude Code：全栈程序员

  

我给Claude Code的定位是从0-1的开拓型员工，我只管提出需求，它负责从0到1填平所有技术细节。

  

大概是五六月份左右，在cc没有发布subagent而且还没有spec概念的时候，我写了一个autoCC的自动化框架，实现了类似subagent和spec工作流的核心流程，每天我的工作就是写需求文档和todo list，它会自动写代码、编译、测试、运行，当时的cc还是不限流不限速的，基本上替我饱和式地搞定绝大部分基础功能的开发。

  

另外还有一个点，不要把Claude Code只当成编程工具。它更是一个通用的Agent框架，通过Claude Code 的 SDK调用，你可以将它的超强执行力嵌入任何工作流，其易用和可控性远超Coze、n8n等平台。

  

cc基本就是我的首席技术官，沟通成本为零，执行力100%。

  

### Codex

  

当然，Claude Code也不是万能的。当遇到它反复无法修复的后端逻辑Bug时，Codex就登场了。我通常会将cc三轮解决不了的问题抛给Codex。它会花个把小时进行慢思考，然后给出一份直击要点的完整解决方案，尤其是gpt5-codex-high。它的定位是找Bug和定位问题在我眼里是当之无愧的No.1。

我的体感是，Claude Code快，擅长前端和0到1；Codex慢，精于后端和复杂Bug定位。 两者结合，解决了项目中99%的问题。快慢搭配，干活不累。

  

### ChatGPT Pro：极致细节和疑难杂症解决

  

剩下1% cc 和 Codex 都解决不了的问题怎么办？直接交给GPT5 Pro。

  

比如我在做Reddit Agent时，要模拟人类自然滑动，细节非常多。通过ChatGPT Pro，半天左右就把这个流程细节和边界情况考虑的非常清楚并且完美实现。

  

虽然Claude和Codex也能做，但是边界情况错误百出，GPT5 Pro对细节和边界的考虑更全面，三四个提示词就能搞定，而且一个复杂问题它可能要思考半小时，对细节的周密考虑远超其他模型。

  

强烈推荐在强推理环节、方案设计环节用GPT5 Pro。

  

### Augment Code

  

除了cc 和 Codex ，我常用的编程工具还有Augment

  

对于基于大型开源项目的二次开发，Augment Code是我的首选，它上下文处理和长任务和复杂项目的稳定性更高。

  

比如我要基于某个开源项目修改，直接github地址扔给他需求文档扔给他，交给他去验证和修改，它就会clone下来后按照文档运行测试然后新增功能，过一会回来验收就好了，在这方面横向比对过cc 和 Codex，它是最稳定的。

  

### CodeRabbit

  

AI编程时代，AI一天能给你写一两万行代码，所以Review机制非常关键。

  

我用的是CodeRabbit。它的Review机制基本上覆盖了所有场景。你的同事写完代码合并时，只要发PR，你就能看到修改和建议。

  

他们也可以在本地CodeRabbit进行第一遍Review。这个工具能极大提高合并时候bug的检出率。

  

使用形式类型如下，pr的时候CodeRabbit会总结分析所有变动，并且给出建议，按需判断修改就OK，用起来几乎无侵入性。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjc5ZDM1YWQ1YmYwMDFiMzEzMGQ2NmU3YWU1ZTZmYmZfeG9qcWFlUDhPdWR2THAyc1hGdWVlazFGV1Q2TnVUaXVfVG9rZW46SFFHd2JqQ0RFb1VGbW54eWtGV2NaZUhTblVoXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MjFmYTliMzRkMDJjZTY5YTI0N2IwY2YxMzAzMjhmNjNfODJwZFN4dzhNUDlreTVQZ3BGRXI4M1RBdzExYmlMR29fVG9rZW46Q1NMY2IwVHE4b0VyRW54V3dLUGNTQkFZblNiXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

### AI编程帮我做了哪些事

  

上面说了我常用的几个AI编程工具，那我用这些工具都做了什么呢，下面从数据采集、自动化运营、自有产品开发、客户交付几个方面展开。

  

#### 数据采集

  

用Claude Code做数据采集，真的是又快又好

  

举个例子，去年十二月的时候写过一篇 https://scys.com/articleDetail/xq_topic/5121541548888524 三天采集了三四十万条YouTube的AI视频，总结了1万个对标频道。

  

但在今年6月，我用Claude Code从一个空文件夹开始，1小时内就完成了一个全新的采集工具，当时效率是每小时十万条。经过几轮迭代优化，现在单机并发每小时能采集近1000万条视频，单机吞吐量峰值超过3400视频/秒

  

过程是这样的，年中的时候因为cc用的越来越顺手，于是我就想试下，从0开始实现下YouTube的数据采集，因为在去年的时候使用cursor没有完成这件事，最终还是我手敲的脚本，半年后的AI的能力又怎么样呢。

  

结果就是如下，在1个小时的时间完全通过对话的方式，从0使用Claude Code写了一个YouTube采集器，当时是一小时十万条，记得很开心还和朋友分享了下

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NWZiYTlmOTg1YmY1ZWZkOGE2ZTdiZTMwNjJkMTk0NzBfNGo0UUgxcEY0SFZCZm5YSjVvZDdJUFNjMkZnUFV5M05fVG9rZW46UnhGU2JENGVYb2R6WGx4Z3VXcmN3Qkd1blliXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjhkODczOTIyNGIyYjdjNzZlZjIwZjFkZTY3YWMwMWNfNmRlWEdvcHA0UGF1RTJqYndOMzlWRGtpVEtDRVJTRGJfVG9rZW46TVQ0U2JTTHFOb3JRMmV4OHRzTWNyOGFUbllHXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

随后接下来的又找了一些时间进行优化**一小时一千万条**了，真正的低成本高数据量采集，单机并发每小时实现一万多个关键词将近一千万条视频的采集，吞吐最高超过了3400/秒，平均每个关键词超过了825个视频。总累计时间不超过两天的时间，我基本就做好了一个每天可以采集几亿条数据的爬虫，放在以前完全不敢想象。

  

同样的方式，我在Twitter上也监控了一万个AI和AI图片/视频博主，过去一年的时间共监控了他们1300万条推文然后进行~~洗稿~~创作，平均每天也会增长一万到三万条左右的新增推文，再加上cc每天定时总结和定时推送（还记得一开始提到的cc sdk吗，cc+skill无敌工作流，不想标题党，但真的降维打击了传统的工作流)，基本上已经解决了选题和最新的AI资讯问题。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NmExNWRhOGIwMzkyMTJjZDM2MjE0NTI4MzA0Yzg5MzZfVFdTdnRkUHo1ZW5ieUIxVkxIWkR5V1BvbjFiTGp5djlfVG9rZW46QkhvVmI1ZW9Kb0N4bHB4R1VtSmNmYmdubjJkXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

其他平台也是类似。比如Reddit同步采集了十几T的数据，基本上把Reddit全站数据全部采集下来了，国内也实现了某书的数据采集。我记得在去年8月份分享过使用RPA加影刀采集商品的帖子，地址是：https://scys.com/articleDetail/xq_topic/5122858455558114，但是一年后使用Claude Code重写了一遍，写工具的效率提高了N倍，采集的效率也提高了N倍。

  

这可能就是生产力的跃迁吧，所以说我一直觉得这每月几千块的AI税是我交过的最值的投资，他带给我的价值早已经是百倍了。

  

其实Claude Code的能力还绝不止于此，很多人还没意识到，它是有大规模生产能力的。

  

#### 账号矩阵运营：全自动化的1000+账号

  

以上是使用cc实现数据采集的实践，实际上还是用CC做了很多类似的工具

  

比如我用Claude Code写了一个Agent，管理了上千个账号，从账号注册，到批量设置人设关联账号，自动评论等多种不同场景的深度的AI介入，从指纹浏览器调度，到批量账号注册，养号，内容生产，到自动发布，都可以随时人介入调整，也可以AI agent进行自动化操作，帮我高效稳定地管理了一千加的跨平台账号矩阵。

  

目前正在加人设关联和图文/视频内容产出，我的目标是打造一个完全由AI驱动的IP MCN，产出不同人设不同风格的多模态内容。

  

当然背后还有许多看不到的功能，但是这么一个相对来说复杂而且解决了我问大问题的一个agent，基本上是完全依赖cc + codex，在其他项目并行的情况下，不到两周的时间就做完了，所以AI coding现在的生产力水平深不见底。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWEyZWJiMDliM2VhZGJjMjAzYjBiMWNmOTk2OGVhYjVfM1dzRU9PYXlJZHh2VGh1bzZYSDVnUWNpM2wxTllPbHpfVG9rZW46UkJOZ2J1TnJQb0UxeUR4aFRQamNUZTlMbkljXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MmU4MDFjYTcxNTc3OGVkNjc0YjcyZTUxOTM0NjQ1MWRfelhSWm5teEZLaWswZVo5VEsyWVlwSEFFSFN5eFRwZFFfVG9rZW46RFVpRGJuQ3Jyb3RVRmx4OHRvcmNzcUZ5bkVkXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

#### 常用的AI Agent框架：企业级智能体的构建

  

上面说了一些数据获取和运营场景，企业交付场景下，在AI Agent场景，我主要用了两个框架 autogen、langgraph，最常用的是langgraph。

  

当然去年也是用Coze、Dify、n8n 、Rpa交付客户。我在24年大概做了一年的RPA和Coze等工作流，也交付了大概120多个工作流，但是后面踩了很多坑，今年年初逐步变成了纯原生实现，不再使用coze或者RPA等低代码平台交付工作流，客户更关注的是功能和稳定性。

  

比如使用langgraph，它基本提供了一套完整的状态机编排能力，能够清晰地定义智能体的决策流程。配合langsmith，整个Agent的运行轨迹状态变化和决策依据都有完整的可观测性，这对B端交付很重要，langgraph的天花板很高，从简单的线性流程到复杂的多Agent协作，都能很优雅地实现。

  

在交付过程中，还涉及到的一些为客户构建行业知识库，清洗行业内的数据、政策更新，生成报告。脏活用cc+特定的pipeline，交付用langgraph，整个流程非常清晰，可调试性也强，有些是和客户的业务场景关联的，就不展开了。

  

强烈建议如果有比较稳定的工作流程，又有AI在其中起决策作用，一定要试下这几个agent框架。

  

以上就是使用cc的一些场景，今年使用cc做的项目已经交付了多个企业级智能体，基本单价在6-30万之间。上半年的时候也使用cc做过很多小的工作室定制，比如论文写作、直播复盘、商品分析、TikTok数据回收、视频自动化工作流、电商产品自动上架等等多到记不过来，大多数定制单都在1万以上，其中论文和tt数据回收几个项目极低成本标准化之后还额外收入了十几万。

  

在没有Claude Code之前，这样的效率和产出规模是完全不可想象的，过去一个人最多同时推进2个项目，现在可以并行处理5-6个项目。关键不在于写代码更快了，而是从需求理解架构设计到落地实现的整个链路都被压缩了。

  

## 二 内容创作与运营

  

上面是AI编程场景，另外在内容创作场景，我的主力AI工具是Cherry Studio + Obsidian。

  

为什么用Cherry Studio？因为它可以让多个模型同时输出。我一般用三家：Gemini 2.5 Pro、Claude 4.5和GPT-5，我希望快速横向对比，让不同模型针对同一个提示词输出不同内容，然后我来选择。

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NGVkM2MwMzUxOWEzNjJiOTIyZGQ1ZmJmYzY0YmFjNWZfdWhnR3ZEeTN5Y095Zk80bTN6Vm40alZiZTAxc3dVU3RfVG9rZW46TVFYQmJpOGxsb2wxazF4bEs4RGM0MXZMbm5jXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

Cherry studio 也支持自定义提示词，比如我有不同的创作场景：网文、朋友圈、公众号。每个场景有不同的提示词，我只要做成智能体然后就可以新建了，它可以同步生成。

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MTI5NjkxNGY4ZWY5N2E5YTg1MGJmOTAzNjYwNzE0MTRfNWgyWTZneEdrYXFBR3U2WDhQTGJubE1tajFRajBlN3FfVG9rZW46RlFCbWI2bWNKbzhuUTB4RjFIaWNRbTJQbkRiXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

生成的文章可以一键导出到obsidian中

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MDdlZjQ1MDFjZjYwM2M1OGZmYWQ2MjNjOTg5ZTZmNjNfNnJtekhzV2FyM0JiOTFWdk9nbGM0MDdZT3BDSDdFR0pfVG9rZW46SXcyNmJxNTc5bzJDRk94ZWNLemNMSEtjbkljXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

生成之后，我就一键保存到Obsidian。

  

### 从Obsidian直接发布到不同平台

  

你没看错，从Obsidian可以直接发布到公众号，而且可以自动采集、裁剪，发布到小红书。整个链路非常短。这个插件就是我基于开源项目加Claude Code不超过三个提示词完成的，可以直接将我的文章发布到公众号。

  

针对公众号批量创作场景，我还写了一个自动化创作Agent。当然也是基于Claude Code做的。这个小agent的设计我特别喜欢，很精巧，是基于Claude Code SDK加Subagent做的。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MTU1MjFlNjBmYWQ2MzMxMTU3MGU3M2Q3NzA1ZDRkMTRfSGVyTW53WVVSUkhnbk9mbXFPVHBFeFJOTjdkOUNJODVfVG9rZW46UFN3QmJyNG12b3ZIa1Z4d1h3U2NuSEx6bjZiXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NzAyMzNjYmFhZWYyOTAxMWQ3ZmE3ZDNkOTc2MDcxNDlfeHFwUjIxb2FVeGtGTjN5WUFFc3VodnVLNEZaOU9KTDNfVG9rZW46SEtxYWJLWXNnb2RwcmV4Y214MGNFTnlEblpjXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

这些agent 可以然我把海外Reddit等不同平台的优质内容二次创作，然后自动发布。

  

因为Obsidian是支持数据库的，所有内容都能结构化管理，看起来非常清晰。

  

### Smart Composer 加速内容创作的加速

  

另外，Obsidian还有个神器 Smart Composer。

  

它可以借助MCP工具，直接从零开始创作。我使用cc自己封装了一个MCP，可以支持把任何社媒链接比如Twitter 小红书等直接给它，它就会解析内容，然后按照预定的提示词模板重写，算是单篇文章轻量级地对cc的补充，改写完成了直接点击发布就好了，obsidian扩展性很好，有需求直接让cc做个插件就好了，基于自己的需求，我让cc写了大概十几个插件满足不同场景的发布和内容审核需求。

  

### 海外账号运营

  

推特运营方面，我用XAI Creator xaicreator.com 基本上管理了我的海外账号的在线运营。最近还在尝试Thread和Instagram的起号，有好的结果了和大家同步。

  

## 三、微信自动化工作流

  

自动化这块我做得比较多了。之前也做过微信的影刀微信自动化，但是因为风控原因，还是废了几个微信号，后来实在没办法转到了飞书一阵，但是始终没有微信方便。

  

后来从生财官方号获取到了灵感，比如下图左边，生财有术服务号会根据情况给我推送提醒，那我自己申请个服务号，设置好规则，让他给我推送每日提醒和设置不就行了嘛，而且服务号是支持对话的，也就是说不管我给他发了什么，他都可以作为一个入口，后台对应分发不同的agent就可以了。

  

比如我发了什么链接，后台的工作流都可以实现自动解析，然后入库处理，最后给我返回一个通知，直接让我审阅一下就行，也可以一键调起来小红书，或者把文章审阅后点击下发布到多平台，很方便。

  

另外后台也可以接一个agent，帮我处理任何不同的任务，包括前一日的热点，甚至是生财筛选内容的推送，平台发布规划，日程安排等等，这样基本上平替了大部分的微信机器人的功能。

  

效率提升N倍吧，基本上借助企业号我把所有基于微信生态的自动化常见需求都自己打通了。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NGEwY2NjMjNmYWQ4YWI1NTVmYWVmNmYwNWZkMjJjMTdfR1o5NUQ3ejl2dFFXc1dzSDJsTElJSXI5ZU91bEpGaG5fVG9rZW46VGlRZ2IwOTI5b0hvM0d4VnhUa2NSSzczbmRlXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWI3OTc2MTg2OWZlODMyMTViNDc3MzkxNjBhY2QxMjlfZERNUlRDUTJwVWRkV1FKQzNoQ01kdnl5NXZXZ2hxcHZfVG9rZW46Wmg3RmJkYjVxb0Q1ZzZ4b0VTcWNINHpmbkVjXzE3NjkwNjE0NDU6MTc2OTA2NTA0NV9WNA)

  

另外还要cue下cc,这个项目是cc + codex一起做的。还是老样子，一行代码没写。

  

回顾到这，我认真想了想，我最近至少已经三个多月手写代码行数不超过100行。真正意义上的开局一个空文件夹，直接让AI实现整个项目。

  

## 四：PPT生成

  

虽然都吐槽PPT，但在分享场景和工作场景，PPT还是必须的。

  

我主要用四个工具：Gamma PPT、Genspark、天工、coze空间。

  

为了PPT，还单独开通了genspark 和 gamma的会员，很好用

  

平时用法是同一个主题，同时发给所有这些网站。哪一个对我的思路启发更大？哪一个样式、布局、设计最符合我的要求？我就用哪一个。

  

## 五 AI生图

  

即梦的生图能力基本上是最强的，尤其是即梦4.0。另外还有就是Nanobanana，视频这块主要是ComfyUI的工作流，comfy的可玩性很强，建议大家有多媒体内容生成需求的话一定要玩转comfyUI。

  

最后，我想分享这一切背后最重要的核心：**养成AI First的习惯，所有的问题我都会找不同的AI同时确定一遍。**

  

以编程为例，现在遇到问题，我的第一反应是：Claude Code解决不了，就找Codex；Codex解决不了，就问GPT-5 Pro。**如果连Pro都解决不了，那大概率不是AI不行，而是我的提问方式或解决问题的方向错了。** 它成为了我判断技术路径可行性的锚点。

  

它都解决不了，说明我的方向错了，就不要浪费时间，赶紧换一种方式实现。

  

从工具到员工的认知转变

  

我的角色定位其实很简单。我只是个会提需求、会引导AI的人。但正因为这样，我才发现了Claude Code的真正价值：它不是工具，而是员工。你把它当工具，它就只能写写代码。你把它当员工，它就能帮你干一整套流程。

  

所以我也很期待看到大家都是怎么用Claude Code或者其他AI工具的，有哪些让你回不去的使用体验。