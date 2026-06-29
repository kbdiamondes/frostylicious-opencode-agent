---
name: tfd-tracking-setup
description: Set up accurate multi-channel tracking for The Fun Depot — Meta CAPI, GA4 events, UTMs, and Google Ads phone call tracking. Use when implementing or fixing conversion tracking.
---

# The Fun Depot — Tracking Setup

Set up 100% accurate conversion tracking across Meta Ads and Google Ads for The Fun Depot.

## When to Use Me

- Implementing Meta Conversions API (CAPI)
- Setting up GA4 key events (form_submitted, phone_call)
- Adding UTM parameters to ad links
- Setting up Google Ads phone call tracking (no CallRail)
- Fixing Meta pixel underreporting (0 tracked vs 5 verified)

## Current State (June 2026)

| Channel | Conversions | Spend | CPL | Issue |
|---------|-------------|-------|-----|-------|
| Meta Ads | 5 | $897.85 | $179.57 | Pixel tracked 0 — manual verification only |
| Google Ads | 48 | $3,569.33 | $74.36 | Forms tracked, phone calls unclear |
| Blended | 53 | $4,467.18 | $84.29 | — |

**Core Problem:** Meta pixel is not capturing conversions. Need CAPI + GA4 + UTMs.

## Steps

### Part 1: Meta Conversions API (CAPI)

**Why:** Server-side tracking that works alongside Meta Pixel. Bypasses browser restrictions, iOS tracking, ad blockers.

#### Step 1: Access CAPI in Meta Events Manager
1. Go to Meta Events Manager → Connected Sources
2. Select your pixel → Set up Conversions API
3. Choose "Manual Implementation" or "Partner Integration"

#### Step 2: Generate Access Token
1. In Events Manager → Settings → Conversions API
2. Generate access token
3. Copy and save securely

#### Step 3: Implement Server-Side Tracking

**Option A: Via Google Tag Manager (Recommended)**
1. Create new server-side tag in GTM
2. Use Meta's CAPI template
3. Configure events: `Lead`, `Purchase`, `CompleteRegistration`
4. Map event parameters (content_name, content_category, value)

**Option B: Via Forminator Webhook**
1. In Forminator → Settings → Webhooks
2. Add webhook URL: `https://graph.facebook.com/v19.0/[PIXEL_ID]/events`
3. Method: POST
4. Headers: `Authorization: Bearer [ACCESS_TOKEN]`
5. Body: Map form fields to Meta event parameters

```json
{
  "data": [
    {
      "event_name": "Lead",
      "event_time": "[timestamp]",
      "user_data": {
        "em": "[hashed_email]",
        "ph": "[hashed_phone]"
      },
      "custom_data": {
        "content_name": "school_form_submission",
        "content_category": "School LP"
      }
    }
  ]
}
```

#### Step 4: Verify CAPI Events
1. Use Meta Events Manager → Test Events
2. Submit a test form
3. Check both Pixel and CAPI events appear
4. Confirm deduplication is working (event_id matching)

### Part 2: GA4 Key Events

**Why:** Independent conversion tracking that feeds into Google Ads and provides backup for Meta.

#### Step 1: Create GA4 Events

**Form Submission Event:**
1. Go to GA4 → Admin → Events → Create Event
2. Event name: `form_submitted`
3. Matching conditions:
   - `page_location` contains `/thank-you` OR
   - `page_location` contains `/confirmation` OR
   - Forminator form submit event
4. Mark as key event (conversion)

**Phone Call Event:**
1. Create event: `phone_call`
2. Matching conditions:
   - Click on `tel:` link OR
   - Phone number click tracking
3. Mark as key event (conversion)

#### Step 2: Link GA4 to Google Ads
1. Go to GA4 → Admin → Product Links → Google Ads Links
2. Link your Google Ads account
3. Import GA4 conversions into Google Ads:
   - Go to Google Ads → Tools → Conversions
   - Import → Google Analytics 4
   - Select `form_submitted` and `phone_call`

### Part 3: UTM Parameters

**Why:** Source attribution for Meta ads. Allows GA4 to attribute conversions to specific campaigns/creatives.

#### UTM Structure for Meta
```
utm_source=facebook
utm_medium=paid
utm_campaign=[campaign_name]
utm_content=[ad_creative_name]
```

#### Implementation
1. Add UTMs to all Meta ad URLs in Ads Manager
2. Use consistent naming:
   - Campaign: `tfd_july_school`, `tfd_july_sports`
   - Content: `school_creative_1`, `sports_creative_1`
3. Test: Click ad → Check GA4 → Verify source shows "facebook / paid"

### Part 4: Google Ads Phone Call Tracking

**Why:** Track phone call conversions without CallRail. Use Google's native forwarding numbers.

#### Method 1: Calls from Ads (Simplest)
1. Go to Google Ads → Tools → Conversions → + New
2. Select "Phone calls"
3. Choose "Calls from ads"
4. Set minimum call duration (e.g., 60 seconds = qualified lead)
5. Create call asset with your business phone number
6. Google replaces number with forwarding number when ad is clicked

**Requirements:**
- Call reporting enabled in account settings
- Call asset or call-only ad with your phone number
- Business in eligible country (Australia ✓)

#### Method 2: Calls to Number on Website (Recommended)
1. Go to Google Ads → Tools → Conversions → + New
2. Select "Phone calls"
3. Choose "Calls to a phone number on my website"
4. Enter your website phone number
5. Set minimum call duration
6. Install Google tag on website
7. Add phone snippet to replace number with forwarding number

**GTM Implementation:**
1. Create new tag: Google Ads Conversion Tracking
2. Conversion ID: [YOUR_ID]
3. Conversion label: [CALL_CONVERSION_LABEL]
4. Trigger: Click - Phone Number (CSS selector: `a[href^="tel:"]`)
5. Add phone snippet to landing page:

```javascript
// Google forwarding number snippet
(function() {
  var options = {
    call_reporting: true,
    phone_number: '+61XXXXXXXXX'
  };
  // Google tag implementation
})();
```

#### Method 3: Click-to-Call Tracking
1. Track when users click phone number links
2. In GTM:
   - Trigger: Click - Phone Number (matches CSS: `a[href^="tel:"]`)
   - Tag: Google Ads Conversion Tracking
   - Conversion action: "Phone Click"
3. Less accurate than forwarding numbers but simpler

#### Recommended Setup for TFD
1. **Primary:** Calls from ads (call assets) — tracks calls from Google Ads directly
2. **Secondary:** Calls to website number — tracks calls after ad click → website visit
3. **Minimum call duration:** 60 seconds (qualifies as lead)

### Part 5: Unified Dashboard

#### Daily Tracking Template
Use `knowledge/TheFunDepot/Ads/TFD_DailyTracking_July2026.csv` with columns:
- Date
- Campaign Name
- Platform (Google/Meta)
- Spend
- Conversions (forms + calls)
- CPA
- Avg CPA (blended)

#### Metrics to Track
| Metric | Source | How to Calculate |
|--------|--------|------------------|
| Total Cost | Google Ads + Meta Ads | Sum of platform spend |
| Total Conversions | GA4 (verified) | Forms + phone calls (both channels) |
| CPA by Campaign | GA4 + UTM | Cost / Conversions per campaign |
| Avg CPA (Blended) | GA4 | Total Cost / Total Conversions |

## Verification Checklist

- [ ] CAPI events firing alongside Meta Pixel
- [ ] GA4 `form_submitted` event marking as conversion
- [ ] GA4 `phone_call` event marking as conversion
- [ ] GA4 linked to Google Ads
- [ ] UTMs present on all Meta ad links
- [ ] Google Ads call reporting enabled
- [ ] Call assets added to campaigns
- [ ] Forwarding numbers appearing on website
- [ ] Minimum call duration set (60 seconds)
- [ ] Daily tracking template ready

## Tips

- CAPI + Pixel deduplication requires matching `event_id` parameters
- Test everything in staging/preview before going live
- Google forwarding numbers take up to 1 hour to activate
- Phone call tracking only works for Google Ads clicks (not organic)
- Monitor first week closely — compare Meta pixel vs CAPI vs GA4 counts
