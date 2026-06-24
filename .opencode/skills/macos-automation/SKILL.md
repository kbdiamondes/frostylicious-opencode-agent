---
name: macos-automation
description: Control macOS windows, apps, and input through native Accessibility APIs
---

# macOS Automation Skill

## What I Do

I control your macOS system-level UI through native Accessibility APIs. I can query apps, move/resize windows, simulate clicks, type text, and press key combinations — all without terminal commands.

## When to Use Me

- User asks "what app is focused" or "list open apps"
- User wants to move, resize, or snap a window
- User wants to click somewhere on screen
- User wants to type text into a focused field
- User wants to press a key combination (e.g., Cmd+Tab)
- User wants screen resolution info

## Steps

**Always use the full Python path and sys.path.insert for imports:**

```bash
/Users/keithdoesmedia/Documents/Programming/frostylicious-opencode-agent/.macos-sys-assist/.venv/bin/python3 -c "
import sys
sys.path.insert(0, '/Users/keithdoesmedia/Documents/Programming/frostylicious-opencode-agent/.macos-sys-assist')
from macos.accessibility import AccessibilityWrapper
from macos.window import WindowManager
from macos.input import InputSimulator

a = AccessibilityWrapper()
wm = WindowManager()
inp = InputSimulator()

# --- Your code here ---
"
```

## Common Operations

### Get Focused App
```python
app = a.get_frontmost_app()
print(f'{app[\"name\"]} ({app[\"bundle_id\"]}, PID: {app[\"pid\"]})')
```

### List Open Apps
```python
for app in a.get_running_apps():
    print(f'{app[\"name\"]} ({app[\"bundle_id\"]})')
```

### Get Screen Resolution
```python
screen = a.get_screen_resolution()
print(f'{screen[\"width\"]}x{screen[\"height\"]}')
```

### Get Window Geometry
```python
pid = int(app['pid'])
geo = wm.get_window_geometry(pid)
print(f'Position: ({geo[\"x\"]}, {geo[\"y\"]}), Size: {geo[\"width\"]}x{geo[\"height\"]}')
```

### Move Window
```python
result = wm.move_window(pid, x, y)
```

### Resize Window
```python
result = wm.resize_window(pid, width, height)
```

### Snap to Left Half
```python
screen = a.get_screen_resolution()
wm.resize_window(pid, screen['width'] // 2, screen['height'])
wm.move_window(pid, 0, 0)
```

### Snap to Right Half
```python
screen = a.get_screen_resolution()
wm.resize_window(pid, screen['width'] // 2, screen['height'])
wm.move_window(pid, screen['width'] // 2, 0)
```

### Full Screen
```python
screen = a.get_screen_resolution()
wm.move_window(pid, 0, 0)
wm.resize_window(pid, screen['width'], screen['height'])
```

### Click at Coordinates
```python
result = inp.click_at(x, y)
```

### Type Text
```python
result = inp.type_string("Hello world")
```

### Press Key Combination
```python
result = inp.press_key("cmd+tab")  # Switch apps
result = inp.press_key("cmd+c")    # Copy
result = inp.press_key("enter")    # Enter
```

## Key Combinations Reference

| Modifier | Keys Available |
|----------|----------------|
| `cmd` | Any letter, tab, space, delete |
| `shift` | Any letter, arrows |
| `ctrl` | Any letter, arrows |
| `alt/option` | Any letter |
| `fn` | Arrows, delete |

**Common combos:** `cmd+tab`, `cmd+c`, `cmd+v`, `cmd+z`, `cmd+q`, `cmd+space`, `ctrl+up`, `alt+tab`

## Allowed Apps

The security layer only allows interaction with apps in `allowed_apps.json`. Current allowed apps:
- Safari, Google Chrome, Visual Studio Code, Mail, TextEdit

To add apps, edit `.macos-sys-assist/allowed_apps.json` with the app's bundle ID.

## Tips

- **Find any app's bundle ID:** `osascript -e 'id of app "AppName"'`
- **Window operations require the app to have a visible window**
- **Click/type actions may require Accessibility permission confirmation**
- **Some apps (like Finder) have limited Accessibility support**
