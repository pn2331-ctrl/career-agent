# Career Agent regression cases

Use fictional or fully de-identified material only. Evaluate behavior, not whether wording is identical between runs.

| Case | Input state | Expected behavior |
| --- | --- | --- |
| Resume-only intake | One source resume, no profile | Extract facts only; ask for target directions, hard rules, additional resume versions, and optional target JDs before proposing a base |
| Weak source material | Duties without evidence of context, ownership, artifact, or result | Ask one focused follow-up set; if the user declines, record `SOURCE-FAITHFUL READY` and build the strongest truthful base without invented impact |
| Missing metrics | User cannot add numbers to factual source bullets | Retain the original responsibility, tool, and context; do not delete it or manufacture an outcome |
| Known conflict | Two sources disagree on a material title, date, tool, scope, or result | Ask the user to choose the active version; preserve source files and do not silently resolve or strengthen the conflict |
| Skills extraction | Source resume lists skills, tools, methods, and projects | Build a source-linked skills inventory before JD matching; label JD terms as directly supported, transferable, or unsupported |
| Multiple directions | Two target directions supported by different evidence | Create two proposed role-family designs; do not merge them into a keyword-based hybrid |
| Search before setup | No confirmed `profile.yaml` or ready plan | Return `UNCONFIGURED PREVIEW`; do not make personalized fit, eligibility, or sponsorship claims |
| Hard sponsorship failure | Confirmed sponsorship need and a JD with direct current refusal | Quote the source and return `DO NOT PURSUE — sponsorship`; never a conditional recommendation |
| Location conflict | Confirmed location hard rule conflicts with JD | Return `DO NOT PURSUE — location` |
| Valid search page | Confirmed profile and ready plan | Return the complete actual Markdown table inline in chat, with Posted, source, explicit recommendation reason, sponsorship evidence, and official-link status |
| Search-record persistence | Current-page results are optionally saved under `job_research` | Deliver the full seven-column table in chat first; a local MD may only be an identical audit copy, never a replacement or a different schema |
| Tailoring before base approval | Selected JD but role-family base remains draft | Explain the missing base approval; do not create a company resume |
| Valid tailoring | Approved base plus verified JD-to-fact map | Copy the base into a company-specific path, make limited mapped changes, retain the base, then run factual/recruiter/artifact QA |
| Layout specification | User supplies a visual reference or approves a layout profile | Create and approve a candidate-specific layout spec; output must not use generic document defaults or an unapproved visual system |
| Template fidelity | Output is rendered against an approved layout spec | Check font, margins, type scale, spacing, alignment, date/bullet geometry, page count, and density; visible `DRAFT` footers fail the artifact gate |
