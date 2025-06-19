import json

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import stylish
from gendiff.parsing_files import parse_data_from_file


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

def generate_formatters(diff, format_name='stylish') -> str:

    if format_name == 'stylish':
        lines = stylish(diff)
        return "{\n" + '\n'.join(lines) + "\n}"
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError("Unsupported format name")
    
def generate_diff(file_path1, file_path2, formatter='stylish'):
    first_file = parse_data_from_file(file_path1)
    second_file = parse_data_from_file(file_path2)
    diff = compute_diff(first_file, second_file)
    return generate_formatters(diff, formatter)