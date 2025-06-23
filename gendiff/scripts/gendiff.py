import argparse

from gendiff.generate_diff import generate_diff


def parser_function():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help='set format of output',
                        default='stylish', type=str
    )

    return parser.parse_args()


def main():
    args = parser_function()

    filepath1 = args.first_file
    filepath2 = args.second_file

    differences = generate_diff(filepath1, filepath2, formatter=args.format)
    print(differences)
    

if __name__ == '__main__':
    main()
