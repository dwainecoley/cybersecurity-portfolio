# Microsoft Graph API Configuration
# No credentials stored here — loaded from .env

GRAPH_API_BASE = "https://graph.microsoft.com/v1.0"
AUTHORITY = "https://login.microsoftonline.com/{tenant_id}"

# Least-privilege scopes
SCOPES = [
    "Mail.Read",
    "Mail.ReadWrite",
    "MailboxSettings.Read",
    "MailboxSettings.ReadWrite"
]
