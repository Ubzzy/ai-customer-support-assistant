
import json
from pathlib import Path

def load_business():
    file_path = Path(__file__).with_name("business.json")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_business(data):
    file_path = Path(__file__).with_name("business.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    business = load_business()

    business["services"]["haircut"] = 35

    save_business(business)

    print("Updated haircut price!")