import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SCENARIO_FILE = BASE_DIR / "scenarios" / "scenarios.json"


def load_scenarios():

    with open(
        SCENARIO_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)
