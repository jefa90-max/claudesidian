import re

file_path = r"D:\Obsidian\Qiao-WorkOS\my-vault\Clippings\用好 AI 跟上时代 8.md"

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
        # Fix numbered list: "N." alone on a line (digits only, e.g. 1. 2. 3. 4.)
        if re.match(r'^\d+\.\s*$', line):
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

        # Fix lettered sub-items: "a." / "b." / "c." alone on a line
        if re.match(r'^[a-zA-Z]\.\s*$', line):
            j = i + 1
            blanks = 0
            while j < len(lines) and lines[j].strip() == '' and blanks < 2:
                j += 1
                blanks += 1
            if j < len(lines) and lines[j].strip() != '':
                letter = re.match(r'^([a-zA-Z]\.)', line).group(1)
                result.append(f"{letter} {lines[j].strip()}")
                i = j + 1
                continue

        # Fix bullet: "•" alone on a line
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

# No plain-text tables found in this file — no table replacements needed.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done!")
