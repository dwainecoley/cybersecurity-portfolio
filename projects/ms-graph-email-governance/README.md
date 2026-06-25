# Email Governance – Microsoft Graph API

**Author:** Dwaine Coley | [github.com/dwainecoley](https://github.com/dwainecoley)
**Language:** Python |
**API:** Microsoft Graph API (v1.0) |
**Auth:** OAuth 2.0 — Azure AD App Registration (Least Privilege) |
**Status:** 🔄 In Progress |
**Started:** June 2026

---

## Scenario

My personal Outlook inbox had accumulated 939 unorganized emails across 235 unique sender domains with no consistent folder taxonomy, no automated sorting rules, and no governance over what was coming in or where it was going. As someone transitioning into GRC and Cloud Security, I recognized this as more than a personal productivity problem — it was an opportunity to apply real information governance principles to a real system using real tools.

Rather than manually cleaning up the inbox through a GUI, I built a Python automation project that connects directly to Outlook via the Microsoft Graph API. This meant navigating Azure Active Directory, OAuth 2.0 authentication flows, API permission scoping, and Python scripting — all from scratch, on a live account.

Every decision made along the way was treated as a security and governance decision, not just a technical one.

---

## Why This Project Matters

**For IAM practice:** Registering an app in Azure Active Directory, configuring OAuth 2.0 delegated permissions, and handling token acquisition via MSAL are the same identity and access management tasks performed in enterprise cloud environments. Doing this on a real API against a live account is fundamentally different from reading about it or running a lab simulation.

**For GRC application:** Governance is not just policy on paper. Designing a folder taxonomy as a data classification exercise, documenting inbox rules as access control policies, and auditing sender domains as a threat surface review — these are information governance concepts applied at personal scale. The same principles apply at enterprise scale.

**For portfolio credibility:** Anyone can claim they understand OAuth 2.0 or least privilege. This project demonstrates it — with working code, architecture documentation, real error resolution, and a complete Git commit history. The errors encountered (AADSTS500113, externally-managed-environment, delegated vs application auth conflicts) are documented as learning artifacts, not hidden.

---

## Goals

- Register a least-privilege OAuth 2.0 application in Azure Active Directory
- Authenticate against the Microsoft Graph API using Python and MSAL
- Audit the full Outlook folder structure and inbox sender landscape programmatically
- Automate inbox cleanup — bulk deletion, folder creation, email sorting, and rule creation
- Document all decisions as governance artifacts in version-controlled markdown
- Produce a reusable, well-commented Python codebase adaptable to other Microsoft 365 environments

---

## Results

| Goal | Outcome |
|------|---------|
| Azure AD App Registration | ✅ Registered with least-privilege delegated scopes |
| OAuth 2.0 Authentication | ✅ Device Code Flow implemented — live delegated token acquired |
| Folder Audit | ✅ 41 top-level folders + full subfolder tree retrieved via API |
| Inbox Sender Analysis | ✅ 939 emails analyzed across 235 unique sender domains |
| Bulk Email Deletion | ✅ 69 emails deleted from unwanted/unknown senders |
| Folder Creation | ✅ 2 new folders created programmatically |
| Email Sorting | ✅ 25 emails moved to correct folders via script |
| Inbox Rules | ✅ 2 automated rules created for future filtering |
| Documentation | ✅ Architecture walkthrough, audit baseline, sender analysis, taxonomy, and rules policy committed to GitHub |
| Token Hygiene | ✅ Short-lived PAT tokens, .env credentials, .gitignore protection applied throughout |

---

## Security Concepts Demonstrated

| Concept | Implementation |
|--------|----------------|
| Identity & Access Management | Azure AD App Registration, OAuth 2.0 delegated scopes |
| Least Privilege Principle | Scoped API permissions — mail and mailbox settings only |
| Data Governance | Folder taxonomy designed as information classification system |
| Security Controls | Inbox rules documented as access control policies |
| Automation & Scripting | Python scripts for audit, remediation, and rule enforcement |
| Token Hygiene | Short-lived credentials, `.env` secrets, `.gitignore` protection |
| OAuth 2.0 Flows | Client credentials vs delegated auth — real-world troubleshooting |
| Redirect URI Security | OAuth 2.0 redirect URI controls as token interception prevention |
| PATH Security | Resolved real PATH conflict between system and Homebrew Python |

---

## Project Structure

```
ms-graph-email-governance/
├── README.md                        ← This file
├── docs/
│   ├── architecture.md              ← Full visual walkthrough with screenshots
│   ├── audit-baseline.md            ← Before state — folder inventory
│   ├── inbox-sender-analysis.md     ← 939 emails, 235 domains analyzed
│   ├── folder-taxonomy.md           ← Inbox classification design decisions
│   ├── rules-policy.md              ← Inbox rules as documented controls
│   └── screenshots/                 ← Step-by-step project screenshots
├── scripts/
│   ├── auth.py                      ← OAuth 2.0 token acquisition (MSAL)
│   ├── audit_folders.py             ← Retrieve full folder structure
│   ├── audit_inbox.py               ← Analyze inbox by sender domain
│   └── inbox_actions.py             ← Delete, create folders, move, create rules
├── config/
│   └── settings.py                  ← API scopes and endpoints (no credentials)
├── .env.example                     ← Credential template
├── .gitignore                       ← Protects .env and venv from version control
└── requirements.txt                 ← Python dependencies
```

---

## Skills Demonstrated

`Python` `Microsoft Graph API` `OAuth 2.0` `Azure AD` `Microsoft Entra ID` `IAM`
`Data Governance` `Inbox Rules` `Security Automation` `Least Privilege` `Token Hygiene`
`MSAL` `REST APIs` `Virtual Environments` `Git` `Technical Documentation`
