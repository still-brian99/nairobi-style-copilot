# Architecture

Phase 1 uses a modular monolith.

```text
User -> FastAPI -> Copilot Agent -> Guarded deterministic tool -> business data
```

The LLM is responsible for intent interpretation, tool selection and explanation. Deterministic Python functions own calculations and data access. This keeps financial calculations and future write operations auditable and testable.

## Phase 1 boundaries

Read-only tools: business snapshot, inventory, margin calculation and daily planning.

Approval-gated future tools: refunds, supplier purchase commitments, material price changes, financial transfers and destructive operations.

## Growth path

Phase 2 adds customers, leads and orders. Phase 3 adds inventory movements, quality inspections and finance ledger. Phase 4 adds WhatsApp and M-Pesa adapters. Phase 5 can split specialist agents only where the workflow complexity justifies it.
