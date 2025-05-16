import json


def format_value(nested_list):
    json_str = json.dumps(nested_list, indent=4, ensure_ascii=False)
    return json_str.replace('"', '')


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