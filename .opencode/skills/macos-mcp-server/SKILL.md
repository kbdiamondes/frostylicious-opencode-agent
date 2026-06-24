---
name: macos-mcp-server
description: Build custom MCP servers for macOS system-level automation with security constraints
---

# macOS MCP Server Builder

## What I Do

I help you build custom Model Context Protocol (MCP) servers for macOS system-level automation. These servers provide safe, constrained access to system operations (window management, input simulation, app queries) while maintaining strict security through allow-lists, confirmation prompts, and native API usage.

## When to Use Me

- When you need to automate macOS UI interactions (moving windows, clicking, typing)
- When you want to add system-level capabilities to an AI assistant
- When you need to build secure automation tools with human-in-the-loop confirmation
- When you want to avoid terminal/shell-based automation for security reasons

## Steps

### 1. Plan the Server Architecture

Define what capabilities you need:
- **Information tools** (read-only): Query app state, get window geometry, screen resolution
- **Action tools** (write): Move windows, click, type, press keys

### 2. Create Project Structure

```
.macos-<name>-assist/
├── server.py           # Main MCP server entry point
├── config.py           # Configuration management
├── security.py         # Security validation layer
├── allowed_apps.json   # App allow-list configuration
├── pyproject.toml      # Python project configuration
├── macos/
│   ├── __init__.py
│   ├── accessibility.py  # macOS Accessibility API wrapper
│   ├── window.py         # Window management
│   └── input.py          # Input simulation
└── tools/
    ├── __init__.py
    ├── information.py   # Read-only tools
    └── actions.py       # Action tools
```

### 3. Implement Security Layer

- Create `allowed_apps.json` with bundle IDs of approved apps
- Implement `SecurityValidator` class that checks:
  - App is in allow-list
  - Actions are allowed for the app
  - Key combinations are not blocked
  - Text input is within length limits
- Add confirmation prompts for invasive actions

### 4. Implement macOS Wrappers

Use `pyobjc` to interface with native macOS frameworks:

```python
# Accessibility (read-only)
import ApplicationServices as AppServices

# Window management
from Quartz import CGMainDisplayID, CGDisplayBounds

# Input simulation
from Quartz import CGEventCreateMouseEvent, CGEventCreateKeyboardEvent
```

**Never use `subprocess`, `os.system`, or shell commands.**

### 5. Define MCP Tools

Create tool definitions with strict input schemas:

```python
Tool(
    name="click_at",
    description="Simulate a mouse click. Requires user confirmation.",
    inputSchema={
        "type": "object",
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"}
        },
        "required": ["x", "y"]
    }
)
```

### 6. Configure OpenCode

Add to `opencode.json`:

```json
{
  "mcp": {
    "macos-<name>-assist": {
      "enabled": true,
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

### 7. Grant Permissions

- System Settings → Privacy & Security → Accessibility
- Add your terminal/Python application

## Tips

- **Find Bundle IDs:** `osascript -e 'id of app "AppName"'`
- **Test Accessibility:** Run `python -c "import ApplicationServices; print(ApplicationServices.AXIsProcessTrusted())"`
- **Security First:** Always implement allow-lists and confirmation prompts for action tools
- **No Shell:** Use `pyobjc` for all macOS interactions to avoid shell injection risks
- **Confirmation Pattern:** Return `{"status": "needs_confirmation", ...}` from action tools to trigger human-in-the-loop gates

## Example: Minimal Secure Server

```python
from mcp.server import Server
from macos.accessibility import AccessibilityWrapper

server = Server("my-macos-assist")

@server.list_tools()
async def list_tools():
    return [Tool(name="get_active_app", description="Get focused app", inputSchema={...})]

@server.call_tool()
async def call_tool(name, arguments):
    if name == "get_active_app":
        wrapper = AccessibilityWrapper()
        return [TextContent(type="text", text=json.dumps(wrapper.get_frontmost_app()))]
```
