# Workspace state and gates

Use this reference whenever a task could create a profile, search plan, base, tailored resume, or personalized job recommendation.

## State model

| State | Required evidence | Permitted work |
| --- | --- | --- |
| `SETUP DRAFT` | Private workspace and source materials may exist | Organize files; ask setup questions; extract facts only |
| `PROFILE CONFIRMED` | Goals, hard rules, authorization wording, and permissions explicitly confirmed | Create JD-calibration records and proposed role-family designs |
| `EVIDENCE READY` | Fact records, skills inventory, open gaps, and the user's evidence mode reviewed | Propose role-family bases within the documented evidence limits |
| `BASE APPROVED` | One role-family design and its layout specification approved by the user | Build or revise that protected base |
| `SEARCH READY` | Confirmed profile plus a ready search plan for the role family | Give personalized job screening and recommendations |
| `APPLICATION READY` | Worthwhile JD, selected approved base, fact map, and all resume QA gates pass | Deliver an application-ready tailored artifact |

## Blocking rules

- Without `PROFILE CONFIRMED`, do not say a role is high-fit, incompatible, worth pursuing, or unsuitable for the user's sponsorship needs. Label any output `UNCONFIGURED PREVIEW`.
- Without `EVIDENCE READY`, do not claim a role family is credible from a resume title or keyword overlap alone. A user may still request a source-faithful general resume after setup; clearly keep its positioning limits.
- Without `BASE APPROVED`, do not create a company-tailored resume. Explain the missing prerequisite instead of making a generic new document.
- A missing metric, incomplete outcome, or declined follow-up is not a base-generation block. Preserve the original claim without expanding it and record its `Evidence-limited` or `Source-faithful` state.
- A known conflict in title, date, scope, tool, or outcome requires a user choice before it becomes an active claim. Preserve the original source file regardless; do not silently resolve the conflict or upgrade either version.
- A hard failure—explicit sponsorship refusal for a user who needs it, location conflict, rejected seniority, or another confirmed hard rule—means `DO NOT PURSUE`, not a conditional recommendation.

## User revisions

Hard rules and active role families remain stable until the user explicitly revises them. Record the change, date, and affected search plans; do not silently reinterpret a condition from a new JD.
