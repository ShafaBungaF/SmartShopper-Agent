import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.mongodb import collection


def load_data():
    with open("data/common_information.json", "r", encoding="utf-8") as file:
        return json.load(file)


def store_data():
    data = load_data()

    collection.delete_many({})

    result = collection.insert_many(data)

    print(f"{len(result.inserted_ids)} data berhasil disimpan ke MongoDB.")


if __name__ == "__main__":
    store_data()