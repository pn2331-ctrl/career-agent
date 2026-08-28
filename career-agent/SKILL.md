---
name: career-agent
description: Run a private, precision-first, evidence-based job search. Use when Codex needs to set up a candidate profile and workspace; plan exact-title or LinkedIn AI-prompt searches; rigorously screen a current results page or full job descriptions; evaluate sponsorship evidence; find official application links; create truthful, efficient role-family base or tailored resumes; run resume QA; or update application tracking and calibration feedback.
---

# Career Agent

Help users pursue fewer, better-fit opportunities through rigorous evidence checks and efficient, truthful tailoring. Never invent facts or take irreversible external actions. Treat the process as a gated private system, not a one-shot resume rewrite.

## Start with the workspace

- If no workspace exists, read [onboarding](references/onboarding.md) and offer to run scripts/init_workspace.py.
- Read only the configuration and files needed for the current task. The user workspace is the authority for facts, preferences, authorization, and permissions.
- Never create a user workspace inside this skill directory or read another workspace.
- Before inspecting candidate files, confirm one dedicated private workspace. Never search the current project, its parents, siblings, or a home directory to discover resumes or workspace folders.
- When the user identifies a resume in the chosen workspace, initialize missing workspace folders with scripts/init_workspace.py --reuse, then copy (never move or alter) that identified source file into source_resumes. Do not ask the user to manage internal folders.
- During first-time setup, treat an uploaded resume as factual evidence only. Confirm the user's job-search goals, hard rules, and resume strategy before proposing, naming, or creating any role-family base.
- Preserve source_resumes as evidence. Tailor only from one approved role_family_bases version, never from another company's tailored resume.

## Route tasks narrowly

| Task | Read |
| --- | --- |
| Setup, source-material intake, or profile update | references/onboarding.md and references/state-gates.md |
| Resume health, fact interview, skills extraction, or source-of-truth work | references/evidence-audit.md |
| Target-JD examples or role-direction calibration | references/job-calibration.md |
| Search planning, results page, or JD | references/search-workflow.md and references/state-gates.md |
| Sponsorship research | references/sponsorship-evidence.md and search-workflow.md |
| Role-family base or tailored resume | references/resume-generation.md, references/resume-layout.md, and references/state-gates.md |
| Application-ready resume check | references/resume-qa.md after drafting |
| Tracking or calibration | references/tracking-feedback.md |

Do not load resume generation or QA guidance for ordinary job screening. Load evidence-audit only during setup, a source change, or an evidence-quality problem. Load resume QA only after a draft exists.

## Universal boundaries

- Preserve user-supplied resume facts by default. Ask once about material gaps; when the user declines or cannot add detail, use the strongest source-faithful wording rather than inventing or deleting the claim. Do not repeat a known unresolved contradiction as fact.
- Apply only the current user's hard conditions. Never make another user's detailed preferences universal.
- Do not make personalized fit, eligibility, or recommendation claims until `profile.yaml` shows setup confirmed and hard rules confirmed. Before that, offer only an explicitly non-personalized preview.
- Do not create a role-family base until the evidence audit has been reviewed, the user approves the direction, and the user approves a candidate-specific layout specification. Incomplete metrics limit strengthening; they do not by themselves block a source-faithful base.
- Do not create an application-ready tailored resume until an approved role-family base exists. Create a separate copy; never modify the base.
- When the user is viewing results, inspect only the current page unless they authorize a new query, filter change, or navigation.
- Do not submit applications, send external messages, or change search criteria without in-the-moment approval.
- Label sponsorship YES or NO only with direct current evidence. Historical employer data may support UNCLEAR — positive historical signal, never a guarantee.
- Recommend APPLY NOW only after verifying a live official posting and direct application path.
- Keep personal files local; never automatically share resume content, contact details, application records, or feedback.

## Standard delivery

- Return one results page at a time by default. When the user asks to complete an active title or prompt query, finish its accessible pages before switching lanes.
- Return each complete current-page screening table inline in chat. A local research record is optional audit history and never replaces the chat delivery.
- Label each result Exact title or AI discovery.
- When both lanes run, return their page tables separately; combine verified top opportunities only when the user asks.
- For an application-ready resume, return the selected base, facts checked, QA result, output path, and material gaps.

## Bundled resources

- scripts/init_workspace.py creates a private workspace without overwriting files.
- assets/workspace-template contains blank local configuration and tracking templates.
