import json
import sys

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import stylish
from gendiff.load_yaml import load_yaml


def format_help():
    text = """
    usage: gendiff [-h] [-f FORMAT] first_file second_file

    Compares two configuration files and shows a difference.

    positional arguments:
      first_file
      second_file

    options:
      -h, --help            show this help message and exit
      -f FORMAT, --format FORMAT
                            set format of output
    """
    print(text)


def help_text():
    if len(sys.argv) > 1 and sys.argv[1] in ('--help', '--h'):
        print("- Use: 'gendiff --format' or 'gendiff --f'")
        print("\n- Choose a formatter: 'stylish', 'plain', or 'json'.")
        print("\n- Insert the selected format after the command: 'gendiff'.")
        print("\n- Choose the file format: 'json' or 'yaml'.")
        print("\n- Insert it after the selected formatter.")
        print("\n- Press Enter.")
        print("\n'Stylish': uses indentation and special characters to")
        print("  indicate changes.")
        print("\n'Plain': displays changes as simple sentences.")
        print("\n'JSON':' returns data in standard JSON format.")
      

def format_usage():
    if len(sys.argv) > 1 and sys.argv[1] in ('--format', '--f'):
        print("Usage examples:")
        print("  gendiff   file1.yaml file2.yaml")
        print("  gendiff   file1.json file2.json")
        print("\nFormatters:")
        print("  stylish")
        print("  plain")
        print("  json")
      

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
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError("Unsupported format name")

