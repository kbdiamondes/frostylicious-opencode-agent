#!/bin/bash
# Wrapper script to run the MarkItDown MCP server

cd "$(dirname "$0")"

# Create venv if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Installing dependencies..."
    pip install -q mcp 'markitdown[all]'
else
    source .venv/bin/activate
fi

exec python3 server.py
