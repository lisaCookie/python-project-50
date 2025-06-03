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

def str_format(node, depth):
    
    if not isinstance(node, dict):
        return str(node)
    lines = []
    indent = SEP * (depth + 2)
    for key, value in node.items():
        lines.append(f"{indent}{key}: {str_format(value, depth + 2)}")
    return '{\n' + '\n'.join(lines) + '\n' + SEP * depth + '}'

def stylish(diff, depth=0):
    lines = []
    indent = SEP * depth
    for item in diff:
        key = item['key']
        type_ = item['type']
        old_value = item.get('old_value')
        new_value = item.get('new_value')
        value = item.get('value')
        children = item.get('children')

        if type_ == 'added':
            lines.append(f"{indent}  + {key}: {str_format(new_value, depth + 2)}")
        elif type_ == 'removed':
            lines.append(f"{indent}  - {key}: {str_format(old_value, depth + 2)}")
        elif type_ == 'unchanged':
            lines.append(f"{indent}    {key}: {str_format(value, depth + 2)}")
        elif type_ == 'modified':
            lines.append(f"{indent}  - {key}: {str_format(old_value, depth + 2)}")
            lines.append(f"{indent}  + {key}: {str_format(new_value, depth + 2)}")
        elif type_ == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(stylish(children, depth + 4))
            lines.append(f"{indent}    }}")
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'