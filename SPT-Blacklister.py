def update_cansellonragfair(file_path, item_ids, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    current_item_id = None

    for line in lines:
        if any(item_id in line for item_id in item_ids):
            current_item_id = line.strip().strip('"')

        if current_item_id and '"cansellonragfair":' in line:
            line = line.replace('"CanSellOnRagfair": true', f'"CanSellOnRagfair": {str(value).lower()}')
            line = line.replace('"CanSellOnRagfair": false', f'"CanSellOnRagfair": {str(value).lower()}')
            current_item_id = None

        updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Example usage
file_path = r"Aki_Data\Server\database\templates.json"
item_ids = ['id1', 'id2', 'id3']  # Replace with your actual item IDs
value = True  # Set to True or False depending on your desired value

update_cansellonragfair(file_path, item_ids, value)