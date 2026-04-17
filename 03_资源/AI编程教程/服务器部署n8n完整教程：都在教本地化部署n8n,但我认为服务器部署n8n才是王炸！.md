最近看到好多人在推n8n,我找了一圈，关于如何在服务器上部署n8n居然没有多少教程，害我一顿鼓捣！

## **为什么一定要服务器部署？**

在我看来，n8n这种神器，一定要将它做成服务化，才能发挥出它最大的能力。

当然了，作为工作流工具，部署本地，已经可以为我们处理很多事情了。但有些能力，就必须将n8n公网化。

比如说n8n中的一个核心节点 Webhook，就必须将n8n配置成公网可访问。

  

**那么，什么是WebHook？为什么我觉得这个很重要？**

不要看它名字洋气，我给大家举个通俗的例子就懂了，比如说我是一个特别厉害的程序员（n8n），擅长使用编程和工具为大家解决问题。

如果是本地部署的情况，大概就是，你必须亲自找到我，比如我在福州，你得来福州。（打开自己的电脑，点进n8n）。然后下达需求任务，让我完成指定的任务（执行工作流）。或者找到我之后，告诉我以后我每天要做哪些事（定时触发）。

  

**但是！不是每个任务都是固定的**，有些任务可能是要根据实际情况做调整的。比如，每天要写的文章？要做的报告？主题可能是根据实际情况变化的。 于是聪明的我（n8n）就给你们留了微信或者电话号码（webhook）。现在，你有任务，就没有必要亲自来找我了（打开电脑里的n8n）。你只需要发个微信或打电话给我，说要做什么任务就可以了。无论你在北京还是上海（无论在不在电脑前），我都可以为你们服务了。这样，**你就拥有一个24小时不停歇的员工了**。

  

## **然而！webhook的能力远远不止这些**

现在网络上，总是喜欢把coze、dify、n8n进行横向比较，进行n选1。但是一个成熟的成年人，从来不做选择...。

为什么要做选择呢？**我觉得每个工具都有自己的强项，完全可以强强结合嘛**，比如说n8n擅长灵活搭建工作流，那么我们可以把主要任务都丢给n8n。而Coze的AI相关工具和插件生态比较好，那我们就让Coze来处理就好了。

**举个例子：**

比如说我有一套AI提取小红书生成AI视频的工作流，很多插件依赖于coze生态，那就不要非要想着用n8n重新搞一套呀。而n8n有一套自动化分析和发布的流程。用coze可能不好实现。那么**webhook就派上用场了，我们在coze工作流里配置上n8n的webhook，通过webhook把生成好的视频提交给 n8n。让n8n完成后续的工作，一套自动生成和自动发布的功能不就搞定了吗？**

  

除此之外，如果我们有其他业务系统，特别是企业！将业务流程跟n8n进行打通就很需要webhook，比如用户下单之后，触发n8n进行发货操作？ 或者客服系统接收到某些关键词可以调用n8n设定好的工作流？等等。

看大家实际的业务场景去设计。总之，我觉得把n8n部署成公网服务，可以打通很多链路，实现更多更强的自动化。

  

**如果你看懂了我上面说的，你就会明白，n8n部署到服务器的重要性了**（PS：本地部署通过内网穿透和ddns等技术手段也可以做成域名访问哈，这种邪修路径，暂时不讨论，哈哈）

那么废话不多说，回到今天的主题：

## 如何给我们的服务器部署一个n8n,并配置上域名实现公网访问？

### 1、心理准备

嗯... 你没看错，就是心理准备，很多小白，一听到服务器、域名什么的，就会有畏难情绪，总觉得这是一个很难的事...

我只能说，你们是对的！！ 肯定不是容易的事，但自从有了AI，很多事情的门槛，已经不足以拦住我们小白了。

大家一定要相信，只要你想学，想做，借着AI的能力，都有办法做成的。

### 2、环境准备

首先，**就是要有服务器**，现在各大服务器厂商一般都有活动，新用户买服务器挺便宜的，比如说n8n的建议配置2核4G的服务器，腾讯云这个三年才五百多，大家可以自己去其他厂商对比哈，我只是举例不做推荐：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=N2FiZGZkM2NiZGM0NGFkYmE3YmJmZTY3NjE4YTdhNzlfb21YM3U3dmJJUHNuZ3V1UUVCNU1JalhtYkJkelFWQVJfVG9rZW46WEYxRGJ2SlZFbzhzd2J4bXJKOGN4NHBSbmRsXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

还有就是**备案好的域名**。（这两个对于小白来说，又将是一个卡点，但这方面的教程，也满大街都是，基本摸索一下都能搞定，这里不做细讲）

服务器和域名准备好之后，接下来需要安装一下宝塔面板，大家可以到宝塔官网获取详细的教程

https://docs.bt.cn/10.0/getting-started/quick-installation-of-bt-panel

### 3、新手必备！github加速神器

很多好东西在github上一搜都有，但是很多新手小白，常常在访问github这一步都会卡住，因为后续有很多地方需要用到github。

**所以！今天我给大家推荐一款免费神器 Watt Toolkit** https://steampp.net/

这是一个主要用来加速访问steam的，但神奇的是它也能帮我们解决github访问问题。

我们进入这个官网，然后下载客户端安装

接着打开客户端，找到网络加速，然后记得勾选github，最后点击一键加速。再次访问github，基本github地址就都可以访问了。我实测过公司电脑和家里电脑，都没有问题，但不保证所有网络都可以，实在不行只能魔法。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MDgyYjYyMmRiNzJlM2U0ZDUxOGI4ZDY0MjUxZjI5YWJfV2hxTGpuaExxVnc3OHRWbjhhYW1ESDJmbXhuUFFaRE5fVG9rZW46UnpDUmJoc0Rmb3pKWXp4ZkFubmM0MmlSbm9nXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

### 4、docker部署n8n

使用docker部署是最方便快捷的方式了，而如果安装了“宝塔面板”又可以省去安装docker本身的麻烦了。

首先，我们打开n8n官网 https://github.com/n8n-io/n8n

可以找到n8n的快速部署命令

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NThiNzcwNDExYTk1NDZhMDA4NDIwMTBhYTIwZjAwOTdfcFBvOWNIOEo1VGN6azdSZURVTUxEUWljNU9yV3ViUmxfVG9rZW46U2JjVGJjWkZ6b2MyOGV4Y3o2UGN3QmFzbjNjXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

接着我们进入我们服务器的宝塔面板中，找到终端，首先执行一下这个命令：

```Plain
docker volume create n8n_data
```

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YTMwN2QzMTc4NmZmNzBmNDdmYzk3Yjk2MTM1Y2MxMTRfOXNFN09ZS09HS2FlRmdxdXFpT0hWZjZOTGdZeHdLendfVG9rZW46SUdGWmJaRFlOb1E0S2V4ZTVPeWNkZ1lVblFlXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

接着我们进入docker的容器选项里，找到创建容器，然后使用以下命令填入创建容器：

```Plain
docker run -i --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

这里注意我们在docker run 后面少了一个参数‘t’ ，这是正确用法，不要加上，会报错。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NzBiZTAyNmQ4MWViZjExYmMwMTE0NGI2ODA3MjA0ZjNfVllWN3Z2YUxEQmlBOTRTMUpkbDJxczc3TTV1bjkydTRfVG9rZW46QWlhV2JXT0hYb25yUkF4TUF4a2NFam9zbmllXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

如果你的**网络环境有神奇的魔法**，容器就会创建成功。但是一般情况下，是无法成功的，因为docker镜像网站，国内无法访问，以前通过设置镜像源可以解决一部分问题，但是n8n 这个即使设置了也还无法使用我们会看到以下报错：

Unable to find image 'docker.n8n.io/n8nio/n8n:latest' locally

docker: Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).

See 'docker run --help'.

要怎么办呢？这个时候需要给我们的服务器上魔法，这里我说个关键字：clash for linux；大家去github上搜索一下就懂了

### 5、设置docker代理

当我们给服务器上了魔法之后，由于docker run的方式不会直接使用魔法代理。因此我们还需配置一下。

我们在终端执行这个命令：

```Plain
sudo vi /etc/systemd/system/docker.service.d/http-proxy.conf
```

  

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MzJmNzRjMjhkOGU1MTIxOTc3NGQwNTc2M2NiMGM3ZWVfN2MzeTJ5VHQ3RUliYlVnZzJ3TGdEaUFka1BGQ2p6bzFfVG9rZW46Q3NqS2JJZndkbzUxRHh4TVpNcmNPMElGbkVjXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

然后在打开的文件中输入以下内容，记得改成你自己的代理地址

```Plain
[Service]
Environment="HTTP_PROXY=http://your-proxy-address:port"
Environment="HTTPS_PROXY=http://your-proxy-address:port"
```

进入编辑器之后，按“i”键进行内容编辑，如图所示，这是我的配置，一般情况下你如果用的是我推荐的clash for linux，默认就是这个配置了，填写好之后，按“esc”键，然后输入wq文件就保存了：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzg3ZDljYmMzN2RlMzhlMWNiZjBmZjVkZTBjZTIwY2JfdEd0Rm52T1M3Q2pzNThnUmdIbXVGUjFwblBpZjNySGdfVG9rZW46WEcwd2IyRDFkb1VhZGh4UUdocWNKSk5ubk9mXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

文件保存之后，还要依次在终端执行以下两个命令，这样代理就配置好了：

```Plain
sudo systemctl daemon-reload
sudo systemctl restart docker
```

接下来，我们重新执行前面docker的部署操作，看到以下日志，说明容器已经创建成功。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmE5YjlkNDM2YTg2ZTU5NDVhYTAwNjFhYmVkYTNlZDNfQ0tpbDFXQUtjQnJxdmFTSmRoMzVIRXYxTFZhdzJ4NjZfVG9rZW46QjBSemJMT1FVb3A0a1h4NHo2VGNEUWVSbmNmXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

### 6、配置http访问

我们如果是本地部署，正常到这里就可以直接用了，直接访问http://localhost:5678就可以了。但是我们需要做成公网可以访问，就还需要给它配置一下域名了，否则我们无法通过这个域名访问n8n。

按照如下图示，找到网站，点击创建，选择反代容器，然后容器选择我们前面创建好的容器n8n,分配个域名给我们的n8n;点击确认。就可以通过这个域名访问n8n了（域名需要提前解析到服务器，这个在买域名和备案过程中，是需要去了解和学习的）

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MmZhMWU4ZjEzODBhZTY1NzYxMDcyMjYxODFiMGM3MTFfSWR0dmREUUtURWdDWVRhYktOSjRwQ3YxZjhLY3JaSzhfVG9rZW46Wnh5ZmJ4NDV1b042OGh4VGN4Q2NmU2oybnJlXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

### 7、配置https证书（ssl证书）

为什么还需要https证书？因为n8n的安全限制，我们使用前面的http地址来访问比如我的 http://n8n.****.com，会出现如下问题：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjIyZmVhZTdiZjZlOTNmMzBlNzY5MGYxMTAyYThhNGRfQTJ1OHphVFlRbjJnUU9XMW5vdUFSaWI3YkV0ZldlbUJfVG9rZW46T0M4bGJiQmJyb28zWjB4S2ZWeGM3Zzl5bjVnXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

所以为了能够成功访问，我们还需要给http配置一下ssl证书，让它支持https访问。还是点击网站，找到我们刚刚加的网站，找到ssl证书这里，正常这个地方是未部署状态，我这里的已经部署过了，显示了证书的有效期。直接点击这个地方。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NWJmMmVlZWZkMjI3NWQyYzk0MzVlZmEwYmI5NzdhNWNfWnRBcE1TSmZQcFREaVBOenFmM1ltU25PNnZibjdDZWVfVG9rZW46VHYzemI2dUlyb1VFY0l4bXM1YWNRa1Nobk1iXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

然后在弹出的页面中选择Let's Encrypt （这个证书是免费的），接着点击申请证书，勾选我们的域名，点击申请证书，等待配置完成就可以了

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YjE2ZjI5NmMyNjNhZGU0MDdkNmM0MThiMmNkY2JmMzVfdUc4ckNUUUxrNDlLeUN2Sm9qMEVRdVZHQTZZQTB0blZfVG9rZW46QjVQRGJ2cFBYb0N2UTR4M1pVc2NQR2NubjFiXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

再次访问我们的域名，记住一定要使用 **https://** 加你的域名访问，成功啦

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MmQzM2JiNTlhMDE0ZWY2YWYzOWJmYTQ2ZTE2OTMyNWVfSk16OEpCTmJ4a2tKcHI2U2NSdGtzNVFMR3FRRzQzWU9fVG9rZW46SjhTVGJiTGNXb3pRVml4TE1xNGNManpsblJmXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

### 8、汉化n8n

n8n原版都是英文，英文不是很好的人，看起来还是比较费力，所以我们需要安装一下汉化版。首先，我们进入我们刚刚配置成功的n8n中，找到关于n8n,查看一下我们的n8n版本

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjE5ZGUzMmJkZmUzNmQ2MGU5NDg5NTdmY2VhYTZlMTBfWHIwdEJ4bXNjbVpvdEZOVGVLbVpjVkluMnQyamZOODJfVG9rZW46QTlIbmJzbDNzb1VPTFR4Z1NLbmNGNHZabnhlXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

然后进入汉化包的地址下载一下我们对应版本的文件，我刚刚上面看到的版本是1.107.3，然后右键第一个tar的压缩包，复制链接

https://github.com/other-blowsnow/n8n-i18n-chinese/releases

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=MTAyMDBmY2E2OTViZTMyZGJlNTRkOWIxNzMxYWY3NDRfWjBkbmszdHhIWHMxakRIVUdYTFF0Y2pRbXZMWUV2NnhfVG9rZW46Vm40RGJSZEwzb2JQNjJ4ZFNpd2N6a1A4blZiXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

我复制后的地址如下：https://github.com/other-blowsnow/n8n-i18n-chinese/releases/download/n8n%401.107.3/editor-ui.tar.gz

接着我们来到宝塔面板终端

选择一个安装目录，如果不熟悉的直接安装默认目录也行

执行以下命令，就是wget加上刚刚我们复制的链接：

```Plain
wget https://github.com/other-blowsnow/n8n-i18n-chinese/releases/download/n8n%401.107.3/editor-ui.tar.gz
```

看到如下结果就下载完成了

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTI2ODE1YWFkOTdiNmM2OWEyNzk1ODVhNzNjMzA1NTFfcDA4QnRIM2M3ZEsySWxBaWdWRmg5ZmsyVEV3Y2wycFZfVG9rZW46VWV1TmJjb1FTb3JmNlF4VkViV2NtbDlKbnliXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

我们下载的是个压缩包，需要执行以下命令进行解压

```Plain
tar -zxvf editor-ui.tar.gz
```

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTBmMTliM2FiMjdjNzQ5ZDcxMzQzMDQyOTMyMGYwOGVfMkFESzVXTTBFYVVzdHg4aXhuVTRlR1ozOHpkblJEZkRfVG9rZW46UWd5eWJPT1JUb2Nzc3Z4c05pSWNFcnJCbmFnXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

我们看到官方的docker安装命令是这样子的：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=OTQ0ZTA0YTI2OWNmYWI5NGNmNTc4MzM4ZjJmMjM4ZTZfRHkxdDBadGM0TllHbHM5ZjFPZ1ZXb1ZlVUllcU95U0tfVG9rZW46TDkxSWJjVkVUb1piYkp4NWFJZmM2ZEdpbmJjXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

这里有个替换的目录，就是我们刚刚下载下来的文件了，我们需要获取一下我们刚刚解压后的目录。直接输入以下命令

```Plain
cd dist
pwd
```

可以看到我的目录地址如下：

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQyNDJmNjdhYTZlNTA0NWUzZDM5MGMwZWZmNzEzOWNfM0hTZlBKcXRUQkxPRWt0TlhjWmhSdnlTNDRrUmpsUFpfVG9rZW46TkIyNmJKd2JOb1hsT2p4MFBHR2N6aXphbjliXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

所以替换官方的命令之后最终命令如下，跟之前的一样，因为我们要在宝塔的docker工具中直接创建容器所以去掉“t参数” 我还顺便改了名称，最终的命令如下，同第三步，复制命令直接去创建容器

```Bash
docker run -i --rm --name n8nCN 
-p 15678:5678 
-v /www/n8ncn/dist:/usr/local/lib/node_modules/n8n/node_modules/n8n-editor-ui/dist 
-v n8n_data:/home/node/.n8n 
-e N8N_DEFAULT_LOCALE=zh-CN 
-e N8N_SECURE_COOKIE=false 
n8nio/n8n
```

等待执行成功，我们到容器这里就可以看到这个新建的容器了

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NjM4ZGUxYzY2ODljZGQ4YWM4NzUwZGM2MDIzZjI4MzlfNWl4d3VnRGdVYzVjQkR0aHVHWUFXYlZtanRkS0daN1JfVG9rZW46UlFnRGJxWHdKb1BYVXR4N3R2WWNmQ2czbjRnXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

但是由于新的容器使用的是新的接口，暂时还没有域名可以访问，所以接下来要把我们刚刚的域名配置给改到这个新的容器来，当然，你也可以使用新的域名。但是我感觉弄多个没什么意义，就把之前的改过来就行了，后续就都用汉化的版本，可以把先前的版本删除了。

我们进入docker里的网站 找到我们之前配置的域名点击进去

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=NGI0ZGYzNjM1MDlmYmEwZjA5ZmM0NTdlY2U5MjYxYzBfd3ltWHdoNldtYWhBWnhjYU91MjBqQ3N2MzY1YmVpbUhfVG9rZW46Vnp5S2JsQXJvb0lTTFd4VVJ1OWMwY2tGbkNiXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

然后找到反向代理的设置，将这个地方的端口5678改成 15678，因为我们新容器的端口是15678 ，最后保存。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=YmU2MWM3Nzc2NTc2MjE0NWU0ZDFhZTEzZTZjZmRkM2FfaXlSV1N3akRWY0kwVnpoemVRR0dKeE1TRHRCVUZFNUtfVG9rZW46SWFOZWJWQnowb01MUlB4YnZWZ2NrZVJNbjZlXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

直接刷新我们的之前的域名网址，就成功出现汉化版了。

![](https://lx5aicqaye6.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzc4MjY4NzljMDYxM2NjNjkxMzljOTM5YTdkYjhjZGVfOUJ2ZjUya1lhR0pSTFV5S1loRWNKb3JxM0w3T0xLR3BfVG9rZW46WlB0Q2JPdWVJb1VPQ0t4Q3dRa2N1SkZRbjljXzE3NjkwNjE1MTc6MTc2OTA2NTExN19WNA)

  

好了！开启你的AI自动化之旅吧~