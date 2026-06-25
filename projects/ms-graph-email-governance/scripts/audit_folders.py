"""
audit_folders.py — Audit Current Outlook Folder Structure
Microsoft Graph API | Outlook Email Governance Project
Author: Dwaine Coley | github.com/dwainecoley

Purpose:
    Read-only script. Pulls all mail folders from Outlook
    and prints a structured report. No changes are made.
"""

import requests
from auth import get_access_token

GRAPH_API = "https://graph.microsoft.com/v1.0"


def get_folders(token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"{GRAPH_API}/me/mailFolders?$top=50"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
        return []


def get_subfolders(token, folder_id):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"{GRAPH_API}/me/mailFolders/{folder_id}/childFolders?$top=50"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("value", [])
    return []


def print_folder_report(folders, token):
    print("\n" + "="*60)
    print("OUTLOOK FOLDER AUDIT REPORT")
    print("="*60)
    print(f"{'Folder Name':<35} {'Total':>6} {'Unread':>7}")
    print("-"*60)

    for folder in folders:
        name = folder.get("displayName", "Unknown")
        total = folder.get("totalItemCount", 0)
        unread = folder.get("unreadItemCount", 0)
        folder_id = folder.get("id")
        print(f"{name:<35} {total:>6} {unread:>7}")

        subfolders = get_subfolders(token, folder_id)
        for sub in subfolders:
            sub_name = f"  └─ {sub.get('displayName', 'Unknown')}"
            print(f"{sub_name:<35} {sub.get('totalItemCount', 0):>6} {sub.get('unreadItemCount', 0):>7}")

    print("="*60)
    print(f"Total folders found: {len(folders)}")
    print("="*60 + "\n")


if __name__ == "__main__":
    print("🔍 Fetching Outlook folder structure...")
    token = get_access_token()
    folders = get_folders(token)
    if folders:
        print_folder_report(folders, token)
    else:
        print("No folders found or access denied.")
