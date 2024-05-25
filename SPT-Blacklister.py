import json
import re


def update_cansellonragfair(file_path, item_id, value):
    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if item_id in data:
            data[item_id]["_props"]["CanSellOnRagfair"] = value

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

            print(f"{data[item_id]['_name']} was changed to {value}")
        else:
            print("Invalid item ID: {item_id}. Skipping.")
    except Exception as e:
        print(f"Error updating item ID {item_id}: {str(e)}")


def process_item_ids(file_path, item_ids, cansellonragfair_value):
    item_ids = item_ids.split(',')
    valid_id_length = 24

    for item_id in item_ids:
        item_id = re.sub(r'[^a-zA-Z0-9]', '', item_id)
        if len(item_id) != valid_id_length:
            print(f"Invalid item ID length: {item_id}. Skipping.")
            continue

        update_cansellonragfair(file_path, item_id, cansellonragfair_value)


def main():
    file_path = 'Aki_Data/Server/Database/templates/items.json'
    cansellonragfair_value = False

    while True:
        print(f"Current Blacklist value: {cansellonragfair_value}")
        item_ids = input("Enter item IDs, separated by commas. q to quit, r to toggle between True and False: ")

        if item_ids.lower() == 'q':
            break

        if item_ids.lower() == 'r':
            cansellonragfair_value = not cansellonragfair_value
            print(f"Blacklist value toggle to {cansellonragfair_value}")
            continue

        else:
            process_item_ids(file_path, item_ids, cansellonragfair_value)



if __name__ == '__main__':
    main()
