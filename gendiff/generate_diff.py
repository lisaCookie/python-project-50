import json

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import stylish
from gendiff.load_yaml import parse_yaml


def load_file(filepath):
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        with open(filepath, 'r') as f:
            content = f.read()
            return parse_yaml(content)
    elif filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported file format")


def compute_diff(data1, data2):
    diff = []
    keys = set(data1.keys()) | set(data2.keys())
    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff.append(
                {'key': key, 'type': 'added', 'new_value': data1[key]} 
            )
        elif key not in data1 and key in data2:
            diff.append(
                {'key': key, 'type': 'removed', 'old_value': data2[key]}  
            )
        elif (isinstance(data1[key], dict) and
              isinstance(data2[key], dict)):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': compute_diff(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'modified',
                'old_value': data2[key], 
                'new_value': data1[key]   
            })
        else:
            diff.append({'key': key, 'type': 'unchanged', 'value': data1[key]})
    return diff


def generate_diff(filepath1, filepath2, format_name='stylish') -> str:
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)
    diff = compute_diff(data1, data2)

    if format_name == 'stylish':
        return "{\n" + stylish(diff) + "\n}"
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError("Unsupported format name")