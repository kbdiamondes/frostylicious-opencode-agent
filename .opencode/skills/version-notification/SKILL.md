---
name: version-notification
description: Add a version-aware update notification system — auto site title, localStorage-based version detection, push notification on version change, "What's New" modal with user-facing changelog.
---

## What I Do
I create a version notification system for web apps. When the version changes, the system pushes a notification to the in-app notification panel, auto-shows a "What's New" modal, and updates the site title. Version detection uses localStorage comparison so it only fires once per update.

## When to Use Me
- User wants a "What's New" or update notification on version change
- User wants the site title to auto-update with version number
- User wants clickable notifications that reveal version details
- The app already has a notification panel/modal system (or you're creating one)

## Steps

### 1. Create version config module (e.g. `js/version.js`)

```javascript
const APP_VERSION = '1.0.0';
const VERSION_DATE = '2026-06-27';
const VERSION_CHANGES = [
  'User-facing description of change 1 (non-technical)',
  'User-facing description of change 2 (non-technical)',
];

function updateSiteTitle() {
  document.title = `App Name v${APP_VERSION} — Tagline`;
}

function checkVersionUpdate() {
  const lastSeen = localStorage.getItem('appLastSeenVersion');
  const current = APP_VERSION;
  if (lastSeen !== current) {
    localStorage.setItem('appLastSeenVersion', current);
    pushNotification('update', `🚀 Updated to v${APP_VERSION} — ${VERSION_DATE}`);
    showVersionModal();
  }
}

function showVersionModal() {
  const overlay = document.getElementById('modalOverlay');
  const content = document.getElementById('modalContent');
  if (!overlay || !content) return;
  content.innerHTML = `
    <div style="padding:24px;">
      <div style="text-align:center;margin-bottom:20px;">
        <div style="font-size:32px;">🚀</div>
        <div style="font-family:'Syne',sans-serif;font-size:20px;font-weight:800;">
          What's New — v${APP_VERSION}
        </div>
        <div style="font-size:12px;color:var(--text-muted);">${VERSION_DATE}</div>
      </div>
      ${VERSION_CHANGES.map(c => `<div style="padding:8px 0;font-size:13px;">✦ ${c}</div>`).join('')}
      <button class="btn btn-accent" onclick="closeModalDirect()" style="width:100%;">Got it</button>
    </div>
  `;
  overlay.classList.add('active');
}

function onVersionNotifClick() {
  closeModalDirect();
  showVersionModal();
}
```

### 2. Add to app init

Call `updateSiteTitle()` and `checkVersionUpdate()` after the app's main render function completes — in every auth/init path (logged in, viewer, no session, re-entry).

### 3. Make notifications clickable

In your notification panel renderer, add `cursor:pointer` and `onclick` for notification type `'update'`:

```javascript
const isUpdate = n.type === 'update';
`<div style="${isUpdate ? 'cursor:pointer;' : ''}" ${isUpdate ? 'onclick="onVersionNotifClick()"' : ''}>...</div>`
```

### 4. Add version.js to script load order

Add `<script src="js/version.js"></script>` after store.js/state module so it has access to the notification system.

## Tips
- **Version string in HTML title**: Set a static initial value in `<title>` (e.g. `v1.0.0`) so it's correct even before JS runs. `updateSiteTitle()` overrides it dynamically.
- **localStorage key**: Use `appLastSeenVersion` to avoid collisions with other apps. Change the prefix per project.
- **First-time users**: Users who never had the key set will see the modal on first visit. This is intentional — it introduces the what's-new system.
- **Modal styling**: Adapt `showVersionModal()` to match your app's modal system (class-based overlay toggle, innerHTML rendering).
- **Bump version on each deploy**: Change `APP_VERSION` at the top of version.js whenever you ship changes. Update `VERSION_CHANGES` with user-facing descriptions.
