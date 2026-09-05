# Nairobi Style Copilot

AI business operating copilot for Nairobi men's fashion and retail entrepreneurs.

## Phase 1

The first release is a modular Python/FastAPI application with:

- one OpenAI Agents SDK copilot
- deterministic tools for business snapshots, inventory, margin calculations, and daily plans
- local SQLite persistence for a simple business dataset
- API endpoint for copilot prompts
- unit tests for core calculations and API health
- GitHub Actions CI

The LLM decides which tool to use; deterministic Python code performs calculations and data access.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
# source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`, then:

```bash
uvicorn app.main:app --reload
```

API docs: `http://127.0.0.1:8000/docs`

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/copilot \\
  -H "Content-Type: application/json" \\
  -d '{"prompt":"What should I focus on today?"}'
```

## Safety boundary

The agent does not execute refunds, supplier purchases, financial transfers, destructive changes, or material price changes in Phase 1. Those become explicit approval-gated actions in later phases.

## Roadmap

Phase 2: customer/lead CRM and orders.  
Phase 3: inventory movements, quality inspections, finance ledger, and dashboard.  
Phase 4: WhatsApp and M-Pesa integrations with verification and approval gates.  
Phase 5: specialist agents, scheduled workflows, evaluations, and controlled autonomy.
