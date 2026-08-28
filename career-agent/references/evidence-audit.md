# Resume health audit and evidence interview

Use this reference after source materials are available and before a role-family base is proposed.

## Audit source material first

Ask whether the user has additional recent resume versions, project material, portfolio links, or application versions for distinct job directions. Preserve each supplied file in `source_resumes`; do not merge them into one invented master resume.

Extract facts into separate records under `fact_inventory` and extract all stated skills, tools, methods, domains, and deliverables into `skills_inventory/index.md`. Link each skill to a source bullet, fact record, or user confirmation; a JD keyword alone never creates a skill.

Use one of these states for each material claim: `Confirmed`, `Source-faithful`, `Evidence-limited`, or `Conflict-open`. Ask once about a material conflict before treating a version as active. Preserve every source file unchanged; do not silently resolve a conflict or promote a source claim to a verified fact.

## Evaluate the existing resume

Review each source resume for these binary questions:

1. Is the intended professional direction visible?
2. Do priority bullets show a real problem or operating context, personal action or decision, method or deliverable, and credible result, consequence, or scope?
3. Are metrics, stakeholder groups, artifacts, and tools traceable?
4. Are the strongest relevant facts near the top rather than hidden under generic duties?
5. Is the structure readable and usable as a visual template?

Do not treat a readable document or accurate job title as evidence that the resume is base-ready.

## Run a focused fact interview

For material gaps, ask only the questions needed to make an existing claim specific and interview-safe. Prefer:

- What problem, user need, or operating context made this work necessary?
- What did the candidate personally decide, create, change, validate, or coordinate?
- What artifact, method, stakeholder group, or implementation shows that ownership?
- What happened afterward: a decision, delivery, workflow consequence, scale, quality effect, or verified metric?

Do not demand a numeric metric when none exists. Record a concrete artifact, scope, decision influenced, or stakeholder value instead. Ask for missing detail once, preferably as one focused set of questions. If the user declines, cannot recall, or does not respond, preserve the strongest faithful source wording and mark it `Source-faithful` or `Evidence-limited`; never manufacture an achievement or erase a truthful responsibility merely because it has no metric.

## Make an evidence-readiness decision

Record one outcome in `fact_inventory/index.md` and explain it to the user:

- `BASE-READY`: source facts and structure can support an evidence-enriched base.
- `SOURCE-FAITHFUL READY`: the user has reviewed gaps or declined further detail; build from existing factual source wording without strengthening unsupported outcomes.
- `REPAIR-FIRST`: facts exist, but priority, wording, or structure should be rebuilt; this is not a reason to erase source content.
- `EVIDENCE-FIRST`: the requested role identity has material gaps; ask the focused questions once, then permit only source-faithful positioning if the user chooses to proceed.
- `INSUFFICIENT`: do not present the requested role identity as credible; preserve and organize the original material, but do not manufacture a targeted base.

Only move to role-family design after the user reviews the fact inventory, open gaps, and readiness decision.
