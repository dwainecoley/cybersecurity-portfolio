"""
inbox_actions.py — Inbox Cleanup + Folder Creation + Rules
Microsoft Graph API | Outlook Email Governance Project
Author: Dwaine Coley | github.com/dwainecoley

Actions performed:
    - Delete emails from specified domains
    - Create new mail folders
    - Move existing emails into new folders
    - Create inbox rules for future auto-filtering
"""

import requests
from auth import get_access_token

GRAPH_API = "https://graph.microsoft.com/v1.0"


def get_headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def delete_emails_by_domain(token, domain):
    headers = get_headers(token)
    deleted = 0
    url = f"{GRAPH_API}/me/mailFolders/inbox/messages?$filter=contains(from/emailAddress/address,'{domain}')&$top=50&$select=id,subject"
    while url:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"❌ Error fetching emails from {domain}: {resp.status_code}")
            break
        data = resp.json()
        for msg in data.get("value", []):
            if requests.delete(f"{GRAPH_API}/me/messages/{msg['id']}", headers=headers).status_code == 204:
                deleted += 1
        url = data.get("@odata.nextLink")
    print(f"🗑️  Deleted {deleted} emails from {domain}")
    return deleted


def create_folder(token, folder_name):
    headers = get_headers(token)
    resp = requests.post(f"{GRAPH_API}/me/mailFolders", headers=headers, json={"displayName": folder_name})
    if resp.status_code == 201:
        print(f"📁 Created folder: {folder_name}")
        return resp.json()["id"]
    elif resp.status_code == 409:
        print(f"📁 Folder already exists: {folder_name}")
        search = requests.get(f"{GRAPH_API}/me/mailFolders?$filter=displayName eq '{folder_name}'", headers=headers)
        folders = search.json().get("value", [])
        return folders[0]["id"] if folders else None
    else:
        print(f"❌ Failed to create folder {folder_name}: {resp.status_code}")
        return None


def move_emails_by_domain(token, domain, folder_id):
    headers = get_headers(token)
    moved = 0
    url = f"{GRAPH_API}/me/mailFolders/inbox/messages?$filter=contains(from/emailAddress/address,'{domain}')&$top=50&$select=id"
    while url:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        data = resp.json()
        for msg in data.get("value", []):
            if requests.post(f"{GRAPH_API}/me/messages/{msg['id']}/move", headers=headers, json={"destinationId": folder_id}).status_code == 201:
                moved += 1
        url = data.get("@odata.nextLink")
    print(f"📨 Moved {moved} emails from {domain} to folder")
    return moved


def create_inbox_rule(token, rule_name, domain, folder_id):
    headers = get_headers(token)
    resp = requests.post(
        f"{GRAPH_API}/me/mailFolders/inbox/messageRules",
        headers=headers,
        json={"displayName": rule_name, "sequence": 1, "isEnabled": True,
              "conditions": {"senderContains": [domain]}, "actions": {"moveToFolder": folder_id}}
    )
    if resp.status_code == 201:
        print(f"⚙️  Rule created: {rule_name}")
        return resp.json()["id"]
    else:
        print(f"❌ Failed to create rule: {resp.status_code} — {resp.json()}")
        return None


if __name__ == "__main__":
    token = get_access_token()

    print("\n" + "="*50)
    print("STEP 1 — Deleting emails from unwanted senders")
    print("="*50)
    delete_emails_by_domain(token, "lazada.com.ph")
    delete_emails_by_domain(token, "eagereverest.com")
    delete_emails_by_domain(token, "jeromeortega.com")

    print("\n" + "="*50)
    print("STEP 2 — Creating new folders")
    print("="*50)
    tpg_id = create_folder(token, "The Points Guy")
    substack_id = create_folder(token, "Substack")

    print("\n" + "="*50)
    print("STEP 3 — Moving existing emails into new folders")
    print("="*50)
    if tpg_id:
        move_emails_by_domain(token, "thepointsguy.com", tpg_id)
    if substack_id:
        move_emails_by_domain(token, "substack.com", substack_id)

    print("\n" + "="*50)
    print("STEP 4 — Creating inbox rules for future emails")
    print("="*50)
    if tpg_id:
        create_inbox_rule(token, "Auto — The Points Guy", "thepointsguy.com", tpg_id)
    if substack_id:
        create_inbox_rule(token, "Auto — Substack", "substack.com", substack_id)

    print("\n✅ All inbox actions complete.")
