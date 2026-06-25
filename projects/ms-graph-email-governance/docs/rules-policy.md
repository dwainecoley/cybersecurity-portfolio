# Inbox Rules Policy

## Purpose

Inbox rules function as **automated access controls** — they determine how incoming information is routed, retained, and surfaced. Documenting them as a policy mirrors how security controls are documented in GRC frameworks.

---

## Rule Design Principles

1. **Specificity** — Rules target sender domain or subject keywords, not broad wildcards
2. **Non-destructive** — No rules auto-delete; items are moved, not removed
3. **Auditable** — Every rule is documented here with its trigger and action
4. **Least Action** — Rules do the minimum needed (move, not mark-read or delete)

---

## Rule Registry

| Rule Name | Trigger | Action | Folder Destination |
|-----------|---------|--------|-------------------|
| Job Boards | From: indeed.com, dice.com, linkedin.com | Move | Career & Job Search |
| Cert Providers | From: comptia.org, coursera.org, tryhackme.com | Move | Cybersecurity & Certs |
| Banking | From: bank domains | Move | Finance & Banking |
| Receipts | Subject contains: order, receipt, invoice, confirmation | Move | Receipts & Orders |
| Subscriptions | Header: List-Unsubscribe present | Move | Subscriptions |

---

## Safe Senders Audit Checklist

- [ ] Review all entries in Safe Senders list
- [ ] Remove domains that are no longer active vendors/contacts
- [ ] Ensure no broad wildcard domains (e.g. `*.com`) are present
- [ ] Verify blocked senders list is current
- [ ] Document final safe senders list in this file after audit
