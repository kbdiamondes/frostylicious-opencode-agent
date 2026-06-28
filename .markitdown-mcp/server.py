#!/usr/bin/env python3
"""
MarkItDown MCP Server
=====================

An MCP server that converts documents to Markdown using Microsoft's MarkItDown.
Supports: PDF, Word, PowerPoint, Excel, Images, Audio, HTML, CSV, JSON, XML, ZIP, and more.

Usage:
    python server.py
"""

import asyncio
import json
import logging
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from mcp.server import Server
from mcp.types import (
    TextContent,
    Tool,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("markitdown-mcp")

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    # Documents
    '.pdf': 'PDF document',
    '.docx': 'Word document',
    '.doc': 'Word document (legacy)',
    '.pptx': 'PowerPoint presentation',
    '.ppt': 'PowerPoint presentation (legacy)',
    '.xlsx': 'Excel spreadsheet',
    '.xls': 'Excel spreadsheet (legacy)',
    '.csv': 'CSV file',
    '.json': 'JSON file',
    '.xml': 'XML file',
    '.html': 'HTML file',
    '.htm': 'HTML file',
    '.epub': 'EPUB ebook',
    # Images
    '.jpg': 'JPEG image',
    '.jpeg': 'JPEG image',
    '.png': 'PNG image',
    '.gif': 'GIF image',
    '.bmp': 'BMP image',
    '.tiff': 'TIFF image',
    '.tif': 'TIFF image',
    '.webp': 'WebP image',
    # Audio
    '.wav': 'WAV audio',
    '.mp3': 'MP3 audio',
    # Archives
    '.zip': 'ZIP archive',
}

# Tool definitions
TOOLS = [
    Tool(
        name="convert_to_markdown",
        description="Convert a document file to Markdown format. Supports PDF, Word, PowerPoint, Excel, images, audio, HTML, CSV, JSON, XML, ZIP, and more.",
        inputSchema={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to convert (local path or URL)"
                }
            },
            "required": ["file_path"]
        }
    ),
    Tool(
        name="convert_text_to_markdown",
        description="Convert raw text content to clean Markdown format.",
        inputSchema={
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "Text content to convert to Markdown"
                },
                "source_type": {
                    "type": "string",
                    "description": "Source file extension (e.g., '.pdf', '.docx', '.html')",
                    "enum": list(SUPPORTED_EXTENSIONS.keys())
                }
            },
            "required": ["content", "source_type"]
        }
    ),
    Tool(
        name="get_supported_formats",
        description="List all supported file formats for conversion.",
        inputSchema={
            "type": "object",
            "properties": {},
            "required": []
        }
    ),
]


def convert_file(file_path: str) -> str:
    """Convert a file to markdown using MarkItDown."""
    try:
        from markitdown import MarkItDown
        
        # Initialize MarkItDown
        md = MarkItDown()
        
        # Convert the file
        result = md.convert(file_path)
        
        return result.text_content
    except ImportError:
        return "Error: MarkItDown not installed. Run: pip install 'markitdown[all]'"
    except Exception as e:
        return f"Error converting file: {str(e)}"


def convert_text(content: str, source_type: str) -> str:
    """Convert text content to markdown based on source type."""
    # For now, return the content as-is
    # In the future, we could parse based on source_type
    return content


async def handle_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Handle tool calls from the MCP client."""
    if tool_name == "convert_to_markdown":
        file_path = arguments.get("file_path", "")
        if not file_path:
            return "Error: file_path is required"
        
        # Check if file exists (for local files)
        if not file_path.startswith(("http://", "https://")):
            if not os.path.exists(file_path):
                return f"Error: File not found: {file_path}"
            
            # Check file extension
            ext = Path(file_path).suffix.lower()
            if ext not in SUPPORTED_EXTENSIONS:
                return f"Error: Unsupported file type: {ext}. Use get_supported_formats to see supported types."
        
        return convert_file(file_path)
    
    elif tool_name == "convert_text_to_markdown":
        content = arguments.get("content", "")
        source_type = arguments.get("source_type", ".txt")
        
        if not content:
            return "Error: content is required"
        
        return convert_text(content, source_type)
    
    elif tool_name == "get_supported_formats":
        formats = "\n".join([f"{ext}: {desc}" for ext, desc in SUPPORTED_EXTENSIONS.items()])
        return f"Supported formats:\n{formats}"
    
    else:
        return f"Error: Unknown tool: {tool_name}"


async def main():
    """Main entry point for the MCP server."""
    # Create the MCP server
    server = Server("markitdown-mcp")
    
    # Register tool handlers
    @server.list_tools()
    async def list_tools():
        return TOOLS
    
    @server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]):
        result = await handle_tool_call(name, arguments)
        return [TextContent(type="text", text=result)]
    
    # Run the server
    logger.info("Starting MarkItDown MCP server...")
    
    # Use stdio for communication
    import mcp.server.stdio
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
