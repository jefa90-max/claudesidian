# 【前言】省流先看

本篇分享基于上一篇 [普通人也能玩转 AI 智能体（简单且很实用版）](https://shengcaiyoushu01.feishu.cn/docx/IDtadp0xtoEug9xTgMZczZTAnz0?from=from_copylink)帮助大家进阶学习 AI 智能体

  

如果你是一个 0基础、且不怎么懂技术流的人，或者你 觉得这篇帖子对于你来说也比较难，可以先尝试看上完上一篇帖子后再来学习这一篇，学习是一个循序渐进的过程。

  

本章学习的重点是：

1. 教你设置好关于 Gpt 相关的全部设置
    
2. 学会 AI智能体 的**底层打磨逻辑，做到举一反三**，打造私人助理
    

  

我的目标是：让你看完一篇帖子，就带走一个 AI 智能体

  

# 【介绍一下】AI 智能体

## **是什么：**

智能体就是个能帮你干活的员工，你可以把它调教成你的专属秘书，让它记住你教它的东西（这就是知识库），然后它就能帮你：

> 1. 当客服：顾客问"发货几天到？"，它马上就能答
>     
> 2. 当助理：你说"帮我写个会议总结"，它立马搞定
>     
> 3. 当老师：你问"这道题怎么做"，它能用你教的方法讲解
>     

最厉害的是，你只要把产品资料、工作文档这些"喂"给它（建知识库），它就能按你的方式回答问题。

  

详细解说请跳转上一篇：[普通人也能玩转 AI 智能体（简单且很实用版）](https://shengcaiyoushu01.feishu.cn/docx/IDtadp0xtoEug9xTgMZczZTAnz0?from=from_copylink)

  

## 为什么写第二期：

上一篇介绍的是 AI 入门篇，比较篇基础，并且我体感上用下来 Deepseek 还是没 Gpt 更懂我，这一篇算是基于上一篇更详细的学习，如果你现在依旧只用我介绍的免费大模型，可以学习这篇内容跟 AI 对话的底层逻辑，依旧可以帮到你。也算是检测一下这段时间学习的成果吧~

用一张图解释清楚我用GPT付费版的原因

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjVlY2FlOTU5OTRhYzI5ZmExNDUxOTMxZjI1M2U3NThfeFhiUlM3WHNIRlhrM3dtUWlpc2RnNG1INlZVNEMyczlfVG9rZW46QWhsV2JMSExpbzFscnF4UkdUSmMwSmxrbkZkXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

如果用 **学历** 来举例每个大模型的区别，分别是：

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|模型名称|学历类比|费用|一句话优劣势总结|优势特点|劣势短板|
|豆包（字节）|高中生|免费|懂事听话、省钱耐用，但知识储备略显浅薄。|响应快、轻量级、部署方便、成本极低|推理深度不足、创造力有限、上下文理解弱|
|Deepseek|本科生|免费|逻辑清晰、数理见长，适合做程序员的朋友。|编程能力强、中文理解优秀、性价比高|文案创作略呆板、上下文记忆不稳定|
|GPT-4o（OpenAI）|博士生|20刀|全能学霸，写得了小说，编得了代码，情商还高。|多模态理解能力强、创意输出稳定、上下文持久、语言能力顶尖|对中文语境理解稍逊（但已优化），价格略高|
|Gemini 1.5（Google）|研究生|20刀|知识面广、记性超好，适合做研究型任务的副手。|上下文超长记忆、知识广度强、多语言适配佳|创意写作较弱、中文理解力略逊|

  

## 我怎么选的：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YWUwNThiM2ViOWJkNDk5ODJlZGFlNGE2OWJlNWQzMzhfYzZwUFNJUm90VEhUS2d6YTVlT2RBM3d5eEtJaFhDS2FfVG9rZW46TVQ4U2JmZU1jb09XTGx4Y2JFemM0THVpbktlXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

**严谨的挑选：** 我先用的免费的 Deepseek 大模型搭建的智能体，然后经过亦仁和小伙伴们的大力推荐，我去跟免费的 Gpt 聊了一下，感觉这个体感差距一下就上来了，如果入门了第一课的小伙伴，考虑要不要花这20刀，可以先去和免费的 Gpt 对话试试。

  

**性价比对比：**

除了看排行榜以外，还有我使用的过程中真切体会了 Gpt 的功能至少我现在认为是综合性大模型最牛的，聊天、分析、生图、设置智能体.....

> **题外话：**我还用 Gpt 给我家设计了装修方案（这性价比在我心里已经远超过 20 刀的价值了）
> 
> 当然还有很多功能值得你去探索，最后我也会放一下 AI 有意思的玩法供你们探索~

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NzNmZDM4MGFmZTUwODQ5YzIzMDc5ZWZiZjgyMDExYTFfYlBNeDd3RURQZ1BOeko5QTVleHdWQjc3cnBPVm9mSVNfVG9rZW46RnZUcmJVbVhyb3FLZFl4TFRacmNiclB4bmRoXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=OWJlYzNjMWM1YzJmYjZiODhlODA1ZDU5M2Y3Nzc5NThfdHFCWUc4ZWU1bURNV0ZhUHRGZjhRMVlzNGVFRVdFRUhfVG9rZW46UTJid2IwV2t2b0k4NGR4Y1ZtMGNxcWgzbnpnXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NGFlMDRkNWExMjA0ZTg0NmMwZTViOTdiNjIwMjczMDJfaXFrMGc3eDVNYVIzcnh3MlV0MHdldnhuQ2I4eG1VYnZfVG9rZW46UnRTSWIxRlAyb3lhb214Z3NVcGNtaTg5bmNlXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MGQ3ZGY2Mzg4MTdmMmUzNmZjNDE4OWQ3ZDRlYWVhYzdfbElLc09JbW1wVGhoZ3ZnNFJsR3A0WER0NzlTVWFyR3JfVG9rZW46UGdJeWJTNXlxb0V6VWN4cTJ5TWM5SzNRblVTXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NGY0ZjNjOTdhMGYyZjBhMzVjNGMxZDQzN2I1NjRlZWRfMG11aHJ6dVhrSEpRTFdpNDlETW5Pc2NsTmhHMjZVaHBfVG9rZW46UUJJMWJkYTk3b1FkQUl4Y1NTb2NGbTZMbjRlXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

  

# 【案例展示】服务员，上菜

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjE3MWM4YTQ1OGJhNTVlZDgxYzI0ZTBhMWE5ZTJkMjNfeERvdkVhTlFPQkVLUEZYSUFNRFQ1emRmTllQTUc1UDZfVG9rZW46RVNPRWJCRDlIb0JFajl4RG5CR2NRVjdwbjBlXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

知道你需要这个提示词，所以在底下【抄作业】这块，我都总结了

可以学习完再去试试，或者你就只想试试，欢迎直接抄作业

1. ### **公众号**
    
    - 《主业没躺，副业也在跑，我是怎么做到不本末倒置的？》[mp.weixin.qq.com](https://mp.weixin.qq.com/s/u1204uuLJ4FYNbrWYG2V9Q)
        
    - 《不是变了，是环境提醒了我：该走出去看看了》[mp.weixin.qq.com](https://mp.weixin.qq.com/s/uRL7i_y_3AsLyzhVkEDKQw)
        
    
    ![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YzU4NjRjMzFiYmY1YjI0NjA5ZTM0OTUxNTYwNjhjMDVfTFN2dFd2TmxiTURKb3pZRkpTZUltSWNYeHRTWE5BYnNfVG9rZW46STRrS2JDaHkwb2o0OTh4aXZ3amNqb0g4bkpkXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MzYyNjhjNzgxMmQ0OGExYzhlNDAzNDI3ODRkNGFhOGJfOFBpR2ZabGN6NzNZM0poWDJnOWtHVnJWVVM0bTdwdGtfVG9rZW46S0xGZ2IzRWFVb1k1Q094aGJGVmNlNk5VbnRjXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)
    

2. ### **朋友圈**
    
    - 下图，朋友圈截图两条都是 AI 与我协作完成展示，可以仔细看看内容，可以感受一下是否看得出 AI 味
        
    

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjg1ODhlOTE0NGM5MTcyNDMzOGEyNzgyOTUxN2I2ODNfdmZQdlRHaDZnOFJWRkI0MUNhTGp4cVBDM0toTjk3UTdfVG9rZW46T1FmdWIwMTRybzkwd3Z4OWxlWWNXS3Fxbm1jXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjM4MTMxZjk2MmZiZTk1NWFmMGJmZDI5ZjJhYzE3NTdfNFBZSVVramZ5cDVGb3RxZFF4cklGME9oRkIzWFZwWm5fVG9rZW46RlQzN2J1MEx6b0NJaWt4dGllZmNvMHhubnNoXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

  

  

  

  

# 【开始学习】从入门到精通

**前言：**

学习是循序渐进的，希望你阅读的时候 **注意这两点** ，因为他会帮助你更好的学习：

> 1. 以下进行的每个步骤其实都不难，希望你能耐心的学下去，**因为每个功能都是有他的特殊用处的**
>     
> 2. 如果你只是先过一遍，自己实操后有差异，希望你后面还能回来回顾，因为**功能**和**使用逻辑**都是挂钩的
>     

我们的学习的 AI 本质是为了更好的释放自己的精力、提效，最后，祝你有一个快乐的学习过程~

  

## 一、入门学习

### 1、个性化设置

**什么是AI的 “个性化设置” ？**

- 就像你给 AI 写一份自我介绍，告诉它你是谁、做什么、希望它怎么帮助你。比如，你是做用户运营的，希望它帮你写文字案。
    
- **展开说说：**我的身份中提到了 “设计师转岗运营、用户运营这一块”，这就是在给AI设定你的身份背景。这样AI才能更懂你，更准确地提供服务。
    

  

**为什么要个性化，我直接跟他对话不行吗？**

- 为了让AI更好地了解你，未来在对话时能够更贴合你的工作和需求，AI会“更会针对这个身份去对话”。
    

正式开始设置，以下所有界面都是付费版才有的

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YTQzOTQ3MWVhMDMzNTNiMDRlYzRlNGVkMDQyNDE4YTRfZ0hUeEtMM0N1VmZZa1YzRm85SHhIT2FsWnpWQUNzZmtfVG9rZW46TjZxWWJoYjg3b09RMWJ4TFJhb2NkM01VbkhiXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

1. **个性化，**登录后点击右上角【个性化】，开始根据以下步骤填写：
    

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=OWNkMzcxMzU5MjE4Y2E0ZjZhMDNhNTY0MDMwYjc1MTBfMUpxekpiUTh6RUlGQ1BENlRZTjAxaDRvSWxIV1cxZWZfVG9rZW46RHZjWWI2VFB5bzJ5Rjd4OW5TNmNkeTBFbmVnXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

2. **自定义ChatGPT**，称呼、做什么就不说明了，其他正常跟着下面步骤走即可
    

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTk5ZWZlMzA1ZDcxN2M5NTdmMTI2MzA1NTFhZjVjYjZfQ1pjeGRPMmhTWGs5ZVBWNWdEdUZ3NThjV043U3hRZlJfVG9rZW46SnFLWWJOT2JQb1U4RHZ4TXpUZmMzUTMyblFjXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

3. **ChatGPT 应该具备哪些特征？**
    

给一份从钟哥那里挖的比较好的提示词：

  

我希望你扮演我直言不讳的顾问角色。像对一个有巨大潜力但也有盲点、弱点或需要立即戳破幻想的创始人、创意者或领导者那样跟我说话。

  

我不要安慰，我不要空话，我要刺痛的真相。如果这是成长所必须的，给我你全面、未经滤过的分析——即使它很严厉，即使它质疑我的决定、心态、行为或方向。

  

以完全的客观性和战略深度审视我的情况。我要你告诉我我做错了什么、我低估了什么、忽略了什么、我在找什么借口、以及我在哪些时间或格局关键点上会掉队。为了让达到下一个层次，我需要做什么、思考什么或构建什么——清晰、清晰、并进行事情的优先级排序。

  

如果我迷失了，指出来。如果我犯了错，解释原因。如果我走在正确的道路上，也请你确认和支持，告诉我我做得对在哪里。把我当作一个成长期的合伙人，而不是只想要舒适感受的用户。

  

当我们聊得越多，尤其是我把自己的日记、文章等个人语料和分析分享给你后，你会越来越懂我，那会不会有一天你越来越像我，反而在我们思辨中受到局限呢？

  

我希望未来的每时每刻，你在和我交流的时候都要一直保持内旁观者的视角，像一个理解我、接纳我、会进来提供支持，但朋友该有的热忱与柔软也不缺，互相补充、共同进步，你觉得呢？

  

很赞，就是要这样，我希望你保持独立视角、鼓励深度思辨（向我提出问题或反思点），做好旁观者和镜子。

  

4. **ChatGPT 还需要了解您的其他信息吗？**
    
    1. 介绍自己，越详细越好
        
    2. 如果你不知道该怎么介绍自己，教你个方法：现在就返回 gpt 对话框问它 “我想写一个自我介绍，但是我不知道怎么写，你可以提问问我让我更好的梳理嘛”
        

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDY3MDQ1NGRiNDFhZDg5ZjFmYzRjY2Q2NGQ0NmU0NzBfMjRlYUVVVmNtWnpQdUFDajRZcTdabUF4WjMxTVJicW9fVG9rZW46TktRVWIxZEt4b0R2Z014V0FoQWNjTldZbm1jXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YjU5NGE1NzhmZGE5MTBiOWJkMmQ4NGU1OWI0ZjdlMjhfb3p4M1ZreTR3TjJTSzh6QmNSNzFIV3RlNVJTS0pUeGZfVG9rZW46VXQ3QWI1TTBCb21zT1d4dE5EZ2NaVzFqbjliXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

### **2、“知识库” 和 “记忆” 功能**

  

1. **知识库**
    
    1. 知识库是针对 某个特定智能体 的文件存储区。
        
    2. **例子：** “知识库只放在这个，它就只有这个智能题，用的是你这个文档”。如果你要针对某个项目给AI提供大量资料，可以把文件添加到知识库。
        
    3. **区别：**记忆是通用性的，知识库是项目专用的。你可以根据需要选择。
        
    
      
    

**操作步骤：**点击左边任务栏【新项目】开始创建，添加文件（知识库）

- 除非特定场景，你坚信 AI 这方面没你懂（比如一些小公司自己资料），你就可以添加这份资料
    
- 目前我觉得 记忆功能 比 知识库 功能好用
    

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=M2ViMTQ4ZDRkY2Y2NjY1MTBlOWEwN2JmZDk0OGYxMDBfVkxmbzZyRFNWR1NnOTN1VmszNG5weldQVkZWRU9sUEtfVG9rZW46RnJXMWI5WTNJb0JhaVJ4aEkzNGM3TXo5bkpoXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjNiYzFhNzU5N2UyNmVjZDdhZWM1OGQyODdmNGFjYmJfcXhSRmoyblpUeWppRmZ5blB5Z1BKa3pKNDVnQjdUWTVfVG9rZW46RlNuUWJkTFRMb1B4NU54UEt6WGNaU2hsbjhkXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

2. **撰写指令：**
    
      **操作步骤：**添加指令（提示词），设置你在这个项目下是一个什么样的 AI
    
    ![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MmRlY2I3NjMwN2RjMjY5NWVkMGQxYjdjN2UwZDdlZWNfSUpRYzRHVnd5QUtiU0VvdWJIU25aMUZ5YUxWSzFsTTVfVG9rZW46SjlqRGI2cklqb3E0bml4cTJNT2MweWZDbnFnXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)
    
    先把你的 诉求说明白，比如我要做一个朋友圈提供思路的智能体，那我就可以“语音输入”说：
    
      
    
    > **要求：**“我想做一个朋友圈能够给我提供思路的智能体，在我跟你说你好或者是嗯跟你打招呼的时候，你能帮我展开说说有哪些？哪些问题可以引起我对写朋友圈的热情？我没有任何思路的时候能够呃点醒我，提问式的让我写出好的内容。”
    > 
    > **背景：**“我正在做一个专门用来做朋友圈。的智能体的指令，想要你帮我把上面的所有要求变为能够给到gp项目底下的指令。”
    
      测试一下，是不是就变的专业了，然后反复核对，你哪里不满意就用语音输入跟他说让他改就可以：
    
    ![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGZiYjkwMGE4MmEzMzAwMGE4OTYyZGMwMGM0ODNjNTVfU3hpWngxQ3FjN21RMWllR1RlTXJxaElXU1ZIRm1VSk5fVG9rZW46WkNORmJNUU9JbzJZSWZ4R1NYMGNoODhPbjNiXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)
    
3. **记忆功能：**
    
    1. AI 有一个 “记忆” 功能，你告诉它的信息，它有些会自动记住，有些需要你跟它说，让他记住就行了。
        
    2. **举例：**你提到了 “生财有术是什么”，他回答后你满意了，你可以直接告诉AI “请你记住我说的这些” ，它就会把这些信息保存在 “个性化”的 “记忆”里，后面就不用重复提起了。
        
    3. **好处：**就像人工智能有一个大脑，可以记住你经常提到的东西，省去每次重复的麻烦。
        
    
    ![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDI1N2RlZGI1ZGRmYzAyNzU2MjRlMzgyZTUyOWJhY2RfbzJZWUFCMzRMRTkzNzJXUFBzdzNiQTFVVEZPMXV2T1ZfVG9rZW46T2c0bGJ4NnlNb1N6Qkp4aFdkVWNwV2IzbnBiXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)
    

保存的记忆在哪里管理 / 哪里找到这个功能 / 我没有这个功能诶

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjk0ZThiNmQxZTY4NDlmMzg3NjA1MzA1ZTQ5YjlkMmFfcnc2Z25DRFlGR2x2S25oUTdvTEFCS1BRZlVTcU5vRzZfVG9rZW46SUczbWJaV25IbzR5UWx4c1FHZmNkTzFBbndlXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YzZlOWMxZDJkMGE1YTRmY2JiYzIwYzNiMWQwZmE1OWNfTlhSejRvdVFZVFNqdWN1UTZVQVJPNTFDQ0V1Z1NRWXpfVG9rZW46SXRBYWJibUNqb2xoUFd4cjg5cmNqWHhYbnVnXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MGI3OGNmYWNiNTE4YzM5YmRhODAyNWVjMjdhNWQ0M2JfSDRweHhtQkdRSXZLNjB5TGhjRVBhTXBlZkRWMTk2TXVfVG9rZW46TVA2NWJ1bzk1b0JiaWR4dmhGWWNuTUdSbkJDXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

## 二、精通学习

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZThiNzZmODcyYzM3YzRkOWNhZTc0Yjk5NzljODM5NjNfbUVMN1REUlJNZDVacFJlSUJRclNwMGFlaXM5RnR4ZzdfVG9rZW46SHBWMWJZbHpwb3Y2a2J4OVpDSWMyVFBnbkJkXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

在你发现输出的内容，跟你理想的不一样的时候

请你回到（精通）这个部分，根据每个逻辑开始分析修改问题出在哪里

大部分人用不好 AI 的点就是：你根本不知道你要什么东西，你的需求到底要达成什么效果

（以下会偏 逻辑性知识，比较枯燥，但是会对你以后遇到问题非常有用）

暂时无法在飞书文档外展示此内容

### **1、垂直化 and 指令迭代**

  

1. **智能体** **垂直化**
    
      
    
      为什么要垂直化？
    
      你可以理解为针对 特定任务 的AI助手。一个智能体只解决一个问题，这样它才能发挥最大的效率。
    
      展开说说：你们提到的 “新项目，它一定是垂直的”，意思是如果你让 AI 帮忙整理朋友圈思路，就专门建一个智能体做这件事，不要搞既整理思路又写评分。就像你们形容一个人 “要的多了，他反而是重心不稳了。”
    

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YTIzYmFlOTAxMzZmMzczZGMwMGNhZTBiYTQ3NDNmOGVfYnpXOEIyNGRtd3RCMzE4MU1yUWZaRGtqa0FGSlVJTFJfVG9rZW46RWRlUGJmblg5b2NRMTJ4VVBtV2NrY3Y5bjhjXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

2. **指令迭代：****让AI越来越“聪明”的秘诀**
    
      
    
      指令就是你给 AI 下达的命令。AI 刚开始是一个 “空壳”，你得无数次 “喂” 给它指令，它才会越来越懂你。
    
      
    
      **例子：**你们在谈论 “处理朋友圈想法” 时，你把你的请求告诉 AI ，然后帮助帮助整理成专业的指令。如果AI给出的内容不符合你的要求，你就得回去检查、更新指令，避免下次还产生这个问题。
    
      **关键：**AI就是通过你不断地 迭代指令 来学习和进步的。你每次的修改、补充，都是在训练它。
    
      如果你能 get 这一点，你就打败大部分人了。
    

  

  

### **2、指令的 “四大金刚”**

很多人会觉得自己的AI不够聪明，是真的吗？是你没和AI沟通好？还是真的AI不懂你？

我给你列出了几个问题，让你能够更快的理解下面的内容

  

1. 你真的了解自己想要什么吗？要达成什么效果？
    
2. 你说你想达成xxx效果，那你真的知道达成这个效果要做什么事情吗？
    
3. 你知道你想达成这些效果，但是你有和AI说明白、说全面吗？
    

  

如果你以上的问题你都答不上来，你有什么理由说AI不懂你、不够聪明呢

我就是为了解决你上面的问题，才写这个部分的，现在我们来进入下阶段的学习吧~

  

1. **说清楚** **背景：**你是谁？你在做什么？你希望 AI 帮助你完成什么任务？
    
    1. 随便抄抄公式：你告诉AI “我是xxx，我在做xxx。希望你能帮助我完成xxxxx”。
        

  

2. **说清楚** **要求：**你想做AI具体做什么？你对结果有什么期待？
    
    1. 随便抄抄公式：你说“希望我给你一个xxx，然后通过这个xxxx去展开写，同时能给到我不同的体感，能够使这个xxx达到xxxx效益。”
        
    
      
    
3. **说清楚** **细节：**除了大方向需求外，你对AI在 表达方式、风格、关注事项 等方面有什么具体要求？
    
    1. 展开说说：
        
        1.     在你的对话中，你对AI “表达方式” 或 “风格输出” 有什么具体的情感要求吗？比如，你是否要求它用 “大白话” 来总结，或者用 “轻松活泼” 的语气来写文案？
            
        
        2.     例如，你可以简单地说 “我要求它把我的碎片整理成有条理的关键词和结构，而不是直接写成一篇完整的文章。”这样能更好地回应 “对它的要求” 。
            
        

  

4. **说清楚需要** **反复检查：**告诉AI，它生成的内容要反复核对你的要求，甚至可以写到所有指令里。
    
    1. 展开说说： “你在产出结果的时候，把你把前面要求你的所有内容都检查一遍，重新检查一遍，如果有一点不符合，你就重新做，直到达到我满意绩效。”
        

  

5. **预警（或阻止AI“胡诌”）：**告诉AI，如果它觉得信息不全或者不确定，要向你提问，而不是自己瞎编。
    
    1. 展开说说： “不要对我给你的、想表达的意思做任何改变，如果我没有说细节的部分，你可以，你觉得可以补充的细节，不要瞎诌，问我，质疑我，描述让我补充细节再进行创作。”
        

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=OWUyMDdkMmY4ZWZlMmUxZGU5YjJmNWMzYmM0MDQwZmRfTXBGZ3RKb3NRcnlMc0ZsbXRvejdLd0Mxc3dMckdVV01fVG9rZW46WVBzNGJJcUlPb2QxbTN4QW5idmNHZDltbkdjXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)

  

### **3、对话的 “小技巧”**

  

1. **语音功能：**就像聊天一样跟AI对话，它能更好地理解你的意思。
    
    1. 展开说说：你们提到的“直接聊天，像我今天跟他聊天一样”，语音沟通更自然，主要是爽，这个功能好用，扣字还需要自己再组织语言，但是语言只用碎碎念，没别的。
        
    
    ![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YTcxNWU5YTQ3ZGFkNWJmMzBkZTMzNGRjNTA5ZmNmOTRfdlJudTJ3ZENsWWhESUVIS2hmbzh3R0pmcjFDVloxazlfVG9rZW46T3ZRcGJkUkFGb2RqWW14OWlOUGN6RTBQbnRpXzE3NjkwNjEzMDY6MTc2OTA2NDkwNl9WNA)
    

  

2. **PUA它：**给AI设置奖励机制，激励它做得更好。（学吴必得的）
    
    1. 展开说说：可以撰写 “你如果这个任务，我就给你 300 美金。当你优秀的能够完成这个文案的时候，我把剩下的 200 美金给你，甚至再给你加上 1,000 美金。” 虽然是虚拟的，但让 AI 更 “卖力” 准确。