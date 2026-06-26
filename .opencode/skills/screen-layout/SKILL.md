---
name: screen-layout
description: Arrange Chrome and OpenCode side-by-side before using Chrome DevTools so the user can watch work in real-time. Use before ANY Chrome DevTools task.
---

## What I Do

Before using Chrome DevTools, I arrange the screen so Keith can watch my work. Chrome goes on the right half, OpenCode on the left half. This happens EVERY time Chrome DevTools is needed.

## When to Use Me

- **Before ANY Chrome DevTools task** — this is mandatory
- When user asks to browse, scrape, automate, or interact with websites
- When webfetch isn't enough and Chrome DevTools is needed

## Steps

1. **Get display info:**
   ```
   macos-sys-assist_get_displays
   ```

2. **Get OpenCode window geometry:**
   ```
   macos-sys-assist_get_window_geometry(pid=<opencode_pid>)
   ```

3. **Find Chrome's PID** — check running processes or use known PID

4. **Position OpenCode on LEFT half:**
   ```
   macos-sys-assist_move_window(x=0, y=0)
   macos-sys-assist_resize_window(width=960, height=1080)
   ```

5. **Position Chrome on RIGHT half:**
   ```
   macos-sys-assist_move_window(x=960, y=0)
   macos-sys-assist_resize_window(width=960, height=1080)
   ```

6. **Then proceed with Chrome DevTools task**

## Tips

- Adjust dimensions based on actual display resolution from `get_displays`
- If Chrome isn't open yet, open it first, then arrange
- Always confirm windows are visible before proceeding
