# Email Governance – Microsoft Graph API

**Author:** Dwaine Coley
**Language:** Python
**API:** Microsoft Graph API (v1.0)
**Auth:** OAuth 2.0 — Azure AD App Registration (Least Privilege)
**Status:** 🔄 In Progress
**Started:** June 2026

---

## Overview

This project automates the audit and restructuring of a personal Outlook inbox using Python and the Microsoft Graph API. It demonstrates real-world application of identity-scoped API access, least-privilege OAuth 2.0 configuration, and email governance controls — all directly relevant to GRC and Cloud Security roles.

---

## Security Concepts Demonstrated

| Concept | Implementation |
|--------|---------------|
| Identity & Access Management | Azure AD App Registration, OAuth 2.0 scopes |
| Least Privilege Principle | Scoped API permissions (read/write mail only) |
| Data Governance | Folder taxonomy design and classification logic |
| Security Controls | Inbox rules as documented access controls |
| Automation & Scripting | Python scripts for audit and remediation |
| Token Hygiene | Short-lived tokens, `.env` secrets management |

---

## Project Structure

```
ms-graph-email-governance/
├── README.md                  ← This file
├── docs/
│   ├── architecture.md        ← OAuth 2.0 flow and Graph API design
│   ├── folder-taxonomy.md     ← Inbox classification decisions
│   └── rules-policy.md        ← Inbox rules as documented controls
├── scripts/
│   ├── auth.py                ← OAuth token acquisition (MSAL)
│   ├── audit_folders.py       ← Export current folder structure
│   ├── create_folders.py      ← Build new folder taxonomy
│   ├── audit_rules.py         ← Export and review inbox rules
│   ├── create_rules.py        ← Apply new ruleset
│   └── audit_safe_senders.py  ← Review safe/blocked senders list
├── config/
│   └── settings.py            ← Scopes and endpoints (no credentials)
├── .env.example               ← Credential template
└── requirements.txt           ← Python dependencies
```

---

## Skills Demonstrated

`Python` `Microsoft Graph API` `OAuth 2.0` `Azure AD` `IAM` `Data Governance` `Inbox Rules` `Security Automation` `Least Privilege` `Token Hygiene`
