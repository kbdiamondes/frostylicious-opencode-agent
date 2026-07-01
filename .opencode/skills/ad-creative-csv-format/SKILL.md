---
name: ad-creative-csv-format
description: Output all Meta/Facebook ad creative as two CSVs in the approved format — one main CSV with creatives as columns, one video scripts CSV with scene-by-scene breakdown. Always include UTM tracking columns.
---

## What I Do

This skill enforces a specific CSV output format for Meta ad creative deliverables. It produces two files:

1. **Main creatives CSV** — Ad elements as rows, each creative as a column. Includes UTM parameters as separate columns.
2. **Video scripts CSV** — Breakdown of each video into scenes (Opening, Setup, Activity, End Card) with timed segments.

Use this whenever producing ad creative for any client so Keith can import directly into Google Sheets without reformatting.

## When to Use Me

This skill is designed to **chain after `ad-creative`**. Once ad copy, headlines, and creative angles are finalized, use this to package them into importable CSVs.

Trigger this skill when:
- Ad creative has been generated and needs structured output
- The user mentions "CSV format," "import to Google Sheets," "put it in a CSV," or "make it importable"
- Delivering Meta/Facebook ad creative with UTM tracking

**Chained workflow:** `ad-creative` → generate copy → `ad-creative-csv-format` → output CSVs

## Steps

### Step 1: Determine the creatives

Identify how many ad sets, how many creatives per set, and the mix (images vs videos).

### Step 2: Build the main CSV (`{client}-ad-creatives-{monthYear}.csv`)

Use **columns = creatives, rows = elements** format:

```
Element,Creative_1_Name,Creative_2_Name,Creative_3_Name,...
Primary Text,"[body copy]","[body copy]","[body copy]",...
Headline,"[headline]","[headline]","[headline]",...
Description,"[description]","[description]","[description]",...
H1 Image Text,"[image overlay top]","[image overlay top]","[image overlay top]",...
H2 Image Text,"[image overlay bottom]","[image overlay bottom]","[image overlay bottom]",...
CTA,"[button text]","[button text]","[button text]",...
Ad Type,Image,Video (15s),...
Campaign,"[campaign_name]","[campaign_name]","[campaign_name]",...
UTM Source,facebook,facebook,...
UTM Medium,paid,paid,...
UTM Campaign,"[campaign_name]","[campaign_name]","[campaign_name]",...
UTM Content,"[creative_slug]","[creative_slug]","[creative_slug]",...
Video Script (15s),,"[script: OPEN → CUT → MONTAGE → END CARD]",...
Visual Direction,"[image direction]","[image direction]","[video direction]",...
Status,New,New,...
```

**H1 Image Text rules:**
- MUST be a **question** (not a statement with a question mark tacked on)
- MUST ask about the service/offer **and** assure the prospect of a good experience
- MUST include locality: "in Perth", "across WA", or similar
- Each creative MUST use a **different question type** — don't repeat "Looking for..." / "Want..." across all creatives
- **Approved question patterns:**
  - `Outcome`: "Want a [service] that [positive outcome] in Perth?"
  - `Need`: "Need [service] for your [event] in Perth?"
  - `Pain`: "Worried about [problem] ruining your [event]?"
  - `Concern`: "Is [problem] threatening your [event]?"
  - `Planning`: "Planning a [event type] in Perth?"
  - `Looking for`: "Looking for [what they want] in Perth?"
  - `Hosting`: "Hosting a [event type] in Perth?"
  - `Capability`: "Can [service] handle your [event type]?"
- Examples: "Want a wedding marquee that wows in Perth?", "Worried about rain on your Perth wedding?", "Need your marquee set up on time in Perth?"
- Don't assume the audience knows where the service operates — state it clearly

**H2 Image Text rules:**
- MUST support the H1 — answer the question or reinforce the message
- MUST clearly name the specific service offered (use "MARQUEE", "MARQUEE HIRE", or the specific product)
- MUST say why the audience must choose (USP, benefit, reason)
- Each creative MUST have a **different H2** — don't repeat the same H2 across creatives
- Examples: "Dependable MARQUEE hire that elevates your celebration", "Weatherproof MARQUEE setups for Perth weddings rain or shine"
- Don't be vague like "Dependable hire..." — say what is being hired and why they should choose

**UTM rules:**
- `utm_source` = `meta` (or `facebook` per client preference)
- `utm_medium` = `paid`
- `utm_campaign` = campaign name (snake_case, lowercase)
- `utm_content` = creative slug (snake_case, lowercase — unique per creative)

### Step 3: Build the video scripts CSV (`{client}-video-scripts-{monthYear}.csv`)

Break each video into 4 scenes per 15-second video:

```
Video,Time,Scene,Visual,Voiceover (Caption)
Creative_Name,0:00-0:03,Opening,[visual description],[voiceover text]
Creative_Name,0:03-0:07,Solution/Setup,[visual description],[voiceover text]
Creative_Name,0:07-0:12,Activity/Reveal,[visual description],[voiceover text]
Creative_Name,0:12-0:15,End Card,[Logo + CTA overlay description],[voiceover text]
```

**Scene structure for 15s video:**
- `0:00-0:03` — Opening: hook, problem, or attention grabber
- `0:03-0:07` — Solution/Setup: product/service introduction
- `0:07-0:12` — Activity/Reveal: social proof, experience, or benefits
- `0:12-0:15` — End Card: logo + CTA

### Step 4: Save to the client's knowledge directory

```
knowledge/{Client}/July 1/{client}-ad-creatives-{monthYear}.csv
knowledge/{Client}/July 1/{client}-video-scripts-{monthYear}.csv
```

## Tips

- **Always include UTM columns.** Never forget tracking parameters. Every ad creative must have a unique `utm_content`.
- **Use double quotes** around cells containing commas or line breaks in the CSV.
- **Element row names** must be exactly as shown (Primary Text, Headline, etc.) — these map to Meta Ads Manager fields.
- **Creative names** should match the naming convention used in the ad platform. Use `SMH_` prefix for Spuds, etc.
- **Ad Type** values: `Image` or `Video (15s)`.
- **Status** column: track with `New`, `Created`, `Live`, `Paused`, etc.
- **Visual Direction** column describes what the image or video should look like — serves as the brief for the designer/videographer.
- The video scripts CSV is the production brief — hand it directly to a video editor.

## Related Skills

- **ad-creative**: **Use this first** — generates the ad copy, headlines, and angles that this skill packages into CSVs. Chained workflow: `ad-creative` → `ad-creative-csv-format`.
