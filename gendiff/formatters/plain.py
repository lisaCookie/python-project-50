def format_plain(diff, path=''):
    result = []

    for item in diff:
        key = item['key']
        current_path = f"{path}.{key}" if path else key

        if item['type'] == 'added':
            result.append(f"Property '{current_path}' was added with value: "
                          f"{format_value(item['new_value'])}")
        elif item['type'] == 'removed':
            result.append(f"Property '{current_path}' was removed")
        elif item['type'] == 'modified':
            result.append(f"Property '{current_path}' was updated. "
                          f"From {format_value(item['old_value'])} to "
                          f"{format_value(item['new_value'])}")
        elif item['type'] == 'nested':
            result.append(format_plain(item['children'], current_path))
      
    return '\n'.join(result)


def format_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)