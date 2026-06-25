"""
auth.py — OAuth 2.0 Token Acquisition via MSAL
Microsoft Graph API | Outlook Email Governance Project
Author: Dwaine Coley | github.com/dwainecoley

Security Note:
  Credentials are loaded from .env — never hardcoded.
  Access tokens are held in memory only — never written to disk.
  This follows least-privilege and token hygiene best practices.
"""

import os
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]


def get_access_token():
    """
    Acquires an access token using the OAuth 2.0 client credentials flow.
    Returns the token string or raises an exception on failure.
    """
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    result = app.acquire_token_silent(SCOPES, account=None)

    if not result:
        result = app.acquire_token_for_client(scopes=SCOPES)

    if "access_token" in result:
        print("✅ Token acquired successfully.")
        return result["access_token"]
    else:
        raise Exception(f"❌ Token acquisition failed: {result.get('error_description')}")


if __name__ == "__main__":
    token = get_access_token()
    print(f"Token (first 20 chars): {token[:20]}...")
