---
name: blog-creator
description: "A reusable prompt template for generating SEO-focused blog posts that build topical authority for a target money page."
---

## What I Do
This skill provides a structured prompt for generating high-quality, SEO-optimized blog posts designed to build topical authority for a specific 'money page' on your website.

## When to Use Me
Use me whenever you need to create supporting content (blog posts) that helps rank your core product or service pages without cannibalizing their target keywords.

## Prerequisites
- The target 'Money Page' URL
- The main target keyword you want the Money Page to rank for
- The target audience/persona context
- **MANDATORY:** Check `knowledge/TheFunDepot/Blog/blog-tracker.md` before creating any blog — this prevents duplicate topics and keywords
- **MANDATORY:** Review `knowledge/TheFunDepot/Blog/seo-best-practices.md` for 2026 SEO guidelines — Information Gain, internal linking rules, and penalty avoidance

## Steps
1. **Check the tracker first** — Read `knowledge/TheFunDepot/Blog/blog-tracker.md` to verify the target keyword doesn't already exist
2. Copy the prompt template below.
3. Fill in the placeholders (Business name, Money Page URL, Target Keyword, etc.).
4. Paste the completed prompt into Frostylicious.
5. **Log the new blog** — After creation, add the blog title, keyword, money page, and date to `knowledge/TheFunDepot/Blog/blog-tracker.md`

---

## Blog Creation Prompt Template

You are a highly experienced Australian content writer and local SEO expert specialising in Perth-based businesses.

**Your task:** Write a blog post for The Fun Depot (formerly Perth Bouncy Castle Hire). The blog's strategic purpose is to build **topical authority** around the page [INSERT MONEY PAGE URL] so that page ranks #1 for **"[INSERT TARGET KEYWORD]"** — not to rank the blog itself.

**Business context:**
- Business: The Fun Depot
- Money page to support: [INSERT MONEY PAGE URL]
- Homepage: https://www.perthbouncycastlehire.com.au
- **Note:** Only include backlinks to perthbouncycastlehire.com.au in the first/second paragraphs IF the goal is to increase Google ranking on SERP for a specific money page. If the goal is NOT to rank The Fun Depot's website, do NOT include these backlinks — the blogs should provide genuine value about Perth activities instead.

---

**SEO Strategy Rules (strictly follow these):**
- Do NOT try to rank this blog for "[INSERT TARGET KEYWORD]" — avoid overusing that exact phrase.
- DO use semantically related, supporting topics (e.g., local Perth weather, backyard party planning, event styling, seasonal considerations, etc.).
- **Only include backlinks to perthbouncycastlehire.com.au in the first or second paragraphs IF the goal is to increase Google ranking on SERP for a specific money page.** If the goal is NOT to rank The Fun Depot's website, do NOT include these backlinks — the blogs should provide genuine value about Perth activities instead.
- The blog should signal to Google that the money page is the authoritative destination for this service in Perth.

---

**Google Helpful Content Compliance (MANDATORY):**
- **Include external links to OTHER relevant Perth resources** — not just your own money page. Google's helpful content update penalises blogs that only promote one business.
- Link to official tourism sites (Tourism WA, Destination Perth), local attractions (Kings Park, Scitech, Perth Zoo), government resources (City of Perth), and community sites (Buggybuddys, local councils).
- **The blog must be genuinely helpful to the reader**, not just a vehicle for self-promotion. Activities and information should be the primary focus; your business mention should be subtle and natural.
- **Aim for 3-5 external links per blog** to demonstrate you're providing comprehensive, useful information about the topic — not just selling your service.
- **Self-promotion should appear at the end**, not dominate the content. The first 80% of the blog should be pure value; the last 20% can mention your service as one option among many.
- **Only include backlinks to perthbouncycastlehire.com.au in the first or second paragraphs IF the goal is to increase Google ranking on SERP for a specific money page.** If the goal is NOT to rank The Fun Depot's website, do NOT include these backlinks — the blogs should provide genuine value about Perth activities instead.
- **Outbound citations to other websites are ONLY added IF the goal is NOT to help a money page/homepage rank higher in Google SERP.** If the goal IS to help a money page rank higher, do NOT add outbound citations — keep link equity focused on the money page. When the goal is genuine value (not SERP ranking), add 3-5 outbound citations to relevant Perth resources (Tourism WA, Destination Perth, local councils, attractions, weather services).

---

**Writing Instructions:**
- **Skip robotic intros.** Get straight to value. Answer the core question in the first 2 lines.
- **Write naturally** — use the way locals actually speak and search, including voice-style queries like "how much space do I need for X in my backyard in Perth?"
- **Include local Perth touches** — suburbs, seasonal weather, outdoor event considerations, local event culture.
- **Include external links to relevant Perth resources** — Tourism WA, Destination Perth, Kings Park, Scitech, Perth Zoo, AGWA, City of Perth, Buggybuddys, local councils. These links demonstrate comprehensive helpfulness and avoid Google's helpful content penalty. **IMPORTANT:** Only add these outbound citations IF the goal is NOT to help a money page/homepage rank higher in Google SERP. If the goal IS to help a money page rank higher, do NOT add outbound citations — keep link equity focused on the money page.
- **Optimise for AI Overviews and Featured Snippets:**
  - Use bold H2 headings framed as questions.
  - Provide direct, clear answers at the top of each section.
  - Keep paragraphs short; use bullet points generously.
- **Tone:** Casual, helpful, trustworthy — like a knowledgeable local talking to Perth residents. No emojis.
- **Points and lists** must use proper `<ul>/<li>` or `<ol>/<li>` HTML formatting — do not use H3 tags for list items.
- **Only include backlinks to perthbouncycastlehire.com.au in the first or second paragraphs IF the goal is to increase Google ranking on SERP for a specific money page.** If the goal is NOT to rank The Fun Depot's website, do NOT include these backlinks — the blogs should provide genuine value about Perth activities instead.

---

**Required Sections:**
1. Opening paragraph — **Only include backlinks to perthbouncycastlehire.com.au IF the goal is to increase Google ranking on SERP for a specific money page.** If the goal is NOT to rank The Fun Depot's website, start with genuine value about the topic.
2. Multiple H2 sections covering supporting topics that build topical authority — **these sections should primarily provide value about the topic, not promote your service**. Include external links to other Perth resources throughout.
3. An FAQ section with **at least 5 questions** locals would realistically ask Google or a voice assistant — formatted as:
   - **Q:** [natural-sounding question]
   - **A:** [clear, helpful answer — 1 to 3 lines max]
4. A closing CTA — **Only include backlinks to perthbouncycastlehire.com.au IF the goal is to increase Google ranking on SERP for a specific money page.** If the goal is NOT to rank The Fun Depot's website, the blog should provide value, not sell.

---

**Output Format:**
- Deliver the **complete article as ready-to-paste HTML code** for a WordPress blog post widget.
- Use proper semantic HTML: `<h2>`, `<p>`, `<ul>`, `<li>`, `<strong>`, `<a href="">`, `<br>` tags.
- Include `<br>` spacing between sections for visual breathing room.
- Do **not** use H3 tags for list points or sub-items — use `<strong>` inside `<p>` or `<li>` instead.
- Do **not** include meta title, meta description, image suggestions, or SEO notes inside the HTML code — provide those **separately below the HTML block** in plain text.
- Ensure that there is proper spacing between list and paragraphs.

**After the HTML, provide separately (plain text, outside the code):**
- **Meta Title** (max 60 characters, includes keyword): DO NOT USE THE MAIN KEYWORD; our goal is to increase topical authority of the Main Pages.
- **Meta Description** (max 155 characters, natural-sounding, includes keyword).
- **SEO Notes** covering: keyword variations used, external links summary (must include 3-5 links to other Perth resources), suggested image ALT texts, content structure overview (H1, H2s, etc.), and voice-search formatting observations.
- **Pre-Publish Checklist** confirmation:
  - [ ] Information Gain: Does this page add something current ranking pages don't have?
  - [ ] No Cannibalization: Is this targeting a distinct intent from existing pages?
  - [ ] Backlinks Check: If goal is to rank money page → backlinks to perthbouncycastlehire.com.au in first/second paragraphs are OK. If goal is NOT to rank TFD → no backlinks to perthbouncycastlehire.com.au in first/second paragraphs.
  - [ ] Outbound Citations Check: If goal is to rank money page → NO outbound citations (keep link equity focused). If goal is NOT to rank money page → include 3-5 outbound citations to relevant Perth resources.
  - [ ] External Links: Does this include 3-5 links to other Perth resources (only if goal is NOT to rank money page)?
  - [ ] Helpful Content: Does this pass Google's self-assessment questions?
