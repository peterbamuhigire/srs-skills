# Feature: Fraud Detection

## Description
Real-time and near-real-time fraud risk assessment for transactions — risk
scoring, behavioral analytics, device fingerprinting, alert management,
and analyst case workflow.

## Standard Capabilities
- Real-time transaction risk scoring (< 200ms per authorization)
- Rules-based and machine-learning fraud model execution
- Velocity checks (transaction count and amount per account per time window)
- Geographic anomaly detection (impossible travel, high-risk country flags)
- Device fingerprinting and session behavioral analysis
- Card-not-present (CNP) enhanced verification (3D Secure 2.x)
- Fraud alert queue with analyst review and case disposition workflow
- Automatic transaction blocking on high-confidence fraud signals
- False positive rate monitoring and model performance reporting
- Chargeback and dispute linkage to originating fraud alerts

## Regulatory Hooks
- BSA: fraud patterns indicative of money laundering must trigger SAR review
- CFPB Reg E: unauthorized transaction dispute resolution within 10 business days
- PCI-DSS Req. 10: all fraud system access and alert dispositions must be logged

## Linked NFRs
- FIN-NFR-001 (Financial Audit Trail — all fraud decisions must be logged)
- FIN-NFR-004 (Availability — fraud scoring must be available whenever payments are processed)
- FIN-NFR-005 (Fraud Detection Response Time — ≤ 200ms at 99th percentile)
