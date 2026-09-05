# Security

## Secrets

Never commit `.env` or API keys. Use GitHub Actions secrets for CI and platform secret stores for deployment.

## Data

Customer contact information and payment references should be treated as confidential business data. Production storage must enforce authentication, least privilege, backups and audit logging.

## Agent safety

The copilot is advisory in Phase 1. Any future tool that changes money, orders, supplier commitments or customer records must have explicit authorization and an auditable action record.
