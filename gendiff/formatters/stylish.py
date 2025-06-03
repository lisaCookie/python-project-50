NONE = '  '
ADD = '+ '
DELETE = '- '
SEP = " "


def str_format(value, depth=2):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEP * (depth + 2)
        lines = [
            f"{indent}{NONE}{key}: {str_format(inner_value, depth + 4)}"
            for key, inner_value in value.items()
        ]
        formatted_string = '\n'.join(lines)
        end_indent = SEP * (depth)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return str(value)

def stylish(diff, depth=1):
    indent = SEP * depth
    lines = []

    for item in diff:
        key = item['key']
        value_type = item['type']
        old_value = item.get('old_value')
        new_value = item.get('new_value')
        children = item.get('children')
        value = item.get('value')

        if value_type == 'added':
            lines.append(
                f"{indent}{ADD}{key}: {str_format(new_value, depth + 2)}"
            )
        elif value_type == 'removed':
            lines.append(
                f"{indent}{DELETE}{key}: {str_format(old_value, depth + 2)}"
            )
        elif value_type == 'modified':
            lines.append(
                f"{indent}{DELETE}{key}: {str_format(old_value, depth + 2)}"
            )
            lines.append(
                f"{indent}{ADD}{key}: {str_format(new_value, depth + 2)}"
            )
        elif value_type == 'unchanged':
            lines.append(
                f"{indent}{NONE}{key}: {str_format(value, depth + 2)}"
            )
        elif value_type == 'nested':
            lines.append(f"{indent}{NONE}{key}: {{")
            lines.append(stylish(children, depth + 4))
            lines.append(f"{indent}}}")

    return '\n'.join(lines)