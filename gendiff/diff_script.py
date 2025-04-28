from gendiff import generate_diff
import sys

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