# Inbox Folder Taxonomy

## Design Philosophy

A well-structured inbox is a governance artifact — it reflects how information is classified, retained, and accessed. This taxonomy applies data classification principles from GRC practice to personal email management.

---

## Proposed Folder Structure

```
Inbox/
├── 📁 Action Required       ← Needs a response or decision
├── 📁 Waiting On            ← Sent, awaiting reply
├── 📁 Reference/
│   ├── Career & Job Search
│   ├── Cybersecurity & Certs
│   ├── Coley Consulting
│   ├── Finance & Banking
│   └── Legal & Compliance
├── 📁 Receipts & Orders
├── 📁 Subscriptions
└── 📁 Archive
```

---

## Classification Logic

| Folder | Retention | Rule Trigger |
|--------|-----------|-------------|
| Action Required | Active until resolved | Manual |
| Waiting On | Active until resolved | Manual |
| Career & Job Search | 12 months | Sender domain (job boards, recruiters) |
| Cybersecurity & Certs | Indefinite | Sender (CompTIA, Coursera, TryHackMe) |
| Coley Consulting | Indefinite | Sender domain / keywords |
| Finance & Banking | 7 years | Sender domain (banks, fintech) |
| Receipts & Orders | 12 months | Subject keywords (order, receipt, invoice) |
| Subscriptions | 30 days | Unsubscribe header present |
| Archive | Indefinite | Age > 90 days, no action taken |
