import json
from datetime import date
from pathlib import Path

from agents import Agent, Runner, function_tool

from app.ai.instructions import AGENT_INSTRUCTIONS

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


@function_tool
def get_business_snapshot() -> str:
    """Return the current demo business profile and weekly targets."""
    return (DATA_DIR / "business.json").read_text(encoding="utf-8")


@function_tool
def get_inventory() -> str:
    """Return current demo inventory."""
    return (DATA_DIR / "inventory.json").read_text(encoding="utf-8")


@function_tool
def calculate_margin(selling_price_kes: float, landed_cost_kes: float) -> str:
    """Calculate gross profit and gross margin for one item."""
    if selling_price_kes < 0 or landed_cost_kes < 0:
        raise ValueError("Prices cannot be negative")
    profit = selling_price_kes - landed_cost_kes
    margin = (profit / selling_price_kes * 100) if selling_price_kes else 0
    return json.dumps(
        {
            "selling_price_kes": selling_price_kes,
            "landed_cost_kes": landed_cost_kes,
            "gross_profit_kes": round(profit, 2),
            "gross_margin_percent": round(margin, 2),
        }
    )


@function_tool
def make_daily_plan(priority: str = "sales") -> str:
    """Create a practical daily execution plan."""
    return json.dumps(
        {
            "date": str(date.today()),
            "priority": priority,
            "plan": [
                "Reconcile yesterday's sales, cash collected and pending orders.",
                "Respond to all pending WhatsApp/Instagram enquiries.",
                "Follow up warm leads and abandoned purchase conversations.",
                "Publish one product, education or offer asset.",
                "Review low-stock and dead-stock items before purchasing.",
                "Review customer issues, quality defects and returns.",
                "Close the day with sales, margin, cash and tomorrow's top 3 priorities.",
            ],
        }
    )


copilot = Agent(
    name="Nairobi Style Copilot",
    instructions=AGENT_INSTRUCTIONS,
    tools=[get_business_snapshot, get_inventory, calculate_margin, make_daily_plan],
)


def run_agent(prompt: str) -> str:
    """Run the copilot. Requires OPENAI_API_KEY at runtime."""
    result = Runner.run_sync(copilot, prompt)
    return str(result.final_output)
