---
name: client-reporting
description: Generate weekly/monthly ad performance reports for clients — CPL, CPA, CVR, conversions, budget recommendations. Use when user asks for client reporting, ad performance summary, or monthly report template.
---

## What I Do

I help create client-facing ad performance reports that include CPL/CPA, CVR, conversions, and budget recommendations. I follow a structured workflow to pull data, calculate metrics, analyze performance, and generate concise client messages.

## When to Use Me

- Weekly client check-ins (every Monday)
- Monthly performance reports (1st of month)
- Budget review discussions
- When user asks "what should I tell the client?"
- When user needs to report ad performance

## Steps

### 1. Ask for Data Source
Ask which platforms to pull from:
- Meta Ads Manager
- Google Ads (Report Editor)
- GA4 (if tracking issues)
- Manual verification (form entries)

### 2. Pull Data (10 min)

**Meta Ads:**
1. Go to Meta Ads Manager → Reporting
2. Set date range (last 7 days or last 30 days)
3. Pull: Spend, Leads, CPC, CTR, Landing Page Views
4. Pull by campaign/ad set if multiple

**Google Ads:**
1. Go to Google Ads → Reports → Report Editor
2. Select Monthly Conversion Report (weekly breakdown)
3. Pull: Spend, Conversions, Cost/Conv, CVR

**GA4 (if needed):**
1. Go to GA4 → Realtime or Acquisition
2. Verify key events (thank-you page visits)
3. Cross-check with Meta/Google numbers

### 3. Calculate Metrics (5 min)

| Metric | Formula |
|---|---|
| **CPL** | Total Spend ÷ Total Leads |
| **CPA** | Total Spend ÷ Total Acquisitions (if close rate data available) |
| **CVR** | Total Leads ÷ Total Clicks (or Sessions) × 100 |
| **Close Rate** | Acquisitions ÷ Leads × 100 |
| **True CPA** | CPL ÷ Close Rate |

### 4. Analyze Performance (5 min)

Ask these questions:
1. Is CPL improving or getting worse vs last period?
2. Which campaign/ad has the best CPL?
3. Which campaign/ad has the worst CPL?
4. Is CVR above or below benchmark?
5. Are we hitting conversion targets?

### 5. Determine Budget Signal (2 min)

**Increase Budget If:**
- ✅ CPL is below target
- ✅ CVR is above 5%
- ✅ Close rate is 20%+
- ✅ Volume is consistent

**Hold Budget If:**
- ⚠️ CPL is stable but not improving
- ⚠️ CVR is 3-5% (average)
- ⚠️ Close rate is 10-20%

**Decrease/Pause If:**
- ❌ CPL is above target and rising
- ❌ CVR is below 2%
- ❌ Close rate is below 10%
- ❌ 3+ weeks of no improvement

### 6. Generate Client Message (5 min)

Use this template:

> **[Client Name] — [Month/Week] Performance**
>
> **Meta Ads:**
> - [X] leads | $[XX] CPL | [X]% CVR
> - Top performer: [Campaign Name]
>
> **Google Ads:**
> - [X] conversions | $[XX] cost/conv | [X]% CVR
> - Top performer: [Campaign Name]
>
> **Recommendation:**
> - [Action: Increase/Hold/Decrease] budget on [Campaign]
> - [Next step: New creatives, pause underperformers, etc.]
>
> **Next check-in:** [Date]

### 7. Update Tracking Sheet (5 min)

1. Open daily tracking CSV for the client
2. Fill in today's data
3. Update totals
4. Save for next report

## Tips

- **Total time:** ~30 min per report
- **Weekly check-ins:** Every Monday, last 7 days
- **Monthly reports:** 1st of month, last 30 days
- **Budget reviews:** Every 2 weeks, CPL trend analysis

## Benchmarks

| Metric | Good | Average | Bad |
|---|---|---|---|
| **Meta CPL** | <$30 | $30-80 | >$80 |
| **Google CPL** | <$50 | $50-100 | >$100 |
| **Meta CVR** | >5% | 2-5% | <2% |
| **Google CVR** | >8% | 3-8% | <3% |
| **Close Rate** | >20% | 10-20% | <10% |

## Files to Reference

- `knowledge/Client_Reporting_Workflow.md` — Full workflow guide
- `knowledge/[Client]/Ads/*_DailyTracking_*.csv` — Daily tracking sheets
- `knowledge/[Client]/Ads/*_CPA_Analysis_*.csv` — CPA calculations
