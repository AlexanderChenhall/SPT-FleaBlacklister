import json
import re

def update_cansellonragfair(file_path, item_id, value):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if item_id in data:
        data[item_id]["_props"]["CanSellOnRagfair"] = value

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        print(f"{data[item_id]['_name']} was changed to {value}")
    else:
        print("Invalid item ID. Please enter a valid ID.")

def main():
    file_path = 'Aki_Data/Server/Database/templates/items.json'
    valid_id_length = 24
    cansellonragfair_value = False

    while True:
        print(f"Current blacklist value: {cansellonragfair_value}")

        item_id = input("Enter an item ID (or 'q' to quit, 'r' to toggle blacklist value true or false): ")

        if item_id.lower() == 'q':
            break

        if item_id.lower() == 'r':
            cansellonragfair_value = not cansellonragfair_value
            print(f"Setting blacklist value to {cansellonragfair_value}")
            continue

        item_id = re.sub(r'[^a-zA-Z0-9]', '', item_id)

        if len(item_id) != valid_id_length:
            print("Invalid ID. Please enter valid ID's")

        update_cansellonragfair(file_path, item_id, cansellonragfair_value)

if __name__ == '__main__':
    main()

