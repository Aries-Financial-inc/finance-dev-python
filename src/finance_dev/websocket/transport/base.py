"""Protocol-independent subscription replay helpers."""

import json
from typing import Any


def subscription_key(message: dict[str, Any]) -> str:
    return json.dumps(
        {"type": message.get("type"), "payload": message.get("payload")},
        sort_keys=True,
        separators=(",", ":"),
    )


def apply_unsubscribe(
    active: dict[str, dict[str, Any]], message: dict[str, Any]
) -> None:
    """Update canonical active subscriptions for full and field-level removals."""
    payload = message.get("payload")
    requested = payload if isinstance(payload, list) else [payload]
    for removal in requested:
        if isinstance(removal, str):
            removal = {"symbol": removal}
        if not isinstance(removal, dict):
            continue
        symbol = removal.get("symbol")
        if not symbol:
            continue
        full = set(removal) <= {"symbol", "type"}
        for key, subscription in list(active.items()):
            body = subscription.get("payload")
            items = body if isinstance(body, list) else [body]
            kept = []
            for original in items:
                if not isinstance(original, dict) or original.get("symbol") != symbol:
                    kept.append(original)
                    continue
                current = dict(original)
                if full:
                    continue
                for category in ("quote", "trade", "level2", "timeAndSales", "greeks"):
                    if removal.get(category):
                        if category == "quote":
                            current.pop("quoteFields", None)
                        elif category == "trade":
                            current.pop("tradeFields", None)
                        elif category == "greeks":
                            current.pop("greeksFields", None)
                        else:
                            current.pop(category, None)
                for field in ("quoteFields", "tradeFields", "greeksFields"):
                    removed = removal.get(field)
                    existing = current.get(field)
                    if removed and isinstance(existing, list):
                        remaining = [
                            value for value in existing if value not in removed
                        ]
                        if remaining:
                            current[field] = remaining
                        else:
                            current.pop(field, None)
                # Chart messages carry a single data mode in `type` and have no
                # other fields to preserve after the symbol is removed.
                if len(current) <= 2 and "symbol" in current and "type" in current:
                    continue
                if len(current) == 1 and "symbol" in current:
                    continue
                kept.append(current)
            if not kept:
                active.pop(key, None)
            elif isinstance(body, list):
                subscription["payload"] = kept
                active.pop(key, None)
                active[subscription_key(subscription)] = subscription
            else:
                subscription["payload"] = kept[0]
                active.pop(key, None)
                active[subscription_key(subscription)] = subscription
