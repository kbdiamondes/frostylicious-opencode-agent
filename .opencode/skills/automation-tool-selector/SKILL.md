---
name: automation-tool-selector
description: Decides which automation approach to use for a task — Chrome DevTools (CDP) for web page interaction, macOS Assistant MCP for OS-level operations, or a hybrid of both.
---

## What I Do

I analyze any task and determine the best automation tool(s) based on whether the work involves web page interaction (clicking buttons, filling forms, file uploads in a browser) or OS-level operations (app lifecycle, file system, window management, screenshots).

## When to Use Me

Every time a task involves automation that could use either Chrome DevTools or macOS Assistant. If the task is purely research (webfetch) or content creation (writing code/copy), skip me. But for any "do something" task involving the browser or OS, consult me first.

Trigger patterns:
- "Upload this file to Google Drive / Dropbox / website"
- "Log in to X and do Y"
- "Find a file and send it somewhere"
- "Open this page and interact with it"
- "Navigate to X and click Y"

## Steps

1. **Analyze the task** — Read the user's request and identify all sub-actions.

2. **Categorize each sub-action:**

   | If task involves... | Use |
   |---|---|
   | Clicking buttons/links/menus in a web page | Chrome DevTools |
   | Filling form fields in a web page | Chrome DevTools |
   | File upload via `<input type="file">` | Chrome DevTools (`DOM.setFileInputFiles`) |
   | Reading/parsing page content | Chrome DevTools |
   | Navigating multi-page web flows | Chrome DevTools |
   | Taking screenshots of page elements | Chrome DevTools |
   | Launching/quitting/focusing apps | macOS Assistant |
   | Resizing/moving windows | macOS Assistant |
   | File system operations (find, read, open) | macOS Assistant |
   | Clipboard operations | macOS Assistant |
   | Full-screen or region screenshots | macOS Assistant |
   | OS-level keyboard shortcuts | macOS Assistant |

3. **If hybrid** — Split the task into OS phases and web phases:
   ```python
   # Example: "Find a PDF and upload it to Google Drive"
   
   # Phase 1: macOS Assistant — Find the file
   find_files(directory="~/Downloads", pattern="*.pdf")
   
   # Phase 2: macOS Assistant — Launch/prepare browser
   open -a "Brave Browser"
   resize_window(width=1280, height=900)
   
   # Phase 3: Chrome DevTools — Web page interaction
   new_page(url="https://drive.google.com")
   # ... click +New, File upload using CDP selectors
   # DOM.setFileInputFiles to bypass native dialog
   ```

4. **Always prefer `DOM.setFileInputFiles` over file dialogs** — Chrome DevTools can set a file path directly on an `<input type="file">` element without simulating clicks or navigating native dialogs. This is significantly more reliable than any combination of coordinate clicks + AppleScript dialog navigation.

5. **Default to macOS Assistant for OS prep** — Even if the core task is web-based, use macOS Assistant to launch the browser, resize windows, and manage the desktop environment before switching to Chrome DevTools for web interaction.

## Tips

- **Don't fight the tool** — If you're doing 3+ blind coordinate clicks in macOS Assistant to hit a web button, you should have switched to Chrome DevTools 2 steps ago.
- **The file dialog is the danger zone** — Native file dialogs triggered by web pages (like Google Drive upload) are notoriously unreliable with coordinate-based clicking. Use CDP `DOM.setFileInputFiles` or keyboard shortcuts (like `Ctrl+C then U` in Google Drive).
- **CDP requires the page to be open** — Launch the browser with macOS Assistant first, then use CDP on the same browser instance.
- **CDP can't find files** — macOS Assistant's `find_files` is better for locating files on disk. Use it in Phase 1, pass the path to CDP in Phase 3.
