
import json
from pathlib import Path

def load_business():
    file_path = Path(__file__).with_name("business.json")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
