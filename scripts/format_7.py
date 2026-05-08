import re

file_path = r"D:\Obsidian\Qiao-WorkOS\my-vault\Clippings\用好 AI 跟上时代 7.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
result = []
i = 0
in_code_block = False

while i < len(lines):
    line = lines[i]

    # Track code blocks
    if line.strip().startswith('```'):
        in_code_block = not in_code_block
        result.append(line)
        i += 1
        continue

    if not in_code_block:
        # Fix numbered list: "N." alone on a line (possibly with trailing spaces)
        if re.match(r'^\d+\.\s*$', line):
            # Skip blank lines (up to 2)
            j = i + 1
            blanks = 0
            while j < len(lines) and lines[j].strip() == '' and blanks < 2:
                j += 1
                blanks += 1
            if j < len(lines) and lines[j].strip() != '':
                num = re.match(r'^(\d+\.)', line).group(1)
                result.append(f"{num} {lines[j].strip()}")
                i = j + 1
                continue

        # Fix bullet: "•" alone on a line (possibly with leading/trailing spaces)
        if re.match(r'^[ \t]*•[ \t]*$', line):
            indent = re.match(r'^([ \t]*)', line).group(1)
            j = i + 1
            blanks = 0
            while j < len(lines) and lines[j].strip() == '' and blanks < 2:
                j += 1
                blanks += 1
            if j < len(lines) and lines[j].strip() != '':
                result.append(f"{indent}- {lines[j].strip()}")
                i = j + 1
                continue

    result.append(line)
    i += 1

new_content = '\n'.join(result)

# Convert plain-text table (lines 129-151 in original, around "检查项 / 问自己")
old_table = """检查项

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

怎么算做完？手机能用吗？有闭环吗？"""

new_table = """| 检查项 | 问自己 |
|--------|--------|
| 问题陈述 | 用户要什么体验？一句话能说清楚吗？ |
| 方案描述 | 功能、数量、交互、视觉，具体到数字了吗？ |
| 技术约束 | 技术栈写了吗？ |
| 红线 | 说清楚"不要什么"了吗？ |
| 交付标准 | 怎么算做完？手机能用吗？有闭环吗？ |"""

new_content = new_content.replace(old_table, new_table)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done!")
