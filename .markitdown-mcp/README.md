# MarkItDown MCP

An MCP server that converts documents to Markdown using Microsoft's [MarkItDown](https://github.com/microsoft/markitdown).

## Supported Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| PDF | `.pdf` | PDF documents |
| Word | `.docx`, `.doc` | Microsoft Word documents |
| PowerPoint | `.pptx`, `.ppt` | Microsoft PowerPoint presentations |
| Excel | `.xlsx`, `.xls` | Microsoft Excel spreadsheets |
| CSV | `.csv` | Comma-separated values |
| JSON | `.json` | JSON files |
| XML | `.xml` | XML files |
| HTML | `.html`, `.htm` | HTML web pages |
| EPUB | `.epub` | EPUB ebooks |
| Images | `.jpg`, `.png`, `.gif`, etc. | Images with OCR |
| Audio | `.wav`, `.mp3` | Audio with transcription |
| ZIP | `.zip` | ZIP archives |

## Installation

The MCP server auto-installs dependencies on first run. Manual setup:

```bash
cd .markitdown-mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

The MCP is automatically started when OpenCode loads. Use the tools:

### Convert a file
```
convert_to_markdown(file_path="/path/to/document.pdf")
```

### Convert a URL
```
convert_to_markdown(file_path="https://example.com/document.docx")
```

### List supported formats
```
get_supported_formats()
```

## How It Works

1. MarkItDown reads the file (local or URL)
2. Extracts text, structure, and metadata
3. Converts to clean Markdown format
4. Returns markdown for LLM consumption

## Benefits

- **Token efficiency** — Markdown is more token-efficient than raw documents
- **LLM-friendly** — LLMs natively understand Markdown
- **Structure preservation** — Headings, lists, tables, links preserved
- **OCR support** — Extract text from images
- **Audio transcription** — Convert speech to text

## Credits

Built on [Microsoft MarkItDown](https://github.com/microsoft/markitdown) (MIT License).
