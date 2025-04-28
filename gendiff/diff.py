import json


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def generate_diff(filepath1, filepath2):
   
    data1 = load_json(filepath1)
    data2 = load_json(filepath2)

    keys = set(data1.keys()).union(set(data2.keys()))
    result = []

    for key in sorted(keys):
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:  
            result.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(result) + "\n}"
