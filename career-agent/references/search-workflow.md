# Search and job-screening workflow

Use this reference for search plans, job-results pages, full JDs, and official-application verification.

## Preflight

Before personalized screening, require `PROFILE CONFIRMED` and a `ready` search plan for the active role family. Confirm that the plan contains the active hard-rule snapshot, role-family design, lane, and filters.

If configuration is incomplete, return only an `UNCONFIGURED PREVIEW`: describe what a JD says, but do not label it high-fit, unsuitable, worth pursuing, or incompatible with the user's sponsorship needs. Ask for the missing profile confirmation before continuing.

## Search lanes

Each role-family plan has two independently evaluated lanes:

- Exact-title: confirmed titles and the precision baseline.
- AI-prompt: a role-specific responsibility prompt for nonstandard titles.

Never combine unrelated role families in a single prompt.

## Decide today's lane

1. If titles are clear and uncalibrated, run one exact-title query to completion, returning each page separately. Run one separate AI-prompt query to completion only when semantic discovery is relevant.
2. After calibration, run the plan's designated primary lane.
3. Add the other lane only after the active query is complete: all accessible result pages for the current exact title or AI prompt have been screened. Add it when the completed query yields too few viable roles against the user threshold, a positive example uses an uncovered title, the user requests exploration, or the plan's exploration cadence is due.
4. Keep exact title as a periodic control even if AI is primary for a title-ambiguous field.
5. Pause an AI lane when it consistently performs worse than the exact control or the user calls it too broad, too narrow, or off-target. Change one prompt variable at a time and increase its version.

Return each page before moving on. Do not switch title, prompt, lane, query, filter, or browser page without permission. If the user asks to complete an active query, finish its accessible pages before switching lanes.

## Screen one current page

1. Record lane, prompt/title version, visible filters, page date, source URL, and each visible posting age or date.
2. Read every visible title.
3. Reject at title level only when a role clearly violates a confirmed hard condition. Read the full JD when title or employer details are ambiguous.
4. For plausible roles, assess responsibilities against the approved role-family design; seniority, location, work model, compensation, contract terms, and other hard rules; current sponsorship evidence; live status; and direct official application path.
5. Deduplicate against the tracker and other lanes.
6. Return the complete user-facing table inline in chat after each page. If the user chose to complete the active query, continue its next page only after that delivery.

## Recommendation contract

Use exactly one status and state its reason:

- `APPLY NOW`: no confirmed hard block, worthwhile fit, a live official direct application path verified, and user eligibility evidence sufficient.
- `VERIFY LINK FIRST`: fit may be worthwhile, but the live official direct path is not verified.
- `HOLD — <reason>`: one material but resolvable uncertainty, such as sponsor silence, seniority ambiguity, or a missing user decision.
- `NETWORK FIRST`: the role is not an immediate application target but the employer or work is strategically relevant.
- `DO NOT PURSUE — <hard rule>`: an explicit user hard rule fails. Never use a softer status for a hard failure.

`YES` and `NO` sponsorship require a direct quote from the current JD or official current employer policy. When silent, use `UNCLEAR — JD silent`; historical data may only add `positive historical signal`, never change that to YES.

## Return table

Return an actual Markdown table, ordered from strongest eligible opportunity to clear rejection:

| Company / title | Posted | Source | Fit reason | Recommendation | Sponsorship evidence | Official application link |
| --- | --- | --- | --- | --- | --- | --- |

Only `APPLY NOW` may contain an already-verified live direct official link. Record a source URL or verified official link for other statuses when available, but label it clearly. Never say merely `UNCLEAR` or `CONDITIONAL REVIEW` without the evidence or decision reason.

End with titles reviewed, JDs opened, recommendation counts, link-verification rate, and common rejection categories.

### Chat-first delivery

The inline table is the user-facing deliverable. Return all screened roles for the current page in chat before writing, linking, or mentioning a local file. Do not replace the table with a short narrative, a file link, a screenshot, or a partial shortlist.

`job_research/*.md` is optional local audit history, not the product interface. Write it only when the user asks to save research or local recording is already authorized. If written, it must preserve the complete inline table using the exact same seven columns and decisions; it may never become the only location of results.

## Calibrate

Ask only when feedback changes the next step.

| Signal | Adjustment |
| --- | --- |
| Right titles but wrong seniority | Adjust approved filters or title modifiers |
| Adjacent jobs but wrong responsibilities | Strengthen AI responsibility anchors |
| Mostly unrelated AI results | Narrow or pause AI and return to exact control |
| Few roles but high relevance | Preserve the lane; add a separate adjacent lane |
