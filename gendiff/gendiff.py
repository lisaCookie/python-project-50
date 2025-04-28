import sys

from .diff import generate_diff


def text():
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


def main():
    
    if len(sys.argv) != 3:
        print("Usage: gendiff filepath1.json filepath2.json")
        sys.exit(1)

    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]
    differences = generate_diff(filepath1, filepath2)
    print(differences)


if __name__ == "__main__":
    main()