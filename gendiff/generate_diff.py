import os
import sys

from gendiff.load_json import load_json


def generate_diff(filepath1, filepath2):
    if not os.path.isfile(filepath1):
        print(f"Файл не найден: {filepath1}")
        sys.exit(1)
    if not os.path.isfile(filepath2):
        print(f"Файл не найден: {filepath2}")
        sys.exit(1)

    data1 = load_json(filepath1)
    data2 = load_json(filepath2)

    keys = set(data1.keys()).union(set(data2.keys()))
    result = []

    for key in sorted(keys):
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:  
            result.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(result) + "\n}"


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_diff file1.json file2.json")
        sys.exit(1)

    filepath1 = os.path.join('files', sys.argv[1])
    filepath2 = os.path.join('files', sys.argv[2])
    
    differences = generate_diff(filepath1, filepath2)
    print(differences)


if __name__ == "__main__":
    main()

