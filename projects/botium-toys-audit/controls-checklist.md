# Controls Assessment Checklist — Botium Toys

**Auditor:** Dwaine Coley
**Framework:** NIST Cybersecurity Framework (CSF)
**Date:** June 2026

---

## Administrative Controls

| Control | In Place | Risk if Missing |
|---------|----------|-----------------|
| Least Privilege | No | Employees have unnecessary access to customer PII/SPII, increasing internal attack surface |
| Separation of Duties | No | No checks against fraud or misuse of sensitive systems |
| Password Policies | No | Weak or inconsistent passwords increase risk of credential-based attacks |
| Password Management System | No | No enforcement of password standards; high IT overhead from resets |

---

## Technical Controls

| Control | In Place | Risk if Missing |
|---------|----------|-----------------|
| Firewall | Yes | N/A |
| Intrusion Detection System (IDS) | No | Breaches can go undetected indefinitely |
| Antivirus Software | Yes | N/A |
| Encryption | No | Customer PII and credit card data exposed in storage and transit |
| Backups | No | Data loss from incident would be irreversible |
| Manual Monitoring for Legacy Systems | Yes | N/A |

---

## Physical Controls

| Control | In Place | Risk if Missing |
|---------|----------|-----------------|
| Locks (offices, storefront, warehouse) | Yes | N/A |
| CCTV Surveillance | Yes | N/A |
| Fire Detection/Prevention | Yes | N/A |
| Disaster Recovery Plan | No | No process to restore operations after a disruption |

---

## Summary

| Category | Controls in Place | Controls Missing |
|----------|-------------------|------------------|
| Administrative | 0 | 4 |
| Technical | 3 | 3 |
| Physical | 3 | 1 |
| **Total** | **6** | **8** |

8 out of 14 controls are not in place. The most critical gaps are
encryption, IDS, least privilege, and disaster recovery — all of which
have direct regulatory and operational impact.
