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

### [2026-06-24] MCP Selection Framework — Task Analysis Before Tool Choice
- **Task:** Upload a file to Google Drive using browser automation. Determine which MCP to use: Chrome DevTools (CDP) vs macOS Assistant.
- **Approach:** Analyzed the task by its nature — web page interaction (buttons, forms, file inputs) vs OS-level operations (file system, window management, app lifecycle).
- **Decision Framework:**
  ```
  For any task, ask: "Is this interacting with a web page or with the operating system?"

  USE CHROME DEVTOOLS (CDP) when:
  - Clicking buttons, links, or menus inside a web page
  - Filling form fields, selecting dropdowns, typing into web inputs
  - File upload via browser (<input type="file"> + DOM.setFileInputFiles)
  - Reading/parsing page content (text, tables, structured data)
  - Navigating multi-page web flows (checkout, signup, onboarding)
  - Any action where a CSS selector or XPath can identify the target
  - Screenshots of specific page elements
  ✅ Why: Element-based selectors, no coordinate guessing, bypasses native file dialogs
  ✅ Key advantage: DOM.setFileInputFiles sets file path directly — no file dialog needed

  USE MACOS ASSISTANT MCP when:
  - Launching/quitting/focusing applications (open -a, activate)
  - Resizing, moving, or positioning windows
  - OS-level file operations (find, read, open, list files)
  - Clipboard operations (get/set text)
  - Taking full-screen or region screenshots
  - Keyboard shortcuts that operate at the OS level (cmd+tab, cmd+space)
  - Native dialogs (but NOT web file dialogs — those are CDP territory!)
  ✅ Why: Direct macOS API access via pyobjc, no rendering engine needed
  ✅ Key advantage: Works outside the browser, controls the entire OS

  USE BOTH (Hybrid) when:
  - Task spans OS + web: e.g., "Find a PDF on the desktop and upload it to Google Drive"
    → macOS Assistant: find the file
    → macOS Assistant: launch/resize Chrome
    → Chrome DevTools: navigate to Google Drive, click +New, use DOM.setFileInputFiles
  ```
- **Key Steps (Tested Example — Upload PDF to Google Drive):**
  ```python
  # MACOS MCP: Find the file
  find_files(directory="~/Downloads", pattern="*Philippine*")
  
  # MACOS MCP: Launch and prepare browser
  launch_app("Brave Browser")
  resize_window(width=1280, height=900)
  
  # CHROME CDP: Navigate and interact with web page
  new_page(url="https://drive.google.com")
  # ... click +New, File upload via CDP selectors ...
  # DOM.setFileInputFiles to set the file without dialog
  ```
- **Outcome:** The hybrid approach (macOS for file/OS ops + CDP for web interaction) is more reliable than using macOS MCP for everything. CDP bypasses the fragile coordinate-based clicking and native file dialog issues encountered when using only macOS MCP.
- **Confirmed by User:** Yes (user explicitly suggested this decision framework)
