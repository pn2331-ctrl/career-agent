# Resume layout specification

Use this reference for every role-family base and tailored resume. Read it with `resume-generation.md`; the layout specification is a hard delivery condition, not a styling suggestion.

## Establish one candidate-specific spec

Store the active spec at `resume_layout/layout-spec.yaml`. It may be distilled from a source PDF/DOCX or deliberately selected as an ATS-friendly profile. An editable template is helpful but not required; never overwrite it or require generation inside it.

Before the first base, confirm the intended page size and count, margins, type system, paragraph rhythm, section order, experience/date layout, bullet geometry, contact layout, and ATS constraints. If a value is unknown, propose a value and obtain approval before drafting. Do not substitute generic document defaults.

## Build from the spec

Generate the resume from structured content and the approved numeric tokens. Preserve the approved hierarchy and information density. Do not introduce a new centered header, font family, title treatment, footer, columns, tables, icons, or decorative system unless the spec explicitly allows it.

The resume page must not display `DRAFT`, QA status, internal paths, or evidence labels. Keep that metadata in its filename, workspace record, and delivery note.

## Render gate

Render the reference (if one exists) and output. Inspect them side by side. A layout passes only if it matches the active spec and has no clipping, overlap, bad wrapping, avoidable blank area, or date/bullet misalignment. A one-page output that leaves a large avoidable blank area fails density review; recover verified source content before shrinking or padding text.

For tailored resumes, retain the exact approved base layout. Content may change only within the approved base's layout budget.
