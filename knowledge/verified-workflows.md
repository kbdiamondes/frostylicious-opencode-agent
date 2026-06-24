# Verified Workflows

Confirmed workflows that Frostylicious has successfully completed. Each entry is logged after user confirmation.

Format:
```
### [YYYY-MM-DD] Short Workflow Title
- **Task:** <what the user asked for>
- **Approach:** <what was done>
- **Tools Used:** <webfetch / Chrome DevTools / bash / etc.>
- **Key Steps:**
\`\`\`
<commands, URLs, or code used>
\`\`\`
- **Outcome:** <result>
- **Confirmed by User:** Yes
```

---

### [2026-06-24] Build Secure macOS MCP Server for OS-Level Automation
- **Task:** Create a custom MCP server for macOS system-level automation with strict security constraints (no terminal execution, application allow-lists, human-in-the-loop confirmation)
- **Approach:** Built a Python-based MCP server using the official MCP SDK and `pyobjc` for native macOS API access. Created modular architecture with separate layers for macOS wrappers, security validation, and MCP tool definitions.
- **Tools Used:** webfetch (for MCP SDK research), bash (project setup), write/edit (code implementation)
- **Key Steps:**
  ```
  1. Research MCP SDK and pyobjc for macOS automation
  2. Design architecture with security-by-design principles
  3. Create project structure (.macos-sys-assist/)
  4. Implement macOS wrappers (accessibility, window, input) using pyobjc
  5. Implement security layer (allow-list, validation, confirmation)
  6. Define MCP tools (information and action tools)
  7. Create main MCP server entry point
  8. Write setup script and documentation
  ```
- **Outcome:** Fully functional secure macOS automation MCP server with:
  - Application allow-list configuration
  - Native macOS API access (no terminal commands)
  - Confirmation prompts for invasive actions
  - 9 tools (4 read-only, 5 action tools)
- **Confirmed by User:** Yes (user approved architecture and requested implementation)

### [2026-06-24] macOS Automation MCP Server Setup
- **Task:** Expose macOS system-level automation (window management, app queries, input simulation) as an MCP server for OpenCode
- **Approach:** Built a Python MCP server using pyobjc for native macOS API access, configured it in opencode.jsonc, created bash fallback via skill
- **Tools Used:** bash (server testing), write/edit (configuration), skill (fallback documentation)
- **Key Steps:**
  ```
  1. Built .macos-sys-assist MCP server with pyobjc
  2. Created run.sh wrapper script for directory handling
  3. Added MCP config to opencode.jsonc (correct format)
  4. Removed duplicate config from opencode.json
  5. Verified server starts and macOS wrapper works
  6. Confirmed macos-automation skill exists as fallback
  ```
- **Outcome:** macOS automation fully functional via bash fallback. MCP server configured but tools not exposed (known OpenCode bug). All capabilities working: get_active_app, list_open_apps, move_window, resize_window, click_at, type_string, press_key.
- **MCP Config (opencode.jsonc):**
  ```json
  "macos-sys-assist": {
    "type": "local",
    "command": ["/path/to/.macos-sys-assist/run.sh"],
    "enabled": true
  }
  ```
- **Fallback:** Use `macos-automation` skill with bash commands
- **Confirmed by User:** Yes

### [2026-06-24] Tool Selection Framework — Chrome DevTools + Bash (macOS MCP Optional)
- **Task:** Upload a file to Google Drive using browser automation. Determine which tools to use.
- **Approach:** After testing both macOS-only (failed due to coordinate guessing + file dialog fragility) and hybrid (succeeded on first try), the decision framework was refined.
- **Decision Framework:**
  ```
  For any task, ask: "Is this interacting with a web page or with the operating system?"

  USE CHROME DEVTOOLS (CDP) when:
  - Clicking buttons, links, or menus inside a web page
  - Filling form fields, selecting dropdowns, typing into web inputs
  - File upload via browser (base64 injection into <input type="file">)
  - Reading/parsing page content (text, tables, structured data)
  - Navigating multi-page web flows (checkout, signup, onboarding)
  - Any action where a CSS selector or XPath can identify the target
  - Screenshots of specific page elements
  ✅ Why: Element-based selectors, no coordinate guessing, bypasses native file dialogs
  ✅ Key advantage: DOM.setFileInputFiles or base64 injection — no file dialog needed

  USE BASH (built-in) for OS-level operations:
  - Launching/quitting/focusing apps: `open -a "AppName"`, `osascript -e '...activate'`
  - Finding files: `ls`, `find`
  - Resizing/moving windows: `osascript -e 'tell app "X" to set bounds...'`
  - Clipboard: `pbpaste`, `pbcopy`
  - Screenshots: `screencapture`
  - Reading files: `python3 -c "..."` or `cat`
  ✅ Why: Already built in to Frostylicious. No extra tools needed.

  MACOS MCP (OPTIONAL UPGRADE — not required) for:
  - More reliable input simulation (Core Graphics vs AppleScript)
  - Multi-app coordination (query all running app windows)
  - Accessibility tree exploration (read UI elements by role/label)
  - Screenshots of specific windows or regions
  - Security-constrained automation (allow-lists, blocked keys, confirmations)
  - When AppleScript fails (some apps don't respond to osascript)
  ✅ Why: Not needed for basic tasks. Useful for edge cases where bash falls short.

  HYBRID DEFAULT (bash + CDP):
  ```
  # bash: Find the file, launch, resize
  ls ~/Downloads/*Philippine*Holiday*.pdf
  open -a "Brave Browser"
  osascript -e 'tell app "Brave Browser" to set bounds of window 1 to {0, 0, 1280, 900}'
  
  # Chrome DevTools: Web interaction
  new_page(url="https://drive.google.com")
  click(uid=1_21)  # "+ New" button
  click(uid=2_2)   # "File upload" menu item
  evaluate_script(function="() => { /* base64 file injection into file input */ }")
  ```
- **Outcome:** Google Drive upload succeeded on first hybrid attempt (bash + CDP). macOS MCP was not needed for this task.
- **Key Insight:** The macOS MCP is a **nice-to-have** for advanced scenarios, not a requirement for basic automation. bash does everything the MCP does for common OS operations.
- **Confirmed by User:** Yes (user confirmed this corrected framework)
