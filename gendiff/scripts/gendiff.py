import os
import sys

from gendiff.generate_diff import generate_diff
from gendiff.help_document import format_help, format_usage, help_text


def main():
    if len(sys.argv) < 2:
        format_help()
        sys.exit(1)

    if sys.argv[1] in ('--help', '--h'):
        help_text()
        sys.exit(0)

    if sys.argv[1] in ('--format', '--f'):
        format_usage()
        sys.exit(0)

    if len(sys.argv) != 4:
        print("Usage: gendiff <format> file1.yaml file2.yaml or "
              "gendiff <format> file1.json file2.json")
        sys.exit(1)

    format_name = sys.argv[1]
    filepath1 = os.path.join('tests', 'test_data', sys.argv[2])  
    filepath2 = os.path.join('tests', 'test_data', sys.argv[3])  

    differences = generate_diff(filepath1, filepath2, format_name=format_name)
    print(differences)


if __name__ == "__main__":
    main()