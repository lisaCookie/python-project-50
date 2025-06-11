def format_value(value, depth):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)

    lines = []
    indent = ' ' * (depth + 4)
    closing_indent = ' ' * depth
    
    for key, val in value.items():
        lines.append(f"{indent}{key}: {format_value(val, depth + 4)}")
    
    return '{\n' + '\n'.join(lines) + '\n' + closing_indent + '}'


def stylish(diff, depth=0):
    lines = []
    indent = ' ' * (depth + 2)
    
    for node in diff:
        key = node['key']
        node_type = node['type']
        
        if node_type == 'nested':
            lines.append(f"{indent}  {key}: {{")
            lines.append(stylish(node['children'], depth + 4))
            lines.append(f"{indent}  }}")
        elif node_type == 'added':
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'], depth + 2)}")
        elif node_type == 'removed':
            lines.append(f"{indent}- {key}: {format_value(node['old_value'], depth + 2)}")
        elif node_type == 'modified':
            lines.append(f"{indent}- {key}: {format_value(node['old_value'], depth + 2)}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'], depth + 2)}")
        elif node_type == 'unchanged':
            lines.append(f"{indent}  {key}: {format_value(node['value'], depth + 2)}")
    
    return '{\n' + '\n'.join(lines) + '\n' + ' ' * depth + '}'
