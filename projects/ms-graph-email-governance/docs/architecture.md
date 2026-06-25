# Architecture — OAuth 2.0 & Microsoft Graph API

## How It Works

This project uses the **OAuth 2.0 Authorization Code Flow** via Microsoft's MSAL (Microsoft Authentication Library) to authenticate with Microsoft Graph API and interact with an Outlook mailbox programmatically.

### Why This Matters in Security

OAuth 2.0 is the industry standard for delegated authorization. Understanding how to register an app, scope its permissions, and securely handle tokens is a foundational IAM skill used in cloud security, GRC tooling, and API security assessments.

---

## Auth Flow Diagram

```
[User / Script]
      |
      | 1. Request token with scopes
      v
[Azure AD App Registration]
      |
      | 2. Validate credentials, issue access token
      v
[Microsoft Graph API]
      |
      | 3. Execute scoped operations (read mail, manage folders, etc.)
      v
[Outlook Mailbox]
```

---

## Scopes Used (Least Privilege)

| Scope | Purpose |
|-------|---------|
| `Mail.Read` | Read mailbox folders and messages |
| `Mail.ReadWrite` | Create and organize folders |
| `MailboxSettings.Read` | Read inbox rules and safe senders |
| `MailboxSettings.ReadWrite` | Create and modify inbox rules |

> **Security Note:** No admin-level or tenant-wide scopes are used. This follows the principle of least privilege — the app can only touch mail, nothing else.

---

## Token Security Practices

- Access tokens stored in memory only — never written to disk
- Credentials loaded from `.env` file — never hardcoded
- `.env` excluded from version control via `.gitignore`
- Token expiry respected — refresh handled by MSAL automatically
