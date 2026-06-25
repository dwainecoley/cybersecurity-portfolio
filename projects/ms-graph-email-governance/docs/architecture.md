# Architecture — OAuth 2.0 & Microsoft Graph API

## How It Works

This project uses the **OAuth 2.0 Authorization Code Flow** via Microsoft's MSAL (Microsoft Authentication Library) to authenticate with Microsoft Graph API and interact with an Outlook mailbox programmatically.

### Why This Matters in Security

OAuth 2.0 is the industry standard for delegated authorization. Understanding how to register an app, scope its permissions, and securely handle tokens is a foundational IAM skill used in cloud security, GRC tooling, and API security assessments.

---

## Step 1 — Azure Portal Login

Access to Azure begins at portal.azure.com. Authentication is tied to the Microsoft account that owns the Outlook mailbox being governed.

![Azure Portal Home](./screenshots/01-azure-portal-home.png)

---

## Step 2 — App Registration

A new App Registration is created inside Azure Active Directory (now Microsoft Entra ID). This gives the Python script its own identity — separate from the user — with only the permissions it needs.

**Key decisions made here:**
- **Name:** `outlook-governance-script`
- **Supported account types:** Single tenant only (My organization only)
- **Redirect URI:** None — not needed for script-based auth

![App Registration Form](./screenshots/02-app-registration-form.png)

---

## Step 3 — App Credentials

After registration, Azure generates three critical identifiers. These are used by the script to authenticate against the correct tenant and application.

| Field | Purpose |
|-------|---------|
| Application (client) ID | Identifies this specific app registration |
| Directory (tenant) ID | Identifies the Azure AD tenant (your account) |
| Object ID | Internal Azure object reference |

> ⚠️ These values are sensitive — stored in `.env` only, never committed to version control.

![App Overview IDs](./screenshots/03-app-overview-ids.png)

---

## Step 4 — Client Secret

A client secret acts as the application's password. It proves to Azure AD that the script is the legitimate registered app.

**Security practices applied:**
- 90-day expiry (short-lived credential rotation)
- Value copied once and stored in `.env` — never logged or hardcoded
- Description labeled for easy identification and future rotation

![Client Secret Created](./screenshots/04-client-secret-created.png)

---

## Step 5 — API Permissions (Least Privilege)

Only the minimum permissions required for the task are granted. No admin-level or tenant-wide scopes are used.

| Permission | Type | Purpose |
|-----------|------|---------|
| `Mail.Read` | Delegated | Read mailbox folder structure |
| `Mail.ReadWrite` | Delegated | Create and organize folders |
| `MailboxSettings.Read` | Delegated | Read inbox rules and safe senders |
| `MailboxSettings.ReadWrite` | Delegated | Create and modify inbox rules |
| `User.Read` | Delegated | Sign in and read user profile (default) |

> **Why Delegated?** Delegated permissions act on behalf of the signed-in user — appropriate for personal mailbox access. Application permissions require tenant-admin consent, which is an enterprise-level capability not available on personal Microsoft accounts.

![API Permissions Granted](./screenshots/05-api-permissions-granted.png)

---

## Auth Flow Diagram

```
[Python Script]
      |
      | 1. Authenticate with Client ID + Secret
      v
[Azure AD / Microsoft Entra ID]
      |
      | 2. Validate credentials, issue access token
      v
[Microsoft Graph API — graph.microsoft.com/v1.0]
      |
      | 3. Execute scoped operations (read mail, manage folders, rules)
      v
[Outlook Mailbox]
```

---

## Token Security Practices

| Practice | Implementation |
|---------|---------------|
| No hardcoded credentials | Loaded from `.env` via `python-dotenv` |
| `.env` never committed | Excluded via `.gitignore` |
| Short-lived tokens | MSAL handles expiry and refresh automatically |
| Least privilege scopes | Only mail and mailbox settings — nothing else |
| Token in memory only | Never written to disk or logged |
