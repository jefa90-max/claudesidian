"""Format the scraped Markdown file:

1. Merge `数字.` followed by blank line(s) and content into `数字. 内容`.
2. Merge `•` (with optional leading whitespace) followed by blank line(s) and
   content into `(indent)- 内容`, preserving leading indent.
3. Replace two specific plain-text tables with proper Markdown tables.

Code blocks (``` fenced) are left untouched.
"""

from __future__ import annotations

import re
from pathlib import Path

FILE_PATH = Path(r"D:\Obsidian\Qiao-WorkOS\my-vault\Clippings\用好 AI 跟上时代 6.md")


def transform_non_code_lines(lines: list[str]) -> list[str]:
    """Apply numbered-list and bullet-list merges to a list of lines.

    Operates on a copy and returns a new list. The list does NOT include
    fence lines.
    """
    result: list[str] = []
    i = 0
    n = len(lines)

    num_only_re = re.compile(r"^(\d+)\.[ \t]*$")
    bullet_only_re = re.compile(r"^([ \t]*)•[ \t]*$")

    while i < n:
        line = lines[i]

        # Numbered list pattern: "N." then 1-2 blank lines then content
        m_num = num_only_re.match(line)
        if m_num:
            # look ahead: skip 1 or 2 blank lines, then content line
            j = i + 1
            blanks = 0
            while j < n and lines[j].strip() == "" and blanks < 2:
                blanks += 1
                j += 1
            if blanks >= 1 and j < n and lines[j].strip() != "":
                # merge
                content = lines[j]
                result.append(f"{m_num.group(1)}. {content}")
                i = j + 1
                continue

        m_bul = bullet_only_re.match(line)
        if m_bul:
            indent = m_bul.group(1)
            j = i + 1
            blanks = 0
            while j < n and lines[j].strip() == "" and blanks < 2:
                blanks += 1
                j += 1
            if blanks >= 1 and j < n and lines[j].strip() != "":
                content = lines[j]
                result.append(f"{indent}- {content.lstrip()}")
                i = j + 1
                continue

        result.append(line)
        i += 1

    return result


def apply_list_transforms(text: str) -> str:
    """Walk the text line-by-line, skip code-fenced blocks unchanged."""
    lines = text.split("\n")
    out: list[str] = []
    in_code = False
    buf_non_code: list[str] = []

    def flush_non_code() -> None:
        if buf_non_code:
            out.extend(transform_non_code_lines(buf_non_code))
            buf_non_code.clear()

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            # toggle: flush pending non-code, then emit fence line as-is
            flush_non_code()
            out.append(line)
            in_code = not in_code
            continue
        if in_code:
            out.append(line)
        else:
            buf_non_code.append(line)
    flush_non_code()
    return "\n".join(out)


TABLE1_OLD = """形式

典型产出

AI 能帮你做什么

文字

文章、脚本、文案

生成初稿、改写润色、去 AI 味

图片

封面、海报、插图

文生图、风格迁移、批量出图

视频

短视频、AI 影片

脚本→分镜→画面→配音→剪辑"""

TABLE1_NEW = """| 形式 | 典型产出 | AI 能帮你做什么 |
|------|---------|--------------|
| 文字 | 文章、脚本、文案 | 生成初稿、改写润色、去 AI 味 |
| 图片 | 封面、海报、插图 | 文生图、风格迁移、批量出图 |
| 视频 | 短视频、AI 影片 | 脚本→分镜→画面→配音→剪辑 |"""


TABLE2_OLD = """类型

工具

介绍

使用门槛

文案写作

Claude（推荐）

kimi /豆包

Claude 更适合对文风有要求的写作任务，写出来的中文最接近真人语感，不容易被认出是 AI 写的。

Claude 国外工具，免费可体验，额度有限，看个人使用量

图片

即梦 AI

中文环境文生图效果较好

有免费使用额度

视频

即梦 Seedance2.0

多模态 AI 视频生成模型，优势：画面稳定不变形，音画自动同步，好操控

生视频有积分消耗，基础会员 69 元/月

剪辑

剪映

免费的国内视频剪辑软件，操作简单

有免费使用额度"""

TABLE2_NEW = """| 类型 | 工具 | 介绍 | 使用门槛 |
|------|------|------|--------|
| 文案写作 | Claude（推荐）<br>kimi /豆包 | Claude 更适合对文风有要求的写作任务，写出来的中文最接近真人语感，不容易被认出是 AI 写的。 | Claude 国外工具，免费可体验，额度有限，看个人使用量 |
| 图片 | 即梦 AI | 中文环境文生图效果较好 | 有免费使用额度 |
| 视频 | 即梦 Seedance2.0 | 多模态 AI 视频生成模型，优势：画面稳定不变形，音画自动同步，好操控 | 生视频有积分消耗，基础会员 69 元/月 |
| 剪辑 | 剪映 | 免费的国内视频剪辑软件，操作简单 | 有免费使用额度 |"""


def replace_tables(text: str) -> str:
    if TABLE1_OLD in text:
        text = text.replace(TABLE1_OLD, TABLE1_NEW, 1)
        print("Table 1 replaced.")
    else:
        print("WARN: table 1 source not found.")
    if TABLE2_OLD in text:
        text = text.replace(TABLE2_OLD, TABLE2_NEW, 1)
        print("Table 2 replaced.")
    else:
        print("WARN: table 2 source not found.")
    return text


def main() -> None:
    raw = FILE_PATH.read_text(encoding="utf-8")
    has_crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")

    # Replace tables FIRST (before list transforms touch them).
    # Note: the standalone `数字.` lines (problem 1) appear ONLY where the
    # number is alone on a line — in the table source, the cells are plain
    # words, so list transforms wouldn't match anyway. But bullet `•` doesn't
    # appear in the table source either. Order is therefore safe; we'll do
    # tables first to be explicit.
    text = replace_tables(text)
    text = apply_list_transforms(text)

    if has_crlf:
        text = text.replace("\n", "\r\n")
    FILE_PATH.write_text(text, encoding="utf-8")
    print(f"Done. Wrote {len(text)} chars to {FILE_PATH}")


if __name__ == "__main__":
    main()
