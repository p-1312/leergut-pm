from pathlib import Path
import json
from datetime import datetime

AUFTRAEGE_PATH = Path("data/auftraege.json")
AUFTRAEGE_PATH.parent.mkdir(exist_ok=True)

def load_auftraege():
    if AUFTRAEGE_PATH.exists():
        with open(AUFTRAEGE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_auftraege(data):
    with open(AUFTRAEGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def neue_anmeldung(lieferant, art, menge, beschreibung, user):
    katalog = [k for k in __import__("modules.katalog", fromlist=[""]).get_katalog() if k["lieferant"] == lieferant and k["art"] == art][0]
    gewicht = katalog.get("gewicht_stk", 0) or (katalog.get("spule_kg", 0) + katalog.get("palette_kg", 0))
    auftraege = load_auftraege()
    nr = f"L2025-{len(auftraege)+1:04d}"
    auftraege.append({
        "nr": nr,
        "datum": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "lieferant": lieferant,
        "art": art,
        "menge": menge,
        "gewicht_gesamt": menge * gewicht,
        "beschreibung": beschreibung,
        "status": "rot",
        "user": user
    })
    save_auftraege(auftraege)
    return nr