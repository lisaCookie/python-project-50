import json
import os 

def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:].lower()

def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()

def parse_yaml(yaml_content):
    lines = yaml_content.strip().split('\n')
    result = {}
    stack = [(result, -1)]

    for line in lines:
        line = line.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue

        indent = len(line) - len(line.lstrip(' '))
        content = line.lstrip()

        if ':' not in content:
            raise ValueError("Invalid YAML line: " + line)

        key, value = content.split(':', 1)
        key = key.strip()
        value = value.strip()
        while stack and stack[-1][1] >= indent:
            stack.pop()

        current_dict = stack[-1][0]

        if value == '':
            new_dict = {}
            current_dict[key] = new_dict
            stack.append((new_dict, indent))
        else:
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.lower() == 'null':
                value = None
            else:
                if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
            current_dict[key] = value

    return result

def parse_data(data, format):
    if format == 'json':
        return json.loads(data)
    if format in ('yaml', 'yml'):
        return parse_yaml(data)
    else:
        raise ValueError(f'Unsupported file format: {format}')

def parse_data_from_file(file_path):
    data = read_file(file_path)
    format = get_file_format(file_path)
    return parse_data(data, format)