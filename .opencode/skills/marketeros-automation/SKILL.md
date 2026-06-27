---
name: marketeros-automation
description: Operate MarketerOS via Chrome DevTools — create clients, manage tasks, update launches, edit SOPs, and perform CRUD operations. Use when user asks to do anything in MarketerOS.
---

## What I Do

I operate MarketerOS (the SOP Dashboard) via Chrome DevTools. I can create clients, manage tasks, update statuses, edit SOPs, and perform any CRUD operation — all through chat.

## When to Use Me

- User says "create a client" or "add client"
- User says "create a task" or "add a task"
- User says "update task status" or "move task to..."
- User says "edit SOP" or "update SOP"
- User says "add to backlog" or "create backlog item"
- User says "check dashboard" or "show me metrics"
- Any request to interact with MarketerOS

## Prerequisites

1. **MarketerOS must be open in Chrome** — check with `list_pages`
2. **User must be logged in** — verify before any operation
3. **Screen layout** — use macOS assistant to arrange windows first (per screen-layout skill)

## Steps

### Step 1: Check Login Status

```
1. chrome-devtools_list_pages → find MarketerOS tab
2. chrome-devtools_take_snapshot → check for login modal or dashboard
3. If login modal visible → ASK USER to log in manually
4. If dashboard visible → proceed
```

**Login detection:**
- Login modal: `<div class="modal-overlay active">` with sign-in form
- Logged in: Sidebar visible with navigation items

### Step 2: Navigate to Target Page

| Target | Navigation |
|--------|------------|
| Dashboard | Click "Dashboard" in sidebar |
| Clients | Click client name in sidebar |
| Active Launches | Click "Active Launches" in sidebar |
| Backlog | Click "Backlog" in sidebar |
| SOPs | Click "SOP Library" in sidebar |
| Checklists | Click "Checklists" in sidebar |
| Calendar | Click "Calendar" in sidebar |
| Team | Click "Team Members" in sidebar |

### Step 3: Perform CRUD Operations

#### Create Client
```
1. Click "Add Client Folder" in sidebar
2. Fill modal: client name, priority, notes
3. Click save/confirm
4. Verify client appears in sidebar
```

#### Create Task (inside client)
```
1. Navigate to client folder
2. Click "Add Task" or equivalent button
3. Fill: title, description, assignees, status, dates
4. Save
```

#### Update Task Status
```
1. Navigate to client or Kanban board
2. Find task by title
3. Click status dropdown or drag to new column
4. Verify status changed
```

#### Create SOP
```
1. Navigate to SOP Library
2. Click "Add SOP"
3. Fill: title, content (WYSIWYG editor), tags
4. Save
```

#### Add Backlog Item
```
1. Navigate to Backlog
2. Click "Add Backlog Item"
3. Fill: title, description, type
4. Save
```

### Step 4: Verify & Report

After each operation:
1. Take screenshot to confirm
2. Report success/failure to user
3. Note any errors encountered

## Page IDs (for reference)

| Page | ID |
|------|-----|
| Dashboard | `page-dashboard` |
| Active Launches | `page-launches` |
| Campaign Metrics | `page-metrics` |
| Backlog | `page-backlog` |
| Calendar | `page-calendar` |
| DAM/Gallery | `page-gallery` |
| SOP Library | `page-sops` |
| Checklists | `page-checklists` |
| Website Log | `page-log` |
| Backups | `page-backups` |
| Team Members | `page-team` |
| Profile | `page-profile` |
| Kanban Board | `page-kanban` |
| Scrum Board | `page-scrum` |

## Key Functions (JS to call via evaluate_script)

| Function | Purpose |
|----------|---------|
| `openAddClientModal()` | Open add client form |
| `deleteClient(id)` | Delete a client |
| `openAddBacklogModal()` | Open add backlog form |
| `openAddSOPModal()` | Open add SOP form |
| `openAddChecklistModal()` | Open add checklist form |
| `openAddLogModal()` | Open add log entry form |
| `openAddWidgetModal()` | Open add metric widget form |
| `openCalendarItemModal()` | Open calendar item form |
| `openAssetModal()` | Open asset upload form |
| `addStatus(type)` | Add custom status |
| `removeStatus(id)` | Remove custom status |

## Tips

- **Always check login first** — don't assume user is logged in
- **Use snapshots over screenshots** — faster, gives element UIDs for clicking
- **Verify after each action** — take snapshot to confirm changes
- **Handle errors gracefully** — if action fails, report to user and suggest manual step
- **Don't navigate away from user's current tab** — open new tab if needed
