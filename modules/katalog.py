import json
from pathlib import Path

KATALOG_PATH = Path("config/katalog.json")

def get_katalog():
    if KATALOG_PATH.exists():
        with open(KATALOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def get_lieferanten():
    return sorted(set(item["lieferant"] for item in get_katalog()))

def get_arten(lieferant):
    return [item for item in get_katalog() if item["lieferant"] == lieferant]