
def load_yaml(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def parse_yaml(yaml_content):
    lines = yaml_content.strip().split('\n')
    result = {}
    current_key = None
    current_dict = result

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            if value == '':
                
                current_key = key
                current_dict[key] = {}
                current_dict = current_dict[key]
            else:
                
                current_dict[key] = value
        else:
            
            raise ValueError("Invalid YAML format")

   
        if current_dict is result:  
            continue
        else:
            current_dict = result  

    return result
