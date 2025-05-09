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