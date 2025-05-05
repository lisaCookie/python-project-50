
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


