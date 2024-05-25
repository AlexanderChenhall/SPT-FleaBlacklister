import json

def update_cansellonragfair(file_path, item_ids, value):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item_id in item_ids:
        if item_id in data:
            data[item_id]["_props"]["CanSellOnRagfair"] = value

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print("File updated successfully.")

def main():
    file_path = r'Aki_Data/Server/database/templates/items.json'

    while True:
        item_ids_input = input("Enter item IDs, comma-separated. q to quit: ")

        if item_ids_input.lower() == 'q':
            break

        item_ids_input = item_ids_input.replace('"', '').replace("'", "").replace(" ", "")
        item_ids = [item_id.strip() for item_id in item_ids_input.split(',')]
        value_input = input("Enter the desired value for CanSellOnRagFair (True/False): ")
        value = value_input.lower()
        update_cansellonragfair(file_path, item_ids, value)

if __name__ == '__main__':
    main()

# test item_ids = ['5672cb124bdc2d1a0f8b4568', '5672cb304bdc2dc2088b456a', '5672cb724bdc2dc2088b456b']
