import json

from fastapi.testclient import TestClient

from app.ai.agent import calculate_margin, get_business_snapshot, get_inventory, make_daily_plan
from app.main import app


def test_margin_calculation() -> None:
    result = json.loads(calculate_margin.on_invoke_tool(None, {"selling_price_kes": 2800, "landed_cost_kes": 1500}))
    assert result["gross_profit_kes"] == 1300
    assert result["gross_margin_percent"] == 46.43


def test_business_snapshot_is_valid_json() -> None:
    payload = json.loads(get_business_snapshot.on_invoke_tool(None, {}))
    assert payload["currency"] == "KES"
    assert "weekly_targets" in payload


def test_inventory_is_valid_json() -> None:
    payload = json.loads(get_inventory.on_invoke_tool(None, {}))
    assert len(payload) >= 1
    assert all("sku" in row for row in payload)


def test_daily_plan_contains_follow_up() -> None:
    payload = json.loads(make_daily_plan.on_invoke_tool(None, {"priority": "sales"}))
    assert any("Follow up" in item for item in payload["plan"])


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
