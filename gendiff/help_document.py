import sys


def format_help():
    text = """
    usage: gendiff [-h] [-f FORMAT] first_file second_file

    Compares two configuration files and shows a difference.

    positional arguments:
      first_file
      second_file

    options:
      -h, --help            show this help message and exit
      -f FORMAT, --format FORMAT
                            set format of output
    """
    print(text)


def help_text():
    if len(sys.argv) > 1 and sys.argv[1] in ('--help', '--h'):
        print("- Use: 'gendiff --format' or 'gendiff --f'")
        print("\n- Choose a formatter: 'stylish', 'plain', or 'json'.")
        print("\n- Insert the selected format after the command: 'gendiff'.")
        print("\n- Choose the file format: 'json' or 'yaml'.")
        print("\n- Insert it after the selected formatter.")
        print("\n- Press Enter.")
        print("\n'Stylish': uses indentation and special characters to")
        print("  indicate changes.")
        print("\n'Plain': displays changes as simple sentences.")
        print("\n'JSON':' returns data in standard JSON format.")
    

def format_usage():
    if len(sys.argv) > 1 and sys.argv[1] in ('--format', '--f'):
        print("Usage examples:")
        print("  gendiff   file1.yaml file2.yaml")
        print("  gendiff   file1.json file2.json")
        print("\nFormatters:")
        print("  stylish")
        print("  plain")
        print("  json")