import json
import sys
import os
from gendiff.load_yaml import load_yaml, parse_yaml

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import stylish
from gendiff.help_document import format_help, help_text, format_usage

def generate_diff(filepath1, filepath2, format_name='stylish'):
 
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

def action_diff():
    if len(sys.argv) < 2:
        format_help()
        sys.exit(1)

    if sys.argv[1] in ('--help', '--h'):
        help_text()
        sys.exit(0)

    if sys.argv[1] in ('--format', '--f'):
        format_usage()
        sys.exit(0)

    if len(sys.argv) != 4:
        print("Usage: gendiff <format> file1.yaml file2.yaml or "
              "gendiff <format> file1.json file2.json")
        sys.exit(1)

    format_name = sys.argv[1]
    filepath1 = os.path.join('tests', 'test_data', sys.argv[2])  
    filepath2 = os.path.join('tests', 'test_data', sys.argv[3])  

    differences = generate_diff(filepath1, filepath2, format_name=format_name)
    print(differences)