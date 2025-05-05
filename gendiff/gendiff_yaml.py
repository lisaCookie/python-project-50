import os
import sys

from gendiff.load_yaml import load_yaml


def gendiff_yaml(filepath1, filepath2):
    data1 = load_yaml(filepath1)
    data2 = load_yaml(filepath2)

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

    return "{\n" + "\n".join(diff) + "\n}"


def main():
    if len(sys.argv) != 3:
        print("Usage: gendiff_yaml file1.yaml file2.yaml")
        sys.exit(1)

    filepath1 = os.path.join('files', sys.argv[1])
    filepath2 = os.path.join('files', sys.argv[2])
    
    differences = gendiff_yaml(filepath1, filepath2)
    print(differences)


if __name__ == "__main__":
    main()