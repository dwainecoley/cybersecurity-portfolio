# Security Audit — Botium Toys

**Course:** Google Cybersecurity Certificate (Coursera)
**Framework:** NIST Cybersecurity Framework (CSF)
**Status:** Complete
**Date:** June 2026

---

## Scenario

Botium Toys is a small U.S. toy company with a growing online presence
serving customers in the U.S. and EU. The IT department conducted an
internal security audit to assess the company's current security posture,
identify gaps in controls, and ensure compliance with PCI DSS, GDPR,
and SOC 1/2.

---

## Scope & Goals

**Scope:** The entire security program at Botium Toys — all assets,
internal processes, and compliance practices.

**Goals:**
- Assess existing controls against industry best practices
- Identify compliance gaps across PCI DSS, GDPR, and SOC 1/2
- Provide prioritized recommendations to reduce risk

---

## Risk Summary

**Risk Score: 8/10 (High)**

Botium Toys lacks several critical controls including encryption, least
privilege access, an intrusion detection system, and a disaster recovery
plan. These gaps create significant exposure to data breaches, regulatory
fines, and operational disruption.

---

## Key Findings

| Finding | Severity | Compliance Impact |
|---------|----------|-------------------|
| No encryption on customer data | Critical | PCI DSS, GDPR |
| No least privilege or separation of duties | High | SOC 1/2, PCI DSS |
| No intrusion detection system (IDS) | High | NIST CSF Detect |
| No disaster recovery plan | High | SOC 1/2 |
| No password management system | Medium | PCI DSS |

---

## Prioritized Recommendations

**1. Implement Encryption (Critical)**
Customer PII and credit card data is stored and transmitted without
encryption. This is a direct PCI DSS and GDPR violation and the
highest-risk gap identified.

**2. Apply Least Privilege and Separation of Duties (High)**
All employees currently have broad access to customer data. Access
should be restricted on a need-to-know basis to reduce internal
attack surface.

**3. Deploy an Intrusion Detection System — IDS (High)**
Without detection capability, a breach could go undetected
indefinitely.

**4. Create a Disaster Recovery Plan (High)**
No backup or recovery process exists. A single incident could cause
irreversible data loss.

**5. Implement a Password Management System (Medium)**
Enforce minimum password requirements and reduce IT overhead from
password reset tickets.

---

## Deliverables

- [Controls Assessment Checklist](./controls-checklist.md)
- [Compliance Checklist](./compliance-checklist.md)

---

## Skills Demonstrated

`Security Auditing` `Risk Assessment` `NIST CSF` `PCI DSS` `GDPR` `SOC 1/2` `Controls Assessment` `Compliance`
