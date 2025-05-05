import os
import sys
import json
from gendiff.load_yaml import load_yaml

def main():
    help_text = """
    gendiff -h
    usage: gendiff [-h] [-f FORMAT] first_file second_file

    Compares two configuration files and shows a difference.

    positional arguments:
    first_file
    second_file

    optional arguments:
    -h, --help            show this help message and exit
    -f FORMAT, --format FORMAT
                        set format of output
    """
    print(help_text)
 

def load_file(filepath):
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return load_yaml(filepath) 
    elif filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported file format")

def gendiff(filepath1, filepath2):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)

    keys = set(data1.keys()).union(set(data2.keys()))
    diff = []

    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
            diff.append("    host: hexlet.io")

    return "{\n" + "\n".join(diff) + "\n}"

def main():
    if len(sys.argv) != 3:
        print("Usage: gendiff file1.yaml file2.yaml or gendiff file1.json file2.json")
        sys.exit(1)

    filepath1 = os.path.join('files', sys.argv[1])
    filepath2 = os.path.join('files', sys.argv[2])
    
    differences = gendiff(filepath1, filepath2)
    print(differences)

if __name__ == "__main__":
    main()
