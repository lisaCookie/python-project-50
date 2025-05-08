import json
import os
import sys

from gendiff.load_yaml import load_yaml


def load_file(filepath):
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return load_yaml(filepath)
    elif filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported file format")


def compute_diff(data1, data2):
    diff = []
    keys = set(data1.keys()).union(set(data2.keys()))

    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff.append({'key': key, 'type': 'removed', 
                          'old_value': data1[key]})
        elif key not in data1 and key in data2:
            diff.append({'key': key, 'type': 'added', 
                          'new_value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({'key': key, 'type': 'nested', 
                          'children': compute_diff(data1[key], 
                                                   data2[key])})
        elif data1[key] != data2[key]:
            diff.append({'key': key, 'type': 'modified', 
                          'old_value': data1[key], 
                          'new_value': data2[key]})
        else:
            diff.append({'key': key, 'type': 'unchanged', 
                          'value': data1[key]})

    return diff


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def stylish(diff, depth=0):
    indent = '    ' * depth
    result = []

    for item in diff:
        key = item['key']
        if item['type'] == 'added':
            result.append(f"{indent}  + {key}: "
                          f"{format_value(item['new_value'])}")
        elif item['type'] == 'removed':
            result.append(f"{indent}  - {key}: "
                          f"{format_value(item['old_value'])}")
        elif item['type'] == 'modified':
            result.append(f"{indent}  - {key}: "
                          f"{format_value(item['old_value'])}")
            result.append(f"{indent}  + {key}: "
                          f"{format_value(item['new_value'])}")
        elif item['type'] == 'nested':
            result.append(f"{indent}    {key}: {{")
            result.append(stylish(item['children'], depth + 1))
            result.append(f"{indent}    }}")
        elif item['type'] == 'unchanged':
            result.append(f"{indent}    {key}: "
                          f"{format_value(item['value'])}")

    return '\n'.join(result)


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)
    
    diff = compute_diff(data1, data2)

    if format_name == 'stylish':
        return "{\n" + stylish(diff) + "\n}"


def main():
    if len(sys.argv) != 3:
        print("Usage: gendiff file1.yaml file2.yaml or "
              "gendiff file1.json file2.json")
        sys.exit(1)

    filepath1 = os.path.join('files', sys.argv[1])
    filepath2 = os.path.join('files', sys.argv[2])
    
    differences = generate_diff(filepath1, filepath2)
    print(differences)


if __name__ == "__main__":
    main()