# Onboarding and private workspace

Use this reference only for first-time setup or a profile update.

## Initialize

Ask the user for a private workspace location, then run:

    python3 <skill-path>/scripts/init_workspace.py <workspace-path>

The initializer refuses to overwrite a non-empty folder. The workspace should not be committed to a public repository.

Treat the user-named workspace as the only permitted candidate-file scope. Do not scan its parent, sibling folders, the current project, or a home directory to locate resumes.

If the chosen workspace already contains user files but is missing the Career Agent folders, run:

    python3 <skill-path>/scripts/init_workspace.py <workspace-path> --reuse

This creates only missing template files and preserves existing files. When the user identifies a source resume in that workspace, copy it into source_resumes without altering or moving the original. Report the copy path. Do not ask the user to select internal subfolders.

## Guided intake

Treat a supplied resume as evidence, not as a statement of the user's job goal. Organize supplied source material in the private workspace; do not ask the user to choose internal subfolders.

### 1. Goals and hard rules

Before proposing, naming, or creating a role-family base, ask and confirm:

1. Which job directions or role families the user wants to pursue.
2. Which titles are acceptable for each direction, and whether the user wants distinct resume versions.
3. Location, work model, seniority, contract, industry, compensation, travel, and other relevant conditions.
4. Work authorization, future sponsorship need, and whether authorization belongs on a resume or only in application forms. Do not give legal advice.
5. Permissions for page inspection, official-link checks, tracker updates, and draft creation. External applications and messages always need fresh approval.

Record the agreed conditions as hard rules in `profile.yaml`. Summarize them and require explicit confirmation before marking setup confirmed. Do not silently change them later.

### 2. Source material and resume strategy

Ask whether the user can provide multiple recent resume versions, especially versions used for different job directions, plus relevant project material or public links. Ask which supplied document should be used as a visual reference, then create or confirm `resume_layout/layout-spec.yaml`. The user may choose a visual reference or a simple ATS-friendly layout profile; do not require that the user give the agent an editable DOCX to work inside. If a DOCX is supplied, preserve it as a reference, never as a file to overwrite.

Collect source resumes, experience, education, projects, outcomes, skills, and claims that must not be used. Extract the complete skills inventory before choosing role-family skills. Then read `evidence-audit.md`; do not generate a base from a single thin fact summary.

### 3. JD calibration

Ask for 2–5 optional job descriptions the user likes, previously applied to, or considers representative. Read `job-calibration.md` and record their patterns separately from candidate facts.

### 4. Confirmation and readiness

Summarize the profile, material received, factual gaps, evidence-readiness decision, and proposed role-family design. The user must approve the relevant layer before it becomes active:

- profile confirmation unlocks personalized search planning;
- evidence review and the chosen evidence mode unlock a role-family proposal;
- role-family and layout-spec approval unlock a base;
- an approved base unlocks tailored-resume creation.

## Store private material

| Location | Content |
| --- | --- |
| candidate_context/profile.yaml | Confirmed goals, hard conditions, authorization wording, and permissions |
| fact_inventory | Source, confirmed, limited, and conflict-open experience facts with provenance |
| skills_inventory | Extracted skills, tools, methods, domains, and supporting source facts |
| source_resumes | Original resume evidence; preserve as read-only |
| resume_layout/layout-spec.yaml | Candidate-approved page, typography, spacing, structure, and ATS rules |
| search_plans | One plan per role family |
| role_family_bases | Approved bases only |

Create a new role-family base only for a distinct professional identity requiring different positioning or evidence order. Do not create several bases because titles are merely similar.

After setup, create the first search plan from the bundled template and read search-workflow.md.
