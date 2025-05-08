import json
import os
import sys

from gendiff.load_yaml import load_yaml
from formatters.plain import format_plain
from gendiff.load_json import load_json
from formatters.stylish import stylish, format_value

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



def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)
    
    diff = compute_diff(data1, data2)

    if format_name == 'stylish':
        return "{\n" + stylish(diff) + "\n}"
    elif format_name == 'plain':
        return format_plain(diff)
    else:
        raise ValueError("Unsupported format name")


def main():
    if len(sys.argv) != 4:
        print("Usage: gendiff <format> file1.yaml file2.yaml or "
              "gendiff <format> file1.json file2.json")
        sys.exit(1)

    format_name = sys.argv[1] 
    filepath1 = os.path.join('files', sys.argv[2])
    filepath2 = os.path.join('files', sys.argv[3])

    differences = generate_diff(filepath1, filepath2, format_name=format_name)
    print(differences)


if __name__ == "__main__":
    main()



