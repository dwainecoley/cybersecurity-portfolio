"""
audit_inbox.py — Inbox Sender Analysis
Microsoft Graph API | Outlook Email Governance Project
Author: Dwaine Coley | github.com/dwainecoley

Purpose:
    Read-only script. Fetches all inbox emails and groups
    them by sender domain showing counts. No changes are made.
"""

import requests
from collections import defaultdict
from auth import get_access_token

GRAPH_API = "https://graph.microsoft.com/v1.0"


def get_all_inbox_emails(token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    emails = []
    url = f"{GRAPH_API}/me/mailFolders/inbox/messages?$top=100&$select=sender,isRead,subject"
    print("📥 Fetching inbox emails (this may take a moment)...")

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            break
        data = response.json()
        emails.extend(data.get("value", []))
        print(f"   Fetched {len(emails)} emails so far...")
        url = data.get("@odata.nextLink")

    return emails


def analyze_senders(emails):
    sender_counts = defaultdict(int)
    sender_unread = defaultdict(int)

    for email in emails:
        address = email.get("sender", {}).get("emailAddress", {}).get("address", "Unknown").lower()
        is_read = email.get("isRead", True)
        domain = address.split("@")[1] if "@" in address else address
        sender_counts[domain] += 1
        if not is_read:
            sender_unread[domain] += 1

    return sender_counts, sender_unread


def print_inbox_report(sender_counts, sender_unread, total):
    sorted_senders = sorted(sender_counts.items(), key=lambda x: x[1], reverse=True)
    print("\n" + "="*65)
    print("INBOX SENDER ANALYSIS REPORT")
    print("="*65)
    print(f"{'Sender Domain':<40} {'Emails':>7} {'Unread':>7}")
    print("-"*65)
    for domain, count in sorted_senders:
        print(f"{domain:<40} {count:>7} {sender_unread.get(domain, 0):>7}")
    print("="*65)
    print(f"Total emails analyzed: {total}")
    print(f"Total unique sender domains: {len(sender_counts)}")
    print("="*65)


if __name__ == "__main__":
    print("🔍 Starting inbox sender analysis...")
    token = get_access_token()
    emails = get_all_inbox_emails(token)
    print(f"DEBUG: Total emails fetched: {len(emails)}")
    if emails:
        sender_counts, sender_unread = analyze_senders(emails)
        print(f"DEBUG: Unique domains found: {len(sender_counts)}")
        print_inbox_report(sender_counts, sender_unread, len(emails))
    else:
        print("No emails found or access denied.")
