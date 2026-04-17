开源的DeekWiki加入MCP，为您的Cursor提供开源项目分析，轻松让AI掌握开源项目使用文档！

tokengo token的技术分享

2025年05月09日 08:25 广东 听全文

OpenDeepWiki是参考DeepWiki作为灵感，基于.NET 9和Semantic Kernel开发的开源项目。它旨在帮助开发者更好地理解和使用代码库，提供代码分析、文档生成、知识图谱等功能。

一分钟添加您需要的开源仓库

打开：OpenDeepWiki 官方网站

点击左上角的添加新仓库：

添加新仓库界面

输入需要添加的仓库地址（只支持http协议，并且只支持http://域名/组织/仓库 的路由格式解析）：

添加仓库输入界面

添加完成以后可能需要等待10分钟左右，当然前面可能会有其他的用户添加的仓库可能需要更长时间：

仓库列表显示界面

接入MCP

然后我们可以点击进入进入OpenDeeWiki仓库，然后点击添加MCP：

进入仓库并点击添加MCP

在这里提供的接入教程我们根据教程先打开cursor或其他的客户端工具，下面我们以cursor为例：

MCP接入教程

OpenDeepWiki支持MCP (ModelContextProtocol)

- 支持单仓库提供MCPServer，针对单个仓库进行分析
    
- 通过OpenDeepWiki作为MCPServer，您可以方便地对开源项目进行分析和理解
    

使用配置

下面是Cursor的使用方式：

{

"mcpServers": {

"OpenDeepWiki": {

"url": "http://opendeep.wiki/api/sze?owner=AIDotNet&name=OpenDeepWiki"

}

}

}

配置说明：

- owner：是仓库组织或拥有者的名称
    
- name：是仓库的名称
    

点击右侧复制按钮，然后输出到cursor的mcp配置当中，然后保存

配置保存界面

然后显示接入成功，然后我们可以开始点击测试效果

测试效果界面

然后输入提问：OpenDeepWiki是什么？

关于OpenDeepWiki的讨论

OpenDeepWiki是什么?

我将使用适当的工具来了解OpenDeepWiki项目的情况。

Read package.json

Could not find file 'README.md' in the workspace.

Listed 14 items in current directory

Listed 11 items in app

Read page.tsx

Listed 9 items in app/components

Called MCP tool CodeRepositoryAnalyzer

1. 代码分析与文档生成：

- 自动分析代码库生成文档。
    
- 支持生成Mermaid图表以可视化代码依赖关系。
    

2. 多语言支持：

- 支持所有编程语言的代码分析和文档生成。
    

3. AI智能分析：

- 基于AI的代码分析和关系理解。
    
- 支持自定义模型和API扩展。
    

Read HomeClient.tsx L1-200

OpenDeepWiki是一个基于.NET 9和Semantic Kernel开发的智能代码分析与文档生成工具，旨在帮助开发者更好地理解和使用代码库。

项目核心功能

- 代码智能分析：自动分析代码结构，提取关键信息和依赖关系
    
- 文档自动生成：生成全面的代码文档，包括Mermaid图表可视化
    
- 多语言支持：适用于所有编程语言的代码分析和文档生成
    
- AI驱动交互：支持通过对话方式查询代码信息，理解代码用法
    
- 知识库构建：建立SEO友好的代码知识库，便于检索和分享
    

技术架构

- 后端：基于.NET 9和Semantic Kernel构建
    
- 前端：使用Next.js、React 19和Ant Design开发的现代界面
    
- 数据库：支持SQLite和PostgreSQL存储分析结果
    
- 部署方式：提供Docker容器化部署，支持ARM和AMD架构
    

这个项目通过AI技术帮助开发者更高效地理解、文档化和使用代码库，显著提升了代码库的可维护性和协作效率。它特别适合团队协作开发和大型项目的知识沉淀。

然后执行我们的MCP服务，得到仓库的解析文档然后ai根据文档生成回复，通过上面的操作我们可以很轻松的让AI了解您使用的开源项目，包括组件使用安装部署等操作。

技术交流群：

开源地址：https://github.com/AIDotNet/OpenDeepWiki