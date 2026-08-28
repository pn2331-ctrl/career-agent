# Role-family bases and tailored resumes

Use this reference only after the relevant gate in `state-gates.md` passes.

## Choose the right artifact

| Request | Required state | Allowed output |
| --- | --- | --- |
| Diagnose a current resume | `SETUP DRAFT` | Audit and fact-interview notes only |
| Build a role-family base | `EVIDENCE READY` plus approved role-family design and layout spec | Proposed or approved base |
| Tailor for one company | `BASE APPROVED` plus selected JD | Separate company-specific draft |
| Deliver for application | Tailored draft passes all QA | Application-ready DOCX and PDF |

If a prerequisite is missing, explain the smallest next step. Do not fill the gap with a generic rewrite.

## Preserve lineage and visual authority

    source_resumes → approved role_family_bases → tailored_resumes

- Source resumes are evidence; never overwrite or company-tailor them.
- Before building a base, read `resume-layout.md` and use one approved `resume_layout/layout-spec.yaml`. A source PDF or DOCX may inform the spec, but do not require editing inside that file. Never create a resume from generic document defaults or invent a new visual system.
- A role-family base is protected after approval. To tailor, copy it to a new company directory; never edit the base or derive Company B from Company A's tailored file.
- Do not create a blended role family merely because two titles share keywords. Use one clear identity and make separate bases when the evidence order or hiring story changes materially.

## Build a role-family base

Before drafting, record:

1. Confirmed role-family design and one-sentence professional identity.
2. User-approved `layout-spec.yaml`, intended page count, and intended base path.
3. Fact records, source-resume coverage map, and skills inventory in the intended priority order.
4. The chosen evidence mode: `evidence_enriched` or `source_faithful`.
5. Material gaps and claims that must not be strengthened or appear.

Write to make existing evidence easier to retrieve, not to create a new identity from job-description language. Priority bullets must show, where evidence exists: operating problem or context; personal action, decision, or ownership; method, artifact, or deliverable; and a result, consequence, scope, or stakeholder value. In `source_faithful` mode, retain a truthful original responsibility when its outcome is missing; clarify it but do not invent a result.

Before reducing content, make a source-coverage map: retain, condense, move, or exclude each material source claim with a reason. Extract relevant skills from the full skills inventory, not from JD keywords. Keep a supported tool when it explains delivery or is material to the role family. Retain the strongest relevant detail; do not compress away credible evidence, skills, projects, or numbers just to create a shorter page. A missing metric is never a reason to erase a truthful source claim.

## Tailor lightly for a selected JD

First determine that the role is worth the user's time. A confirmed hard failure means do not tailor. For a viable role, create a JD-to-fact map containing:

1. Material responsibilities, qualifications, tools, and evidence types.
2. The exact verified fact or evidence-story source for every proposed change.
3. Unsupported requirements, recorded as gaps rather than claims.
4. The selected approved base and new output path.

Make the smallest truthful changes that clarify fit: usually summary language, skill ordering, evidence ordering, and a few supported bullet refinements. Map each JD term as `directly supported`, `transferable`, or `unsupported`. Feature direct matches; phrase transferable evidence conservatively; record unsupported terms as gaps. Never rewrite the whole resume, manufacture a product identity, convert responsibilities into unsupported skills, or add a metric, tool, credential, domain, or years of experience to satisfy a JD.

## Content quality rules

During base-building and tailoring, require all of the following:

1. One recognizable professional identity in the top third.
2. Evidence-led bullets, not duty lists or AI-sounding summaries.
3. Visible ownership, concrete artifact or method, and credible consequence where verified.
4. Metrics only from sources; otherwise use verified scope, stakeholder, decision, or deliverable.
5. Natural JD language only beside supporting evidence.
6. A skill appears only when it exists in the skills inventory and has a nearby source or fact-record reference. The skills section is a retrieval index, not proof by itself.
7. No generic italic explanation lines, empty buzzwords, or keyword-stuffed skill taxonomies.
8. Balanced, readable use of the approved page specification; do not shrink body text or leave avoidable large blank areas.

Read `resume-qa.md` after every draft. Never call an artifact application-ready until all blocking gates pass.

## Storage

    resume_templates/<selected-template>
    role_family_bases/<role-family>/drafts/<version>.docx
    role_family_bases/<role-family>/approved/<version>.docx
    tailored_resumes/<company>/<role-slug>/<company>_<role-slug>_<date>_vN.docx

Create matching PDFs only after the relevant QA passes. Preserve submitted, approved, and source versions.
