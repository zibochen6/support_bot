# support_bot





## wiki 爬取保存

根据seeed wiki的链接URL命名规则，使用关键词来爬取需要的页面！

**关键词List**："recomputer", "reComputer","Jetson","jetson","robotics"

**更新机制**：

​	通过维护`url_index.json`文件来记录哪些页面已经爬取过，没有则界定为新增页面，爬取update database

 

流程：

**1.结构检查**

检查是否存在已经爬取的`url_index.json`文件

不存在：新建

存在：下一步

**2.筛选目标url**

获取wiki上所有的url链接，从https://wiki.seeedstudio.com/sitemap.xml 读取然后按照多关键词来过滤url，以提取到所需的url. (过滤掉r1000，r2000，除中文和英语以外的页面)

**3.解析url内容并保存为markdown文件**

提取正文内容以及标题，并且保存到本地



## FAISS 向量库搭建

**收集文档**：遍历本地 `.md` 文件

**清洗/结构化**：保留标题层级、去掉无意义内容（可选）

1. 移除图片类内容：Markdown 图片、HTML <img>、<figure>、data URI 图片。
2. 移除 HTML 注释与无意义锚点（如 [[](#...)](https://file+.vscode-resource.vscode-cdn.net/Users/chenzibo/.vscode/extensions/openai.chatgpt-0.4.76-darwin-arm64/webview/#)）。
3. 移除商店 CTA 单行链接（如 “Get One Now / 立即购买”）。
4. 压缩“噪声表格”：
   - 触发条件：行数 > 40，或列数 > 20，或单行过长，或空白比例过高。
   - 输出为 [TABLE COMPRESSED] + 列摘要 + 行摘要。
5. 保留代码块不做清理，避免误伤命令/配置。
6. 多余空行压缩为最多两行。

**分块 Chunking**：把每篇文档切成小段（带重叠）

**向量化 Embedding**：对每个 chunk 生成向量

**建 FAISS Index**：把所有向量加进索引

**保存索引+元数据**：FAISS 只存向量，文本/路径等要自己保存

**检索**：query→embedding→faiss.search→拿回 topK chunks



## RAG

**（可选）重排 rerank**：用交叉编码器/LLM 对 topK 再排序，提高准确率

**（可选）RAG**：把检索到的 chunks 喂给 LLM 生成回答
