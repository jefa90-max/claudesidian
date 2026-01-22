# Scripts Directory

Helper scripts for vault automation and web content capture.

## Available Scripts

### Attachment Management

These are primarily called via npm/pnpm commands in package.json:

- `update-attachment-links.js` - Updates note links after moving attachments
- `fix-renamed-links.js` - Fixes links after renaming files

### Web Content Capture

**Note**: These scripts require API keys to function:

#### firecrawl-scrape.sh

Scrapes a single URL and saves as markdown.

```bash
# Requires FIRECRAWL_API_KEY environment variable
.scripts/firecrawl-scrape.sh <url> <output_file>
```

#### firecrawl-batch.sh

Scrapes multiple URLs and auto-generates filenames.

```bash
# 需要 FIRECRAWL_API_KEY 环境变量

# 基本用法 - 保存到 00_收件箱/剪藏/
.scripts/firecrawl-batch.sh <url1> <url2> <url3>

# 自定义输出目录
.scripts/firecrawl-batch.sh -o 01_项目/研究/ <url1> <url2>
.scripts/firecrawl-batch.sh --output-dir 03_资源/文章/ <url1> <url2>
```

### Transcript Extraction

#### transcript-extract.sh

Extracts transcripts from YouTube videos.

```bash
# 基本用法 - 保存到 00_收件箱/剪藏/
.scripts/transcript-extract.sh <youtube-url>

# 自定义输出目录
.scripts/transcript-extract.sh <youtube-url> 01_项目/研究/
```

## NPM Scripts

Run these from the vault root with `pnpm`:

| Command                        | Description                           |
| ------------------------------ | ------------------------------------- |
| `attachments:list`             | Show first 20 unprocessed attachments |
| `attachments:count`            | Count unprocessed attachments         |
| `attachments:organized`        | 统计已整理文件夹中的文件数量          |
| `attachments:unprocessed`      | Same as count                         |
| `attachments:refs <file>`      | Find references to a specific file    |
| `attachments:sizes`            | Show 20 largest attachment files      |
| `attachments:orphans`          | Find unreferenced attachments         |
| `attachments:recent`           | Show files added in last 7 days       |
| `attachments:create-organized` | 创建"已整理"子文件夹                  |

## Setup Requirements

### For Web Scraping

1. Get a Firecrawl API key from [firecrawl.dev](https://firecrawl.dev)
2. Add to your shell profile:
   ```bash
   export FIRECRAWL_API_KEY="your-key-here"
   ```

### For Transcript Extraction

- Requires `yt-dlp` and `jq` installed:

  ```bash
  # macOS
  brew install yt-dlp jq

  # Linux
  apt-get install yt-dlp jq
  ```

## Adding Custom Scripts

1. Create script in `.scripts/`
2. Make it executable: `chmod +x .scripts/your-script.sh`
3. Add npm script to `package.json` if needed
4. Document here

## Notes

- Scripts assume Unix-like environment (macOS/Linux)
- Windows users may need WSL or Git Bash
- All paths are relative to vault root
- Check script comments for additional requirements
