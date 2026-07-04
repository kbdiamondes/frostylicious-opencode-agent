---
name: marketeros-feature-stability
description: Pre-commit smoke tests, regression testing, and version bump protocol for MarketerOS. Run before every commit, after every feature, and before every version bump to prevent core features from breaking.
---

## What I Do

I enforce development workflow discipline for MarketerOS. I run smoke tests before commits, regression tests after features, and version bump protocols before releases. I prevent the "every update breaks core features" problem.

## When to Use Me

- **Before every commit** — run smoke tests to catch syntax errors and broken flows
- **After building a feature** — run regression tests for the modified area
- **Before bumping a version** — run full release candidate testing
- **When something breaks** — use the debugging protocol and file coupling map
- **When splitting large files** — use the file size guidelines

Trigger patterns:
- "About to commit" / "Before I push"
- "Feature is done" / "Ready to ship"
- "Bump version to" / "Release v0.25.x"
- "Something broke" / "X stopped working"
- "Which files affect Y?"

## Prerequisites

1. **MarketerOS project** at `/Users/keithdoesmedia/Documents/Programming/marketeros/marketeros/website/`
2. **Node.js** installed (for `node --check` syntax validation)
3. **Git** initialized in the project

## Steps

### Phase 1: Pre-Commit Smoke Test (Run Before EVERY Commit)

Run these checks. Takes <2 minutes.

#### Step 1: JavaScript Syntax Check

```bash
# From the MarketerOS website directory
cd /Users/keithdoesmedia/Documents/Programming/marketeros/marketeros/website/

# Check all JS files for syntax errors
for file in js/*.js; do
  node --check "$file" 2>&1 || echo "SYNTAX ERROR: $file"
done
```

**If any file has a syntax error → FIX IT BEFORE COMMITTING.**

#### Step 2: HTML Structure Check

```bash
# Verify script tags are balanced
SCRIPT_OPEN=$(grep -c "<script" index.html)
SCRIPT_CLOSE=$(grep -c "</script>" index.html)
echo "Script open: $SCRIPT_OPEN, close: $SCRIPT_CLOSE"
# These must be equal
```

#### Step 3: Check for Oversized Files

```bash
# Flag any JS file over 500 lines (should be split)
for file in js/*.js; do
  LINES=$(wc -l < "$file")
  if [ "$LINES" -gt 500 ]; then
    echo "WARNING: $file is $LINES lines — consider splitting"
  fi
done
```

#### Step 4: Manual Flow Verification

Confirm these core flows work (do each one):

| Flow | How to Test | Expected |
|------|-------------|----------|
| Login | Open app → enter credentials → Sign In | Dashboard loads |
| Navigate | Click each sidebar item | Page renders |
| Create Client | Clients → Add Client → save | Client appears |
| Create Campaign | Campaigns → New → save | Campaign appears |
| Create Task | Tasks → Add Task → save | Task appears |
| Search | Type in search bar | Results appear |

#### Step 5: Console Error Check

Open browser DevTools → Console tab. Verify:
- [ ] No red errors
- [ ] No failed network requests
- [ ] No undefined references

#### Pre-Commit Checklist (Copy & Paste)

```
PRE-COMMIT CHECKLIST
====================
[ ] JS syntax check passed (node --check)
[ ] HTML structure balanced
[ ] No files over 500 lines
[ ] Login flow works
[ ] Dashboard loads
[ ] Can create client
[ ] Can create campaign
[ ] Can create task
[ ] Search returns results
[ ] No console errors
[ ] Sidebar navigation works
[ ] Modals open/close correctly
```

### Phase 2: Feature Regression Test (Run After EACH Feature)

After building a feature, test the modified area + dependent areas.

#### Step 1: Identify Modified Files

```bash
# See what files changed
git status
git diff --name-only
```

#### Step 2: Map to Feature Area

| Modified Files | Feature Area | Regression Test |
|---------------|--------------|-----------------|
| `js/ui.js`, `js/init.js`, `index.html` | Auth/Login | Login, logout, signup, password reset |
| `js/dashboard.js`, `css/dashboard.css` | Dashboard | Stats, charts, links, responsive |
| `js/clients.js` | Clients | CRUD, search, filtering, detail view |
| `js/launches.js` | Campaigns | CRUD, status changes, metrics |
| `js/clients.js` (tasks) | Tasks | CRUD, status, assignment, priority |
| `js/content-calendar.js` | Calendar | Events, create/edit, navigation |
| `js/sops.js` | SOPs | CRUD, copy/export, checklists |
| `js/reports.js` | Reports | Data, charts, export |
| `js/client-portal.js` | Portal | Share link, messaging, approvals |
| `js/search.js` | Search | Results for all entity types |
| `js/navigation.js` | Navigation | All routes, back/forward |
| `js/profile.js` | Settings | Profile save, workspace settings |

#### Step 3: Run Regression Test for That Area

```
REGRESSION TEST: [Feature Area]
================================
Happy Path:
[ ] Create — works without error
[ ] Read — detail view loads
[ ] Update — changes save and persist
[ ] Delete — removes correctly

Edge Cases:
[ ] Empty state — shows helpful message
[ ] Long text — doesn't break layout
[ ] Special characters — no XSS or layout issues
[ ] Rapid clicks — no duplicates created

Integration:
[ ] Appears in search results
[ ] Appears in dashboard stats
[ ] Appears in activity feed
[ ] Relates correctly to other entities

Visual:
[ ] Responsive at 768px
[ ] Responsive at 480px
[ ] Dark mode consistent
[ ] Icons render
[ ] No console errors
```

### Phase 3: Version Bump Protocol (Run Before EACH Release)

Before bumping the version number, run the full release candidate test.

#### Step 1: Pre-Bump Checks

```
PRE-BUMP CHECKLIST
==================
[ ] All features for this version complete
[ ] Smoke test passes
[ ] Regression test for modified areas passes
[ ] No console errors
[ ] No broken images/icons
[ ] Responsive at 768px and 480px
```

#### Step 2: Bump Version

```javascript
// In js/version.js — update this value
const APP_VERSION = '0.25.5'; // ← Change this
```

#### Step 3: Update Changelog

Add entry to `docs/changelog-user-guide.md`:

```markdown
## v0.25.5 — [Feature Name]

### What's New
- [Feature description]

### Fixes
- [Bug fix description]

### Files Changed
- `js/feature.js` — [what changed]
```

#### Step 4: Post-Bump Verification

```
POST-BUMP CHECKLIST
===================
[ ] Version number updated
[ ] Changelog updated
[ ] All pages still load
[ ] Auth flow works
[ ] Dashboard loads
[ ] No regressions
```

### Phase 4: Debugging Protocol (When Something Breaks)

#### Step 1: Identify Scope

- Is it **one page** or **all pages**?
- Is it **one feature** or **multiple features**?
- Did it work **before** the last commit?

#### Step 2: Check Console

Open DevTools → Console. Look for:
- Red errors = bugs
- Yellow warnings = potential issues
- Network failures = API errors

#### Step 3: Check the File Coupling Map

**When you modify a file, test the files it affects:**

| File You Modified | Also Test These |
|-------------------|-----------------|
| `index.html` | ALL JS files, ALL CSS files |
| `js/init.js` | `js/ui.js`, login flow, session |
| `js/ui.js` | `js/init.js`, auth modal, sign in/up |
| `js/navigation.js` | ALL page JS files, sidebar |
| `js/dashboard.js` | `js/clients.js`, `js/launches.js`, stats |
| `js/clients.js` | `js/dashboard.js`, `js/search.js`, tasks |
| `js/launches.js` | `js/dashboard.js`, `js/metrics.js`, campaigns |
| `js/sops.js` | `js/checklists.js`, SOP CRUD |
| `js/search.js` | `js/clients.js`, `js/launches.js`, `js/sops.js` |
| `js/reports.js` | `js/clients.js`, `js/launches.js`, charts |
| `js/client-portal.js` | `js/sharing.js`, `js/messaging.js`, portal |
| `css/base.css` | ALL components |
| `css/components.css` | Buttons, cards, tags |
| `css/dashboard.css` | Dashboard layout |

#### Step 4: Binary Search (If You Don't Know What Broke It)

```bash
# Find the last good commit
git log --oneline -10

# Test each commit
git checkout [commit-hash]
# Test in browser
git checkout main
```

#### Step 5: Fix and Test

1. Fix the bug
2. Run smoke test
3. Run regression test for the affected area
4. Commit with clear message

## File Size Guidelines

Keep files under 500 lines. When they exceed this, split:

| Current File | Lines | Split Into |
|-------------|-------|-----------|
| `dashboard.js` | 1074 | `dashboard.js`, `dashboard-stats.js`, `dashboard-charts.js` |
| `clients.js` | 894+ | `clients.js`, `client-tasks.js`, `client-detail.js` |
| `launches.js` | 802+ | `launches.js`, `campaign-metrics.js`, `campaign-detail.js` |
| `sops.js` | 645 | `sops.js`, `sop-templates.js` |
| `profile.js` | 688 | `profile.js`, `csv-import.js`, `settings.js` |

## Safe Development Rules

1. **One feature per commit** — don't bundle unrelated changes
2. **Test before you commit** — run the smoke test (2 min saves 30 min debugging)
3. **Keep files small** — split when over 500 lines
4. **Don't modify shared state directly** — use functions that coordinate updates
5. **Use feature flags** — for big changes, toggle on/off without breaking

## Quick Reference

### Before Every Commit
```
□ node --check js/*.js
□ Test login flow
□ Test the feature you changed
□ Check console for errors
```

### After Every Feature
```
□ Run regression test for that area
□ Test edge cases
□ Test responsive (768px, 480px)
□ Test integration (search, dashboard)
```

### Before Every Version Bump
```
□ All features complete
□ Full regression test passes
□ No console errors
□ Version number updated
□ Changelog updated
```

### When Something Breaks
```
□ Check console for errors
□ Identify scope (one page vs all)
□ Check file coupling map
□ Binary search git history if needed
□ Fix, test, commit
```

## Tips

- **2 minutes of testing saves 30 minutes of debugging.** Always run the smoke test.
- **One feature per commit.** If something breaks, you know exactly what caused it.
- **Check the coupling map.** If you modified `js/clients.js`, test `js/dashboard.js` and `js/search.js` too.
- **Split large files.** 500+ line files are a ticking time bomb.
- **Use feature flags for big changes.** Ship code without activating it, test in production, flip the switch when ready.
