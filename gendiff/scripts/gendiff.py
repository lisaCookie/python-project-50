import sys

def main():
    help_text = """
    gendiff -h
    usage: gendiff [-h] first_file second_file

    Compares two configuration files and shows a difference.

    positional arguments:
    first_file
    second_file

    optional arguments:
    -h, --help            show this help message and exit
    """
    print(help_text)

if __name__ == "__main__":
    main()