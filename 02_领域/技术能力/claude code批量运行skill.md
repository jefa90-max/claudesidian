示例：
批量执行流程
针对 D:\AI英语 中 $ARGUMENTS 开头的两位数文件夹，
使用 Task 代理（general-purpose 类型）串行处理

【执行方式】
前台串行代理：每个文件夹启动一个 Task 代理，等待完成后再启动下一个

【执行流程】
1. 用 Bash 列出所有符合条件的文件夹（$ARGUMENTS 开头的两位数）
2. 用 Bash 检查每个文件夹是否已有 extracted.vtt（已完成则跳过）
3. 对每个未完成的文件夹，启动一个 Task 代理执行 /youtube-learn

【Task 代理调用方式】
```
Task(
  subagent_type: "general-purpose",
  description: "youtube-learn [文件夹名]",
  prompt: "调用 Skill 工具执行 /youtube-learn D:\\AI英语\\[文件夹名] --roles"
)
```
注意：不设 run_in_background，代理在前台运行

【严格要求】
- 禁止创建 .py 文件
- 代理内部只能用 Skill 工具调用 /youtube-learn
- 检查文件夹状态可以用 Bash
- 代理内禁止自己写代码实现处理逻辑
