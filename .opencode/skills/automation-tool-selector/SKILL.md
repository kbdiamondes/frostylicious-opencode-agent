---
name: automation-tool-selector
description: Decides which tools to use for automation — Chrome DevTools (CDP) for web pages, bash for OS prep, and optionally macOS MCP for advanced app control.
---

## What I Do

I analyze any task and determine the best tools. For web interaction → **Chrome DevTools**. For OS-level prep (launch apps, find files, resize windows) → **bash**. The macOS MCP is an optional upgrade for specific advanced use cases.

## When to Use Me

Every time a task involves automation that mixes the browser and the operating system. If it's pure research (`webfetch`) or content creation, skip me.

Trigger patterns:
- "Upload this file to Google Drive / Dropbox / website"
- "Log in to X and do Y"
- "Find a file and send it somewhere"
- "Open this page and interact with it"
- "Navigate to X and click Y"
- "Take a screenshot and upload it"

## Steps

1. **Analyze the task** — Identify all sub-actions. Categorize each one:

   | Action | Tool (Required) | macOS MCP (Optional Upgrade) |
   |---|---|---|
   | Click buttons, fill forms, read page content | **Chrome DevTools** | — |
   | File upload via `<input type="file">` | **Chrome DevTools** (`setFileInputFiles` or base64 injection) | — |
   | Navigate multi-page web flows | **Chrome DevTools** | — |
   | Screenshot of specific page elements | **Chrome DevTools** | — |
   | Launch/quitt/focus apps | **bash** (`open -a`, `osascript`) | `launch_app()` — more reliable PID tracking |
   | Resize/move windows to known dimensions | **bash** (`osascript`) | `resize_window()`, `move_window()` — precise pixel control |
   | Find files on disk | **bash** (`find`, `ls`) | `find_files()` — structured JSON return |
   | Read file contents | **bash** (`python3 -c "..."`) | `read_file()` — built-in size/max_lines safety |
   | Full-screen or region screenshots | **bash** (`screencapture`) | `screenshot()` — custom paths, window/region selectors |
   | Clipboard operations | **bash** (`pbpaste`, `pbcopy`) | `get_clipboard()`, `set_clipboard()` — structured API |
   | OS-level keyboard shortcuts | **bash** (`osascript`) | `press_key()` — Core Graphics, more reliable than AS |
   | Window geometry queries | **bash** (`osascript`) | `get_window_geometry()` — Accessibility API, more accurate |

2. **Default to Chrome DevTools + bash** — For 90% of tasks, these two built-in tools are all you need:
   ```
   # bash: Find file, launch browser
   ls ~/Downloads/*Holiday*.pdf
   open -a "Brave Browser"
   osascript -e 'tell app "Brave Browser" to set bounds of window 1 to {0, 0, 1280, 900}'
   
   # Chrome DevTools: Web interaction
   new_page(url="https://drive.google.com")
   click(uid=1_21)  # + New button
   click(uid=2_2)   # File upload
   evaluate_script(function="() => { /* base64 file injection */ }")
   ```

3. **Upgrade to macOS MCP when** (see detailed use cases below).

## macOS MCP Use Cases

The macOS MCP is not needed for basic automation. Use it when:

### 1. Reliable Input Simulation (Core Graphics vs AppleScript)
AppleScript's `keystroke` and `click` can be flaky — sometimes they miss or the timing is off. The MCP uses **Core Graphics events** (`CGEventPost`) which is the same low-level mechanism macOS uses internally. Use it when:
- AppleScript key combinations fail silently
- You need pixel-perfect click coordinates
- The timing/sequence of input events matters (e.g., drag-and-drop)

### 2. Multi-App Workflows
When you need to coordinate actions across 3+ applications:
- Query which apps are running and their windows
- Get precise window geometry for each
- Move/resize for a recording or presentation layout
- Simulate input across apps in sequence

### 3. Screenshot Automation at Scale
The MCP's `screenshot_window()` and `screenshot_region()` let you capture specific app windows or areas of the screen without manual cropping. Use for:
- Automated documentation generation
- Bug reporting (capture error states)
- Social media content at scale

### 4. Accessibility Tree Exploration
The MCP can query what UI elements are on screen via the Accessibility API. This is useful for:
- Reading text from apps that don't have accessibility support
- Finding UI elements by role/label (future feature)
- Understanding what's visible when screenshots aren't available

### 5. Clipboard Automation Pipelines
Read from clipboard → process → write back. Example: capture selected text from any app, process it, paste it back. The MCP's clipboard tools are simpler than `pbpaste`/`pbcopy` for this because they integrate with the rest of the MCP workflow.

### 6. Security-Constrained Automation
If you need to:
- Restrict which apps can be automated (allow-list)
- Block destructive key combinations
- Require user confirmation before actions
- Limit text input length

### 7. When AppleScript Fails
Some apps don't respond to AppleScript. The MCP's Accessibility API and Core Graphics input can work where AppleScript can't. If `osascript` gives you `execution error`, try the MCP.

## Tips

- **You don't need the macOS MCP for most tasks.** bash + Chrome DevTools covers ~90% of use cases, including the Google Drive upload workflow.
- **Don't fight the tool** — If you're doing 3+ blind coordinate clicks to hit a web button, switch to Chrome DevTools 2 steps ago.
- **The file dialog is the danger zone** — Always use CDP `setFileInputFiles` or base64 injection for browser file uploads. Never navigate the macOS file dialog.
- **CDP can't find files** — Use bash `find` or `ls` then pass the path to CDP.
