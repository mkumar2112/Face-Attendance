import json


def Extract_Name_from_Json(file_path, key):
    # Read the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Read the value of the "Name" key
    value = data.get(key)

    # Print the name or use it as needed
    print(value)

    return value

